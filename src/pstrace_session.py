"""
pstrace_session.py

Este módulo carga un archivo .PSSESSION utilizando el SDK completo de PalmSens,
usando reflexión para evitar problemas de namespace.
"""

import os
import sys
import logging

# 1. Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 2. Cargar pythonnet y clr
try:
    import pythonnet
    pythonnet.load("coreclr")
    import clr
    logging.info("pythonnet y clr cargados correctamente.")
except Exception as e:
    logging.error("Error al cargar pythonnet/clr: %s", e)
    sys.exit(1)

# 3. Agregar ruta del SDK a sys.path
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk', 'PSPythonSDK', 'pspython'))
if not os.path.isdir(sdk_path):
    logging.error("La ruta del SDK no existe: %s", sdk_path)
    sys.exit(1)
sys.path.append(sdk_path)
logging.info("Ruta del SDK añadida: %s", sdk_path)

# 4. Verificar módulo pspymethods
try:
    import pspymethods
    logging.info("pspymethods importado correctamente.")
except ImportError as e:
    logging.error("Error al importar pspymethods: %s", e)
    sys.exit(1)

# 5. Cargar la DLL con reflexión
from System.Reflection import Assembly
dll_path = os.path.join(sdk_path, "PalmSens.Core.Windows.dll")
if not os.path.exists(dll_path):
    logging.error("DLL no encontrada: %s", dll_path)
    sys.exit(1)
try:
    assembly = Assembly.LoadFile(dll_path)
    logging.info("DLL cargada con Assembly.LoadFile.")
except Exception as e:
    logging.error("Error al cargar la DLL: %s", e)
    sys.exit(1)

# 6. Localizar el tipo LoadSaveHelperFunctions
tipo = assembly.GetType("PalmSens.Windows.LoadSaveHelperFunctions")
if tipo is None:
    logging.error("Tipo no encontrado: PalmSens.Windows.LoadSaveHelperFunctions")
    sys.exit(1)
logging.info("Tipo encontrado: %s", tipo.FullName)

# 7. Obtener el método LoadSessionFile
# Primero probamos la sobrecarga que recibe sólo el filepath
metodo = tipo.GetMethod("LoadSessionFile", [clr.GetClrType(str)])
if metodo is None:
    # Si no existe, probamos la sobrecarga con booleano
    metodo = tipo.GetMethod("LoadSessionFile", [clr.GetClrType(str), clr.GetClrType(bool)])
if metodo is None:
    logging.error("Método LoadSessionFile no encontrado en %s", tipo.FullName)
    sys.exit(1)
logging.info("Método LoadSessionFile localizado.")

# 8. Función para cargar la sesión
def cargar_sesion(file_path):
    try:
        # Ajusta según la sobrecarga
        params = [file_path] if metodo.GetParameters().Length == 1 else [file_path, False]
        sesion = metodo.Invoke(None, params)
        logging.info("Sesión cargada exitosamente.")
        return sesion
    except Exception as e:
        logging.error("Error invocando LoadSessionFile: %s", e)
        return None

# 9. Bloque principal
if __name__ == "__main__":
    archivo = os.path.join(os.path.dirname(__file__), "..", "data", "ultima_medicion.pssession")
    logging.info("Cargando sesión desde: %s", archivo)
    datos = cargar_sesion(archivo)
    if datos is not None:
        logging.info("Datos de la sesión: %s", datos)
    else:
        logging.error("No se pudieron cargar los datos de la sesión.")
