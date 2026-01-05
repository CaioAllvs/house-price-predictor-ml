import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
import joblib
import os

# 1. DATA GATHERING (Using corrected logic)
# Variable names in English, but data content stays in Portuguese context
data = {
    'size_m2':      [50, 60, 80, 100, 120, 150, 200, 45, 300, 85, 400, 55],
    'bedrooms':     [1, 2, 2, 3, 3, 3, 4, 1, 5, 2, 6, 1],
    'neighborhood': ['Centro', 'Centro', 'Suburbio', 'Nobre', 'Nobre', 'Suburbio', 'Nobre', 'Centro', 'Nobre', 'Suburbio', 'Nobre', 'Suburbio'],
    'price':        [220000, 280000, 210000, 650000, 800000, 350000, 1300000, 190000, 2200000, 230000, 3500000, 150000]
}

df = pd.DataFrame(data)

# 2. FEATURE ENGINEERING
# X = Features, y = Target
X = df[['size_m2', 'bedrooms', 'neighborhood']]
y = df['price']

# 3. SPLIT TRAIN/TEST
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. PIPELINE SETUP
# Converting 'neighborhood' to numbers
column_trans = make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore'), ['neighborhood']), 
    remainder='passthrough'
)

# Creating the model pipeline with Random Forest
model = make_pipeline(column_trans, RandomForestRegressor(n_estimators=100, random_state=42))

# 5. TRAINING
print("\nTraining Random Forest Model...")
model.fit(X_train, y_train)

# 6. EVALUATION
score = model.score(X_test, y_test)
print(f"Model R² Score: {score:.2f}")

# 7. SAVING THE MODEL
# Check if folder exists
if not os.path.exists('model'):
    os.makedirs('model')

joblib.dump(model, 'model/house_prices_model.pkl')
print("\nModel saved successfully at 'model/house_prices_model.pkl'!")