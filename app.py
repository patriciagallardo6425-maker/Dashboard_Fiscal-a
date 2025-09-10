import pandas as pd
import streamlit as st
url = "https://github.com/patriciagallardo6425-maker/Misi-n-1-AI/raw/refs/heads/main/datos_generales_ficticios__.csv"
df = pd.read_csv(url, sep=";", encoding="utf-8")


st.dataframe(df)
#Elegir columnas
seleccion_columnas = ["FECHA_HECHOS", "DELITO", "ETAPA", "MUNICIPIO_HECHOS", "FISCAL_ASIGNADO", "DEPARTAMENTO"]
# Actualizo el dataframe con las columnas de interés, ordenadas por fecha y reseteo el índice
df= df[seleccion_columnas].sort_values(by="FECHA_HECHOS", ascending=True).reset_index(drop=True)

#Convertir la columna FECHA_HECHOS a formato fecha
df["FECHA_HECHOS"]= pd.to_datetime(df["FECHA_HECHOS"], errors="coerce")

df_serie_tiempo = df.copy() 
df_serie_tiempo["FECHA_HECHOS"]= df["FECHA_HECHOS"].dt.date

filas= df.shape [0]
columnas = df.shape[1]

st.subheader("Datos ordenados por fecha de hechos")
st.dataframe(df)
st.write (f"Filas: {filas} \n Columnas: {columnas}")
st.dataframe (df)

#Cálculo de municipios con más delitos
max_municipio = df["MUNICIPIO_HECHOS"].value_counts().index[0].upper()
max_cantidad_municipio= df["MUNICIPIO_HECHOS"].value_counts().iloc[0]

# Construir la página
st.title("Dashboard de Delitos - Fiscalía")
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="centered") #or wide 
st.header("Dashboard de Delitos - Fiscalía")


st.markdown(f"Municipio con más delitos: {max_municipio}", unsafe_allow_html=True)
st.markdown(f"Cantidad de delitos: {max_cantidad_municipio}", unsafe_allow_html=True)

st.subheader("Tipo de delito")
delitos = df["DELITO"].value_counts()
st.bar_chart(delitos)


   

