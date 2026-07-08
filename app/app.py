from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "crop_model.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
# Crop Information Dictionary
crop_info = {
    "rice": {
        "water": "High",
        "soil": "Clayey Soil",
        "fertilizer": "Nitrogen-rich fertilizer",
        "tip": "Maintain standing water during early growth."
    },
    "maize": {
        "water": "Moderate",
        "soil": "Loamy Soil",
        "fertilizer": "Balanced NPK fertilizer",
        "tip": "Ensure proper sunlight and avoid waterlogging."
    },
    "chickpea": {
        "water": "Low",
        "soil": "Sandy Loam",
        "fertilizer": "Phosphorus-rich fertilizer",
        "tip": "Requires well-drained soil."
    },
    "kidneybeans": {
        "water": "Moderate",
        "soil": "Loamy Soil",
        "fertilizer": "Organic Compost",
        "tip": "Avoid excess irrigation."
    },
    "pigeonpeas": {
        "water": "Low",
        "soil": "Black Soil",
        "fertilizer": "Potassium-rich fertilizer",
        "tip": "Suitable for drought-prone regions."
    },
    "mothbeans": {
        "water": "Low",
        "soil": "Sandy Soil",
        "fertilizer": "Organic Compost",
        "tip": "Thrives in dry climates."
    },
    "mungbean": {
        "water": "Moderate",
        "soil": "Loamy Soil",
        "fertilizer": "Balanced NPK",
        "tip": "Maintain moderate soil moisture."
    },
    "blackgram": {
        "water": "Moderate",
        "soil": "Clay Loam",
        "fertilizer": "Nitrogen-rich fertilizer",
        "tip": "Avoid standing water."
    },
    "lentil": {
        "water": "Low",
        "soil": "Loamy Soil",
        "fertilizer": "Organic Compost",
        "tip": "Needs cool weather."
    },
    "pomegranate": {
        "water": "Moderate",
        "soil": "Well-drained Soil",
        "fertilizer": "Potassium-rich fertilizer",
        "tip": "Prune regularly."
    },
    "banana": {
        "water": "High",
        "soil": "Rich Loamy Soil",
        "fertilizer": "Nitrogen-rich fertilizer",
        "tip": "Maintain continuous irrigation."
    },
    "mango": {
        "water": "Moderate",
        "soil": "Deep Loamy Soil",
        "fertilizer": "Organic Compost",
        "tip": "Avoid waterlogging."
    },
    "grapes": {
        "water": "Moderate",
        "soil": "Sandy Loam",
        "fertilizer": "Balanced NPK",
        "tip": "Requires proper pruning."
    },
    "watermelon": {
        "water": "Moderate",
        "soil": "Sandy Soil",
        "fertilizer": "Potassium-rich fertilizer",
        "tip": "Requires full sunlight."
    },
    "muskmelon": {
        "water": "Moderate",
        "soil": "Sandy Loam",
        "fertilizer": "Balanced NPK",
        "tip": "Avoid excess watering."
    },
    "apple": {
        "water": "Moderate",
        "soil": "Well-drained Loam",
        "fertilizer": "Organic Compost",
        "tip": "Needs cool climate."
    },
    "orange": {
        "water": "Moderate",
        "soil": "Loamy Soil",
        "fertilizer": "Balanced NPK",
        "tip": "Maintain proper drainage."
    },
    "papaya": {
        "water": "Moderate",
        "soil": "Rich Loamy Soil",
        "fertilizer": "Nitrogen-rich fertilizer",
        "tip": "Protect from frost."
    },
    "coconut": {
        "water": "High",
        "soil": "Sandy Coastal Soil",
        "fertilizer": "Organic Manure",
        "tip": "Requires regular irrigation."
    },
    "cotton": {
        "water": "Moderate",
        "soil": "Black Soil",
        "fertilizer": "Potassium-rich fertilizer",
        "tip": "Monitor pest attacks regularly."
    },
    "jute": {
        "water": "High",
        "soil": "Alluvial Soil",
        "fertilizer": "Nitrogen fertilizer",
        "tip": "Requires humid climate."
    },
    "coffee": {
        "water": "Moderate",
        "soil": "Acidic Loamy Soil",
        "fertilizer": "Organic Compost",
        "tip": "Grow under partial shade."
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Read Inputs
    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    # ==========================
    # Input Validation
    # ==========================

    if not (0 <= ph <= 14):
        return render_template(
            "index.html",
            error="Please enter a valid Soil pH value (0 - 14)."
        )

    if not (0 <= humidity <= 100):
        return render_template(
            "index.html",
            error="Humidity must be between 0 and 100%."
        )

    if not (0 <= temperature <= 60):
        return render_template(
            "index.html",
            error="Temperature must be between 0°C and 60°C."
        )

    if rainfall < 0:
        return render_template(
            "index.html",
            error="Rainfall cannot be negative."
        )

    if N < 0 or P < 0 or K < 0:
        return render_template(
            "index.html",
            error="N, P, and K values cannot be negative."
        )

    # ==========================
    # Prediction
    # ==========================

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(data)[0]

    probabilities = model.predict_proba(data)[0]
    confidence = round(max(probabilities) * 100, 2)

    info = crop_info.get(
        prediction.lower(),
        {
            "water": "Moderate",
            "soil": "Suitable Agricultural Soil",
            "fertilizer": "Balanced NPK Fertilizer",
            "tip": "Follow standard agricultural practices."
        }
    )

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        info=info,
        N=N,
        P=P,
        K=K,
        temperature=temperature,
        humidity=humidity,
        ph=ph,
        rainfall=rainfall
    )

if __name__ == "__main__":
    app.run(debug=True)