import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.data_loader import load_data
from config.settings import GOLDEN_ZONE

st.title("📊 GOLDEN ZONE ANALYTICS")
st.caption("Statistical Process Control & Tolerance Compliance Matrix")
st.divider()

df = load_data()
total_shots = len(df)

# Create summary compliance grid
st.subheader("⚠️ Parameter Out-of-Spec Distribution")
compliance_data = []

for param, (low, high) in GOLDEN_ZONE.items():
    under_spec = int((df[param] < low).sum())
    in_spec = int(((df[param] >= low) & (df[param] <= high)).sum())
    over_spec = int((df[param] > high).sum())
    
    compliance_data.append({
        "Parameter": param.upper(),
        "Below Limit (Low)": under_spec,
        "Inside Golden Zone": in_spec,
        "Above Limit (High)": over_spec,
        "Yield Rate (%)": round((in_spec / total_shots) * 100, 2)
    })

import pandas as pd
comp_df = pd.DataFrame(compliance_data)
st.dataframe(comp_df, use_container_width=True, hide_index=True)

st.divider()

# Advanced Bell Curve / Histogram Distribution View
st.subheader("📈 Statistical Distribution Analysis")
selected_p = st.selectbox("Select Process Parameter for Distribution Plot", list(GOLDEN_ZONE.keys()))

low_limit, high_limit = GOLDEN_ZONE[selected_p]

fig = px.histogram(
    df, x=selected_p, nbins=30, 
    title=f"Histogram Chart for {selected_p.upper()}",
    template="plotly_white", color_discrete_sequence=["#1f77b4"]
)

# Overlay tolerance boundary gate lines
fig.add_vline(x=low_limit, line_dash="dash", line_color="red", annotation_text="LSL (Lower Spec Limit)")
fig.add_vline(x=high_limit, line_dash="dash", line_color="red", annotation_text="USL (Upper Spec Limit)")

st.plotly_chart(fig, use_container_width=True)

