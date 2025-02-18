import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
def cargar_datos(archivo):
    datos = pd.read_csv(archivo)
    return datos

# Calcular la estimación de crecimiento
def calcular_crecimiento(datos, columna):
    datos['Crecimiento'] = datos[columna].pct_change() * 100
    return datos

# Función principal de Streamlit
def main():
    st.title('Estimación de Crecimiento de la Divisa TRM')

    # Cargar el archivo CSV
    archivo = st.file_uploader("Sube tu archivo CSV", type=["csv"])

    if archivo is not None:
        datos = cargar_datos(archivo)
        st.write("Datos cargados:")
        st.write(datos.head())

        # Seleccionar la columna para calcular el crecimiento
        columna = st.selectbox("Selecciona la columna para calcular el crecimiento", datos.columns)

        if columna:
            datos = calcular_crecimiento(datos, columna)
            st.write("Datos con crecimiento calculado:")
            st.write(datos.head())

            # Graficar el crecimiento
            plt.figure(figsize=(10, 6))
            plt.plot(datos.index, datos['Crecimiento'], marker='o', linestyle='-')
            plt.title('Estimación de Crecimiento de la Divisa TRM')
            plt.xlabel('Índice')
            plt.ylabel('Crecimiento (%)')
            plt.grid(True)
            st.pyplot(plt)

if __name__ == "__main__":
    main()
