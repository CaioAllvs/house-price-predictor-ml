import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

# 1. LOAD REAL DATA
# Ensure 'houses_to_rent_v2.csv' is in the same folder
try:
    df = pd.read_csv('houses_to_rent_v2.csv')
except FileNotFoundError:
    print("ERROR: File 'houses_to_rent_v2.csv' not found. Please download it from Kaggle.")
    exit()

# 2. DATA CLEANING & ENGINEERING
# Filter for São Paulo only to improve accuracy
df = df[df['city'] == 'São Paulo']

# Rename columns for better readability
df = df.rename(columns={
    'total (R$)': 'price', 
    'area': 'size_m2', 
    'rooms': 'bedrooms'
})

# Select relevant features
# Now including bathrooms and parking spaces
df_clean = df[['size_m2', 'bedrooms', 'bathroom', 'parking spaces', 'price']]

# Remove outliers (Unrealistic data points)
df_clean = df_clean[df_clean['size_m2'] < 1000] # Remove mansions > 1000m²
df_clean = df_clean[df_clean['price'] < 50000]  # Remove rentals > 50k

# 3. SPLIT DATA
X = df_clean[['size_m2', 'bedrooms', 'bathroom', 'parking spaces']]
y = df_clean['price']

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. BUILD MODEL (Random Forest)
# We use Random Forest because it handles outliers better than Linear Regression
model = RandomForestRegressor(n_estimators=100, random_state=42)

# 5. TRAIN MODEL
print("\nTraining model with real data from São Paulo...")
model.fit(X_train, y_train)

# 6. EVALUATE
score = model.score(X_test, y_test)
print(f"R² Score (Accuracy on test data): {score:.2f}")

# 7. SAVE MODEL
if not os.path.exists('model'):
    os.makedirs('model')
joblib.dump(model, 'model/house_prices_model.pkl')
print("\nModel saved successfully!")