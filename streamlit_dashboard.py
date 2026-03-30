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
    features = np.array([[temp, pres, dewp, wspm, lag1, lag2, lag3]])
    
    prediction = model.predict(features)
    
    st.success(f"Predicted PM2.5: {prediction[0]:.2f}")
