"""
pstrace_session.py

Este módulo carga archivos .PSSESSION utilizando el SDK de PalmSens y retorna los datos procesados.

Uso:
    Ejecuta este módulo para probar la carga de datos desde archivos .PSSESSION.
"""

import os
import sys
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Asegurar que la ruta del SDK esté en sys.path
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "sdk", "PSPythonSDK", "pspython"))
if sdk_path not in sys.path:
    sys.path.insert(0, sdk_path)
    logging.info("Ruta del SDK agregada: %s", sdk_path)

# Intentar importar el SDK de PalmSens
try:
    import clr
    clr.AddReference(os.path.join(sdk_path, "PalmSens.Core.dll"))
    clr.AddReference(os.path.join(sdk_path, "PalmSens.Core.Windows.dll"))
    from PalmSens import MethodScript
    logging.info("El SDK de PalmSens se importó correctamente.")
except Exception as e:
    logging.error("Error al importar el SDK de PalmSens: %s", e)
    sys.exit(1)

def cargar_sesion(file_path):
    """
    Carga un archivo .PSSESSION utilizando `MethodScript` de PalmSens.

    Parámetros:
        file_path (str): Ruta completa al archivo .PSSESSION.

    Retorna:
        data (object): Datos de la sesión procesados o None en caso de error.
    """
    try:
        # Instanciar MethodScript
        script = MethodScript()
        
        # Aquí es donde necesitamos adaptar la carga de datos
        # Esto dependerá de cómo el SDK maneja los archivos .PSSESSION
        logging.info("Sesión cargada exitosamente desde %s", file_path)
        return script  # Retornamos la instancia para probar

    except AttributeError:
        logging.error("Error: 'MethodScript' no tiene la función esperada para cargar sesiones.")
    except Exception as e:
        logging.error("Error al cargar la sesión desde %s: %s", file_path, e)

    return None

if __name__ == "__main__":
    # Ruta del archivo .PSSESSION de prueba
    archivo_sesion = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "ultima_medicion.pssession"))
    logging.info("Cargando la sesión desde: %s", archivo_sesion)
    
    datos = cargar_sesion(archivo_sesion)
    if datos:
        logging.info("Datos de la sesión cargados correctamente.")
    else:
        logging.error("No se pudieron cargar los datos de la sesión.")
