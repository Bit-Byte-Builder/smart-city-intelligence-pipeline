import streamlit as st
import pickle
import numpy as np

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
    import pandas as pd

features = pd.DataFrame([{
    'TEMP', 'PRES', 'DEWP', 'WSPM', 'PM2.5_lag1', 'PM2.5_lag2',
       'PM2.5_lag3', 'PM2.5_rolling_mean_24h', 'PM2.5_rolling_std_24h', 'hour',
       'month', 'wd_E', 'wd_ENE', 'wd_ESE', 'wd_N', 'wd_NE', 'wd_NNE',
       'wd_NNW', 'wd_NW', 'wd_S', 'wd_SE', 'wd_SSE', 'wd_SSW', 'wd_SW', 'wd_W',
       'wd_WNW', 'wd_WSW'
}])
    
prediction = model.predict(features)
    
st.success(f"Predicted PM2.5: {prediction[0]:.2f}")
