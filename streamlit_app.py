import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('diabetes_model.pkl')

# Page title
st.title("🩺 Diabetes Risk Prediction")

st.markdown("Fill in the details below and click **Predict** to see your diabetes risk. 0 = NO, 1 = YES")

# Input form
features = {
    'HighBP': st.selectbox("High Blood Pressure", [0, 1]),
    'HighChol': st.selectbox("High Cholesterol", [0, 1]),
    'CholCheck': st.selectbox("Had Cholesterol Check", [0, 1]),
    'BMI': st.slider("BMI", 10, 70, 25),
    'Smoker': st.selectbox("Smoker", [0, 1]),
    'Stroke': st.selectbox("Stroke", [0, 1]),
    'HeartDiseaseorAttack': st.selectbox("Heart Disease or Attack", [0, 1]),
    'PhysActivity': st.selectbox("Physical Activity", [0, 1]),
    'Fruits': st.selectbox("Eats Fruits", [0, 1]),
    'Veggies': st.selectbox("Eats Vegetables", [0, 1]),
    'HvyAlcoholConsump': st.selectbox("Heavy Alcohol Consumption", [0, 1]),
    'AnyHealthcare': st.selectbox("Has Any Healthcare", [0, 1]),
    'NoDocbcCost': st.selectbox("Couldn’t Afford Doctor", [0, 1]),
    'GenHlth': st.slider("General Health (1=Excellent, 5=Poor)", 1, 5, 3),
    'MentHlth': st.slider("Poor Mental Health Days (0–30)", 0, 30, 0),
    'PhysHlth': st.slider("Poor Physical Health Days (0–30)", 0, 30, 0),
    'DiffWalk': st.selectbox("Difficulty Walking", [0, 1]),
    'Sex': st.selectbox("Sex (0=Female, 1=Male)", [0, 1]),
    'Age': st.slider("Age Group (1–13)", 1, 13, 9),
    'Education': st.slider("Education Level (1–6)", 1, 6, 4),
    'Income': st.slider("Income Level (1–8)", 1, 8, 5)
}

# Predict on click
if st.button("Predict"):
    X_input = np.array(list(features.values())).reshape(1, -1)
    prediction = model.predict(X_input)[0]
    if prediction == 1:
        st.error("🔴 At Risk of Diabetes")
    else:
        st.success("🟢 No Diabetes Detected")
