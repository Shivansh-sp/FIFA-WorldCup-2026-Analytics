import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Player Analytics",
    page_icon="👤",
    layout="wide"
)


df = pd.read_csv("data/fifa_world_cup_2026_feature_engineered.csv")
df["match_date"] = pd.to_datetime(df["match_date"])

st.title("👤 Player Analytics")

st.write("Analyse the performance of any player throughout the FIFA World Cup 2026.")

players = sorted(df["player_name"].unique())

selected_player = st.selectbox(
    "Select a Player",
    players
)

player_df = df[df["player_name"] == selected_player]

info = player_df.iloc[0]


st.divider()

st.subheader("Player Performance Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "⚽ Goals",
        int(player_df["goals"].sum())
    )

with col2:
    st.metric(
        "🎯 Assists",
        int(player_df["assists"].sum())
    )

with col3:
    st.metric(
        "⭐ Avg Rating",
        round(player_df["player_rating"].mean(), 2)
    )

with col4:
    st.metric(
        "📈 Performance Score",
        round(player_df["performance_score"].mean(), 2)
    )



st.subheader("Player Information")

col1, col2 = st.columns(2)

with col1:

    st.write(f"**Name:** {info['player_name']}")
    st.write(f"**Nationality:** {info['nationality']}")
    st.write(f"**Team:** {info['team']}")
    st.write(f"**Club:** {info['club_name']}")
    st.write(f"**Position:** {info['position']}")

with col2:

    st.write(f"**Age:** {info['age']} years")
    st.write(f"**Height:** {info['height_cm']} cm")
    st.write(f"**Weight:** {info['weight_kg']} kg")
    st.write(f"**Preferred Foot:** {info['preferred_foot']}")
    st.write(f"**Market Value:** €{info['market_value_eur']:,.0f}")


st.divider()

col1, col2 = st.columns(2)

with col1:

    attack = pd.DataFrame({
        "Statistic": [
            "Goals",
            "Assists",
            "Shots",
            "Shots On Target"
        ],
        "Value": [
            player_df["goals"].sum(),
            player_df["assists"].sum(),
            player_df["shots"].sum(),
            player_df["shots_on_target"].sum()
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
        "Statistic": [
            "Pass Accuracy",
            "Successful Passes",
            "Key Passes"
        ],
        "Value": [
            player_df["pass_accuracy"].mean(),
            player_df["successful_passes"].sum(),
            player_df["key_passes"].sum()
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

st.subheader("Defensive Statistics")

defence = pd.DataFrame({

    "Statistic":[
        "Tackles",
        "Interceptions",
        "Clearances",
        "Blocks"
    ],

    "Value":[
        player_df["tackles"].sum(),
        player_df["interceptions"].sum(),
        player_df["clearances"].sum(),
        player_df["blocks"].sum()
    ]

})

fig = px.bar(

    defence,

    x="Statistic",

    y="Value",

    color="Value",

    title="Defensive Contribution"

)

st.plotly_chart(fig,use_container_width=True)


st.divider()

st.subheader("Player Rating Over Tournament")

rating = player_df.sort_values("match_date")

fig = px.line(

    rating,

    x="match_date",

    y="player_rating",

    markers=True,

    title="Player Rating by Match"

)

st.plotly_chart(fig,use_container_width=True)


st.divider()

st.subheader("Physical Performance")

physical = pd.DataFrame({

    "Metric":[
        "Distance Covered",
        "Sprint Distance",
        "Top Speed",
        "Stamina Score"
    ],

    "Value":[
        player_df["distance_covered_km"].mean(),
        player_df["sprint_distance_km"].mean(),
        player_df["top_speed_kmh"].mean(),
        player_df["stamina_score"].mean()
    ]

})

fig = px.bar(

    physical,

    x="Metric",

    y="Value",

    color="Value",

    title="Physical Performance"

)

st.plotly_chart(fig,use_container_width=True)


st.subheader("Match History")

match_columns = [

    "match_date",
    "opponent_team",
    "tournament_stage",
    "match_result",
    "minutes_played",
    "goals",
    "assists",
    "shots",
    "pass_accuracy",
    "player_rating",
    "performance_score"

]

st.dataframe(

    player_df[match_columns]
    .sort_values("match_date"),

    use_container_width=True

)


with st.expander("View Complete Player Dataset"):

    st.dataframe(

        player_df,

        use_container_width=True

    )