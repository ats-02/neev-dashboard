import streamlit as st
import plotly.graph_objects as go
from utils.data_loader import load_data

st.title("🔮 PREDICTIVE MAINTENANCE")
st.caption("Tooling Degradation Modeling & Equipment Health Lifespan Tracking")
st.divider()

df = load_data()
current_shots = len(df)
DIE_LIFE_CAPACITY = 100000  # Engineering standard limit threshold lifespan for HPDC Die Molds

wear_percentage = min((current_shots / DIE_LIFE_CAPACITY) * 100, 100.0)
remaining_shots = max(DIE_LIFE_CAPACITY - current_shots, 0)

col1, col2 = st.columns(2)

with col1:
    st.subheader("⚙️ Tooling Lifespan Status")
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = wear_percentage,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Die Core Wear Level (%)"},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 60], 'color': "green"},
                {'range': [60, 85], 'color': "yellow"},
                {'range': [85, 100], 'color': "red"}
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Maintenance Metric Breakdown")
    st.metric("Total Cumulative Cycles Completed", f"{current_shots:,} shots")
    st.metric("Estimated Cycles Remaining Before Refurbishment", f"{remaining_shots:,} shots")
    
    if wear_percentage > 85:
        st.error("🚨 CRITICAL ALERT: Die mold core block degradation limits breached! Schedule production pause for tool reconditioning immediately.")
    elif wear_percentage > 60:
        st.warning("⚠️ MAINTENANCE WARNING: Plunger tip and tool cavity degradation accelerating. Ensure tool lubrication spray ratios are optimized.")
    else:
        st.success("🟢 Tooling degradation margins are safe. Structural components are operating within normal wear tolerances.")

