import streamlit as st
import pandas as pd
import joblib

# 1. PAGE CONFIG
st.set_page_config(page_title="Avaliador de Imóveis", page_icon="🏠")

st.title("🏠 Avaliador de Imóveis com ML")
st.write("Insira as características do imóvel para receber uma estimativa de preço baseada em Machine Learning.")

# 2. LOAD MODEL
try:
    model = joblib.load('model/house_prices_model.pkl')
except FileNotFoundError:
    st.error("ERRO: O arquivo do modelo não foi encontrado. Execute 'train_model.py' primeiro.")
    st.stop()

# 3. UI & INPUTS (Sidebar)
st.sidebar.header("Características")

# Input: Size
size = st.sidebar.number_input("Tamanho (m²)", min_value=10, max_value=1000, value=70, step=10)

# BUSINESS LOGIC: Limit bedrooms based on size (1 bedroom per 15m² min)
max_bedrooms = int(size / 15)
if max_bedrooms < 1:
    max_bedrooms = 1

# Input: Bedrooms (Dynamic Slider)
bedrooms = st.sidebar.slider(
    "Quantidade de Quartos", 
    min_value=1, 
    max_value=max_bedrooms, 
    value=min(2, max_bedrooms) # Default value logic
)

# Feedback message about the limit
if max_bedrooms < 5:
    st.sidebar.caption(f"⚠️ Nota: Para {size}m², limitamos a {max_bedrooms} quartos por lógica de espaço.")

# Input: Neighborhood
# Note: The values must match exactly what was used in training ('Centro', not 'Center')
neighborhood = st.sidebar.selectbox("Bairro", ["Centro", "Suburbio", "Nobre"])

# 4. PREDICTION LOGIC
if st.button("Calcular Preço"):
    # Creating DataFrame with ENGLISH column names (must match training data)
    input_data = pd.DataFrame({
        'size_m2': [size],
        'bedrooms': [bedrooms],
        'neighborhood': [neighborhood]
    })
    
    # Predict
    prediction = model.predict(input_data)[0]
    
    # Display Result
    st.success(f"💰 Preço estimado: **R$ {prediction:,.2f}**")