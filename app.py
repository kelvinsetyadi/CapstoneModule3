import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("d:/Purwadhika/xgboostmodel.pkl")

model = load_model()

# Mapping ocean proximity to coordinates and average values
location_mapping = {
    'San Francisco': (-122.4194, 37.7749),
    'Oakland': (-122.2711, 37.8044),
    'Alameda': (-122.2430, 37.7652),
    'Los Angeles': (-118.2437, 34.0522),
    'Long Beach': (-118.1937, 33.7701),
    'Santa Monica': (-118.4912, 34.0195),
    'Fresno': (-119.7871, 36.7378),
    'Bakersfield': (-119.0187, 35.3733),
    'Sacramento': (-121.4944, 38.5816),
    'Santa Barbara': (-119.6982, 34.4208),
    'San Diego': (-117.1611, 32.7157),
    'Monterey': (-121.8947, 36.6002),
    'Avalon': (-118.3278, 33.3428)
}

# UI
st.title("California Housing Price Predictor")

ocean_proximity_mapping = {
    'NEAR BAY': ['San Francisco', 'Oakland', 'Alameda'],
    '<1H OCEAN': ['Los Angeles', 'Long Beach', 'Santa Monica'],
    'INLAND': ['Fresno', 'Bakersfield', 'Sacramento'],
    'NEAR OCEAN': ['Santa Barbara', 'San Diego', 'Monterey'],
    'ISLAND': ['Avalon']
}

# Inputs
ocean_proximity = st.selectbox("Select Ocean Proximity", list(ocean_proximity_mapping.keys()))
city = st.selectbox("Select City", ocean_proximity_mapping[ocean_proximity])
income = st.number_input(
    "Monthly Income ($)",
    min_value=1000,
    max_value=15000,
    value=3000,
    step=100,
    help="Enter estimated household monthly income (in USD)"
)
house_age = st.slider("House Age (Years)", 1, 52, 10)
rooms = st.slider("Number of Rooms", 5, 400, 100)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)

# Derived/assumed values
longitude, latitude = location_mapping[city]
population = 1000  # dummy value or compute from rooms
households = 100   # dummy or derived value
total_rooms = rooms
total_bedrooms = bedrooms
median_income = (income * 12) / 10000
housing_median_age = house_age

# Create input DataFrame
input_data = pd.DataFrame([{
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'ocean_proximity': ocean_proximity
}])

# Prediction
if st.button("Predict Housing Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Housing Price: ${prediction[0]:,.2f}")


