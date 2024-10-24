from . import model, storage_client, bucket_name
import cv2
import numpy as np

def download_image(source_blob_name):
    """
    Fungsi untuk mendownload gambar dari Google Cloud Storage dan mengembalikannya sebagai gambar OpenCV.
    """
    bucket = storage_client.bucket(bucket_name)  # Dapatkan bucket
    blob = bucket.blob(source_blob_name)  # Dapatkan objek blob (file) berdasarkan namanya

    image_data = blob.download_as_bytes()  # Unduh gambar dalam bentuk bytes

    # Konversi dari bytes ke array numpy dan kemudian ke gambar OpenCV
    image_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    return image

def predict_image(image_name):
    """
    Fungsi untuk mendownload gambar dari Google Cloud Storage, melakukan prediksi menggunakan YOLO,
    dan mengembalikan hasil prediksi.
    """
    image = download_image(image_name)  # Download gambar dari bucket

    results = model.predict(image, save=True)  # Lakukan prediksi dan simpan hasil

    return results  # Kembalikan hasil prediksi
