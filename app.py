import os
import urllib.request
import numpy as np
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)

MODEL_URL = (
    "https://github.com/Dileep3015/TRAFFIC-VOLUME/"
    "releases/download/v1.0-model/model.pkl"
)

MODEL_PATH = "model.pkl"
ENCODER_PATH = "encoder.pkl"


def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model.pkl...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        print("Model downloaded successfully.")


# Download the model if it is not already available
download_model()

# Load model and encoder
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_features = [
            float(request.form["holiday"]),
            float(request.form["temp"]),
            float(request.form["rain"]),
            float(request.form["snow"]),
            float(request.form["weather"]),
            float(request.form["year"]),
            float(request.form["month"]),
            float(request.form["day"]),
            float(request.form["hours"]),
            float(request.form["minutes"]),
            float(request.form["seconds"])
        ]

        features_values = np.array(input_features).reshape(1, -1)

        prediction = model.predict(features_values)

        traffic_volume = round(float(prediction[0]))

        if traffic_volume < 500:
            traffic_level = "Low Traffic"
        elif traffic_volume < 2000:
            traffic_level = "Medium Traffic"
        else:
            traffic_level = "High Traffic"

        text = (
                f"Estimated Traffic Volume: "
                f"{traffic_volume:,} vehicles "
                f"({traffic_level})"
                )

        return render_template(
            "index.html",
            prediction_text=text
        )

    except Exception as e:
        print(f"Prediction error: {e}")
        return "An error occurred during prediction.", 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )