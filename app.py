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

import pandas as pd
import streamlit as st
import plotly.express as px

url = 'https://github.com/patriciagallardo6425-maker/Misi-n-1-AI/raw/refs/heads/main/datos_generales_ficticios__.csv'
df = pd.read_csv(url, sep=';', encoding='utf-8')

# Crear lista de las Columnas de Interés
seleccion_columnas = ['FECHA_HECHOS','DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
# Actualizo el dataframe -df- con las columnas de interés, ordenadas por fecha y reseteo el índice
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

# Convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha (sin hora)
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

conteo_municipios = df['MUNICIPIO_HECHOS'].value_counts()

# CÁLCULO DE MUNICIPIO CON MAS DELITOS
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

# CALCULO DE LA ETAPA QUE MAS VECES SE PRESENTA
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER INDICE .index[0]
etapa_mas_frecuente = df['ETAPA'].value_counts().index[0].upper()
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER VALOR .iloc[0]
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]

# CONSTRUIR LA PÁGINA
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="wide")
st.markdown ("# <font color  = #70BF5A > Dashboard de Delitos - Fiscalía </font>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .bloc-container {
        padding: 3rem 2 rem 2 rem 2 rem;
        max-width: 1600px;
    }
</style>    
""",
unsafe_allow_html= True
)

st.image ("Encabezado/Encabezado.png", use_container_width=True)

st.title("Dashboard de Delitos - Fiscalía")

st.dataframe(df)

# Gráfico de barras apiladas por departamento y tipo de delito
df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig)
st.write(df_delitos)

# Crear 4 columnas para las tarjetas
col1, col2, col3, col4 = st.columns(4)

with col1: 
    # Tarjetas
    ## Tarjeta 1 Municipio con más delitos
    st.markdown (f"""# <h3 style="color: #F2A88D; background-color: #FFF6F5; border: 2px solid #F2A88d; border-radius: 10px; padding:10px;text-align: center"> Municipio con más delitos: <br>{max_municipio.upper()}</h3><br>""", unsafe_allow_html=True)

with col2:

    ## Tarjeta 2 Cantidad de delitos en el municipio con más delitos
    st.markdown (f"""# <h3 style="color: #F2A88D; background-color: #FFF6F5; border: 2px solid #F2A88d; border-radius: 10px; padding:10px;text-align: center"> con {max_cantidad_municipio} reportes</h3><br>""", unsafe_allow_html=True)


st.subheader(f"Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")
st.subheader(f'{etapa_mas_frecuente} tiene {cant_etapa_mas_frecuente} registros')

st.subheader('Comportamiento Delitos')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

st.subheader('Departamentos con mas Casos')
departamento = df['DEPARTAMENTO'].value_counts()
st.bar_chart(departamento)


st.subheader("Distribución por Departamentos")
fig = px.pie(
	names=departamento.index,  # Para los nombres de la Torta
	values=departamento.values # Para los valores de la Torta
)

fig.update_traces(textposition='outside', textinfo='percent+label')
fig.update_layout(showlegend=False, height=400)
st.plotly_chart(fig) 