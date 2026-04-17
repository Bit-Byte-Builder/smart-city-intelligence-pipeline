# 🌆 Smart City Air Quality Prediction System

> 🚦 Think of it as a "weather app for pollution" — but with prediction + real-time insights.

---

## 🚀 Key Highlights

- Predicts future air pollution levels (PM2.5) before they become harmful  
- Combines ML predictions with real-time weather & AQI data  
- Detects gaps between predicted vs actual pollution (model performance insight)  
- Interactive dashboard for easy decision-making  
- Supports early action like traffic control & pollution alerts  

---

A system that predicts air pollution levels and combines them with live data to help cities act before pollution becomes dangerous.

🚧 Deployment in progress  

---

## 📌 Overview

This project acts like a **pollution forecast system for cities**.

Just like a weather app predicts rain, this system predicts air pollution levels (PM2.5) in advance and combines them with real-time data.

It helps cities take early action instead of reacting after pollution becomes dangerous.

---

## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn, XGBoost  
- Matplotlib, Seaborn  
- Streamlit (deployment)  

---

## 🧠 Feature Engineering

- Lag features (PM2.5_lag1, lag2, lag3)  
- Rolling statistics (24-hour mean & std)  
- Rate of change (PM2.5_diff)  
- Time features (hour, month)  
- Wind direction encoding  

---

## 🤖 Models Used

- Random Forest Regressor  
- XGBoost Regressor (final model)  

---

## 📈 Model Comparison

| Model              | MAE        | R2 Score |
|--------------------|------------|----------|
| Random Forest      | 10.338469  | 0.942163 |
| Baseline XGBoost   | 10.0561    | 0.9477   |
| Optimized XGBoost  | 10.0785    | 0.9479   |

👉 **Insight:**  
Optimized XGBoost provided slightly better accuracy and more stable predictions.

👉 **Why it matters:**  
More accurate predictions mean better early warnings, helping authorities act before pollution spikes.

---

## 📁 Project Structure
smart-city-air-quality/
│
├── data/ # Raw & processed datasets
├── notebooks/ # EDA & experimentation
├── src/ # Core ML pipeline
├── models/ # Trained models (.pkl)
├── app/ # Streamlit dashboard
├── requirements.txt # Dependencies
└── README.md

---

## 📸 Dashboard Preview

---

### 🏙️ 1. Smart Dashboard Interface
This is the main control panel where users enter a city and instantly get live weather + pollution inputs.  
Think of it like a **pollution control room dashboard**.

![Dashboard](https://github.com/Bit-Byte-Builder/smart-city-intelligence-pipeline/blob/main/dashboard_main.png)

---

### 📊 2. Prediction Output
Shows predicted PM2.5 levels before pollution actually rises.  
Like a **weather forecast, but for pollution spikes**.

![Prediction](https://github.com/Bit-Byte-Builder/smart-city-intelligence-pipeline/blob/main/prediction_output.png)

---

### 🎯 3. AQI Gauge Visualization
A color-coded speedometer-style chart that quickly tells how bad the air is.  
Green = Safe, Red = Dangerous.

![AQI Gauge](https://github.com/Bit-Byte-Builder/smart-city-intelligence-pipeline/blob/main/api_guage.png)

---

### 📈 4. Pollution Trend Analysis
Shows how pollution is changing over time.  
Helps identify whether things are **improving or getting worse**.

![Trend](https://github.com/Bit-Byte-Builder/smart-city-intelligence-pipeline/blob/main/trend_chart.png)
---

## 🎯 Use Cases

- City authorities monitoring pollution trends  
- Public health awareness & alerts  
- Urban planning & traffic regulation  
- Environmental research & analysis  

---

## ⚙️ How to Run

```bash
git clone <repo-link>
cd smart-city-air-quality

pip install -r requirements.txt
streamlit run app/streamlit_dashboard.py

🔮 Future Improvements
> Add traffic & industrial emission data
> Real-time alerts (SMS / notifications)
> Deploy on cloud (AWS / GCP)
> Mobile-friendly dashboard

👨‍💻 Author

Sachin Kumar
📌 Data Science Enthusiast
