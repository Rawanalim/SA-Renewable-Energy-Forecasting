import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1️⃣ Import the exact functions from your team's files
from data_loader import load_data
from preprocessing import clean_data1, clean_data2, merge
from model import train_forecaster, forecast_future
from visualization import plot_forecast
from evaluation import evaluate_forecast

# Application page configuration
st.set_page_config(page_title="Saudi Renewable Energy AI", page_icon="🇸🇦", layout="wide")

st.title("🇸🇦 Saudi Arabia Renewable Energy Forecasting Platform")
st.subheader("Automated MLOps Production Dashboard Linked directly to main.py scripts")

st.write("---")

# Sidebar dashboard control panel
st.sidebar.header("🛠️ Pipeline Controller")
run_pipeline = st.sidebar.button("🚀 Run Live AI Pipeline")

# Execute core pipeline upon button click or default load
if run_pipeline or True:
    with st.spinner("Executing core main.py pipeline models..."):
        try:
            # 2️⃣ Execute core team pipeline steps sequentially
            data1_raw, data2_raw = load_data()
            d1_cleaned = clean_data1(data1_raw)
            d2_cleaned = clean_data2(data2_raw)
            df_raw = merge(d1_cleaned, d2_cleaned)
            
            st.success("🎯 Backend Pipeline executed successfully from main.py files!")
            
            # 3️⃣ Calculate real metrics dynamically to display on top metrics block
            total_projects = len(df_raw)
            total_current_capacity = df_raw['Capacity (MW)'].sum()
            avg_capacity = df_raw['Capacity (MW)'].mean()
            
            # 4️⃣ Display real system KPI metrics calculated from your actual data
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Total Tracked Projects", value=f"{total_projects} Projects")
            with col2:
                st.metric(label="Total System Capacity", value=f"{int(total_current_capacity):,} MW")
            with col3:
                st.metric(label="Average Project Capacity", value=f"{avg_capacity:.2f} MW")
                
            st.write("---")
            
            # 5> Side-by-Side layout for Dataframe and the actual team Forecast Chart
            left_col, right_col = st.columns(2)
            with left_col:
                st.subheader("📋 Core Cleaned & Merged Data Preview")
                st.dataframe(df_raw, use_container_width=True)
                
            with right_col:
                st.subheader("📈 Team Generated AI System Forecast")
                
                # 6️⃣ Capture and display the exact matplotlib plot from visualization.py
                # Since plot_forecast doesn't return text, we capture the active plt figure
                fig, ax = plt.subplots()
                plot_forecast(df_raw) # Calls
