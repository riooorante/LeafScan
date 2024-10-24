from flask import Blueprint, request, redirect, url_for

main = Blueprint("main", __name__)

@main.route("/predict-image", method=["POST"])
def predict_image():
    pass