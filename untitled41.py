# -*- coding: utf-8 -*-
"""Untitled41.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iDtWKQZpl669fybORiSPS44vlWz1a7N7
"""

import streamlit as st
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Saraswathi Kondapalli | AI & ML Portfolio", layout="wide")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://via.placeholder.com/150", width=150)  # Placeholder for profile image
    st.title("Saraswathi Kondapalli")
    st.write("AI & ML Engineer | Data Scientist")
    st.write("📍 India")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/saraswathi-kondapalli-531041220/)")
    st.markdown("[GitHub](https://github.com/Saraswathi0)")
    st.markdown("[Resume](https://drive.google.com/file/d/1CI6r7iz6PQtZ4T60_6fdh9ly3L9Y21SD/view?usp=drivesdk)")

# --- HOME PAGE ---
st.title("Welcome to My AI & ML Portfolio")
st.write("Showcasing my work in Data Science, Machine Learning, and AI-driven solutions.")

# --- PROJECTS SECTION ---
st.header("🚀 Projects")

# Diabetes Prediction Model
st.subheader("📌 Diabetes Prediction Model")
st.write("A machine learning model to predict diabetes using logistic regression and random forest.")
st.markdown("[GitHub Repository](https://github.com/Saraswathi0/cognico.git)")

# Medimapper Project
st.subheader("📌 Medimapper - AI in Healthcare")
st.write("Machine learning models to analyze healthcare datasets for personalized medicine recommendations.")
st.markdown("[GitHub Repository](https://github.com/Saraswathi0/Medimapper-project-)")

# Crop Yield Prediction
st.subheader("📌 Crop Yield Prediction System")
st.write("A model leveraging historical weather data and market trends to optimize crop selection.")
st.markdown("[GitHub Repository](https://github.com/Saraswathi0/crop-yield-prediction.git)")

# Cervical Cancer Prediction
st.subheader("📌 Cervical Cancer Prediction")
st.write("Comparing multiple ML techniques to predict cervical cancer risk using patient medical records.")
st.markdown("[GitHub Repository](https://github.com/Saraswathi0/survey-of-cervical-cancer-prediction-using-machine-learning.git)")

# --- CONTACT SECTION ---
st.header("📞 Contact Me")
st.write("Feel free to reach out for collaborations or freelance projects.")
st.write("📧 Email: saraswathikondapalli09@gmail.com")
st.markdown("[Hire Me on Upwork](#)")

# --- DEPLOYMENT INSTRUCTIONS ---
st.sidebar.header("Deploy Locally:")
st.sidebar.code("""
pip install streamlit pandas plotly
streamlit run app.py
""", language='bash')
