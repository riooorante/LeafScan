import logging
import cv2
import os
import numpy as np

from ultralytics import YOLO
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction
from google.cloud import storage
from . import storage_client, bucket_name, model_path

def resize_image_by_percentage(image_bytes, scale_percent=100):
    """
    Resize image based on the given percentage scale.

    :param image_bytes: Byte data of the image.
    :param scale_percent: Scaling percentage (e.g., 50 for 50%, 100 for 100%).
    :return: Resized image.
    """
    # Mengonversi byte ke array numpy dan mendecode gambar
    image_array = np.frombuffer(image_bytes.getvalue(), np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Mendapatkan dimensi asli gambar
    original_height, original_width = image.shape[:2]

    # Menghitung dimensi baru berdasarkan persentase
    new_width = int(original_width * scale_percent / 100)
    new_height = int(original_height * scale_percent / 100)
    dim = (new_width, new_height)

    # Resize gambar dengan dimensi baru
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resized_image

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


def predict_image_obj_detection_sahi(image_bytes, image_name, confidence_level=0.5, ):
    """
    Predicts an uploaded image using YOLOv8 and SAHI for object detection.
    :param image_bytes: The uploaded image file in bytes.
    :param confidence_level: The confidence threshold for the detection model.
    :return: A dictionary containing the original image URL, detected classes, and local predicted image path.
    """

    image = resize_image_by_percentage(image_bytes, 60)
    # Save the uploaded image locally
    uploaded_image_path = os.path.join("D:\\Computer-Vision\\LeafScan\\predicted", "uploaded_image.jpg")
    cv2.imwrite(uploaded_image_path, image)
    source_blob_name = "uploaded_images/uploaded_image.jpg"

    # Initialize the detection model
    detection_model = AutoDetectionModel.from_pretrained(
        model_type="yolov8",
        model_path=model_path,
        confidence_threshold=confidence_level,
        device="cpu"
    )

    # Perform prediction
    result = get_sliced_prediction(
        uploaded_image_path,
        detection_model,
        slice_height=356,
        slice_width=356,
        overlap_width_ratio=0.5,
        overlap_height_ratio=0.5,
    )

    # Get detected classes
    detected_classes = {obj.category.name for obj in result.object_prediction_list}

    logging.info("Prediksi Selesai")

    # Save the prediction result visuals
    predicted_image_path = os.path.join("D:\\Computer-Vision\\LeafScan\\predicted", "predicted_sahi.jpg")
    result.export_visuals(export_dir="D:\\Computer-Vision\\LeafScan\\predicted", file_name="predicted_sahi")

    # Upload the original image to GCP
    # original_image_url = upload_image_to_gcp(image, source_blob_name)

    return {
        "original_image_url": "Test",
        "detected_classes": list(detected_classes),
        "local_predicted_image_path": predicted_image_path
    }
