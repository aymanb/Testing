import numpy as np
import plotly.graph_objects as go
import streamlit as st

z = np.random.random_sample((3, 2))
fig = go.Figure(data=go.Contour(z=z))

st.plotly_chart(
    fig, 
    theme="streamlit",  # ✨ Optional, this is already set by default!
)
