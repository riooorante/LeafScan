from flask import Blueprint, request, redirect, url_for, jsonify
from utils.message_flow import Flow
from cv.predict import predict_image_obj_detection

main = Blueprint("main", __name__)

@main.route("/predict-image", methods=["POST"])
def predict_image():
    llm = Flow()
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
        print("")

        llm_result = llm.result_flow(result["detected_classes"])

        return llm_result
    except Exception as e:
        return jsonify({"error": str(e)}), 500