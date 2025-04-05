import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('weather_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_weather(input_data):
    # Convert input data to DataFrame if it's not already
    if not isinstance(input_data, pd.DataFrame):
        input_data = pd.DataFrame(input_data, index=[0])

    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit app UI
st.title("Weather Prediction for BBQ")

# Input fields for features
date = st.number_input("Date (1-31)", min_value=1, max_value=31, value=5)
month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=4)
temp_max = st.number_input("Maximum Temperature (°C)", value=15)
temp_min = st.number_input("Minimum Temperature (°C)", value=5)
wind_speed = st.number_input("Wind Speed (km/h)", value=10)
humidity = st.number_input("Humidity (%)", value=60)
pressure = st.number_input("Pressure (hPa)", value=1010)
cloud_amount = st.number_input("Cloud Amount (%)", value=30)

# Create input data DataFrame
input_data = pd.DataFrame({
    'DATE': [date],
    'MONTH': [month],
    'OSLO_TEMP_MAX': [temp_max],
    'OSLO_TEMP_MIN': [temp_min],
    'OSLO_WIND_SPEED': [wind_speed],
    'OSLO_HUMIDITY': [humidity],
    'OSLO_PRESSURE': [pressure],
    'OSLO_CLOUD_AMOUNT': [cloud_amount]
}, index=[0])

# Make prediction when button is clicked
if st.button("Predict"):
    prediction = predict_weather(input_data)

    # Interpret the prediction
    if prediction == 1:
        st.success("BBQ weather is predicted!")
    else:
        st.error("BBQ weather is not predicted.")
