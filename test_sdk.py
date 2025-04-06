import sys, os
import clr
from System.Reflection import Assembly

# 1) Añadir la carpeta 'src' al path para que Python encuentre pstrace_session.py
project_root = os.path.abspath(os.path.dirname(__file__))
src_path     = os.path.join(project_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)
print("Ruta 'src' añadida:", src_path)

# 2) Añadir la ruta del SDK al path
sdk_path = os.path.join(project_root, 'sdk', 'PSPythonSDK', 'pspython')
if sdk_path not in sys.path:
    sys.path.insert(0, sdk_path)
print("Ruta SDK añadida:", sdk_path)

# 3) Cargar la DLL de PalmSens.Core.Windows
dll_path = os.path.join(sdk_path, "PalmSens.Core.Windows.dll")
print("Cargando DLL desde:", dll_path)
Assembly.LoadFile(dll_path)

# 4) Importar pstrace_session
try:
    from pstrace_session import cargar_sesion
    print("✅ pstrace_session importado correctamente.")
except ImportError as e:
    print("❌ No se pudo importar pstrace_session:", e)
    sys.exit(1)

# 5) Verificar que LoadSaveHelperFunctions está disponible
import PalmSens.Core.Windows as PCW
print("Namespaces en PalmSens.Core.Windows:")
for attr in dir(PCW):
    print(" ", attr)

try:
    from PalmSens.Core.Windows.LoadSaveHelperFunctions import LoadSaveHelperFunctions
    print("✅ LoadSaveHelperFunctions importado correctamente.")
except ImportError as e:
    print("❌ Error al importar LoadSaveHelperFunctions:", e)
