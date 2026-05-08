# Renewable Energy Forecasting - SA

**Predicting Renewable Energy Capacity in Saudi Arabia using Machine Learning.**

This project provides a software framework to analyze renewable energy data (Solar, Wind, etc.) in the Kingdom of Saudi Arabia, featuring a predictive model to estimate production capacities for future projects.

## Overview

The project focuses on processing two main types of data:

* Installed Projects: Current real-world operational capacities.

* Planned Projects: Targeted future expansions.

The model utilizes the Linear Regression algorithm to establish relationships between various factors and the resulting energy capacity.

## Code Structure
| Function | Descreption |
| --- | --- |
| load_data() | load two different files from a local directory |
| clean_data1(data1) | Handle the Missing Values and drop the unnecessary Columns |
| clean_data2(data2) | drop the unnecessary Columns, add city column and rename some columns to match data1 |
| merge_and_encode(data1, data2) | stack the cleaned datasets. then Standardize and encode the columns to ensure optimal model training |
| split_installed_planned(df) | Separate installed and planned rows to make to DataFrame |
| train_renewable_model(X_train, y_train) | use Linear Regression to train the model on historical project data to forecast the expected energy capacity |
| get_predictions(model, X_test) | Predect the estimated capacity or output for the projects in testing set |
| evaluate_model(y_test, y_pred) | use $R^2$ and MAE and MSE to evaluate the model performance |
## Getting Started

 [1] Prerequisites
 
  Ensure you have the following packages installed:
  
  * pip install pandas scikit-learn
  
 [2] Data Setup
 
  Place the following files in a folder named data/:
  
  * saudi-arabia-planned-and-installed-renewables-by-project.csv
  * renewable_energy_projects.csv

## Tech Stack

* Pandas: For large-scale data manipulation and energy dataset cleaning.
* Scikit-learn: For building and evaluating predictive machine learning models.
* Linear Regression: The primary algorithm used for capacity forecasting.
