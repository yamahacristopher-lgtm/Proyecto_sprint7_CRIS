import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehicles EDA", layout="wide")

@st.cache_data
def load_data(path: str):
    return pd.read_csv(path)

st.header("Análisis Exploratorio de Vehicles")

DATA_PATH = "vehicles_us.csv"
df = load_data(DATA_PATH)

st.write("Vista rápida del dataset:", df.head())

num_cols = df.select_dtypes(include="number").columns.tolist()

st.subheader("Controles")
col1, col2, col3 = st.columns(3)

hist_x = st.selectbox("Histograma: columna numérica", num_cols if num_cols else [None])
scat_x = st.selectbox("Dispersión: eje X (numérico)", num_cols if num_cols else [None])
scat_y = st.selectbox("Dispersión: eje Y (numérico)", num_cols if num_cols else [None])

if st.button("Mostrar histograma"):
    if hist_x:
        fig = px.histogram(df, x=hist_x, nbins=50, title=f"Histograma de {hist_x}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No hay columnas numéricas disponibles para el histograma.")

if st.button("Mostrar dispersión"):
    if scat_x and scat_y:
        fig = px.scatter(df, x=scat_x, y=scat_y, title=f"Dispersión {scat_x} vs {scat_y}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Selecciona columnas numéricas para X e Y.")
