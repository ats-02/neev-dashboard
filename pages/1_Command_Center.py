import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.golden_zone import calculate_health
from utils.metrics import production_summary

# NOTE: st.set_page_config removed to prevent multi-page configuration crashes

# Custom CSS for high-density industrial dashboard card components
st.markdown("""
    <style>
    .block-container {padding-top: 1.5rem; padding-bottom: 1.5rem;}
    div[data-testid="stMetric"] {
        background-color: #f8f9fa;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #e9ecef;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Data Processing Pipeline
# ----------------------------
df = load_data()
latest = df.iloc[-1]
health = calculate_health(latest)
summary = production_summary(df)

# ----------------------------
# Header & Real-time Status Banner
# ----------------------------
header_col, status_col = st.columns([3, 1], vertical_alignment="center")

with header_col:
    st.title("🏭 UNO MINDA HPDC COMMAND CENTER")
    st.caption("Real-Time Machine Monitoring & Process Intelligence")

with status_col:
    if health >= 80:
        st.success(f"🟢 MACHINE HEALTHY ({health}%)")
    elif health >= 60:
        st.warning(f"🟡 ATTENTION REQUIRED ({health}%)")
    else:
        st.error(f"🔴 CRITICAL CONDITION ({health}%)")

st.divider()

# ----------------------------
# Production Aggregates (KPIs)
# ----------------------------
with st.container():
    kpi_cols = st.columns(5)
    
    kpi_cols[0].metric(label="Total Shots", value=f"{int(summary['total_shots']):,}")
    kpi_cols[1].metric(label="Avg Cycle Time", value=f"{float(summary['avg_cycle_time']):.2f} s")
    kpi_cols[2].metric(label="Avg Cast Pressure", value=f"{float(summary['avg_cast_pressure']):.1f} bar")
    kpi_cols[3].metric(label="Current Hi-V", value=f"{float(latest['hi_v']):.2f} m/s")
    kpi_cols[4].metric(label="Health Score", value=f"{health}%")

st.divider()

# ----------------------------
# Dual Analytics & Monitoring Layout
# ----------------------------
graph_col, snapshot_col = st.columns([1.1, 0.9], gap="large")

with graph_col:
    st.subheader("📊 Process Trend Analysis")
    
    # Mapping raw columns to human-readable titles
    param_display = {
        "lo_v": "Low Velocity (Lo-V)",
        "hi_v": "High Velocity (Hi-V)",
        "v_rise": "Velocity Rise Time (V-Rise)",
        "intensify": "Intensification Pressure",
        "p_rise": "Pressure Rise Time (P-Rise)",
        "biscuit_thick": "Biscuit Thickness",
        "cast_pressure": "Cast Pressure",
        "cycle_time": "Cycle Time"
    }
    
    selected_label = st.selectbox(
        "Select Trend Parameter",
        options=list(param_display.keys()),
        format_func=lambda x: param_display[x],
        label_visibility="collapsed"
    )
    
    fig = px.line(
        df,
        x="cycle",
        y=selected_label,
        markers=True,
        title=f"Historical {param_display[selected_label]} Trend",
        template="plotly_white"
    )
    fig.update_layout(margin=dict(l=15, r=15, t=35, b=15), height=380)
    st.plotly_chart(fig, use_container_width=True)

with snapshot_col:
    st.subheader("⏱️ Parameter Snapshot")
    
    # Grid optimization for compact numeric scannability
    c1, c2 = st.columns(2)
    c1.metric("Lo-V", f"{float(latest['lo_v']):.2f} m/s")
    c2.metric("Hi-V", f"{float(latest['hi_v']):.2f} m/s")
    
    c3, c4 = st.columns(2)
    c3.metric("V-Rise", f"{float(latest['v_rise']):.3f} s")
    c4.metric("Intensify", f"{float(latest['intensify']):.1f} bar")
    
    c5, c6 = st.columns(2)
    c5.metric("P-Rise", f"{float(latest['p_rise']):.3f} s")
    c6.metric("Biscuit Thickness", f"{float(latest['biscuit_thick']):.1f} mm")
    
    c7, c8 = st.columns(2)
    c7.metric("Cast Pressure", f"{float(latest['cast_pressure']):.1f} bar")
    c8.metric("Cycle Time", f"{float(latest['cycle_time']):.1f} s")

st.divider()

# ----------------------------
# Real-Time Data Pipeline Log
# ----------------------------
with st.container():
    st.subheader("📋 Latest 25 Shots Log")
    st.dataframe(
        df.tail(25).sort_values(by="cycle", ascending=False),
        use_container_width=True,
        height=280
    )
