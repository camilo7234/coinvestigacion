import sys
import os
import clr

# Agregar la ruta del SDK si no está ya en sys.path
sdk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk', 'PSPythonSDK', 'pspython'))
if sdk_path not in sys.path:
    sys.path.append(sdk_path)
print("Ruta del SDK agregada:", sdk_path)

# Cargar la DLL usando AddReference
dll_path = os.path.join(sdk_path, "PalmSens.Core.dll")
print("Cargando DLL desde:", dll_path)
# Usar AddReference para cargar por nombre (pythonnet no ofrece AddReferenceToFileAndPath en CPython)
clr.AddReference("PalmSens.Core")

# Intentar importar el subnamespace LoadSaveHelperFunctions
try:
    from PalmSens.Core.LoadSaveHelperFunctions import LoadSaveHelperFunctions
    print("LoadSaveHelperFunctions importado exitosamente.")
except ImportError as e:
    print("Error al importar LoadSaveHelperFunctions:", e)

# Listar atributos del módulo PalmSens.Core
import PalmSens.Core as PC
print("Atributos disponibles en PalmSens.Core:")
for attr in dir(PC):
    print(attr)
