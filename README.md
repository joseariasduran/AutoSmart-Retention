# AutoSmart-Retention: Análisis Predictivo de Posventa Automotriz

![Status](https://img.shields.io/badge/Status-Completed-success)
![Topic](https://img.shields.io/badge/Topic-Data%20Science-blue)

## 📌 Contexto del Negocio
En el sector automotriz, la rentabilidad se desplaza de la venta del auto (front-end) hacia el servicio técnico (back-end). Este proyecto utiliza Machine Learning para identificar qué clientes tienen mayor probabilidad de no regresar al taller una vez finalizado su periodo de garantía.

## 📊 El Dataset
El análisis se basa en datos históricos de servicios que incluyen:
- **Kilometraje promedio anual.**
- **Frecuencia de visitas** al taller.
- **Gasto promedio** en refacciones y mano de obra.
- **Tipo de cliente** (Flotilla vs. Particular).
- **Antigüedad del vehículo.**

## 🛠️ Tecnologías Utilizadas
- **Python 3.9+**
- **Pandas & NumPy** (Procesamiento de datos)
- **Scikit-Learn & XGBoost** (Modelado predictivo)
- **Matplotlib & Seaborn** (Visualización)

## 📈 Hallazgos Principales (EDA)
1. Los clientes que recorren más de 20,000 km al año tienen un 30% más de probabilidad de abandonar el taller oficial por costos de mantenimiento.
2. La falta de una tercera visita preventiva es el "punto de quiebre" para la lealtad del cliente.

## 🤖 Modelado
Se implementó un modelo de **Random Forest Classifier** logrando:
- **Accuracy:** 87%
- **Recall:** 0.82 (Crucial para no perder clientes en riesgo).

## 🚀 Cómo usar este repo
1. Clona el repositorio.
2. Instala dependencias: `pip install -r requirements.txt`.
3. Ejecuta el notebook en `notebooks/02_Modelado.ipynb`.
