# Traffic Volume Prediction

Traffic Volume Prediction is a machine learning project that predicts the estimated traffic volume on a road based on different weather and time-related conditions.

I built this project to explore how machine learning can be used with real-world traffic data and to understand how factors such as temperature, rain, snow, weather conditions, and date/time can influence traffic volume.

## About the Project

The project uses a Random Forest Regression model to predict traffic volume. The model was trained using traffic and weather-related data and then integrated into a Flask web application.

The web application provides a simple interface where users can enter the required parameters and get a predicted traffic volume.

### Key Features

- Predicts traffic volume using a trained machine learning model
- Uses weather and time-related features for prediction
- Random Forest Regression model
- Flask-based web application
- Label encoding for categorical data
- Jupyter Notebook for data analysis and model development

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Flask
- HTML/CSS
- Jupyter Notebook

## Project Structure

```text
TRAFFIC-VOLUME/
│
├── app.py
├── encoder.pkl
├── templates/
│   └── index.html
├── traffic volume.csv
├── TRAFFICTELLIGENCE.ipynb
├── model/
│   └── model.txt
├── package.json
├── package-lock.json
├── .gitignore
└── README.md