import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import time

st.set_page_config(page_title="Production Analytics", page_icon="🏭", layout="wide")

st.title("🏭 Factory Line Throughput Monitor")

if 'total_count' not in st.session_state:
    st.session_state.total_count = 0
    st.session_state.production_log = pd.DataFrame(columns=['Time', 'Items_Per_Min'])

placeholder = st.empty()

# Simulation of Serial data from Arduino
for _ in range(100):
    new_items = np.random.randint(5, 15) # Simulated batch count
    st.session_state.total_count += new_items
    ipm = new_items * 12 # Extrapolated Items Per Minute
    
    new_entry = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), ipm]], 
                             columns=['Time', 'Items_Per_Min'])
    st.session_state.production_log = pd.concat([st.session_state.production_log, new_entry]).tail(20)

    with placeholder.container():
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Units", st.session_state.total_count)
        m2.metric("Current IPM", f"{ipm} units/min", delta="-5%" if ipm < 80 else "Normal")
        m3.metric("Line Efficiency", "94%", delta="Optimal")

        if ipm < 70:
            st.warning("⚠️ BOTTLENECK DETECTED: Production speed dropped below threshold.")

        fig = px.bar(st.session_state.production_log, x='Time', y='Items_Per_Min', 
                     color='Items_Per_Min', color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
        
    time.sleep(5)
