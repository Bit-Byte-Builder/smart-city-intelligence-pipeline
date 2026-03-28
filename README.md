# 🌆 Smart City Intelligence Platform

## 🚀 Key Highlights

- Advanced time-series feature engineering  
- Model comparison (Random Forest vs XGBoost)  
- End-to-end ML pipeline  
- Deployable Streamlit application  

---

End-to-end Machine Learning system for predicting urban air pollution (PM 2.5) using time-series envirronmental data. 

🚧 Deployment in progress

---

## 📌 Overview

This project predicts **PM2.5 air pollution levels** using environmental and time-series data.

It simulates a **Smart City AI system** that helps in:

- monitoring pollution
- forecasting air quality
- supporting urban decision-making

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

  Model              | MAE        | R2 Score   
| :----------------- | :--------- | :--------- |
| Random Forest      | 10.338469  | 0.942163   |
| Baseline XGBoost   | 10.0561    | 0.9477     |
| Optimized XGBoost  | 10.0785    | 0.9479     |

Optimized XGBoost model performed better with lower error and higher predictive accuracy compared to Random Forest. This system can help city authorities anticipate pollution spikes and take preventive actions.

---

## 📁 Project Structure

smart-city-intelligence-platform

├── data/
├── notebooks/
│ └── smart_city_analysis.ipynb
├── src/
├── models/
│ └── pollution_model.pkl
├── app/
│ └── streamlit_dashboard.py
├── requirements.txt
└── README.md

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app/streamlit_dashboard.py

## 🌐 Live Demo

Deployment in progress 🚧

💼 Author

Sachin Kumar 
