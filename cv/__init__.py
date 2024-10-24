import os
from dotenv import load_dotenv
from google.cloud import storage
from ultralytics import YOLO

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
model_path = "yolo11n.pt"  # Path ke model YOLO
model = YOLO(model_path)
