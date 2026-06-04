import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.golden_zone import calculate_health
from utils.metrics import production_summary

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="Command Center",
    page_icon="🏭",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------

df = load_data()

latest = df.iloc[-1]

health = calculate_health(latest)

summary = production_summary(df)

# ----------------------------
# Header
# ----------------------------

st.title("🏭 UNO MINDA HPDC COMMAND CENTER")

st.markdown(
    "Real-Time Machine Monitoring & Process Intelligence"
)

# ----------------------------
# KPI SECTION
# ----------------------------

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric(
        "Total Shots",
        summary["total_shots"]
    )

with col2:
    st.metric(
        "Avg Cycle Time",
        summary["avg_cycle_time"]
    )

with col3:
    st.metric(
        "Avg Cast Pressure",
        summary["avg_cast_pressure"]
    )

with col4:
    st.metric(
        "Current Hi-V",
        latest["hi_v"]
    )

with col5:
    st.metric(
        "Health Score",
        f"{health}%"
    )

st.divider()

# ----------------------------
# Machine Health Status
# ----------------------------

st.subheader("Machine Status")

if health >= 80:

    st.success(
        "🟢 MACHINE HEALTHY"
    )

elif health >= 60:

    st.warning(
        "🟡 ATTENTION REQUIRED"
    )

else:

    st.error(
        "🔴 CRITICAL CONDITION"
    )

st.divider()

# ----------------------------
# Live Parameter Trend
# ----------------------------

st.subheader("Process Trend Analysis")

parameter = st.selectbox(
    "Select Parameter",
    [
        "lo_v",
        "hi_v",
        "v_rise",
        "intensify",
        "p_rise",
        "biscuit_thick",
        "cast_pressure",
        "cycle_time"
    ]
)

fig = px.line(
    df,
    x="cycle",
    y=parameter,
    markers=True,
    title=f"{parameter} Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------
# Current Parameter Snapshot
# ----------------------------

st.subheader("Current Process Parameters")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Lo-V", latest["lo_v"])
c2.metric("Hi-V", latest["hi_v"])
c3.metric("V-Rise", latest["v_rise"])
c4.metric("Intensify", latest["intensify"])

c5,c6,c7,c8 = st.columns(4)

c5.metric("P-Rise", latest["p_rise"])
c6.metric("Biscuit Thickness", latest["biscuit_thick"])
c7.metric("Cast Pressure", latest["cast_pressure"])
c8.metric("Cycle Time", latest["cycle_time"])

st.divider()

# ----------------------------
# Latest Records
# ----------------------------

st.subheader("Latest 25 Shots")

st.dataframe(
    df.tail(25),
    use_container_width=True
)
