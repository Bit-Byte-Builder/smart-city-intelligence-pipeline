import streamlit as st

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
    st.success("App is working 🚀 (model will be connected next)")
