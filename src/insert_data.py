# src/insert_data.py

import os, sys, logging

# 1) Rutas al proyecto y SDK
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
sdk_path = os.path.join(project_root, 'sdk', 'PSPythonSDK', 'pspython')
if sdk_path not in sys.path:
    sys.path.insert(0, sdk_path)

from db_connection import conectar_bd
from pstrace_session import cargar_sesion

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def insertar_mediciones(conn, session):
    """
    Inserta las mediciones de un SessionManager en la BD.
    """
    # 1) Obtener la colección de mediciones
    try:
        measurements = list(session.Measurements)  # Convierte el IEnumerable a lista Python
    except Exception:
        # Si no es enumerable, intenta acceder a .Measurements como atributo
        measurements = session.Measurements

    count = len(measurements)
    logging.info("Cantidad de mediciones a insertar: %d", count)

    cursor = conn.cursor()
    try:
        for meas in measurements:
            # Ajusta estos nombres de propiedades según el objeto Measurement real:
            voltage     = meas.Potential        # p.ej. Potential o Voltage
            current_avg = meas.CurrentAverage   # o Current, o calcula promedio si son múltiples
            cursor.execute(
                "INSERT INTO measurements (experiment_id, voltage, current_avg) VALUES (%s, %s, %s)",
                (1, voltage, current_avg)
            )
        conn.commit()
        logging.info("✅ Mediciones insertadas correctamente.")
    except Exception as e:
        conn.rollback()
        logging.error("Error al insertar datos: %s", e)
    finally:
        cursor.close()

if __name__ == "__main__":
    # 1) Cargar la sesión desde el .pssession
    ruta = os.path.join(project_root, "data", "ultima_medicion.pssession")
    session = cargar_sesion(ruta)
    if not session:
        logging.error("No se pudo cargar la sesión, deteniendo.")
        sys.exit(1)

    # 2) Conectar a la BD
    conn = conectar_bd()
    if not conn:
        logging.error("No se pudo conectar a la base de datos.")
        sys.exit(1)

    # 3) Insertar las mediciones
    insertar_mediciones(conn, session)

    # 4) Cerrar la conexión
    conn.close()
