"""
pstrace_session.py

Este módulo carga uno o varios archivos .PSSESSION utilizando el SDK de PalmSens y retorna los datos procesados.
Utiliza el método 'load_session' de la clase MethodSCRIPTDevice para extraer la información de la sesión.

Uso:
    Ejecuta este módulo para probar la carga de datos a partir de archivos .PSSESSION.
    Para facilitar el uso, se puede extender posteriormente para que el sistema lea automáticamente todos
    los archivos en una carpeta determinada.
"""

import os
import sys
import logging

# Configuración del logging para registrar la actividad y errores.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Asegurar que la ruta del SDK esté en sys.path (no se modifica según la estructura establecida).
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

def cargar_sesion(file_path):
    """
    Carga un archivo .PSSESSION utilizando el SDK de PalmSens.

    Parámetros:
        file_path (str): Ruta completa al archivo .PSSESSION.

    Retorna:
        data (object): Estructura de datos con la información de la sesión (por ejemplo, lista de diccionarios),
                       o None en caso de error.
    """
    try:
        # Instanciar el dispositivo. No es necesario especificar el puerto, ya que se trabaja con archivo.
        device = pspymethods.MethodSCRIPTDevice()
        # Se asume que el método load_session existe en el SDK. Si el nombre o los parámetros difieren,
        # ajusta esta llamada de acuerdo a la documentación oficial.
        data = device.load_session(file_path)
        logging.info("Sesión cargada exitosamente desde %s", file_path)
        return data
    except Exception as e:
        logging.error("Error al cargar la sesión desde %s: %s", file_path, e)
        return None

if __name__ == "__main__":
    # Definir la ruta al archivo .PSSESSION de prueba.
    # Se usa la ruta completa proporcionada: "C:\coinvestigacion\data\ultima_medicion.pssession"
    archivo_sesion = os.path.join(os.path.dirname(__file__), "..", "data", "ultima_medicion.pssession")
    logging.info("Cargando la sesión desde: %s", archivo_sesion)
    
    datos = cargar_sesion(archivo_sesion)
    if datos is not None:
        logging.info("Datos de la sesión: %s", datos)
    else:
        logging.error("No se pudieron cargar los datos de la sesión.")
