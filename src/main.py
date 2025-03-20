import sys
import os
import logging

# Configuración básica del logging para registrar información y errores.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Construir la ruta absoluta a la carpeta 'pspython' del SDK (no se modifica la ruta, según lo indicado).
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sdk', 'PSPythonSDK', 'pspython'))
logging.info("Ruta del SDK: %s", sdk_path)

# Agregar la ruta al sys.path si aún no está incluida.
if sdk_path not in sys.path:
    sys.path.append(sdk_path)
    logging.info("Se agregó la ruta del SDK al sys.path.")

# Intentar importar el módulo 'pspymethods'.
try:
    import pspymethods
    logging.info("El módulo 'pspymethods' se importó correctamente.")
except ImportError as e:
    logging.error("No se pudo importar el SDK de PalmSens. Verifica que la ruta sea correcta. Error: %s", e)
    # Si la importación falla, se termina la ejecución para evitar errores posteriores.
    sys.exit(1)
