import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# 1️⃣ Import the exact functions from your team's files
from data_loader import load_data
from preprocessing import clean_data1, clean_data2, merge
from visualization import plot_yearly_growth, plot_solar_vs_wind, plot_regional_distribution, plot_forecast
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
            # 2️⃣ Load and clean the raw data using team's functions
            data1_raw, data2_raw = load_data()
            d1_cleaned = clean_data1(data1_raw)
            d2_cleaned = clean_data2(data2_raw)
            df_merged = merge(d1_cleaned, d2_cleaned)
            
            # 🛠️ EXACT COLUMNS MATCHING FIX
            # Force creating 'Capacity' column to satisfy custom plotting functions
            if 'Capacity (MW)' in df_merged.columns:
                df_merged['Capacity'] = df_merged['Capacity (MW)']
            
            if 'Capacity (MW)' in d1_cleaned.columns:
                d1_cleaned['Capacity'] = d1_cleaned['Capacity (MW)']

            st.success("🎯 Backend Pipeline executed successfully from main.py files!")
            
            # 3️⃣ Calculate real KPI metrics dynamically using proper database columns
            total_projects = len(df_merged)
            total_current_capacity = df_merged['Capacity'].sum()
            avg_capacity = df_merged['Capacity'].mean()
            
            # 4️⃣ Display real system KPI metrics calculated from your actual data
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Total Tracked Projects", value=f"{total_projects} Projects")
            with col2:
                st.metric(label="Total System Capacity", value=f"{int(total_current_capacity):,} MW")
            with col3:
                st.metric(label="Average Project Capacity", value=f"{avg_capacity:.2f} MW")
                
            st.write("---")
            
            # 5️⃣ Grid Layout for the actual team Charts (Matching your main.py order)
            st.subheader("📊 Team System Visualizations & AI Forecasts")
            
            # First row of charts: Growth and Solar vs Wind
            c1, c2 = st.columns(2)
            with c1:
                st.write("### Yearly Renewable Growth (Installed)")
                fig1 = plt.figure(figsize=(8, 4.5))
                # Pass d1_cleaned with the enforced 'Capacity' column
                plot_yearly_growth(d1_cleaned)
                st.pyplot(plt.gcf())
                plt.close(fig1)
                
            with c2:
                st.write("### Solar vs Wind Capacity Comparison")
                fig2 = plt.figure(figsize=(8, 4.5))
                plot_solar_vs_wind(df_merged)
                st.pyplot(plt.gcf())
                plt.close(fig2)
                
            # Second row of charts: Regional and Vision 2030 AI Forecast
            c3, c4 = st.columns(2)
            with c3:
                st.write("### Regional Project Distribution")
                fig3 = plt.figure(figsize=(8, 4.5))
                plot_regional_distribution(df_merged)
                st.pyplot(plt.gcf())
                plt.close(fig3)
                
            with c4:
                st.write("### Future Renewable Energy Capacity Forecast (Vision 2030)")
                fig4 = plt.figure(figsize=(8, 4.5))
                # Generate forecast using team's prediction logic and unpack values
                future_2030, vision_target, trend_fit, yearly, slope = plot_forecast(df_merged, forecast_until=2030)
                st.pyplot(plt.gcf())
                plt.close(fig4)
                
            # 6️⃣ Display Dataframe at the bottom
            st.write("---")
            st.subheader("📋 Cleaned Dataset Main Preview")
            st.dataframe(df_merged, use_container_width=True)
                    
        except Exception as e:
            st.error(f"Pipeline Execution Error: {str(e)}")
