import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("C:\\Users\\shravan\\OneDrive\\Desktop\\house_price\\house_price_regression_dataset.csv")
df.columns = df.columns.str.lower()

# Features and target
x = df.drop(["house_price"], axis=1)
y = df["house_price"]

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Model building
rfr = RandomForestRegressor()

# Training
rfr.fit(x_train, y_train)

# Prediction
y_pred_rf = rfr.predict(x_test)

print("Model trained successfully ✅")

# Save model
joblib.dump(rfr, "random_forest_house_price_model.pkl")

print("Model saved successfully ✅")