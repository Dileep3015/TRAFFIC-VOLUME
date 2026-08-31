# 🚦 Interactive Traffic Volume Prediction & Visualization

An interactive machine learning web application that estimates traffic volume based on weather conditions, holidays, date, and time-related inputs, with an interactive map for location-based visualization.

The project combines **Machine Learning, Flask, Leaflet/OpenStreetMap, GitHub Releases, and Render deployment** into a complete end-to-end application.

🌐 **Live Application:**  
https://traffic-volume-predictor.onrender.com

---

## 📌 About the Project

Traffic conditions can change significantly depending on weather, holidays, date, and time.

This project was developed to explore how machine learning can be used to estimate traffic volume from these factors and present the result through a simple web interface.

The application allows users to:

- Enter weather and time-related information
- Select holiday and weather conditions
- Enter date and time information
- Predict estimated traffic volume using a trained Random Forest model
- Classify the prediction as Low, Medium, or High Traffic
- Select a location directly from an interactive map
- Use the browser's current location
- Quickly navigate to Bengaluru
- View the selected latitude and longitude
- Visualize the prediction together with the selected location

The goal was not only to build a machine learning model, but to turn it into a usable web application and deploy it online.

---

## ✨ Key Features

### 🤖 Machine Learning Prediction

The application uses a trained **Random Forest Regression** model to estimate traffic volume.

The model uses the following input features:

- Holiday
- Temperature
- Rain
- Snow
- Weather condition
- Year
- Month
- Day
- Hour
- Minute
- Second

The predicted value is then categorized into:

| Traffic Volume | Classification |
|---|---|
| `< 500` | 🟢 Low Traffic |
| `500 - 1999` | 🟡 Medium Traffic |
| `>= 2000` | 🔴 High Traffic |

---

### 🗺️ Interactive Traffic Map

The project was extended with an interactive map using **Leaflet** and **OpenStreetMap**.

Users can click on the map to select a traffic location.

The application displays:

- 📍 Latitude
- 📍 Longitude
- 🚦 Traffic prediction
- Traffic classification

The selected location is displayed visually using a map marker and popup.

---

### 📍 Location Features

The map provides additional location functionality:

#### Use My Location

The application can request the user's browser location and display it on the map.

#### Bengaluru

A dedicated button allows users to quickly move the map to Bengaluru.

#### Manual Location Selection

Users can click anywhere on the map to select a location.

This makes the application more interactive than a traditional machine learning prediction form.

---

## 🏗️ System Architecture

The project follows a simple end-to-end architecture:

```text
                User
                  │
                  ▼
        ┌───────────────────┐
        │   Flask Web App   │
        └─────────┬─────────┘
                  │
        ┌─────────┴──────────┐
        │                    │
        ▼                    ▼
 Prediction Form       Interactive Map
        │                    │
        ▼                    ▼
 Random Forest        Leaflet + OpenStreetMap
        │                    │
        └─────────┬──────────┘
                  │
                  ▼
          Traffic Prediction
                  │
                  ▼
       Low / Medium / High
