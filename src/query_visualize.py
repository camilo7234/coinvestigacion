import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from db_connection import conectar_bd
import logging

# Configuración básica del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obtener_mediciones(conn):
    """
    Consulta la base de datos para obtener las mediciones de voltaje y corriente promedio.
    
    Parámetros:
        conn: Conexión activa a la base de datos PostgreSQL.
    
    Retorna:
        df (DataFrame): DataFrame de pandas con las columnas 'voltage' y 'current_avg', ordenado por measurement_time.
    """
    try:
        query = "SELECT voltage, current_avg FROM measurements ORDER BY measurement_time;"
        df = pd.read_sql(query, conn)
        logging.info("Mediciones obtenidas correctamente de la base de datos.")
        return df
    except Exception as e:
        logging.error("Error al obtener las mediciones: %s", e)
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error

def graficar_mediciones(df):
    """
    Genera un gráfico de línea que muestra el perfil de voltametría a partir de las mediciones.
    
    Parámetros:
        df (DataFrame): DataFrame que debe contener las columnas 'voltage' y 'current_avg'.
    """
    if df.empty:
        logging.warning("El DataFrame está vacío. No hay datos para graficar.")
        return
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(df['voltage'], df['current_avg'], marker='o', linestyle='-')
        plt.xlabel("Voltaje (V)")
        plt.ylabel("Corriente Promedio (μA)")
        plt.title("Perfil de Voltametría")
        plt.grid(True)
        plt.show()
        logging.info("Gráfico generado correctamente.")
    except Exception as e:
        logging.error("Error al graficar las mediciones: %s", e)

if __name__ == "__main__":
    conn = conectar_bd()
    if conn:
        try:
            df = obtener_mediciones(conn)
            graficar_mediciones(df)
        finally:
            conn.close()
            logging.info("Conexión a la base de datos cerrada.")
    else:
        logging.error("No se pudo establecer la conexión a la base de datos.")
