import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Car Sales Ads",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load data
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_ads.csv")