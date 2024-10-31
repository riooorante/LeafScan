from flask import Blueprint, request, jsonify
from utils.message_flow import Flow
from cv.predict import predict_image_obj_detection
from cv.predict_sahi import predict_image_obj_detection_sahi

main = Blueprint("main", __name__)

# Buat instance Flow di luar fungsi untuk digunakan kembali
llm = Flow()

@main.route("/predict-image", methods=["POST"])
def predict_image():
    """
    Route untuk menerima gambar dari method POST, memanggil fungsi prediksi,
    dan mengembalikan URL gambar asli, hasil prediksi dari GCP, serta kelas yang terdeteksi.
    """
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    image_file = request.files['image']

    model_path = "path/to/yolo_model.pt"
    confidence_level = 0.3

    try:
        result = predict_image_obj_detection(image_file, confidence_level)
        print("")  # Mungkin Anda ingin menambahkan logging di sini

        # Pastikan result["detected_classes"] ada dan dalam format yang tepat
        if "detected_classes" not in result:
            return jsonify({"error": "No classes detected"}), 400

        llm_result = llm.result_flow(result["detected_classes"])

        return jsonify(llm_result)  # Pastikan mengembalikan JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500


