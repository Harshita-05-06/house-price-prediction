import streamlit as st
import pickle
import numpy as np

# page config
st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# load model
model = pickle.load(open("house-price.pkl", "rb"))

# title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)

st.markdown("### Enter house details below:")

# layout using columns
col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input("Sqft Living", min_value=0.0)
    bedrooms = st.number_input("Bedrooms", min_value=0)
    bathrooms = st.number_input("Bathrooms", min_value=0.0)

with col2:
    grade = st.number_input("Building Grade", min_value=0)
    basement = st.number_input("SqFt Finished Basement")
    year = st.number_input("Year Built", min_value=1900)

# predict button
if st.button("🔮 Predict Price"):

    features = np.array([[
    sqft,
    bedrooms,
    bathrooms,
    grade,
    year,
    basement
    ]])

    prediction = model.predict(features)[0]

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            background-color:#e8f5e9;
            padding:20px;
            border-radius:10px;
            text-align:center;
            font-size:22px;
            color:#2e7d32;">
            💰 Predicted House Price: ₹{prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )