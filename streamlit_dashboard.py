import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open("models/pollution_model.pkl", "rb"))

# UI
st.title("Smart City Intelligence Platform")
st.write("Air Pollution Prediction System")

# =========================
# Inputs (OUTSIDE BUTTON)
# =========================
temp = st.number_input("Temperature", value=25.0)
pres = st.number_input("Pressure", value=1013.0)
dewp = st.number_input("Dew Point", value=10.0)
wspm = st.number_input("Wind Speed", value=2.0)

lag1 = st.number_input("PM2.5 Last Hour", value=50.0)
lag2 = st.number_input("PM2.5 2 Hours Ago", value=45.0)
lag3 = st.number_input("PM2.5 3 Hours Ago", value=40.0)

# Wind direction (IMPORTANT)
wd = st.selectbox("Wind Direction", [
    'N','NNE','NE','ENE','E','ESE','SE','SSE',
    'S','SSW','SW','WSW','W','WNW','NW','NNW'
])

# =========================
# Prediction Button
# =========================
if st.button("Predict"):

    # Step 1: Create base features
    features = pd.DataFrame([{
        "TEMP": temp,
        "PRES": pres,
        "DEWP": dewp,
        "WSPM": wspm,
        "PM2.5_lag1": lag1,
        "PM2.5_lag2": lag2,
        "PM2.5_lag3": lag3,
        "PM2.5_rolling_mean_24h": lag1,
        "PM2.5_rolling_std_24h": 1,
        "hour": 12,
        "month": 3
    }])

    # Step 2: Add wind direction columns
    wd_cols = [
        'wd_N','wd_NNE','wd_NE','wd_ENE','wd_E','wd_ESE','wd_SE','wd_SSE',
        'wd_S','wd_SSW','wd_SW','wd_WSW','wd_W','wd_WNW','wd_NW','wd_NNW'
    ]

    for col in wd_cols:
        features[col] = 0

    # Step 3: Set selected wind direction
    features[f'wd_{wd}'] = 1

    # Step 4: Fix column order (CRITICAL)
    feature_columns = pickle.load(open("models/feature_columns.pkl", "rb"))
    features = features.reindex(columns=feature_columns, fill_value=0)

    # Step 5: Predict with error handling
    try:
        prediction = model.predict(features)
        st.success(f"Predicted PM2.5: {prediction[0]:.2f}")

    # Add AQI label
    if prediction[0] <= 30:
        st.success("🟢 Air Quality: Good")
    elif prediction[0] <= 60:
        st.warning("🟡 Air Quality: Moderate")
    elif prediction[0] <= 90:
        st.error("🔴 Air Quality: Poor")
    else:
        st.error("Air Quality: Severe")
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
