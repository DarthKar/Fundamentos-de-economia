import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar los datos desde un archivo CSV
def cargar_datos(archivo):
    datos = pd.read_csv(archivo, delimiter=';', decimal=',')
    datos['Periodo'] = pd.to_datetime(datos['Periodo(MMM DD, AAAA)'], format='%Y/%m/%d')
    datos['TRM'] = datos['Tasa Representativa del Mercado (TRM)']
    return datos

# Graficar los datos
def graficar_datos(datos):
    plt.figure(figsize=(10, 6))
    plt.plot(datos['Periodo'], datos['TRM'], marker='o', linestyle='-')
    plt.title('Tasa Representativa del Mercado (TRM)')
    plt.xlabel('Fecha')
    plt.ylabel('TRM')
    plt.grid(True)
    st.pyplot(plt)

# Crear un modelo de estimación
def modelo_estimacion(datos):
    # Preparar los datos para el modelo
    X = np.arange(len(datos)).reshape(-1, 1)
    y = datos['TRM'].values

    # Crear y entrenar el modelo
    modelo = LinearRegression()
    modelo.fit(X, y)

    # Predecir valores futuros
    futuro = np.arange(len(datos), len(datos) + 30).reshape(-1, 1)
    predicciones = modelo.predict(futuro)

    # Graficar las predicciones
    plt.figure(figsize=(10, 6))
    plt.plot(datos['Periodo'], datos['TRM'], marker='o', linestyle='-', label='TRM Real')
    plt.plot(pd.date_range(start=datos['Periodo'].iloc[-1], periods=30, closed='right'), predicciones, marker='x', linestyle='--', color='red', label='Estimación')
    plt.title('Estimación de la Tasa Representativa del Mercado (TRM)')
    plt.xlabel('Fecha')
    plt.ylabel('TRM')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# Función principal de Streamlit
def main():
    st.title('Estimación de la Tasa Representativa del Mercado (TRM)')

    # Cargar el archivo CSV
    archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if archivo is not None:
        datos = cargar_datos(archivo)
        st.write("Datos cargados:")
        st.write(datos.head())

        graficar_datos(datos)
        modelo_estimacion(datos)

if __name__ == "__main__":
    main()
