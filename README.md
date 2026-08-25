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
├── netlify/
│   └── functions/
│       └── predict.py          # Netlify serverless function for predictions
│
├── templates/
│   └── index.html              # Web UI frontend
│
├── app.py                       # Flask web application
├── encoder.pkl                  # Trained label encoder
├── model.pkl                    # Trained ML model
├── requirements.txt             # Python dependencies
├── .python-version              # Python version specification (3.12.13)
├── .gitignore
└── README.md
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dileep3015/TRAFFIC-VOLUME.git
   cd TRAFFIC-VOLUME
   ```

2. **Set Python version** (if using pyenv)
   ```bash
   pyenv install 3.12.13
   pyenv local 3.12.13
   ```

3. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Local Development (Flask)

Run the Flask development server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Netlify Deployment

The project includes a Netlify serverless function for predictions:
- Function: `netlify/functions/predict.py`
- Endpoint: `/.netlify/functions/predict`

To deploy to Netlify:
1. Connect your GitHub repository to Netlify
2. Set build command: `pip install -r requirements.txt`
3. The function will be automatically deployed

## Making Predictions

### Via Web UI
1. Navigate to `http://localhost:5000`
2. Fill in the traffic parameters:
   - Holiday (0/1)
   - Temperature
   - Rain
   - Snow
   - Weather condition
   - Year, Month, Day
   - Hours, Minutes, Seconds
3. Click "Predict" to get the estimated traffic volume

### Via API
Send a POST request to the prediction endpoint:
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "holiday": 0,
    "temp": 20.5,
    "rain": 0,
    "snow": 0,
    "weather": 1,
    "year": 2024,
    "month": 1,
    "day": 15,
    "hours": 9,
    "minutes": 30,
    "seconds": 0
  }'
```