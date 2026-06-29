import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

body{
    background-color:#f5f7fa;
}

.stButton>button{
    width:100%;
    background:#4CAF50;
    color:white;
    border:none;
    border-radius:10px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#2E7D32;
}

.metric-card{
    background:#E8F5E9;
    padding:25px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("house-price.pkl", "rb"))

# ---------------- TITLE ---------------- #
st.title("🏠 House Price Predictor")
st.write("Predict the estimated value of a house using Machine Learning.")

# ---------------- SIDEBAR ---------------- #
with st.sidebar:
    st.header("ℹ About")

    st.write("""
This app predicts house prices using a trained Machine Learning model.

### Features Used
- 🏡 Living Area
- 🛏 Bedrooms
- 🚿 Bathrooms
- ⭐ Building Grade
- 🏠 Basement Area
- 📅 Year Built
""")

# ---------------- INPUTS ---------------- #

col1, col2 = st.columns(2)

with col1:

    sqft = st.slider(
        "🏡 Living Area (Sqft)",
        500,
        10000,
        2000
    )

    bedrooms = st.slider(
        "🛏 Bedrooms",
        1,
        10,
        3
    )

    bathrooms = st.slider(
        "🚿 Bathrooms",
        1,
        8,
        2
    )

with col2:

    grade = st.slider(
        "⭐ Building Grade",
        1,
        13,
        7
    )

    basement = st.slider(
        "🏠 Basement Area",
        0,
        5000,
        0
    )

    year = st.slider(
        "📅 Year Built",
        1900,
        2025,
        2005
    )

# ---------------- HOUSE SUMMARY ---------------- #

st.subheader("📋 House Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Area", f"{sqft} sqft")

with c2:
    st.metric("Bedrooms", bedrooms)

with c3:
    st.metric("Bathrooms", bathrooms)

house_age = 2026 - year

st.info(f"🏠 House Age: **{house_age} years**")

# ---------------- PREDICTION ---------------- #

if st.button("🔮 Predict Price"):

    features = np.array([[
        sqft,
        bedrooms,
        bathrooms,
        grade,
        year,
        basement
    ]])

    with st.spinner("Calculating estimated price..."):

        prediction = model.predict(features)[0]
        price = np.exp(prediction)

    st.success("Prediction Completed!")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">

    <h3>💰 Estimated House Price</h3>

    <h1 style="color:#2E7D32;">
    ₹ {price:,.0f}
    </h1>

    </div>
    """, unsafe_allow_html=True)

    # House Category

    if price < 300000:
        st.info("🏠 Budget Home")

    elif price < 700000:
        st.success("🏡 Mid-Range Home")

    else:
        st.warning("🏰 Luxury Home")
