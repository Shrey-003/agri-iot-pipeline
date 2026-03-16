import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="Agri IoT Dashboard", layout="wide", page_icon="🌾")
st.title("🌾 Agricultural IoT Sensor Dashboard")

@st.cache_data
def load_data():
    conn = sqlite3.connect("db/agri.db")
    df = pd.read_sql("SELECT * FROM sensor_readings", conn)
    conn.close()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
location = st.sidebar.multiselect("Select Field", df["location"].unique(), default=df["location"].unique())
sensor = st.sidebar.multiselect("Select Sensor", df["sensor_id"].unique(), default=df["sensor_id"].unique())
filtered = df[(df["location"].isin(location)) & (df["sensor_id"].isin(sensor))]

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Soil Moisture", f"{filtered['soil_moisture'].mean():.1f}%")
col2.metric("Avg Temperature", f"{filtered['temperature_c'].mean():.1f}°C")
col3.metric("Avg Humidity", f"{filtered['humidity_pct'].mean():.1f}%")
col4.metric("Irrigation Alerts", filtered[filtered["irrigation_alert"] == "YES"].shape[0])

st.divider()

# Charts
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("Soil Moisture Over Time")
    fig1 = px.line(filtered.sort_values("timestamp"), x="timestamp", y="soil_moisture",
                   color="location", template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

with col_b:
    st.subheader("Temperature Distribution by Field")
    fig2 = px.box(filtered, x="location", y="temperature_c",
                  color="location", template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

col_c, col_d = st.columns(2)
with col_c:
    st.subheader("Irrigation Alert Breakdown")
    alert_counts = filtered["irrigation_alert"].value_counts().reset_index()
    fig3 = px.pie(alert_counts, names="irrigation_alert", values="count",
                  color_discrete_map={"YES": "red", "NO": "green"})
    st.plotly_chart(fig3, use_container_width=True)

with col_d:
    st.subheader("Avg Rainfall by Field")
    rain_df = filtered.groupby("location")["rainfall_mm"].mean().reset_index()
    fig4 = px.bar(rain_df, x="location", y="rainfall_mm",
                  color="location", template="plotly_dark")
    st.plotly_chart(fig4, use_container_width=True)

st.divider()
st.subheader("📋 Raw Sensor Readings")
st.dataframe(filtered.tail(100), use_container_width=True)
