import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df = pd.read_csv('cars_workshop.csv')

st.header('Market of used cars data')
st.write('Filter the data below to see the ads by manufacturer')

#Filling NA values
df['year_produced'] = df.groupby('model_name').fillna(df['year_produced'].median())
df['engine_capacity'] = df.groupby('model_name').fillna(df['engine_capacity'].median())
df['odometer_value'] = df.groupby('model_name').fillna(df['odometer_value'].median())

df = df.drop(df.columns[0], axis=1)
manufacturer_choice = df['manufacturer_name'].unique()
selected_manu = st.selectbox('Select a manufacturer',manufacturer_choice)

min_year, max_year = int(df['year_produced'].min()), int(df['year_produced'].max())

year_range = st.slider("Choose years",value = (min_year,max_year), min_value = min_year, max_value = max_year)

actual_range = list((year_range[0],year_range[1]+1))

df_filtered = df[(df.manufacturer_name == selected_manu) & (df.year_produced.isin(list(actual_range)))]
st.table(df_filtered)

st.header('Price analysis')
st.write("""
##### Let's analyze what influences price the most. We will check how distribution of price varies depending on transmission, engine or body type and state""")

list_for_his = ['transmission','engine_type','body_type','state']
selected_type = st.selectbox('Split for price distribution', list_for_his)

fig1 = px.histogram(df, x='price_usd', color= selected_type)
fig1.update_layout(title= "<b>Split of price by {}</b>".format(selected_type))

st.plotly_chart(fig1)
