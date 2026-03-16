# 🌾 Agricultural IoT Data Pipeline & Dashboard

A complete end-to-end data engineering project that simulates IoT sensor data from agricultural fields, processes it through an ETL pipeline, stores it in a SQLite data warehouse, and visualizes it on a real-time interactive dashboard.

## 🚀 Live Demo
[👉 Click here to view the dashboard](https://agri-iot-pipeline-ny9dmipfappafqkuxcaczip.streamlit.app/)

## 📌 Features
- **ETL Pipeline** — generates, transforms & loads 500+ IoT sensor readings
- **SQLite Data Warehouse** — structured storage for sensor data
- **Real-time Dashboard** — interactive filters, KPI cards, and 4 charts
- **Irrigation Alerts** — automatic flag when soil moisture drops below 35%

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Data Generation | Python, NumPy, Faker |
| ETL Pipeline | Pandas, SQLite3 |
| Dashboard | Streamlit, Plotly |
| Version Control | Git, GitHub |

## 📁 Project Structure
```
agri-iot-pipeline/
├── data/               # Generated CSV data
├── db/                 # SQLite database
├── pipeline/
│   └── etl.py          # ETL script
├── app/
│   └── dashboard.py    # Streamlit dashboard
├── requirements.txt
└── README.md
```

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/Shrey-003/agri-iot-pipeline.git
cd agri-iot-pipeline
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run ETL Pipeline
```bash
python pipeline/etl.py
```

### 4. Launch Dashboard
```bash
streamlit run app/dashboard.py
```

## 📊 Dashboard Preview
> KPI Cards: Avg Soil Moisture | Avg Temperature | Avg Humidity | Irrigation Alerts  
> Charts: Soil Moisture Over Time | Temperature Distribution | Irrigation Alerts | Rainfall by Field
