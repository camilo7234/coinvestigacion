import psycopg2
import logging

# Configuración básica del logging para registrar información y errores
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def conectar_bd():
    """
    Establece la conexión con la base de datos PostgreSQL.

    Parámetros de conexión:
        - dbname: "deteccion_metales"
        - user: "postgres"
        - password: "1234"
        - host: "localhost"
        - port: "5432"

    Retorna:
        conn: Objeto de conexión a la base de datos si la conexión es exitosa,
              de lo contrario, retorna None.
    """
    try:
        conn = psycopg2.connect(
            dbname="deteccion_metales",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        logging.info("Conexión exitosa a la base de datos.")
        return conn
    except Exception as e:
        logging.error("Error conectando a la BD: %s", e)
        return None

if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        logging.info("Prueba de conexión exitosa.")
        conexion.close()
    else:
        logging.error("La conexión a la base de datos falló.")

