import streamlit as st
from utils.data_loader import load_data

st.set_page_config(layout="wide")

df = load_data()

latest = df.iloc[-1]

st.title("🏭 HPDC Command Center")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Lo-V",
    latest["lo_v"]
)

col2.metric(
    "Hi-V",
    latest["hi_v"]
)

col3.metric(
    "Cast Pressure",
    latest["cast_pressure"]
)

col4.metric(
    "Cycle Time",
    latest["cycle_time"]
)

st.divider()

st.subheader("Latest Shots")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

