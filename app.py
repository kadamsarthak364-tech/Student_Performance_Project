
import streamlit as st
import pandas as pd
import joblib

# Page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load trained model
model = joblib.load("student_performance_model.pkl")

# Main heading
st.title("🎓 Student Performance Prediction System")
st.write("Welcome to the Student Performance Prediction System!")
st.divider()

# Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox(
    "Select Page",
    ["Home", "Prediction", "About"]
)

if menu == "Home":
    st.header("Home")
    st.write("Welcome to our Machine Learning Project!")
    st.success("Application is running successfully!")

elif menu == "Prediction":

    st.header("🎓 Student Information")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender", ["male", "female"]
        )

        race = st.selectbox(
            "Race/Ethnicity",
            ["group a", "group b", "group c", "group d", "group e"]
        )

        parental_education = st.selectbox(
            "Parental Education",
            [
                "high school",
                "some high school",
                "some college",
                "associate's degree",
                "bachelor's degree",
                "master's degree"
            ]
        )

        lunch = st.selectbox("Lunch", ["0", "1"])

    with col2:
        preparation = st.selectbox(
            "Test Preparation Course", ["0", "1"]
        )

        math_score = st.number_input(
            "Math Score", 0, 100, 50
        )

        reading_score = st.number_input(
            "Reading Score", 0, 100, 50
        )

        writing_score = st.number_input(
            "Writing Score", 0, 100, 50
        )

        science_score = st.number_input(
            "Science Score", 0, 100, 50
        )

    if st.button("Predict Performance"):

        input_data = pd.DataFrame([{
            "gender": gender,
            "race_ethnicity": race,
            "parental_level_of_education": parental_education,
            "lunch": lunch,
            "test_preparation_course": preparation,
            "math_score": math_score,
            "reading_score": reading_score,
            "writing_score": writing_score,
            "science_score": science_score
        }])

        prediction = model.predict(input_data)

        st.success(
            f"Predicted Performance: {prediction[0]}"
        )

elif menu == "About":
    st.header("About Project")
    st.write(
        "This project predicts student academic "
        "performance using Machine Learning."
    )
