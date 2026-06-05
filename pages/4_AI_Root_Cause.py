import streamlit as st
from utils.data_loader import load_data
from config.settings import GOLDEN_ZONE

st.title("🧠 AI ROOT CAUSE DETECTION")
st.caption("Expert System Rule Engine for Real-Time Casting Defect Diagnosis")
st.divider()

df = load_data()
latest = df.iloc[-1]

st.subheader("🔍 Active Anomaly Tracking System")

# Evaluate parameter bounds
status = {}
for param, (low, high) in GOLDEN_ZONE.items():
    val = latest[param]
    if val < low:
        status[param] = "LOW"
    elif val > high:
        status[param] = "HIGH"
    else:
        status[param] = "OK"

# Display deviations
anomalies_detected = False
for param, stat in status.items():
    if stat != "OK":
        st.error(f"❌ Anomaly: **{param.upper()}** is currently too **{stat}** (Current Value: {latest[param]})")
        anomalies_detected = True

if not anomalies_detected:
    st.success("✨ Zero Process Anomalies Detected on the Latest Shot. Machine physics are fully stable.")
else:
    st.divider()
    st.subheader("🛠️ Automated Root Cause Diagnostics")
    
    # Casting Expert System Diagnosis Logic Rules
    if status.get("hi_v") == "LOW" and status.get("cast_pressure") == "LOW":
        st.warning("""
        ### 🚨 Diagnostic: High Risk of Cold Shut / Short Fill Defect
        * **Probable Root Cause**: Insufficient plunger velocity matched with low intensification pressure prevents the molten aluminum alloy cavity fill sequence from finishing before cooling.
        * **Corrective Action**: Inspect hydraulic accumulation line pressure seals, increase step-2 shot velocity limits, or check for mechanical piston resistance.
        """)
        
    elif status.get("biscuit_thick") == "HIGH" and status.get("intensify") == "LOW":
        st.warning("""
        ### 🚨 Diagnostic: High Risk of Internal Gas Porosity
        * **Probable Root Cause**: Excess biscuit thickness combined with low intensification pressure indicates that gas venting paths were choked, leaving compressed air pockets inside the casting die.
        * **Corrective Action**: Decrease ladle pour weight, optimize casting vent profiles, and increase phase-3 intensification trigger timing.
        """)
        
    elif status.get("cast_pressure") == "HIGH" and status.get("biscuit_thick") == "LOW":
        st.warning("""
        ### 🚨 Diagnostic: High Risk of Die Flash / Core Damage
        * **Probable Root Cause**: Excess pressure spikes exceeding safety specs against an abnormally thin biscuit layer create extreme parting plane forces, causing molten metal to escape the die.
        * **Corrective Action**: Verify tie-bar tonnage calibration clamping values and inspect structural sealing surfaces for debris.
        """)
    else:
        st.info("💡 **Diagnostic Note**: Minor independent variable drift detected. Monitor parameter trends closely to see if variations compound over time.")

