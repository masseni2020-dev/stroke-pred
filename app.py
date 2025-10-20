import streamlit as st
import pickle
with open('Saving.pkl', "rb") as file:
    loaded_model=pickle.load(file)

st.title("🧠 Stroke Prediction App")
st.write("Enter the patient details to predict the risk of stroke:")

hypertension = st.selectbox("Hypertension (0=No, 1=Yes)", [0, 1])
heart_disease = st.selectbox("Heart Disease (0=No, 1=Yes)", [0, 1])
age = st.number_input("Age", min_value=0, max_value=120, value=45)
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, max_value=300.0, value=92.86)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=35.1)

gender = st.selectbox("Gender (0=Female, 1=Male, 2=Other)", [0, 1, 2])
ever_married = st.selectbox("Ever Married (0=No, 1=Yes)", [0, 1])
work_type = st.selectbox("Work Type (0,1,2,3,4)", [0, 1, 2, 3, 4])
Residence_type = st.selectbox("Residence Type (0=Rural, 1=Urban)", [0, 1])
smoking_status = st.selectbox("Smoking Status (0=never,1=formerly,2=smokes)", [0, 1, 2])

if st.button("Predict Stroke"):
    # Collect features into a list (match model training order)
    input_features = [[gender, ever_married, work_type, Residence_type,
                       heart_disease, hypertension, smoking_status,
                       age, avg_glucose_level, bmi]]
    
    prediction = loaded_model.predict(input_features)
    
    # Display result
    if prediction[0] == 0:
        st.success("✅ Low risk of stroke")
    else:
        st.error("⚠️ High risk of stroke")


