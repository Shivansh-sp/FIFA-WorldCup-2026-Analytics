import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Tournament Analytics",
    page_icon="🏆",
    layout="wide"
)

df = pd.read_csv("data/fifa_world_cup_2026_feature_engineered.csv")
df["match_date"] = pd.to_datetime(df["match_date"])

st.title("🏆 Tournament Analytics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Players", df["player_name"].nunique())

with col2:
    st.metric("Teams", df["team"].nunique())

with col3:
    st.metric("Matches", df["match_id"].nunique())

with col4:
    st.metric("Goals", int(df["goals"].sum()))

st.divider()

col1, col2 = st.columns(2)

with col1:

    top_goal = (
        df.groupby("player_name")["goals"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_goal,
        x="goals",
        y="player_name",
        orientation="h",
        color="goals",
        title="Top Goal Scorers"
    )

    fig.update_layout(
        yaxis={"categoryorder":"total ascending"}
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    top_assists = (
        df.groupby("player_name")["assists"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_assists,
        x="assists",
        y="player_name",
        orientation="h",
        color="assists",
        title="Top Assist Providers"
    )

    fig.update_layout(
        yaxis={"categoryorder":"total ascending"}
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:

    rating = (
        df.groupby("team")["player_rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        rating,
        x="team",
        y="player_rating",
        color="player_rating",
        title="Best Teams by Rating"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    stages = (
        df["tournament_stage"]
        .value_counts()
        .reset_index()
    )

    stages.columns = ["Stage","Matches"]

    fig = px.pie(
        stages,
        names="Stage",
        values="Matches",
        hole=0.5,
        title="Tournament Stage Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig = px.scatter(
        df,
        x="pass_accuracy",
        y="player_rating",
        color="position",
        title="Pass Accuracy vs Player Rating"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.scatter(
        df,
        x="distance_covered_km",
        y="player_rating",
        color="position",
        title="Distance Covered vs Player Rating"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Top 20 Tournament Players")

players = (
    df.groupby("player_name")
    .agg({
        "team":"first",
        "goals":"sum",
        "assists":"sum",
        "player_rating":"mean",
        "performance_score":"mean"
    })
    .round(2)
    .sort_values("player_rating", ascending=False)
    .head(20)
    .reset_index()
)

st.dataframe(players, use_container_width=True)