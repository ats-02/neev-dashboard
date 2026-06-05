import streamlit as st
import plotly.graph_objects as go
from utils.data_loader import load_data

st.title("📟 MACHINE DIGITAL TWIN")
st.caption("Real-Time Spatial Simulation & 3-Phase Injection Mechanics")
st.divider()

df = load_data()
latest = df.iloc[-1]

# ---------------------------------------------------------
# Dynamic Spatial Schematic Layout (Plunger Position Simulation)
# ---------------------------------------------------------
st.subheader("⚙️ Live Plunger Stroke Simulation")

# Simulate a physical plunger displacement bar using plotly gauge
fig_twin = go.Figure()
fig_twin.add_trace(go.Indicator(
    mode="gauge+number",
    value=float(latest['biscuit_thick']),
    title={'text': "Biscuit Thickness End Position (mm)"},
    gauge={
        'shape': "bullet",
        'axis': {'range': [0, 40]},
        'threshold': {
            'line': {'color': "green", 'width': 4},
            'thickness': 0.75,
            'value': 21
        },
        'bar': {'color': "#2ca02c" if 18 <= latest['biscuit_thick'] <= 24 else "#d62728"},
        'steps': [
            {'range': [0, 18], 'color': "#ff9999"},
            {'range': [18, 24], 'color': "#c6efce"},
            {'range': [24, 40], 'color': "#ff9999"}
        ]
    }
))
fig_twin.update_layout(height=180, margin=dict(l=20, r=20, t=40, b=20))
st.plotly_chart(fig_twin, use_container_width=True)

st.divider()

# ---------------------------------------------------------
# 3-Phase Injection Breakdown
# ---------------------------------------------------------
st.subheader("🔄 3-Phase Process Execution Analytics")

p1, p2, p3 = st.columns(3)

with p1:
    st.info("### 🟦 Phase 1: Slow Shot")
    st.markdown("**Objective**: Pre-fill sleeve, prevent wave air entrapment.")
    st.metric("Low Velocity (Lo-V)", f"{float(latest['lo_v']):.2f} m/s", help="Target: 0.25 - 0.27 m/s")
    st.caption("🟢 Phase Status: Stable Laminar Flow" if 0.25 <= latest['lo_v'] <= 0.27 else "⚠️ Phase Status: Turbulence Risk")

with p2:
    st.info("### 🟨 Phase 2: Fast Injection")
    st.markdown("**Objective**: Fill die cavity instantly before metal freezes.")
    st.metric("High Velocity (Hi-V)", f"{float(latest['hi_v']):.2f} m/s", help="Target: 3.90 - 4.20 m/s")
    st.metric("Velocity Rise Time (V-Rise)", f"{float(latest['v_rise']):.3f} s")
    st.caption("🟢 Phase Status: Cavity Fill In Spec" if 3.90 <= latest['hi_v'] <= 4.20 else "❌ Phase Status: Velocity Deficit")

with p3:
    st.info("### 🟥 Phase 3: Intensification")
    st.markdown("**Objective**: Compress remaining gas, eliminate shrinkage porosity.")
    st.metric("Intensification Pressure", f"{float(latest['intensify']):.1f} bar", help="Target: 230 - 240 bar")
    st.metric("Cast Pressure", f"{float(latest['cast_pressure']):.1f} bar", help="Target: 930 - 950 bar")
    st.caption("🟢 Phase Status: Full Compressive Hold" if 230 <= latest['intensify'] <= 240 else "🚨 Phase Status: Low Density/Porosity Hazard")

