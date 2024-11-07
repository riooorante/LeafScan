import os
from dotenv import load_dotenv
from google.cloud import storage
from ultralytics import YOLO
from google.cloud import storage
import cv2
import numpy as np
from ultralytics import YOLO
from sahi.predict import get_sliced_prediction




# Load environment variables dari file .env
load_dotenv()

# Ambil nama bucket dari environment
bucket_name = os.getenv("GCP_STORAGE_URL")

# Pastikan nama bucket valid
if not bucket_name:
    raise ValueError("Nama bucket tidak ditemukan di environment. Pastikan GCP_STORAGE_URL diatur di file .env")

# Inisialisasi klien Google Cloud Storage
storage_client = storage.Client()

# Inisialisasi YOLO model
model_path = "models/best-v2-2510240737.pt"  # Path ke model YOLO
model = YOLO(model_path)
