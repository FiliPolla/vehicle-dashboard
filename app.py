import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.header('Panel de Control de Anuncios de Venta de Vehículos')

# Leer el dataset
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir el histograma
hist_button = st.button('Mostrar histograma de odómetro')

if hist_button:
    st.write('Histograma: Distribución del kilometraje de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Mostrar gráfico de dispersión de odómetro vs precio')

if scatter_button:
    st.write('Gráfico de dispersión: Kilometraje vs Precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)