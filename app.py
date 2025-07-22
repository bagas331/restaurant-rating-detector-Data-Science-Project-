import streamlit as st
import numpy as np
import joblib

# Load Scaler dan Model
scaler = joblib.load("Scaler.pkl")
model = joblib.load("model.pkl")

# Konfigurasi Halaman
st.set_page_config(layout="wide")
st.title("Restaurant Rating Prediction App")
st.caption("This app helps you predict a restaurant's review class")
st.divider()

# Input User
averagecost = st.number_input("Estimated average cost for two", min_value=50, max_value=999999, value=1000, step=200)
tablebooking = st.selectbox("Restaurant has table booking?", ["Yes", "No"])
onlinedelivery = st.selectbox("Restaurant has online delivery?", ["Yes", "No"])
pricerange = st.selectbox("Price range (1 cheapest - 4 most expensive)", [1, 2, 3, 4])

predict_button = st.button("Predict the Review!")

st.divider()

# Proses Input
if predict_button:
    bookingstatus = 1 if tablebooking == "Yes" else 0
    deliverystatus = 1 if onlinedelivery == "Yes" else 0

    input_values = [[averagecost, bookingstatus, deliverystatus, pricerange]]

    # Scaling input
    scaled_input = scaler.transform(input_values)

    # Prediksi
    prediction = model.predict(scaled_input)

    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else :
        st.write("Excellent")