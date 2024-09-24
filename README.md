# OVERVIEW
This repository contains jupyter notebook and data for exploring an air quality dataset. The dataset includes information about various air pollutants such as SO2, NO2, CO, O3, as well as temperature, pressure, rain, wind direction, and wind speed.
## VARIABLE:
- SO2: Sulfur dioxide concentration
- NO2: Nitrogen dioxide concentration
- CO: Carbon monoxide concentration
- O3: Ozone concentration
- Temperature: Temperature in degrees Celsius
- Pressure: Atmospheric pressure
- Rain: Rainfall amount
- Wind Direction: Direction of wind
- Wind Speed: Speed of wind

## ANALYSIS TASK:
Data Gathering: Gather and load the dataset into Python environment.
Data Cleaning: Clean the dataset by handling missing values and inconsistencies.
Exploratory Data Analysis (EDA): Perform EDA to understand the distribution and relationships among different variables.
Plotting (Visualization): Create visualizations such as scatter plots, bar charts, and time series plots to explore the data.
Summary: Calculate summary statistics for different pollutants and meteorological parameters.

## Setup Environment - Anaconda
**conda create --name main-ds python=3.12.3
conda activate main-ds
pip install -r requirements.txt**

## Setup Environment - Shell/Terminal
install dependensi:
mkdir AirQuality_Analyst
cd AirQuality_Analyst
pipenv install
pipenv shell
pip install -r requirements.txt

install streamlit:
pip install streamlit-folium
'''

## Run steamlit app
Lokal:
C:\Users\nurul alam\Desktop\AirQuality_Analyst>
Cd Dashboard
streamlit run Dashboard_air.py

Streamlit cloud:
https://airqualityanalystt.streamlit.app/
