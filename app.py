import streamlit as st
import pandas as pd
import joblib


model = joblib.load("laptop_price_model.pkl")

st.title("💻 Laptop Price Prediction App")


brand = st.text_input("Enter Laptop Brand")
processor = st.text_input("Enter Processor")
ram = st.number_input("Enter RAM (GB)", min_value=2, max_value=64, step=2)
rom = st.number_input("Enter Storage (GB)", min_value=128, max_value=2000, step=128)
spec_rating = st.slider("Specification Rating", 1, 100, 50)


input_data = pd.DataFrame({
    "brand": [brand],
    "processor": [processor],
    "Ram": [ram],
    "ROM": [rom],
    "spec_rating": [spec_rating]
})


if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Laptop Price: ₹ {int(prediction)}")
