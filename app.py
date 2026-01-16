import streamlit as st
import pandas as pd
import joblib
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Configuración de la página
st.set_page_config(page_title="AutoSmart Retention Dashboard", layout="wide")

st.title("🚗 AutoSmart: Predicción de Retención en Posventa")
st.markdown("""
Esta aplicación predice la probabilidad de que un cliente **abandone el taller oficial** una vez terminada su garantía. Utiliza un modelo de Machine Learning (Random Forest).
""")

# Barra lateral para entrada de datos
st.sidebar.header("Datos del Cliente / Vehículo")

def user_input_features():
    edad = st.sidebar.slider("Edad del Vehículo (Años)", 1, 15, 3)
    km = st.sidebar.number_input("Kilometraje Anual Promedio", 5000, 50000, 15000)
    servicios = st.sidebar.slider("Total de Servicios Realizados", 1, 20, 5)
    gasto = st.sidebar.slider("Gasto Promedio por Visita (USD)", 50, 1000, 250)
    garantia = st.sidebar.selectbox("¿Garantía Vigente?", ("Sí", "No"))
    quejas = st.sidebar.selectbox("Número de quejas previas", (0, 1, 2, 3))
    
    data = {
        'edad_vehiculo_años': edad,
        'km_anuales_promedio': km,
        'servicios_realizados': servicios,
        'gasto_promedio_usd': gasto,
        'garantia_vigente': 1 if garantia == "Sí" else 0,
        'quejas_abiertas': quejas
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Mostrar datos ingresados
st.subheader("📊 Datos del Cliente a Evaluar")
st.write(input_df)

# Simulación de Predicción (En un caso real, cargarías el modelo .pkl)
# Aquí lo calculamos basado en lógica del modelo para demostración
probabilidad = 0.1
if input_df['garantia_vigente'][0] == 0: probabilidad += 0.4
if input_df['edad_vehiculo_años'][0] > 5: probabilidad += 0.3
if input_df['quejas_abiertas'][0] > 0: probabilidad += 0.15

st.subheader("🔮 Resultado de la Predicción")
col1, col2 = st.columns(2)

with col1:
    if probabilidad > 0.5:
        st.error(f"ALTO RIESGO DE ABANDONO: {probabilidad*100:.1f}%")
    else:
        st.success(f"CLIENTE LEAL: Probabilidad de abandono {probabilidad*100:.1f}%")

with col2:
    st.info("💡 **Recomendación:** Enviar cupón de descuento en mano de obra o check-up gratuito.")