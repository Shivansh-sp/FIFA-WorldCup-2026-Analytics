import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.header("Project Overview")

st.write("""
This project analyses FIFA World Cup 2026 player performance using data science and machine learning techniques.

The dashboard enables users to explore player statistics, compare team performance, analyse tournament insights and evaluate machine learning models used to predict player ratings.
""")

st.header("Dataset")

st.write("""
• 54,600 Player Records

• 83 Engineered Features

• Match Statistics

• Physical Performance Metrics

• Defensive & Offensive Statistics

• Tournament Performance
""")

st.header("Machine Learning")

st.write("""
Models Implemented:

• Linear Regression

• Decision Tree Regressor

• Random Forest Regressor

• Gradient Boosting Regressor

Best Model:
Gradient Boosting Regressor

R² Score: 0.9784
""")

st.header("Technologies Used")

st.write("""
Python

Pandas

NumPy

Scikit-Learn

Plotly

Streamlit

Matplotlib

Seaborn
""")

st.header("Project Workflow")

st.write("""
Data Collection

↓

Data Cleaning

↓

Feature Engineering

↓

Exploratory Data Analysis

↓

Machine Learning

↓

Model Evaluation

↓

Interactive Dashboard
""")

st.header("Developed By")

st.write("""
Shivansh Pushkarna

B.Tech Computer Science Engineering

Guru Nanak Dev Engineering College

Data Science & Machine Learning Project
""")