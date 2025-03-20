import psycopg2
from db_connection import conectar_bd
from pstrace_connection import obtener_datos_pstrace
import logging

# Configuración básica del logging para registrar información y errores.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def insertar_mediciones(conn, datos):
    """
    Inserta las mediciones en la tabla 'measurements' de la base de datos.

    Parámetros:
        conn: Objeto de conexión a la base de datos.
        datos: Lista de diccionarios, cada uno con las claves 'experiment_id', 'voltage' y 'current_avg'.

    Retorna:
        None
    """
    cursor = conn.cursor()
    try:
        # Registrar la cantidad de registros a insertar
        logging.info("Cantidad de mediciones a insertar: %d", len(datos))
        for medicion in datos:
            # Verificar que el diccionario contenga las claves necesarias.
            if all(key in medicion for key in ('experiment_id', 'voltage', 'current_avg')):
                cursor.execute(
                    "INSERT INTO measurements (experiment_id, voltage, current_avg) VALUES (%s, %s, %s)",
                    (medicion['experiment_id'], medicion['voltage'], medicion['current_avg'])
                )
            else:
                logging.warning("Medición incompleta, se omite: %s", medicion)
        conn.commit()
        logging.info("✅ Datos insertados correctamente.")
    except Exception as e:
        conn.rollback()
        logging.error("Error al insertar datos: %s", e)
    finally:
        cursor.close()

if __name__ == "__main__":
    # Obtener datos directamente desde PS Trace mediante el SDK
    datos = obtener_datos_pstrace()
    if datos:
        conn = conectar_bd()
        if conn:
            try:
                insertar_mediciones(conn, datos)
            finally:
                conn.close()
        else:
            logging.error("No se pudo establecer la conexión a la base de datos.")
    else:
        logging.error("No se obtuvieron datos desde PS Trace.")
