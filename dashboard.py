import streamlit as st
import pandas as pd
import os

# -------------------------------
# ⚙️ Page Config
# -------------------------------
st.set_page_config(page_title="Urban Crash Dashboard", layout="wide")

st.title("🚦 Urban Crash Analytics Dashboard")

# -------------------------------
# 📂 Gold Layer Path
# -------------------------------
BASE_PATH = "data_lake/gold"   # 👉 change to /app/data_lake/gold if using Docker

crash_area_path = os.path.join(BASE_PATH, "crash_by_area")
monthly_trend_path = os.path.join(BASE_PATH, "monthly_trend")
high_risk_path = os.path.join(BASE_PATH, "high_risk")

# -------------------------------
# 📥 Load Data
# -------------------------------
@st.cache_data
def load_data():
    crash_area = pd.read_parquet(crash_area_path)
    monthly_trend = pd.read_parquet(monthly_trend_path)
    high_risk = pd.read_parquet(high_risk_path)
    return crash_area, monthly_trend, high_risk

try:
    crash_area, monthly_trend, high_risk = load_data()
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# -------------------------------
# 🧠 Smart Column Detection
# -------------------------------
def get_category_column(df):
    # pick string column (area/month/street)
    for col in df.columns:
        if df[col].dtype == "object":
            return col
    return df.columns[0]

def get_value_column(df, category_col):
    # pick numeric column (count)
    for col in df.columns:
        if col != category_col:
            return col

# Detect columns dynamically
area_col = get_category_column(crash_area)
area_val = get_value_column(crash_area, area_col)

month_col = get_category_column(monthly_trend)
month_val = get_value_column(monthly_trend, month_col)

street_col = get_category_column(high_risk)
street_val = get_value_column(high_risk, street_col)

# -------------------------------
# 📊 KPI Section
# -------------------------------
st.subheader("📌 Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Areas", len(crash_area))
col2.metric("Total Crashes", int(crash_area[area_val].sum()))
col3.metric("High Risk Streets", len(high_risk))

# -------------------------------
# 📍 Crash by Area
# -------------------------------
st.subheader("📍 Crash Count by Area")

st.bar_chart(crash_area.set_index(area_col)[area_val])

with st.expander("View Data"):
    st.dataframe(crash_area)

# -------------------------------
# 📅 Monthly Trend
# -------------------------------
st.subheader("📅 Monthly Crash Trend")

st.line_chart(monthly_trend.set_index(month_col)[month_val])

with st.expander("View Data"):
    st.dataframe(monthly_trend)

# -------------------------------
# 🚨 High Risk Streets
# -------------------------------
st.subheader("🚨 Top High Risk Streets")

st.bar_chart(high_risk.set_index(street_col)[street_val])

with st.expander("View Data"):
    st.dataframe(high_risk)

# -------------------------------
# 🔍 Filter Section
# -------------------------------
st.subheader("🔍 Filter by Area")

selected_area = st.selectbox(f"Select {area_col}", crash_area[area_col].unique())

filtered_data = crash_area[crash_area[area_col] == selected_area]

st.write(f"📊 Data for {selected_area}")
st.dataframe(filtered_data)

# -------------------------------
# 🧪 Debug Section (optional)
# -------------------------------
with st.expander("⚙️ Debug Info"):
    st.write("Crash Area Columns:", crash_area.columns)
    st.write("Monthly Trend Columns:", monthly_trend.columns)
    st.write("High Risk Columns:", high_risk.columns)

# -------------------------------
# ✅ Footer
# -------------------------------
st.markdown("---")
st.success("✅ Dashboard running successfully from Gold Layer!")