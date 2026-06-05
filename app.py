import streamlit as st

# Global configuration - must be called FIRST and ONLY here
st.set_page_config(
    page_title="UNO MINDA HPDC Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.title(" UNO MINDA DIGITAL FACTORY")

st.markdown("""
### NEEV Project

Design & Implementation of an In-House IoT Architecture
for Injection Moulding / HPDC Machines

### Features

✅ Real-Time Monitoring

✅ Golden Zone Analytics

✅ AI Root Cause Detection

✅ Predictive Maintenance

✅ Factory Copilot

---

Select a module from the sidebar to begin monitoring.
""")
