import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_data
from utils.golden_zone import calculate_health

st.title("💼 MANAGEMENT IMPACT & OEE")
st.caption("Enterprise Cost Savings, Carbon Footprint Optimization & Asset Performance")
st.divider()

df = load_data()
latest = df.iloc[-1]
total_shots = len(df)

# Calculate dynamic scrap rates based on historical data breaches
out_of_spec_count = 0
for index, row in df.iterrows():
    if not (0.25 <= row['lo_v'] <= 0.27 and 3.90 <= row['hi_v'] <= 4.20 and 930 <= row['cast_pressure'] <= 950):
        out_of_spec_count += 1

scrap_rate = (out_of_spec_count / total_shots) * 100
yield_rate = 100.0 - scrap_rate

# ---------------------------------------------------------
# High-Level Management KPIs
# ---------------------------------------------------------
m1, m2, m3, m4 = st.columns(4)

# Simulated OEE parameters derived from process health
availability = 92.5  # Plant average operational uptime %
performance = 94.0   # Speed optimization index %
quality = yield_rate # Dynamic quality yield from Golden Zone data
oee_score = (availability / 100) * (performance / 100) * (quality / 100) * 100

m1.metric("Overall Equipment Effectiveness (OEE)", f"{oee_score:.1f}%", delta=f"{(oee_score - 85.0):+.1f}% vs Target")
m2.metric("First-Time Yield Rate", f"{yield_rate:.1f}%")

# Cost calculations (Assuming average aluminum casting part cost is ₹850)
estimated_savings = out_of_spec_count * 850 * 0.40  # 40% cost reduction by catching bugs before casting completes
m3.metric("NEEV Cost Deflection Saved", f"₹{int(estimated_savings):,}", delta="Accumulated This Month", delta_color="inverse")

# Carbon footprint data (Assuming IoT optimization reduced cycle power by 0.12 kWh per shot)
co2_saved = total_shots * 0.12 * 0.85  # kg of CO2 saved
m4.metric("Carbon Footprint Reduced", f"{co2_saved:.1f} kg CO2", delta="Energy Optimization")

st.divider()

# ---------------------------------------------------------
# OEE Visual Breakdown
# ---------------------------------------------------------
st.subheader("📊 OEE Component Analysis")

oee_data = pd.DataFrame({
    "Metric Category": ["Availability (Uptime)", "Performance (Speed)", "Quality (Yield Rate)"],
    "Score (%)": [availability, performance, round(quality, 1)]
})

fig_oee = px.bar(
    oee_data, 
    x="Score (%)", 
    y="Metric Category", 
    orientation='h',
    text="Score (%)",
    color="Score (%)",
    color_continuous_scale=px.colors.sequential.Blues,
    template="plotly_white"
)
fig_oee.update_layout(xaxis=dict(range=[0, 110]), showlegend=False, height=260)
st.plotly_chart(fig_oee, use_container_width=True)

st.markdown("""
***
### 💡 Plant Manager Strategic Briefing
* **Quality Protection**: By utilizing the **Golden Zone Analytics Engine**, the machine automatically flags out-of-spec shots before parts enter the downstream machining line, dramatically lowering customer warranty claim risks.
* **Energy Savings**: Stabilizing cycle times between **45s and 50s** cuts heating cylinder energy loss peaks, directly aligning with **Uno Minda's Green Factory Sustainability Directives**.
""")

