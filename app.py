# app.py
import streamlit as st
import pandas as pd
from utils.validation import validate_dataframe, validate_no_nulls

# Configuración de página
st.set_page_config(page_title="Análisis Penguins", layout="wide")

st.title("🐧 Análisis de Datos: Palmer Penguins")

# Carga de datos
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/penguins.csv")
        return df
    except FileNotFoundError:
        st.error("No se encontró el archivo penguins.csv")
        return None

df = load_data()

if df is not None:
    # Validación
    if validate_dataframe(df):
        st.success("✅ Datos validados correctamente.")
        
        # KPIs básicos
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Registros", len(df))
        with col2:
            nulos = validate_no_nulls(df, df.columns)
            st.metric("Valores Nulos Detectados", nulos)

        # Visualización Tabular
        st.subheader("📊 Visualización Tabular de Datos")
        st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
        
        # Gráfica de ejemplo (Distribución de masa corporal)
        st.subheader("Distribución de Masa Corporal por Especie")
        chart_data = df.groupby('species')['body_mass_g'].mean()
        st.bar_chart(chart_data)
    else:
        st.error("❌ El archivo no tiene el formato esperado.")
else:
    st.warning("Esperando carga de datos...")   

"""
# app.py
import streamlit as st
import pandas as pd
import os

# Obtener la ruta absoluta del directorio donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "penguins.csv")

@st.cache_data
def load_data():
    # Verificar si el archivo existe antes de intentar leerlo
    if not os.path.exists(DATA_FILE):
        st.error(f"❌ El archivo no se encuentra en: {DATA_FILE}")
        return None
    
    try:
        df = pd.read_csv(DATA_FILE)
        return df
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
        return None

# Resto de tu aplicación...
df = load_data()
"""
