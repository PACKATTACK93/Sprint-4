import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("vehicles_us.csv")

st.set_page_config(page_title="Vehicle Ads Explorer", layout="wide")

st.title("🚗 Vehicle Ads Data Explorer")

# Sidebar filters
st.sidebar.header("🔧 Filter Listings")

# Price slider
min_price = int(df['price'].min())
max_price = int(df['price'].max())
price_range = st.sidebar.slider("Price Range", min_price, max_price, (min_price, max_price))

# Year slider
min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())
year_range = st.sidebar.slider("Model Year Range", min_year, max_year, (min_year, max_year))

# Mileage (odometer) range
min_mileage = int(df['odometer'].min())
max_mileage = int(df['odometer'].max())
mileage_range = st.sidebar.slider("Mileage Range (Odometer)", min_mileage, max_mileage, (min_mileage, max_mileage))

# Condition multi-select
condition_options = st.sidebar.multiselect("Condition", options=df['condition'].dropna().unique(), default=list(df['condition'].dropna().unique()))

# 4WD toggle
show_4wd_only = st.sidebar.checkbox("Only show 4WD vehicles")

# Apply filters
filtered_df = df[
    (df['price'].between(*price_range)) &
    (df['model_year'].between(*year_range)) &
    (df['odometer'].between(*mileage_range)) &
    (df['condition'].isin(condition_options))
]

if show_4wd_only:
    filtered_df = filtered_df[filtered_df['is_4wd'] == 1]

st.markdown(f"### Showing {len(filtered_df)} results")

# Scatter plot: Price vs Days Listed
fig1 = px.scatter(filtered_df, x='days_listed', y='price', color='condition',
                  title='📈 Price vs Days Listed', hover_data=['model', 'model_year'])
st.plotly_chart(fig1, use_container_width=True)

# Scatter plot: Model Year vs Price
# fig2 = px.scatter(filtered_df, x='model_year', y='price', color='fuel',
# title='📉 Price vs Model Year', hover_data=['make', 'model'])
#st.plotly_chart(fig2, use_container_width=True)

# Histogram: Price distribution
fig3 = px.histogram(filtered_df, x='price', nbins=30, title='💰 Price Distribution', color='condition')
st.plotly_chart(fig3, use_container_width=True)

# Histogram: Mileage distribution
fig4 = px.histogram(filtered_df, x='odometer', nbins=30, title='🛣️ Mileage Distribution (Odometer)', color='condition')
st.plotly_chart(fig4, use_container_width=True)

# Heatmap: Price vs Mileage
fig5 = px.density_heatmap(filtered_df, x='price', y='odometer', title='🔥 Price vs Mileage Heatmap')
st.plotly_chart(fig5, use_container_width=True)