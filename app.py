import streamlit as st
import pandas as pd
import pickle


model_path = r"C:\data science\CV projects\customer churn\new_churn_model.pkl"
model = pickle.load(open(model_path, "rb"))
st.title("📉 Customer Churn Prediction Dashboard")

st.sidebar.header("Customer Information")

# Inputs
senior = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
tenure_group = st.sidebar.selectbox("Tenure Group", ["0-12 months", "13-24 months", "25-48 months", "49-72 months"])
monthly_charges = st.sidebar.slider("Monthly Charges", 10, 150, 70)
total_charges = st.sidebar.number_input("Total Charges", 0.0, 8000.0, 1000.0)
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["No", "Yes"])

# Prepare input dataframe
input_df = pd.DataFrame({
    'SeniorCitizen': [1 if senior == "Yes" else 0],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges_float': [total_charges],
    'Contract_One year': [1 if contract == "One year" else 0],
    'Contract_Two year': [1 if contract == "Two year" else 0],
    'PaperlessBilling_Yes': [1 if paperless_billing == "Yes" else 0],
    'tenure_group_0-12 months': [1 if tenure_group == "0-12 months" else 0],
    'tenure_group_13-24 months': [1 if tenure_group == "13-24 months" else 0],
    'tenure_group_25-48 months': [1 if tenure_group == "25-48 months" else 0],
    'tenure_group_49-72 months': [1 if tenure_group == "49-72 months" else 0]
})

# Add missing columns expected by model (safety)
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[model.feature_names_in_]

# Predict churn
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ This customer is likely to churn!")
    else:
        st.success("✅ This customer is likely to stay!")