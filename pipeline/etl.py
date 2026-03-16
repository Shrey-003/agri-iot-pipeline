import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import random
import os

def generate_sensor_data(n=500):
    np.random.seed(42)
    base_time = datetime.now() - timedelta(hours=n)
    records = []
    for i in range(n):
        timestamp = base_time + timedelta(hours=i)
        records.append({
            "timestamp": timestamp,
            "sensor_id": random.choice(["S001", "S002", "S003", "S004"]),
            "location": random.choice(["Field_A", "Field_B", "Field_C"]),
            "soil_moisture": round(np.random.normal(45, 10), 2),
            "temperature_c": round(np.random.normal(28, 5), 2),
            "humidity_pct": round(np.random.normal(60, 15), 2),
            "rainfall_mm": round(max(0, np.random.normal(3, 4)), 2)
        })
    df = pd.DataFrame(records)
    df.to_csv("data/sensor_data.csv", index=False)
    print(f"Generated {n} records.")
    return df

def transform(df):
    df.dropna(inplace=True)
    df["soil_moisture"] = df["soil_moisture"].clip(0, 100)
    df["humidity_pct"] = df["humidity_pct"].clip(0, 100)
    df["temperature_c"] = df["temperature_c"].clip(-10, 60)
    df["irrigation_alert"] = df["soil_moisture"].apply(
        lambda x: "YES" if x < 35 else "NO"
    )
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    df["date"] = pd.to_datetime(df["timestamp"]).dt.date
    print("Transform complete.")
    return df

def load(df, db_path="db/agri.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("sensor_readings", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Loaded {len(df)} rows into {db_path}.")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    os.makedirs("db", exist_ok=True)
    df = generate_sensor_data(500)
    df = transform(df)
    load(df)
    print("ETL Pipeline complete!")
