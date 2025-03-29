import sys
import os

# Agregar la ruta del SDK a sys.path
sdk_path = os.path.join(os.getcwd(), "sdk", "PSPythonSDK", "pspython")
if sdk_path not in sys.path:
    sys.path.append(sdk_path)

# Intentar importar la librería
try:
    import pspymethods
    print("PSPythonSDK importado correctamente")
except ImportError as e:
    print("Error al importar PSPythonSDK:", e)

# Función de prueba
def funcion_importante():
    return "Función ejecutada correctamente"
