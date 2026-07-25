import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Team Analytics",
    page_icon="🌍",
    layout="wide"
)

df = pd.read_csv("data/fifa_world_cup_2026_feature_engineered.csv")
df["match_date"] = pd.to_datetime(df["match_date"])

st.title("🌍 Team Analytics")

teams = sorted(df["team"].unique())

selected_team = st.selectbox(
    "Select a Team",
    teams
)

team_df = df[df["team"] == selected_team]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚽ Goals",
        int(team_df["goals"].sum())
    )

with col2:
    st.metric(
        "🎯 Assists",
        int(team_df["assists"].sum())
    )

with col3:
    st.metric(
        "⭐ Avg Rating",
        round(team_df["player_rating"].mean(), 2)
    )

with col4:
    st.metric(
        "🏟 Matches",
        team_df["match_id"].nunique()
    )

st.divider()

st.subheader("Team Information")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Team:** {selected_team}")
    st.write(f"**Players:** {team_df['player_name'].nunique()}")
    st.write(f"**Tournament Stage:** {team_df['tournament_stage'].mode()[0]}")

with col2:
    st.write(f"**Average Age:** {round(team_df['age'].mean(),1)} Years")
    st.write(f"**Average Height:** {round(team_df['height_cm'].mean(),1)} cm")
    st.write(f"**Average Weight:** {round(team_df['weight_kg'].mean(),1)} kg")

st.divider()

col1, col2 = st.columns(2)

with col1:

    attack = pd.DataFrame({
        "Statistic":[
            "Goals",
            "Assists",
            "Shots",
            "Shots On Target"
        ],
        "Value":[
            team_df["goals"].sum(),
            team_df["assists"].sum(),
            team_df["shots"].sum(),
            team_df["shots_on_target"].sum()
        ]
    })

    fig = px.bar(
        attack,
        x="Statistic",
        y="Value",
        color="Value",
        title="Attacking Statistics"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    passing = pd.DataFrame({
        "Statistic":[
            "Pass Accuracy",
            "Successful Passes",
            "Key Passes"
        ],
        "Value":[
            team_df["pass_accuracy"].mean(),
            team_df["successful_passes"].sum(),
            team_df["key_passes"].sum()
        ]
    })

    fig = px.bar(
        passing,
        x="Statistic",
        y="Value",
        color="Value",
        title="Passing Statistics"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:

    defence = pd.DataFrame({
        "Statistic":[
            "Tackles",
            "Interceptions",
            "Clearances",
            "Blocks"
        ],
        "Value":[
            team_df["tackles"].sum(),
            team_df["interceptions"].sum(),
            team_df["clearances"].sum(),
            team_df["blocks"].sum()
        ]
    })

    fig = px.bar(
        defence,
        x="Statistic",
        y="Value",
        color="Value",
        title="Defensive Statistics"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    physical = pd.DataFrame({
        "Statistic":[
            "Distance Covered",
            "Sprint Distance",
            "Top Speed",
            "Stamina Score"
        ],
        "Value":[
            team_df["distance_covered_km"].mean(),
            team_df["sprint_distance_km"].mean(),
            team_df["top_speed_kmh"].mean(),
            team_df["stamina_score"].mean()
        ]
    })

    fig = px.bar(
        physical,
        x="Statistic",
        y="Value",
        color="Value",
        title="Physical Performance"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Average Player Rating Across Matches")

rating = (
    team_df.groupby("match_date")["player_rating"]
    .mean()
    .reset_index()
)

fig = px.line(
    rating,
    x="match_date",
    y="player_rating",
    markers=True,
    title="Average Team Rating"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Top Players")

top_players = (
    team_df.groupby("player_name")
    .agg({
        "goals":"sum",
        "assists":"sum",
        "player_rating":"mean",
        "performance_score":"mean"
    })
    .round(2)
    .sort_values("player_rating", ascending=False)
    .reset_index()
)

st.dataframe(
    top_players,
    use_container_width=True
)

st.divider()

st.subheader("Match History")

history = team_df[
    [
        "match_date",
        "opponent_team",
        "tournament_stage",
        "match_result",
        "goals",
        "assists",
        "player_rating",
        "performance_score"
    ]
].sort_values("match_date")

st.dataframe(
    history,
    use_container_width=True
)

with st.expander("View Complete Team Dataset"):
    st.dataframe(
        team_df,
        use_container_width=True
    )

