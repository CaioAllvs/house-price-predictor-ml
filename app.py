import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(page_title="Rent Predictor", page_icon="🏠")

# Title and Description
st.title("🏠 SP Rent Price Predictor")
st.write("Enter the property details below to estimate the monthly rent based on real market data.")

# Load the Trained Model
try:
    model = joblib.load('model/house_prices_model.pkl')
except FileNotFoundError:
    st.error("Error: Model file not found. Please run 'train_model.py' first.")
    st.stop()

# --- SIDEBAR (User Inputs) ---
st.sidebar.header("Property Features")

# Input fields (Must match the training data columns)
size = st.sidebar.number_input("Size (m²)", min_value=10, max_value=1000, value=70, step=5)
bedrooms = st.sidebar.slider("Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.sidebar.slider("Bathrooms", min_value=1, max_value=10, value=1)
parking = st.sidebar.slider("Parking Spaces", min_value=0, max_value=10, value=1)

# --- MAIN AREA (Prediction) ---
if st.button("💰 Estimate Rent"):
    # Create a DataFrame with user inputs
    input_data = pd.DataFrame({
        'size_m2': [size],
        'bedrooms': [bedrooms],
        'bathroom': [bathrooms],
        'parking spaces': [parking]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display result
    st.success(f"Estimated Monthly Rent: **R$ {prediction:,.2f}**")
    
