import streamlit as st
from utils.data_loader import load_data
from utils.golden_zone import calculate_health

st.title("🤖 FACTORY COPILOT AI")
st.caption("Natural Language Interface for Machine Diagnostics & Standard Operating Procedures (SOPs)")
st.divider()

df = load_data()
latest = df.iloc[-1]
health = calculate_health(latest)

# Pre-packaged smart diagnostic query buttons
st.write("💡 **Ask Copilot Quick-Queries:**")
c1, c2, c3 = st.columns(3)
q1 = c1.button("📋 Summarize Machine Health State")
q2 = c2.button("🔧 Get Biscuit Defect SOP Fix")
q3 = c3.button("📊 Analyze Velocity Anomalies")

user_input = st.text_input("Ask the Factory Intelligence Copilot anything about this HPDC Machine:", placeholder="e.g., What should I check if cast pressure drops below 930 bar?")

response_placeholder = st.container()

with response_placeholder:
    if q1:
        st.markdown(f"""
        ### 🤖 Copilot Summary Report:
        * **Current Condition**: The machine health score is currently at **{health}%**.
        * **Process Diagnostics**: The latest recorded production shot cycle number is **{int(latest['cycle'])}**. 
        * **Operational Status**: Cast Pressure is holding at `{latest['cast_pressure']} bar` and high velocity is clocking at `{latest['hi_v']} m/s`.
        """)
    elif q2:
        st.markdown("""
        ### 🤖 SOP Reference: Biscuit Thickness Issues
        1. **If Biscuit is too thick (> 24mm)**: The system shows ladle metering overpour issues. Recalibrate dosing furnace timing or step-piston cutoff heights.
        2. **If Biscuit is too thin (< 18mm)**: Check for metal leakage across die parting lines, or verify insufficient initial charge weight from the ladle line feeding system.
        """)
    elif q3:
        st.markdown(f"""
        ### 🤖 Plunger Velocity Analysis Report:
        * The current Low Velocity (`lo_v`) is running at `{latest['lo_v']} m/s` (Target: 0.25 - 0.27).
        * The current High Velocity (`hi_v`) is running at `{latest['hi_v']} m/s` (Target: 3.90 - 4.20).
        * If these values lag, check hydraulic circuit oil viscosity temperatures and evaluate pump valves for particulate buildup.
        """)
    elif user_input:
        # Dynamic search matcher for user custom input phrases
        query = user_input.lower()
        if "pressure" in query:
            st.markdown(f"### 🤖 Copilot Response:\nYour latest intensification pressure reading is `{latest['intensify']} bar` and cast pressure is `{latest['cast_pressure']} bar`. If pressure drops below limits, inspect nitrogen accumulator pre-charge gas pressures and verify hydraulic check valves for internal backflow leakage.")
        elif "cycle" in query:
            st.markdown(f"### 🤖 Copilot Response:\nYour last recorded cycle processing time duration clocked in at `{latest['cycle_time']} seconds`. Variations here point directly to erratic die opening/closing strokes or manual slide sequencing intervention pauses from local machine operators.")
        else:
            st.markdown("### 🤖 Copilot Response:\nI received your query. Based on current system settings, all core parameters are logged in your local data frames. For physical maintenance protocols, please cross-reference your specific **Uno Minda Plant SOP manuals** or launch one of the targeted diagnostic templates listed above.")

