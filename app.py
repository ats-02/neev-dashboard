import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
page_title="UNO MINDA HPDC Dashboard",
layout="wide"
)

st.title("🏭 UNO MINDA HPDC Digital Monitoring System")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Production", "12,450")
col2.metric("OEE", "84%")
col3.metric("Rejection", "2.1%")
col4.metric("Downtime", "45 min")

st.divider()

machine_status = pd.DataFrame({
"Machine":["PDC-01","PDC-02","PDC-03","PDC-04"],
"Status":["Running","Running","Breakdown","Idle"]
})

st.subheader("Machine Status")
st.dataframe(machine_status,use_container_width=True)

st.divider()

time = np.arange(100)

pressure = np.random.normal(250,5,100)

df = pd.DataFrame({
"Time":time,
"Cast Pressure":pressure
})

fig = px.line(
df,
x="Time",
y="Cast Pressure",
title="Live Cast Pressure"
)

st.plotly_chart(fig,use_container_width=True)

