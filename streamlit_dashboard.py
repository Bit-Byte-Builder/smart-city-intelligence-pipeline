import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go

# -----------------------------
# Background color function
# -----------------------------
def set_background(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Load model
# -----------------------------
model = pickle.load(open("models/pollution_model.pkl", "rb"))
feature_columns = pickle.load(open("models/feature_columns.pkl", "rb"))

# -----------------------------
# UI
# -----------------------------
st.title("🌆 Smart City Intelligence Platform")
st.write("Air Pollution Prediction System")

# -----------------------------
# Inputs
# -----------------------------
temp = st.number_input("Temperature")
pres = st.number_input("Pressure")
dewp = st.number_input("Dew Point")
wspm = st.number_input("Wind Speed")

lag1 = st.number_input("PM2.5 Last Hour")
lag2 = st.number_input("PM2.5 2 Hours Ago")
lag3 = st.number_input("PM2.5 3 Hours Ago")

wd = st.selectbox("Wind Direction", [
    'N','NNE','NE','ENE','E','ESE','SE','SSE',
    'S','SSW','SW','WSW','W','WNW','NW','NNW'
])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    try:
        # Step 1: Create features
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

        # Step 2: Wind encoding
        wd_cols = [
            'wd_N','wd_NNE','wd_NE','wd_ENE','wd_E','wd_ESE','wd_SE','wd_SSE',
            'wd_S','wd_SSW','wd_SW','wd_WSW','wd_W','wd_WNW','wd_NW','wd_NNW'
        ]

        for col in wd_cols:
            features[col] = 0

        features[f'wd_{wd}'] = 1

        # Step 3: Fix column order
        features = features.reindex(columns=feature_columns, fill_value=0)

        # Step 4: Predict
        prediction = model.predict(features)
        value = prediction[0]

        st.success(f"Predicted PM2.5: {value:.2f}")

        # -----------------------------
        # AQI Label + Background
        # -----------------------------
        if value <= 30:
            set_background("#d4edda")
            st.success("🟢 Air Quality: Good")

        elif value <= 60:
            set_background("#fff3cd")
            st.warning("🟡 Air Quality: Moderate")

        elif value <= 90:
            set_background("#ffe5b4")
            st.error("🟠 Air Quality: Poor")

        else:
            set_background("#f8d7da")
            st.error("🔴 Air Quality: Severe")

        # -----------------------------
        # Gauge Chart
        # -----------------------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': "PM2.5 Level"},
            gauge={
                'axis': {'range': [0, 200]},
                'bar': {'color': "black"},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 60], 'color': "yellow"},
                    {'range': [60, 90], 'color': "orange"},
                    {'range': [90, 200], 'color': "red"},
                ],
            }
        ))

        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Error: {str(e)}")
