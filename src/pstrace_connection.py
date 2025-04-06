"""
pstrace_connection.py

Módulo para obtener datos del potenciostato en tiempo real.
Actualmente, si no hay dispositivo, reutiliza la carga desde un archivo .pssession.
"""

import os
import sys
import logging

# 1) Añadir ruta raíz del proyecto para importar pstrace_session
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 2) Importar la función que ya carga y procesa .pssession
try:
    from pstrace_session import cargar_sesion
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("pstrace_session importado correctamente.")
except ImportError as e:
    logging.error("Error al importar pstrace_session: %s", e)
    sys.exit(1)

def obtener_datos_pstrace():
    """
    Obtiene los datos del potenciostato.
    Si no hay dispositivo, lee el archivo .pssession de prueba.
    """
    # Ruta al archivo de prueba
    archivo = os.path.join(project_root, "data", "ultima_medicion.pssession")
    logging.info("Obteniendo datos desde archivo de prueba: %s", archivo)
    return cargar_sesion(archivo)
