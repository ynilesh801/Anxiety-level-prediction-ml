import streamlit as st
import pandas as pd
import pickle

# ---------------- LOAD SAVED OBJECTS ----------------
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

st.title("Anxiety Level Prediction")
st.write("Enter the details below to predict anxiety level")

# ---------------- USER INPUTS ----------------

Age = st.number_input("Age", 10, 100)
Sleep_Hours = st.number_input("Sleep Hours", 0.0, 24.0)
Physical_Activity = st.number_input("Physical Activity (hrs/week)", 0.0, 50.0)
Caffeine_Intake = st.number_input("Caffeine Intake (mg/day)", 0.0, 1000.0)
Alcohol_Consumption = st.number_input("Alcohol Consumption (drinks/week)", 0.0, 50.0)
Stress_Level = st.slider("Stress Level (1-10)", 1, 10)
Heart_Rate = st.number_input("Heart Rate (bpm)", 40, 200)
Breathing_Rate = st.number_input("Breathing Rate (breaths/min)", 5, 40)
Sweating_Level = st.slider("Sweating Level (1-5)", 1, 5)
Therapy_Sessions = st.number_input("Therapy Sessions (per month)", 0, 30)
Diet_Quality = st.slider("Diet Quality (1-10)", 1, 10)

Gender = st.selectbox("Gender", ["Male", "Female", "Other"])
Occupation = st.selectbox(
    "Occupation",
    [
        "Student", "Engineer", "Doctor", "Teacher", "Artist",
        "Musician", "Scientist", "Nurse", "Chef", "Lawyer",
        "Athlete", "Freelancer", "Other"
    ]
)
Smoking = st.selectbox("Smoking", ["Yes", "No"])
Family_History = st.selectbox("Family History of Anxiety", ["Yes", "No"])
Dizziness = st.selectbox("Dizziness", ["Yes", "No"])
Medication = st.selectbox("Medication", ["Yes", "No"])
Recent_Event = st.selectbox("Recent Major Life Event", ["Yes", "No"])

# ---------------- CREATE INPUT DATAFRAME ----------------

input_df = pd.DataFrame([{
    "Age": Age,
    "Sleep Hours": Sleep_Hours,
    "Physical Activity (hrs/week)": Physical_Activity,
    "Caffeine Intake (mg/day)": Caffeine_Intake,
    "Alcohol Consumption (drinks/week)": Alcohol_Consumption,
    "Stress Level (1-10)": Stress_Level,
    "Heart Rate (bpm)": Heart_Rate,
    "Breathing Rate (breaths/min)": Breathing_Rate,
    "Sweating Level (1-5)": Sweating_Level,
    "Therapy Sessions (per month)": Therapy_Sessions,
    "Diet Quality (1-10)": Diet_Quality,
    "Gender": Gender,
    "Occupation": Occupation,
    "Smoking": Smoking,
    "Family History of Anxiety": Family_History,
    "Dizziness": Dizziness,
    "Medication": Medication,
    "Recent Major Life Event": Recent_Event
}])

# ---------------- ENCODING (ONLY CATEGORICAL) ----------------

obj_cols = [
    "Gender",
    "Occupation",
    "Smoking",
    "Family History of Anxiety",
    "Dizziness",
    "Medication",
    "Recent Major Life Event"
]

input_df[obj_cols] = encoder.transform(input_df[obj_cols])

# ---------------- FIX FEATURE ORDER ----------------
input_df = input_df.reindex(columns=feature_columns)

# ---------------- SCALING ----------------
input_scaled = scaler.transform(input_df.values)

# ---------------- PREDICTION ----------------
if st.button("Predict Anxiety Level"):
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("High Anxiety Level Detected")
    else:
        st.success("Low Anxiety Level Detected")
