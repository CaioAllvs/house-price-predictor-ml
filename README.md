# 🏠 House Price Predictor (ML Study Project)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Educational-orange)

## 📋 About the Project

This is an educational project designed to demonstrate **Machine Learning** concepts applied with **Python**. It consists of a web application where users can input property features (size, bedrooms, location) to get a price estimate.

> **⚠️ IMPORTANT DISCLAIMER:**
> This project uses **Mock Data** (synthetic data) generated programmatically for study and visualization purposes. The predictions are based on mathematical logic trained on this synthetic dataset and **do not reflect real-world market prices**.
>
> *The goal is to showcase code structure, pipeline implementation, and library usage (Scikit-Learn, Pandas, Streamlit).*

## 🛠 Technologies & Skills

* **Python**: Logic and data manipulation.
* **Scikit-Learn**:
    * **Random Forest Regressor**: Selected algorithm to handle non-linear patterns.
    * **Pipelines**: To encapsulate pre-processing (OneHotEncoding).
* **Streamlit**: For rapid frontend prototyping.
* **Pandas**: Data engineering.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/house-price-predictor-ml.git](https://github.com/SEU-USUARIO/house-price-predictor-ml.git)

2. **Install dependencies:**
pip install -r requirements.txt

3. **Train the Model: Run the training script to generate the .pkl file locally.**
  python train_model.py 

4. **Run the App:**
streamlit run app.py

-------------------------------------------------
Developed by Caio Alves as part of a Machine Learning Portfolio.