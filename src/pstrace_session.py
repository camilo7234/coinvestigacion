"""
pstrace_session.py

Este módulo carga un archivo .PSSESSION utilizando el SDK completo de PalmSens.
Se utiliza el método LoadSessionFile de la clase LoadSaveHelperFunctions (del namespace PalmSens.Core.LoadSave)
para extraer la sesión completa.

Uso:
    Ejecuta este módulo para probar la carga de datos a partir de un archivo .PSSESSION.
"""

import os
import sys
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Agregar la ruta del SDK al sys.path
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk', 'PSPythonSDK', 'pspython'))
if sdk_path not in sys.path:
    sys.path.append(sdk_path)
logging.info("Ruta del SDK agregada: %s", sdk_path)

# Intentar importar el módulo pspymethods para confirmar la carga del SDK
try:
    import pspymethods
    logging.info("El módulo 'pspymethods' se importó correctamente en pstrace_session.py.")
except ImportError as e:
    logging.error("Error al importar 'pspymethods': %s", e)
    sys.exit(1)

# Importar pythonnet (clr) y cargar el ensamblado PalmSens.Core.dll
try:
    import clr
    import pythonnet
    pythonnet.load("coreclr")
    clr.AddReference("System")
    dll_path = os.path.join(sdk_path, "PalmSens.Core.dll")
    if not os.path.exists(dll_path):
        logging.error("No se encontró el archivo DLL en la ruta esperada: %s", dll_path)
        sys.exit(1)
    clr.AddReference(dll_path)
    # Intentar importar LoadSaveHelperFunctions desde el namespace correcto, según la documentación:
    from PalmSens.Core.LoadSave import LoadSaveHelperFunctions
    logging.info("Se importó correctamente LoadSaveHelperFunctions desde PalmSens.Core.LoadSave.")
except Exception as e:
    logging.error("Error al importar LoadSaveHelperFunctions: %s", e)
    logging.error("Verifica que la DLL 'PalmSens.Core.dll' esté en la carpeta %s y que la versión del SDK sea compatible.", sdk_path)
    sys.exit(1)

def cargar_sesion(file_path):
    """
    Carga un archivo .PSSESSION utilizando el método LoadSessionFile del SDK completo de PalmSens.

    Parámetros:
        file_path (str): Ruta completa al archivo .PSSESSION.

    Retorna:
        data (object): Objeto que contiene la sesión completa (por ejemplo, un SessionManager),
                       o None en caso de error.
    """
    try:
        data = LoadSaveHelperFunctions.LoadSessionFile(file_path)
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
