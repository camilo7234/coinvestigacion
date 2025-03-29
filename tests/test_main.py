import sys
import os

# Aseguramos que la carpeta raíz se incluya en sys.path para poder importar main.py.
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "proyecto", "src"))

from main import funcion_importante  # Ajusta el nombre si es diferente

def test_funcion_importante():
    # Esperamos que la función retorne el string "Función ejecutada correctamente"
    resultado = funcion_importante()
    assert resultado == "Función ejecutada correctamente", "El resultado no es el esperado"
