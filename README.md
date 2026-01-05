# 🏠 Real Estate Price Predictor (Brazil)

A Machine Learning web application to predict rental prices in São Paulo, Brazil, using real estate market data.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Status](https://img.shields.io/badge/Status-Educational-orange)

## 🧠 About the Project
This project moved from a simple linear regression prototype to a robust **Random Forest** model trained on real-world data.

**Key Features:**
* **Real Dataset:** Trained on the [Brazilian Houses to Rent Dataset](https://www.kaggle.com/datasets/rubenssjr/brasilian-houses-to-rent) (Kaggle), specifically filtered for São Paulo.
* **Algorithm:** Uses **Random Forest Regressor** to handle non-linear relationships and outliers.
* **Interactive App:** Built with **Streamlit** for real-time predictions.
* **Data Cleaning:** Implements strict filtering logic to remove outliers (e.g., inconsistent square footage or unrealistic prices).

## 📊 Model Performance
The model takes into account:
* Size ($m^2$)
* Number of Bedrooms
* Number of Bathrooms
* Parking Spaces

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/CaioAllvs/house-price-predictor-ml.git](https://github.com/CaioAllvs/house-price-predictor-ml.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Train the Model (Optional):**
    *If you want to retrain with the latest data:*
    ```bash
    python train_model.py
    ```
4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 🛠 Snacks
* Python
* Pandas (Data Engineering)
* Scikit-Learn (Machine Learning)
* Streamlit (Web Framework)

---
Developed by Caio Alves