import streamlit as st
import pandas as pd
import joblib
import base64

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="🏠 House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ==============================
# BACKGROUND IMAGE
# ==============================
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
    """, unsafe_allow_html=True)

# 👉 change path
set_bg("C:\\Users\\shravan\\OneDrive\\Desktop\\house.jfif")

# ==============================
# TRANSPARENT + WHITE TEXT UI
# ==============================
st.markdown("""
<style>

/* Transparent glass effect */
.block-container {
    background: rgba(0,0,0,0.65);
    padding: 2rem;
    border-radius: 15px;
}

/* Make text white */
h1, h2, h3, h4, h5, h6, p, label, div {
    color: white !important;
}

/* Inputs */
.stNumberInput input {
    background-color: rgba(255,255,255,0.1);
    color: black !important;
}

/* Button */
.stButton>button {
    background-color: #00c6ff;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.stButton>button:hover {
    background-color: #0072ff;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# LOAD MODEL
# ==============================
model = joblib.load("random_forest_house_price_model.pkl")

# ==============================
# TITLE
# ==============================
st.markdown("<h1 style='text-align:center;'>🏠 House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Predict house price using ML</p>", unsafe_allow_html=True)

st.divider()

# ==============================
# INPUT SECTION
# ==============================
st.subheader("📋 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    square_footage = st.number_input("Enter square footage", value=1000)
    num_bedrooms = st.number_input("Enter no of bedrooms", value=6)
    num_bathrooms = st.number_input("Enter no of bathrooms", value=4)
    year_built = st.number_input("Enter year built", value=2025)

with col2:
    lot_size = st.number_input("Enter lot size", value=3000)
    garage_size = st.number_input("Enter garage size", value=1)
    neighborhood_quality = st.slider("Neighborhood quality (1-10)", 1, 10, 6)

st.divider()

# ==============================
# PREDICTION
# ==============================
if st.button("🚀 Predict House Price"):

    data = pd.DataFrame([[
        square_footage,
        num_bedrooms,
        num_bathrooms,
        year_built,
        lot_size,
        garage_size,
        neighborhood_quality
    ]], columns=[
        
        "square_footage","num_bedrooms","num_bathrooms","year_built","lot_size","garage_size","neighborhood_quality"
    ])

    prediction = model.predict(data)

    st.divider()

    st.success(f"💰 Predicted House Price: ₹ {prediction[0]:,.2f}")