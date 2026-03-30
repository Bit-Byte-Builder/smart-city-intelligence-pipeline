import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open("models/pollution_model.pkl", "rb"))

st.title("Smart City Intelligence Platform")

st.write("Air Pollution Prediction System")

# Inputs
temp = st.number_input("Temperature")
pres = st.number_input("Pressure")
dewp = st.number_input("Dew Point")
wspm = st.number_input("Wind Speed")

lag1 = st.number_input("PM2.5 Last Hour")
lag2 = st.number_input("PM2.5 2 Hours Ago")
lag3 = st.number_input("PM2.5 3 Hours Ago")

if st.button("Predict"):

    # Step 1: Create features FIRST
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

    # Step 2: Define wd features
    wd_features = [
        'wd_N','wd_NNE','wd_NE','wd_ENE','wd_E','wd_ESE','wd_SE','wd_SSE',
        'wd_S','wd_SSW','wd_SW','wd_WSW','wd_W','wd_WNW','wd_NW','wd_NNW'
    ]

    # Step 3: Add missing columns
    for col in wd_features:
        features[col] = 0

    # Step 4: Set one direction
    features['wd_NE'] = 1

    # Ensure correct column order (VERY IMPORTANT)
    features = features.reindex(sorted(features.columns), axis=1)

    # Step 5: Predict
    prediction = model.predict(features)

    st.success(f"Predicted PM2.5: {prediction[0]:.2f}")

