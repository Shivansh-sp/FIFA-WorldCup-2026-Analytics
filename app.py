import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="FIFA World Cup 2026 Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)


df = pd.read_csv("data/fifa_world_cup_2026_feature_engineered.csv")


st.title("⚽ FIFA World Cup 2026 Analytics Dashboard")

st.markdown("""
Welcome to the **FIFA World Cup 2026 Player Performance Analytics Dashboard**.

Use the sidebar to navigate through the different analytics pages.
""")


st.divider()

st.subheader("📈 Tournament Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Players", df["player_name"].nunique())

with col2:
    st.metric("🌍 Teams", df["team"].nunique())

with col3:
    st.metric("🏟 Matches", df["match_id"].nunique())

with col4:
    st.metric("⚽ Goals", int(df["goals"].sum()))



st.divider()

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)



col1, col2 = st.columns(2)

with col1:

    st.subheader("🏆 Top 10 Goal Scorers")

    top_scorers = (
        df.groupby("player_name")["goals"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_scorers,
        x="goals",
        y="player_name",
        orientation="h",
        color="goals",
        title="Top Goal Scorers"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.subheader("⚽ Position Distribution")

    position = (
        df["position"]
        .value_counts()
        .reset_index()
    )

    position.columns = ["Position", "Players"]

    fig = px.pie(
        position,
        names="Position",
        values="Players",
        hole=0.5
    )

    st.plotly_chart(fig, use_container_width=True)


st.divider()

col3, col4 = st.columns(2)

with col3:

    st.subheader("🌍 Top Teams by Average Rating")

    team_rating = (
        df.groupby("team")["player_rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        team_rating,
        x="team",
        y="player_rating",
        color="player_rating"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    st.subheader("🏟 Tournament Stage Distribution")

    stage = (
        df["tournament_stage"]
        .value_counts()
        .reset_index()
    )

    stage.columns = ["Stage", "Count"]

    fig = px.bar(
        stage,
        x="Stage",
        y="Count",
        color="Count"
    )

    st.plotly_chart(fig, use_container_width=True)


st.sidebar.title("⚽ FIFA Dashboard")
st.sidebar.success("Select a page from the sidebar.")