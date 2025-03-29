import sys
import os

# Agregar la ruta del directorio actual para la importación
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import funcion_importante  # Importamos la función

def test_funcion_importante():
    assert funcion_importante() == "Función ejecutada correctamente"
