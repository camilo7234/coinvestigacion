import sys
import os
import pytest

# Agregamos la ruta del módulo 'src' para poder importar pstrace_connection.py
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

# Importamos la función correcta
from pstrace_connection import obtener_datos_pstrace

def test_cargar_sesion_existente():
    """
    Prueba que al cargar un archivo .PSSESSION válido se retornen datos.
    Asegúrate de que 'ultima_medicion.pssession' exista en la carpeta 'data'.
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "ultima_medicion.pssession"))
    datos = obtener_datos_pstrace(script_path=file_path)
    assert datos is not None, "No se cargaron datos desde el archivo de sesión válido."

def test_cargar_sesion_inexistente():
    """
    Prueba que al intentar cargar un archivo .PSSESSION inexistente la función retorne None.
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "archivo_inexistente.pssession"))
    datos = obtener_datos_pstrace(script_path=file_path)
    assert datos is None, "La función debería retornar None para un archivo inexistente."
