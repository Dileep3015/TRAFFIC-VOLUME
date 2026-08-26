# 🚦 Traffic Volume Prediction

A machine learning web application that predicts traffic volume using weather conditions and time-based information.

The project uses a Random Forest regression model trained on historical traffic data and provides predictions through a simple Flask web interface.

## 🌐 Live Demo

**Try the application:**  
https://traffic-volume-predictor.onrender.com

---

## 📌 About the Project

Traffic volume can vary significantly depending on factors such as weather, time of day, and date.

This project explores how machine learning can be used to estimate traffic volume from these factors. The trained model is integrated into a Flask application, allowing users to enter relevant conditions and receive an estimated traffic volume.

The application also provides a simple traffic classification:

- **Low Traffic**
- **Medium Traffic**
- **High Traffic**

The goal of the project was not only to train a machine learning model, but also to take the model through the complete process of data preprocessing, model training, evaluation, serialization, and deployment.

---

## ✨ Features

- Predict traffic volume from weather and time-related inputs
- Random Forest regression model
- Weather condition handling
- Date and time feature extraction
- Missing-value preprocessing
- Model evaluation using MAE, RMSE, and R²
- Flask-based web interface
- Trained model stored as a GitHub Release asset
- Deployed and accessible through Render

---

## 🧠 Machine Learning Approach

The project follows a typical machine learning workflow:

```text
Raw Traffic Data
       ↓
Data Cleaning
       ↓
Missing Value Handling
       ↓
Feature Engineering
       ↓
Feature / Target Separation
       ↓
Train-Test Split
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Serialization
       ↓
Flask Integration
       ↓
Render Deployment
