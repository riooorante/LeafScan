# Menggunakan base image Python 3.11.9
FROM python:3.11.9-slim

# Menentukan working directory di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt .

# Menginstal dependencies yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dari host ke container
COPY . .

# Menjalankan aplikasi Flask saat container dijalankan
CMD ["python", "run.py"]

# Menjalankan Flask pada port 5000 (Anda bisa menyesuaikan dengan port Flask Anda)
EXPOSE 5000
