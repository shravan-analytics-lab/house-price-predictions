# 🏠 House Price Prediction using Machine Learning

## 📌 Project Overview

This project implements an **end-to-end Machine Learning pipeline** to predict house prices based on various property features. It demonstrates how raw data is transformed into actionable insights using **data preprocessing, model training, evaluation, and deployment**.

The core of this project is the use of the **Random Forest Regressor**, a powerful ensemble algorithm capable of capturing complex, non-linear relationships in real-world housing data.

---

## 🧠 How Machine Learning is Used in This Project

Machine Learning is used here to **learn patterns from historical housing data** and make predictions for new, unseen data.

### 🔍 Problem Type

* **Supervised Learning**
* **Regression Task** (predicting continuous values → house prices)

---

## ⚙️ Complete Machine Learning Pipeline

### 1️⃣ Data Collection

* Dataset contains historical house data with features like:

  * Size of house
  * Number of bedrooms & bathrooms
  * Year built
  * Neighborhood quality

👉 The model learns from this historical data.

---

### 2️⃣ Data Preprocessing

Before training, the dataset is cleaned and prepared:

* Converted column names to lowercase for consistency
* Checked for missing values
* Ensured correct data types
* Selected relevant features

👉 This step ensures the model receives clean and structured input.

---

### 3️⃣ Feature Selection

The model uses the following input features:

```id="5r3ozl"
square_footage
num_bedrooms
num_bathrooms
year_built
lot_size
garage_size
neighborhood_quality
```

### 🎯 Target Variable:

```id="bdvb98"
house_price
```

👉 The goal of the model is to **map these features → house price**

---

### 4️⃣ Train-Test Split

* 80% → Training Data
* 20% → Testing Data

👉 Why?

* Prevents overfitting
* Tests model performance on unseen data

---

### 5️⃣ Model Training using Random Forest

```python id="i3v5bx"
RandomForestRegressor()
```

### 🌲 How Random Forest Works Internally

Random Forest is an **ensemble learning technique** based on decision trees:

#### Step-by-step:

1. Creates multiple decision trees from the dataset
2. Each tree is trained on:

   * Random subset of data (Bootstrap Sampling)
   * Random subset of features
3. Each tree makes its own prediction
4. Final prediction = **average of all tree outputs**

---

### 🧠 Why This Works Well

* Reduces overfitting (compared to single decision tree)
* Captures **non-linear relationships**
* Handles feature interactions automatically

---

### 📊 Example of Learning

The model learns patterns like:

* Larger square footage → higher price
* Better neighborhood → higher value
* More bedrooms/bathrooms → increased price
* Newer houses → higher price

👉 Instead of hardcoding rules, the model **learns these relationships automatically**

---

### 6️⃣ Model Evaluation

After training, predictions are compared with actual values using:

* **Mean Absolute Error (MAE)** → average prediction error
* **R² Score** → how well the model explains variance

👉 This ensures the model is reliable before deployment

---

### 7️⃣ Model Saving

```python id="8y4m3f"
joblib.dump(model, "random_forest_house_price_model.pkl")
```

👉 This allows reuse without retraining

---

## 📓 Detailed Notebook Workflow

The Jupyter Notebook contains the **core ML development process**:

### ✔️ Data Exploration (EDA)

* Analyzed relationships between features and house price
* Observed trends:

  * Area vs Price
  * Bedrooms vs Price
  * Neighborhood Quality impact

---

### ✔️ Model Building

* Imported RandomForestRegressor
* Trained model on dataset
* Generated predictions

---

### ✔️ Model Validation

* Compared predicted vs actual values
* Measured performance using metrics

---

### ✔️ Key Learnings

* Housing prices depend on multiple interacting features
* Non-linear models perform better than linear ones
* Feature importance plays a major role

---

## 🌐 Deployment using Streamlit

The trained model is integrated into a **Streamlit web application**.

### 🔮 Prediction Flow:

1. User enters house details
2. Inputs are converted into structured format (DataFrame)
3. Model processes input
4. Output (predicted price) is displayed instantly

```python id="xci7ht"
model.predict(data)
```

---

## ⚖️ Why Random Forest Instead of Linear Regression?

| Linear Regression                 | Random Forest               |
| --------------------------------- | --------------------------- |
| Assumes linear relationship       | Handles non-linear patterns |
| Simple model                      | Complex ensemble model      |
| Less accurate for real-world data | Higher accuracy             |

👉 Housing data is complex → Random Forest performs better

---

## 🧪 Example Prediction

**Input:**

* Square Footage: 2000
* Bedrooms: 3
* Bathrooms: 2
* Year Built: 2015
* Lot Size: 4000
* Garage Size: 2
* Neighborhood Quality: 7

👉 Model predicts a realistic house price based on learned patterns

---

## 🛠️ Technologies Used

* Python
* Pandas & NumPy
* Scikit-learn
* Joblib
* Streamlit

---

## 📁 Project Structure

```id="v5y4hc"
📦 House Price Prediction
 ┣ 📜 house_price_prdicton.py
 ┣ 📜 app.py
 ┣ 📜 dataset.csv
 ┣ 📜 model.pkl
 ┣ 📜 notebook.ipynb
 ┗ 📜 README.md
```

---

## 🔥 Advanced Concepts Applied

* Supervised Learning
* Regression Modeling
* Ensemble Learning (Random Forest)
* Model Evaluation Metrics
* Feature-based Prediction
* End-to-End ML Pipeline
* Model Deployment

---

## 🎯 Conclusion

This project demonstrates how Machine Learning can be used to solve real-world problems by:

* Learning patterns from historical data
* Generalizing to new unseen inputs
* Delivering accurate predictions through a deployed application

The use of Random Forest ensures robustness, accuracy, and scalability, making it ideal for predicting house prices.

---

## 🙌 Author

**Shravan B**

---

⭐ If you found this project useful, consider giving it a star!
