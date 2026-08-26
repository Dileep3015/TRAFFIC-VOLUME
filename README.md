# 🚦 Traffic Volume Prediction

A Machine Learning web application that predicts traffic volume based on weather and time-related inputs.

## 🌐 Live Demo

👉 **[Try the Traffic Volume Predictor](https://traffic-volume-predictor.onrender.com)**

## 📊 Model Performance

- **Model:** Random Forest Regressor
- **MAE:** 528.59
- **RMSE:** 818.83
- **R² Score:** 0.8286

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- HTML/CSS
- Render

## ✨ Features

- Traffic volume prediction
- Weather-based prediction
- Time-based prediction
- Low / Medium / High traffic classification
- Deployed Flask web application

## 🚀 Deployment

The application is deployed using Render.

The trained `model.pkl` is distributed through the GitHub Release:

**Traffic Volume Model v1.0**

The model is downloaded automatically by the Flask application when required.

## 📁 Project Structure

```text
TRAFFIC-VOLUME/
├── app.py
├── encoder.pkl
├── requirements.txt
├── README.md
├── TRAFFICTELLIGENCE.ipynb
├── templates/
│   └── index.html
└── .gitignore
