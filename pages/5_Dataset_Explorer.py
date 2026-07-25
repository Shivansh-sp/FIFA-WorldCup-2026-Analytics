import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📁",
    layout="wide"
)

df = pd.read_csv("data/fifa_world_cup_2026_feature_engineered.csv")
df["match_date"] = pd.to_datetime(df["match_date"])

st.title("📁 Dataset Explorer")

st.write("Explore and filter the FIFA World Cup 2026 Player Performance Dataset.")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    player = st.selectbox(
        "Player",
        ["All"] + sorted(df["player_name"].unique().tolist())
    )

with col2:
    team = st.selectbox(
        "Team",
        ["All"] + sorted(df["team"].unique().tolist())
    )

with col3:
    position = st.selectbox(
        "Position",
        ["All"] + sorted(df["position"].unique().tolist())
    )

stage = st.selectbox(
    "Tournament Stage",
    ["All"] + sorted(df["tournament_stage"].unique().tolist())
)

filtered = df.copy()

if player != "All":
    filtered = filtered[filtered["player_name"] == player]

if team != "All":
    filtered = filtered[filtered["team"] == team]

if position != "All":
    filtered = filtered[filtered["position"] == position]

if stage != "All":
    filtered = filtered[filtered["tournament_stage"] == stage]

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Rows", filtered.shape[0])

with col2:
    st.metric("Columns", filtered.shape[1])

with col3:
    st.metric("Players", filtered["player_name"].nunique())

with col4:
    st.metric("Teams", filtered["team"].nunique())

st.divider()

st.subheader("Filtered Dataset")

st.dataframe(
    filtered,
    use_container_width=True
)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Filtered Dataset",
    csv,
    "filtered_dataset.csv",
    "text/csv"
)

st.divider()

st.subheader("Dataset Information")

info = pd.DataFrame({
    "Property":[
        "Rows",
        "Columns",
        "Numerical Columns",
        "Categorical Columns",
        "Missing Values",
        "Duplicate Rows"
    ],
    "Value":[
        df.shape[0],
        df.shape[1],
        len(df.select_dtypes(include=["int64","float64"]).columns),
        len(df.select_dtypes(include="object").columns),
        int(df.isnull().sum().sum()),
        int(df.duplicated().sum())
    ]
})

st.dataframe(
    info,
    use_container_width=True
)

st.divider()

st.subheader("Column Names")

st.dataframe(
    pd.DataFrame(df.columns, columns=["Columns"]),
    use_container_width=True
)

with st.expander("View Complete Dataset"):
    st.dataframe(
        df,
        use_container_width=True
    )