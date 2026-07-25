import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Model Performance",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning Model Performance")

st.write(
    "This page presents the performance of the machine learning models developed to predict FIFA World Cup player ratings."
)

st.divider()

st.subheader("🏆 Best Model")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "Gradient Boosting")

with col2:
    st.metric("R² Score", "0.9784")

with col3:
    st.metric("RMSE", "0.4645")

with col4:
    st.metric("MAE", "0.2837")

st.divider()

st.subheader("📊 Model Comparison")

comparison = pd.DataFrame({
    "Model":[
        "Gradient Boosting",
        "Random Forest",
        "Linear Regression",
        "Decision Tree"
    ],
    "R²":[
        0.9784,
        0.9781,
        0.9720,
        0.9546
    ],
    "RMSE":[
        0.4645,
        0.4680,
        0.5291,
        0.6732
    ],
    "MAE":[
        0.2837,
        0.2841,
        0.3517,
        0.4094
    ]
})

st.dataframe(comparison, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        comparison,
        x="Model",
        y="R²",
        color="R²",
        title="Model Comparison (R² Score)"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        comparison,
        x="Model",
        y="RMSE",
        color="RMSE",
        title="RMSE Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("📌 Top Feature Importance")

try:

    model = joblib.load("models/best_player_rating_model.pkl")
    features = joblib.load("models/feature_names.pkl")

    importance = pd.DataFrame({
        "Feature": features,
        "Importance": model.feature_importances_
    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    ).head(15)

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        title="Top 15 Important Features"
    )

    fig.update_layout(
        yaxis={"categoryorder":"total ascending"}
    )

    st.plotly_chart(fig, use_container_width=True)

except Exception as e:

    st.warning("Feature importance could not be loaded.")
    st.write(e)

st.divider()

st.subheader("📈 Model Summary")

st.success("""
✔ Target Variable : Player Rating

✔ Best Model : Gradient Boosting Regressor

✔ Total Dataset Size : 54,600 Records

✔ Features Used : 83

✔ Test Size : 20%

✔ Prediction Type : Regression

✔ Performance : Excellent (R² ≈ 0.98)
""")

st.divider()

st.subheader("📖 Project Workflow")

workflow = go.Figure()

workflow.add_trace(go.Scatter(
    x=[1,2,3,4,5,6],
    y=[1,1,1,1,1,1],
    mode="markers+text",
    text=[
        "Data Collection",
        "Cleaning",
        "Feature Engineering",
        "EDA",
        "Model Training",
        "Evaluation"
    ],
    textposition="top center",
    marker=dict(size=20)
))

workflow.update_layout(
    showlegend=False,
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    height=300,
    title="Machine Learning Pipeline"
)

st.plotly_chart(workflow, use_container_width=True)

st.divider()

st.subheader("📋 Conclusion")

st.info("""
Gradient Boosting Regressor achieved the highest prediction accuracy among all tested algorithms.

The model explains approximately 97.84% of the variation in player ratings, demonstrating excellent predictive capability on the engineered football performance dataset.
""")