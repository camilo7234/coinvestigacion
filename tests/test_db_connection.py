import sys
import os
import pytest

# Agregamos la ruta del módulo 'src'
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from db_connection import conectar_bd

def test_conexion_bd_exitoso():
    """
    Verifica que conectar_bd() retorne un objeto de conexión (no None).
    """
    conn = conectar_bd()
    assert conn is not None, "La conexión a la base de datos falló."
    if conn:
        conn.close()
