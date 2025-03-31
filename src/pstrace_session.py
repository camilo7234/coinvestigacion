"""
pstrace_session.py

Este módulo carga un archivo .PSSESSION utilizando el wrapper simplificado del SDK de PalmSens para Windows.
Emplea la función LoadMeasurement de la clase SimpleLoadSaveFunctions para extraer la información de la sesión.

Uso:
    Ejecuta este módulo para probar la carga de datos a partir de un archivo .PSSESSION.
"""

import os
import sys
import logging

# Configuración del logging para registrar actividad y errores.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Asegurar que la ruta del SDK esté en sys.path.
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk', 'PSPythonSDK', 'pspython'))
if sdk_path not in sys.path:
    sys.path.append(sdk_path)
    logging.info("Ruta del SDK agregada: %s", sdk_path)

# Intentar importar el módulo 'pspymethods'.
try:
    import pspymethods
    logging.info("El módulo 'pspymethods' se importó correctamente en pstrace_session.py.")
except ImportError as e:
    logging.error("Error al importar 'pspymethods': %s", e)
    sys.exit(1)

# Importar pythonnet (clr) y cargar el ensamblado PalmSens.Core.Windows.
try:
    import clr
    # Cargar el ensamblado PalmSens.Core.Windows (que se encuentra en tu carpeta de SDK)
    clr.AddReference("PalmSens.Core.Windows")
    from PalmSens.Core.Windows import SimpleLoadSaveFunctions
    logging.info("Se importó correctamente SimpleLoadSaveFunctions desde PalmSens.Core.Windows.")
except Exception as e:
    logging.error("Error al importar SimpleLoadSaveFunctions: %s", e)
    sys.exit(1)

def cargar_sesion(file_path):
    """
    Carga un archivo .PSSESSION utilizando el wrapper simplificado del SDK de PalmSens para Windows.
    Emplea la función LoadMeasurement de la clase SimpleLoadSaveFunctions para obtener la sesión.

    Parámetros:
        file_path (str): Ruta completa al archivo .PSSESSION.

    Retorna:
        data (object): Objeto con la información de la sesión (por ejemplo, un objeto SimpleMeasurement),
                       o None en caso de error.
    """
    try:
        data = SimpleLoadSaveFunctions.LoadMeasurement(file_path)
        logging.info("Sesión cargada exitosamente desde %s", file_path)
        return data
    except Exception as e:
        logging.error("Error al cargar la sesión desde %s: %s", file_path, e)
        return None

if __name__ == "__main__":
    # Definir la ruta al archivo .PSSESSION de prueba.
    archivo_sesion = os.path.join(os.path.dirname(__file__), "..", "data", "ultima_medicion.pssession")
    logging.info("Cargando la sesión desde: %s", archivo_sesion)
    
    datos = cargar_sesion(archivo_sesion)
    if datos is not None:
        logging.info("Datos de la sesión: %s", datos)
    else:
        logging.error("No se pudieron cargar los datos de la sesión.")
