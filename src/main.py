import sys
import os

# Construir la ruta absoluta a la carpeta 'pspython' del SDK
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk', 'PSPythonSDK', 'pspython'))
print("Ruta del SDK:", sdk_path)

# Agregar la ruta al sys.path si aún no está incluida
if sdk_path not in sys.path:
    sys.path.append(sdk_path)

# Intentar importar el módulo 'pspymethods'
try:
    import pspymethods
    print("El módulo 'pspymethods' se importó correctamente.")
except ImportError as e:
    print("No se pudo importar el SDK de PalmSens. Verifica que la ruta sea correcta. Error:", e)
