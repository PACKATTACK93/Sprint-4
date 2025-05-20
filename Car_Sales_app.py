import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from PIL import Image

# Set page configuration
# Scatterplot of price data vs days listed
fig_scatter1 = px.scatter('filtered_df', x='days_listed', y='price', title='Price vs Days Listed')
st.plotly_chart(fig_scatter1)

# Scatterplot of model year vs price (with whatever filtering/adjustments you need)
fig_scatter2 = px.scatter('filtered_df', x='model_year', y='price', title='Price vs Model Year')
st.plotly_chart(fig_scatter2)

# Add a plotly histogram for price distribution
fig_hist = px.histogram('filtered_df', x='price', title='Price Distribution')
st.plotly_chart(fig_hist)
# Add a plotly histogram for mileage distribution
fig_hist_mileage = px.histogram('filtered_df', x='mileage', title='Mileage Distribution')
st.plotly_chart(fig_hist_mileage)
# Add a plotly histogram for year distribution
fig_hist_year = px.histogram('filtered_df', x='model_year', title='Model Year Distribution')
st.plotly_chart(fig_hist_year)
# Add a plotly histogram for days listed distribution
fig_hist_days_listed = px.histogram('filtered_df', x='days_listed', title='Days Listed Distribution')
st.plotly_chart(fig_hist_days_listed)
# Add a plotly histogram for price vs mileage
fig_hist_price_mileage = px.histogram_2d('filtered_df', x='price', y='mileage', title='Price vs Mileage')
st.plotly_chart(fig_hist_price_mileage)
