import logging
import cv2
import os
import numpy as np

from ultralytics import YOLO
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from google.cloud import storage
from . import storage_client, bucket_name, model_path

def upload_image_to_gcp(image, destination_blob_name):
    """
    Function to upload an image to Google Cloud Storage.
    """
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    _, image_encoded = cv2.imencode('.jpg', image)
    blob.upload_from_string(image_encoded.tobytes(), content_type='image/jpeg')

    return f"gs://{bucket_name}/{destination_blob_name}"


def save_image_locally(image, local_path):
    """
    Function to save an image to the local filesystem.
    """
    cv2.imwrite(local_path, image)


def predict_image_obj_detection_sahi(image_file, confidence_level=0.5):
    """
    Function to predict an uploaded image using YOLOv8 and SAHI for object detection.
    The image is uploaded to GCP first, and the prediction results are also uploaded to GCP.

    :param image_file: The uploaded image file.
    :param confidence_level: The confidence threshold for the detection model.
    :return: A dictionary containing the original image URL, detected classes, and local predicted image path.
    """
    # Membaca gambar dari file yang diunggah
    image_array = np.frombuffer(image_file.read(), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Simpan gambar yang diunggah ke direktori lokal
    uploaded_image_path = os.path.join("D:\\Computer-Vision\\LeafScan\\predicted", f"uploaded_{image_file.filename}")
    cv2.imwrite(uploaded_image_path, image)
    print(f"Uploaded image saved to: {uploaded_image_path}")

    # Nama blob untuk GCP
    source_blob_name = f"uploaded_images/{image_file.filename}"

    detection_model = AutoDetectionModel.from_pretrained(
        model_type="yolov8",
        model_path=model_path,
        confidence_threshold=confidence_level,
        device="cpu"
    )

    result = get_sliced_prediction(
        uploaded_image_path,
        detection_model,
        slice_height=256,
        slice_width=256,
        overlap_width_ratio=0.2,
        overlap_height_ratio=0.2,
    )

    logging.info(result.object_prediction_list)
    detection = set()
    for obj in result.object_prediction_list:
        detection.add(obj.category.name)

    detection = list(detection)

    logging.info(f"ini adalah list dari detection {detection}")

    os.makedirs("D:\\Computer-Vision\\LeafScan\\predicted", exist_ok=True)

    saved_path = os.path.join("D:\\Computer-Vision\\LeafScan\\predicted", "predicted_sahi.jpg")
    result.export_visuals(export_dir="D:\\Computer-Vision\\LeafScan\\predicted", file_name="predicted_sahi")

    return {
        "original_image_url": f"gs://{bucket_name}/{source_blob_name}",
        "detected_classes": detection,
        "local_predicted_image_path": saved_path
    }
