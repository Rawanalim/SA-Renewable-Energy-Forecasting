# Renewable Energy Forecasting - Saudi Arabia

Predicting Renewable Energy Capacity in Saudi Arabia using Machine Learning and Data Analysis.

## Overview

This project analyzes renewable energy growth in Saudi Arabia using official datasets from Data Saudi and KAPSARC.

The system processes installed and planned renewable energy projects, generates visualizations, and forecasts future renewable energy capacity using a Linear Regression model.

The project focuses on:
- Renewable energy growth analysis
- Solar vs Wind comparison
- Regional distribution analysis
- Forecasting renewable energy capacity until 2030
- Comparing forecasted results with Vision 2030 targets

## Forecasting Model

The project uses a Linear Regression model to learn historical cumulative renewable energy growth trends and forecast future renewable energy capacity until 2030.

The forecasted results are compared with the Vision 2030 renewable energy benchmark of approximately 58.7 GW.

## Code Structure

| Function | Description |
|---|---|
| `load_data()` | Load renewable energy datasets |
| `clean_data1(data1)` | Clean the first dataset |
| `clean_data2(data2)` | Clean and standardize the second dataset |
| `create_raw_dataset(data1, data2)` | Merge cleaned datasets |
| `train_renewable_model(X, y)` | Train Linear Regression forecasting model |
| `plot_yearly_growth(df_raw)` | Visualize yearly renewable energy growth |
| `plot_solar_vs_wind(df_raw)` | Compare solar and wind energy |
| `plot_regional_distribution(df_raw)` | Visualize regional distribution |
| `plot_forecast(df_raw)` | Forecast renewable energy capacity |
| `evaluate_forecast(...)` | Evaluate forecasting performance |

## Project Pipeline

Data Collection  
→ Data Preprocessing  
→ Forecasting Model  
→ Forecast Evaluation  
→ Visualization  

## Evaluation Metrics

- Trend Fit (R²)
- Achievement Rate
- Gap Analysis
- Estimated Yearly Growth

## Getting Started

Install required packages:

pip install pandas numpy matplotlib scikit-learn

Place the following datasets inside the `data/` folder:

- saudi-arabia-planned-and-installed-renewables-by-project.csv
- renewable_energy_projects.csv

## Tech Stack

- Pandas
- NumPy
- Scikit-learn
- Linear Regression
- Matplotlib
