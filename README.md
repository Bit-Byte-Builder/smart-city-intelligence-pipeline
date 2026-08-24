# 🏙️ Smart City Intelligence Pipeline — Air Quality Prediction System

> An end-to-end machine learning system for PM2.5 prediction with real-time weather and air-quality data integration through an interactive Streamlit dashboard.

## 🌐 Live Demo

🚀 **Try the deployed application:**

https://smart-city-intelligence-pipeline-5ywfzfesmb7rzvqqlmjq4l.streamlit.app/

The application combines machine learning predictions with live weather, geolocation, and air-quality data to provide an interactive view of current and predicted PM2.5 conditions.

---

## 📌 Project Overview

Air pollution monitoring is often reactive: authorities and citizens may only respond after pollution levels have already increased.

This project explores a predictive approach by using historical PM2.5 patterns and meteorological variables to estimate PM2.5 levels and combine those predictions with real-time environmental data.

The system provides:

- PM2.5 prediction using machine learning
- Real-time weather information
- Real-time PM2.5 information
- Interactive pollution trend visualisation
- AQI-style visual indicators
- City-based geolocation
- A Streamlit dashboard for interactive analysis

## 🌍 Why This Project Matters

Air-quality monitoring is often reactive, while predictive analytics can provide an additional signal about potential short-term pollution changes.

This project demonstrates how historical pollution patterns, meteorological variables, and real-time environmental APIs can be combined into a single interactive system for exploratory and predictive air-quality analysis.

The system is intended as a prototype and decision-support demonstration rather than an official forecasting or monitoring service.

### End-to-End Workflow

**Historical Data → Data Preparation → Feature Engineering → Model Training → Model Evaluation → Model Persistence → Real-Time API Integration → Streamlit Deployment**

---

## 🎯 Project Objectives

- Build a machine-learning model for PM2.5 prediction.
- Engineer temporal and meteorological features from historical pollution data.
- Compare multiple regression models.
- Evaluate model performance using MAE and R².
- Integrate real-time weather and air-quality information.
- Provide an interactive dashboard for exploring pollution conditions.
- Demonstrate how predictive analytics can support early environmental monitoring.

---

## 📊 Dataset

The project uses historical air-quality and meteorological observations containing variables related to:

- PM2.5 concentration
- Temperature
- Atmospheric pressure
- Dew point
- Wind speed
- Wind direction
- Time-based observations

The target variable for the regression models is: `PM2.5`

Historical observations are used to create lagged and rolling features that capture recent pollution behaviour.

---

## 🧠 Feature Engineering

Several features were engineered to capture temporal patterns and environmental relationships.

### ⏱️ Lag Features

Previous PM2.5 observations are used as predictive variables:

- PM2.5_lag1
- PM2.5_lag2
- PM2.5_lag3

These features provide information about recent pollution levels.

### 📈 Rolling Statistics

Rolling statistics were used to represent recent pollution behaviour:

- 24-hour rolling mean
- 24-hour rolling standard deviation

### 🔄 Rate of Change

A PM2.5 difference feature was used to capture short-term changes in pollution levels.

### 🕐 Time Features

Temporal variables include:

- Hour
- Month

These features allow the model to capture recurring temporal patterns.

### 🌬️ Wind Direction Encoding

Categorical wind-direction values were transformed into model-compatible numerical features using one-hot encoding.

---

## 🤖 Models Used

The project evaluates tree-based regression models for PM2.5 prediction.

### Random Forest Regressor

Used as a non-linear ensemble baseline capable of modelling complex relationships between environmental variables.

### XGBoost Regressor

XGBoost was evaluated as a gradient-boosting approach and selected as the final model for the deployed application.

Two XGBoost configurations were evaluated:

- Baseline XGBoost
- Optimized XGBoost

---

## 📏 Model Evaluation

Model performance was evaluated using:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual PM2.5 values.

**Lower MAE is better.**

### R² Score

R² measures how much of the variation in the target variable is explained by the model.

**Higher R² is better.**

---

## 📊 Model Comparison

| Model | MAE | R² Score |
|---|---:|---:|
| Random Forest | 10.338469 | 0.942163 |
| Baseline XGBoost | 10.0561 | 0.9477 |
| Optimized XGBoost | 10.0785 | 0.9479 |

### Insight

The optimized XGBoost model achieved the highest R² score among the evaluated models, while its MAE remained very close to the baseline XGBoost model.

The difference between the two XGBoost configurations is small, indicating that the optimization produced only a marginal improvement in the evaluated metrics.

Optimized XGBoost was selected as the deployed model because it achieved the highest R² among the evaluated configurations, although the improvement over baseline XGBoost was marginal.

### Why It Matters

Better PM2.5 predictions can support environmental monitoring by providing an additional predictive signal alongside real-time observations.

However, model predictions should be treated as decision-support information rather than a replacement for official air-quality monitoring systems.

---

## 🌍 Real-Time Data Integration

The Streamlit application integrates external environmental data to complement the machine-learning prediction.

### Geolocation

The application uses the selected city to obtain geographic coordinates.

### Weather Data

Real-time weather information includes:

- Temperature
- Atmospheric pressure
- Dew point
- Wind speed

### Air-Quality Data

The application retrieves real-time PM2.5 information and displays it alongside the model prediction.

This allows users to compare:

### Predicted PM2.5 vs. Real-Time PM2.5

and observe the difference between the model estimate and the current measured value.

---

## 🖥️ Streamlit Dashboard

The deployed application provides an interactive interface where users can:

1. Enter a city.
2. Retrieve its location.
3. Fetch current weather conditions.
4. Enter recent PM2.5 observations.
5. Select wind direction.
6. Generate a PM2.5 prediction.
7. Compare the prediction with real-time PM2.5.
8. Visualise the recent PM2.5 trend.
9. View an AQI-style PM2.5 gauge.

---

## 📸 Dashboard Preview

### 🏙️ 1. Smart Dashboard Interface

The main dashboard allows users to enter a city and retrieve live weather and pollution inputs.

![Dashboard](https://github.com/Bit-Byte-Builder/Smart-City-Intelligence-Pipeline/blob/main/dashboard_main.png)

---

### 📊 2. Prediction Output

Displays the predicted PM2.5 level generated by the trained machine-learning model.

![Prediction](https://github.com/Bit-Byte-Builder/Smart-City-Intelligence-Pipeline/blob/main/prediction_output.png)

---

### 🎯 3. AQI Gauge Visualization

A colour-coded, AQI-style gauge provides an intuitive visual indication of pollution severity.

![AQI Gauge](https://github.com/Bit-Byte-Builder/Smart-City-Intelligence-Pipeline/blob/main/api_gauge.png)

---

### 📈 4. Pollution Trend Analysis

Shows how pollution levels are changing over time and helps identify recent trends.

![Trend](https://github.com/Bit-Byte-Builder/Smart-City-Intelligence-Pipeline/blob/main/trend_chart.png)

---

## 🏗️ Project Architecture

```text
Historical Pollution Data
          │
          ▼
   Data Preparation
          │
          ▼
  Feature Engineering
          │
          ▼
 Model Training & Evaluation
          │
          ▼
   Trained XGBoost Model
          │
          ▼
      Model Artifact
          │
          ▼
   Streamlit Application
       ┌──┴──────────────┐
       │                 │
       ▼                 ▼
Weather API          Air Quality API
       │                 │
       └───────┬─────────┘
               ▼
      Interactive Dashboard
               │
               ▼
     Prediction + Insights
```

## 📁 Project Structure

```text
Smart-City-Intelligence-Pipeline/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── models/
│   ├── feature_columns.pkl
│   └── pollution_model.pkl
│
├── Smart_City_Intelligence_Pipeline.ipynb
│
├── streamlit_dashboard.py
│
├── dashboard_main.png
├── prediction_output.png
├── api_gauge.png
├── trend_chart.png
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 💾 Model Artifacts

The trained model and feature information are stored in the `models/` directory.

```text
models/
├── pollution_model.pkl
└── feature_columns.pkl
```

### pollution_model.pkl

Contains the trained XGBoost regression model used by the Streamlit application to generate PM2.5 predictions.

### feature_columns.pkl

Contains the feature-column structure used during model training. The application uses this artifact to ensure that input features are aligned with the model's expected feature structure.


Keeping these artifacts in the repository allows the deployed application to load the trained model without retraining it every time the application starts.


## 🛠️ Tech Stack

### Programming
- Python
 
### Data Analysis
- Pandas
- NumPy
 
### Machine Learning
- Scikit-learn
- XGBoost

### Visualization
- Plotly
- Matplotlib
- Seaborn
 
### Web Application
- Streamlit

### APIs
- OpenWeather Geocoding API
- OpenWeather Current Weather API
- OpenWeather Air Pollution API

### Model Persistence
- Pickle

## 📦 Installation

Clone the repository:
```bash
git clone https://github.com/Bit-Byte-Builder/Smart-City-Intelligence-Pipeline.git
cd Smart-City-Intelligence-Pipeline
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```


## 🔐 API Configuration

The application uses an external weather and air-quality API.

### Do not hard-code API credentials in streamlit_dashboard.py.

### Local Development

Create the following file in the project directory:
.streamlit/secrets.toml

Add your API key:

```TOML
OPENWEATHER_API_KEY = "your_api_key_here"
```

## ▶️ Run Locally

After configuring the API key, run:

```bash
streamlit run streamlit_dashboard.py
```

## 🧪 Notebook

The repository also includes the original project notebook:

`Smart_City_Intelligence_Pipeline.ipynb`

The notebook contains the data preparation, feature engineering, model development, and evaluation workflow used to build the deployed application.

## 💡 Potential Use Cases

The system can serve as a prototype for:

- Urban air-quality monitoring
- Environmental data analysis
- Pollution trend analysis
- Public awareness dashboards
- Smart-city analytics
- Environmental research
- Predictive pollution monitoring

For real-world deployment, predictions would need to be validated against authoritative monitoring stations and domain-specific environmental standards.

## ⚠️ Limitations

This project is a machine-learning prototype and should not be treated as an official air-quality monitoring or forecasting system.

Important limitations include:

- Model performance depends on the historical dataset and feature availability.
- Real-time API measurements may differ from model predictions.
- The current application relies partly on user-provided recent PM2.5 lag values.
- The application uses a simplified feature construction process for interactive predictions.
- Environmental conditions can change rapidly and may not be fully represented by the available features.
- Model performance should be evaluated using robust temporal validation before production deployment.
- Official air-quality measurements should be preferred for public-health decisions.

## 🔮 Future Improvements

Potential improvements include:

- Automated retrieval of historical PM2.5 lag values.
- More robust time-series validation.
- Multi-step PM2.5 forecasting.
- Additional meteorological variables.
- Traffic and industrial-emission data integration.
- Real-time pollution alerts.
- SMS or notification-based warnings.
- Model monitoring and drift detection.
- Prediction intervals and uncertainty estimation.
- Explainable AI using SHAP.
- Cloud-based scalable deployment.
- Mobile-friendly dashboard.
- Integration with official air-quality monitoring sources.

## 📚 Learning Outcomes

This project provided practical experience in:

- Data preprocessing
- Exploratory Data Analysis
- Feature engineering
- Time-based features
- Regression modelling
- Random Forest
- XGBoost
- Model evaluation
- Model persistence
- API integration
- Streamlit application development
- Interactive data visualization
- Deploying a machine-learning application

## 📌 Conclusion

This project demonstrates an end-to-end machine-learning approach to PM2.5 prediction, covering data preparation, feature engineering, regression modelling, model evaluation, model persistence, real-time API integration, and Streamlit deployment.

It also demonstrates how historical environmental data and real-time information can be combined into an interactive decision-support prototype for exploratory air-quality analysis.

The system is intended as a portfolio and analytical prototype rather than an official air-quality forecasting or monitoring service.

## 👨‍💻 Author

### Sachin Kumar

### 📌 Data Science Enthusiast
