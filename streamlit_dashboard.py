import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import logging
import datetime
import plotly.graph_objects as go
import plotly.express as px

# -------------------------------
# ⚙️ CONFIG
# -------------------------------
st.set_page_config(page_title="Smart City Intelligence", layout="wide")

# -------------------------------
# 📝 LOGGING SETUP
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# -------------------------------
# 🎨 Background
# -------------------------------
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

# -------------------------------
# 🌍 GEO LOCATION
# -------------------------------
def get_lat_lon(city, api_key):
    try:
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},IN&limit=1&appid={api_key}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        if len(data) == 0:
            logging.warning(f"Geolocation returned no results for city: {city}")
            return None, None
        return data[0]["lat"], data[0]["lon"]
    except Exception as e:
        logging.error(f"Geolocation API failed for city '{city}': {e}")
        return None, None

# -------------------------------
# 🌦️ WEATHER FETCH (AUTO)
# -------------------------------
def get_weather_data(lat, lon, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={api_key}"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            logging.error(f"Weather API returned status {res.status_code} for lat={lat}, lon={lon}")
            return None

        data = res.json()

        temp = data["main"]["temp"]
        pres = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        # Approximate dew point
        dewp = temp - ((100 - humidity) / 5)

        return temp, pres, dewp, wind

    except Exception as e:
        logging.error(f"Weather API failed for lat={lat}, lon={lon}: {e}")
        return None

# -------------------------------
# 🌫️ REAL AQI
# -------------------------------
def get_real_pm25(lat, lon, api_key):
    try:
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
        return data["list"][0]["components"]["pm2_5"]
    except Exception as e:
        logging.error(f"Air quality API failed for lat={lat}, lon={lon}: {e}")
        return None

# -------------------------------
# 🔑 API KEY — loaded from Streamlit secrets
# -------------------------------
# The API key is stored in .streamlit/secrets.toml and is NEVER committed to the repo.
# .gitignore already excludes .streamlit/secrets.toml.
#
# To set up locally, create the file:
#   .streamlit/secrets.toml
# with the contents:
#   OPENWEATHER_API_KEY = "your_api_key_here"
#
try:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]
except KeyError:
    st.error(
        "🔑 API key not found. Please create `.streamlit/secrets.toml` with:\n\n"
        "OPENWEATHER_API_KEY = \"your_api_key_here\""
    )
    st.stop()

# -------------------------------
# 🤖 LOAD MODEL
# -------------------------------
model = pickle.load(open("models/pollution_model.pkl", "rb"))
feature_columns = pickle.load(open("models/feature_columns.pkl", "rb"))

# -------------------------------
# 🏙️ HEADER
# -------------------------------
st.title("🏙️ Smart City Intelligence Pipeline")
st.caption("AI-powered Air Quality Monitoring & Prediction")

# -------------------------------
# 🌍 CITY INPUT
# -------------------------------
city = st.text_input("Enter City", "Katihar")

lat, lon = get_lat_lon(city, API_KEY)

if lat:
    st.success(f"📍 Location: {city}")
else:
    st.warning("⚠️ Location not found")

# -------------------------------
# 🌦️ AUTO WEATHER
# -------------------------------
weather = None

if lat and lon:
    weather = get_weather_data(lat, lon, API_KEY)

    if weather:
        temp, pres, dewp, wspm = weather

        st.success("🌦️ Weather auto-fetched")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Temp (°C)", temp)
        c2.metric("Pressure", pres)
        c3.metric("Dew Point", f"{dewp:.2f}")
        c4.metric("Wind Speed", wspm)

    else:
        st.warning("⚠️ Could not fetch weather data")

# -------------------------------
# 📥 USER INPUT (ONLY LAGS NOW)
# -------------------------------
lag1 = st.number_input("PM2.5 Last Hour", 0.0, 500.0, 50.0)
lag2 = st.number_input("PM2.5 2 Hours Ago", 0.0, 500.0, 45.0)
lag3 = st.number_input("PM2.5 3 Hours Ago", 0.0, 500.0, 40.0)

wd = st.selectbox("Wind Direction", [
    'N','NNE','NE','ENE','E','ESE','SE','SSE',
    'S','SSW','SW','WSW','W','WNW','NW','NNW'
])

# -------------------------------
# 🔮 PREDICT
# -------------------------------
if st.button("🚀 Predict AQI"):

    try:
        if weather is None:
            st.error("Weather data not available. Cannot predict.")
            st.stop()

        # -------------------------------
        # ⏱️ REAL-TIME FEATURE ENGINEERING
        # -------------------------------
        # Use actual current time instead of hardcoded constants
        now = datetime.datetime.now()
        current_hour = now.hour
        current_month = now.month

        # Compute rolling statistics from user-provided lag values
        # instead of using a hardcoded constant of 1
        pm25_values = [lag1, lag2, lag3]
        rolling_mean = float(np.mean(pm25_values))
        if len(pm25_values) > 1:
            rolling_std = float(np.std(pm25_values, ddof=1))
        else:
            rolling_std = 0.0

        # Feature engineering
        features = pd.DataFrame([{
            "TEMP": temp,
            "PRES": pres,
            "DEWP": dewp,
            "WSPM": wspm,
            "PM2.5_lag1": lag1,
            "PM2.5_lag2": lag2,
            "PM2.5_lag3": lag3,
            "PM2.5_rolling_mean_24h": rolling_mean,
            "PM2.5_rolling_std_24h": rolling_std,
            "hour": current_hour,
            "month": current_month
        }])

        wd_cols = [
            'wd_N','wd_NNE','wd_NE','wd_ENE','wd_E','wd_ESE','wd_SE','wd_SSE',
            'wd_S','wd_SSW','wd_SW','wd_WSW','wd_W','wd_WNW','wd_NW','wd_NNW'
        ]

        for col in wd_cols:
            features[col] = 0

        features[f'wd_{wd}'] = 1

        features = features.reindex(columns=feature_columns, fill_value=0)

        # Prediction
        pred = model.predict(features)[0]

        # -------------------------------
        # 📊 METRICS
        # -------------------------------
        m1, m2, m3 = st.columns(3)
        m1.metric("Predicted PM2.5", f"{pred:.2f}")
        m2.metric("Last Hour", lag1)
        m3.metric("Wind Speed", wspm)

        # -------------------------------
        # 🌈 AQI LABEL
        # -------------------------------
        if pred <= 30:
            set_background("#d4edda")
            label = "🟢 Good"
        elif pred <= 60:
            set_background("#fff3cd")
            label = "🟡 Moderate"
        elif pred <= 90:
            set_background("#ffe5b4")
            label = "🟠 Poor"
        else:
            set_background("#f8d7da")
            label = "🔴 Severe"

        st.subheader(f"Air Quality: {label}")

        # -------------------------------
        # 🌍 REAL AQI
        # -------------------------------
        if lat:
            real = get_real_pm25(lat, lon, API_KEY)

            if real:
                st.info(f"🌍 Real PM2.5: {real:.2f}")
                st.write(f"📉 Model Error: {(real - pred):.2f}")
            else:
                st.warning("⚠️ Could not fetch real-time AQI")

        # -------------------------------
        # 📈 TREND
        # -------------------------------
        trend_df = pd.DataFrame({
            "Time": ["-3h", "-2h", "-1h", "Now"],
            "PM2.5": [lag3, lag2, lag1, pred]
        })

        fig_line = px.line(trend_df, x="Time", y="PM2.5",
                           markers=True, title="PM2.5 Trend")

        st.plotly_chart(fig_line, use_container_width=True)

        # -------------------------------
        # 🎯 GAUGE
        # -------------------------------
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pred,
            title={'text': "PM2.5 Level"},
            gauge={
                'axis': {'range': [0, 200]},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 60], 'color': "yellow"},
                    {'range': [60, 90], 'color': "orange"},
                    {'range': [90, 200], 'color': "red"},
                ],
            }
        ))

        st.plotly_chart(fig_gauge, use_container_width=True)

    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        st.error(f"Error: {str(e)}")
