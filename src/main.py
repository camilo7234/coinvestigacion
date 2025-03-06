import sys
import os

# Agrega la ruta del SDK al PYTHONPATH
sdk_path = os.path.join(os.path.dirname(__file__), '..', 'sdk')
sys.path.append(sdk_path)

# IMPORTANTE: Ajusta el nombre del módulo y las funciones según la documentación del SDK.
try:
    import ps_sdk  # Supongamos que el SDK se importa con este nombre
except ImportError as e:
    print("No se pudo importar el SDK de PalmSens. Verifica que la ruta sea correcta.", e)
    sys.exit(1)

def test_connection():
    # Inicializa la conexión con el dispositivo PalmSens a través del SDK.
    # Reemplaza 'DispositivoPalmSens' y 'conectar()' con los nombres reales.
    try:
        dispositivo = ps_sdk.DispositivoPalmSens()
        if dispositivo.conectar():
            print("Conexión exitosa con PSTrace 5.9")
        else:
            print("Error al conectar con PSTrace 5.9")
    except Exception as ex:
        print("Excepción durante la conexión:", ex)

if __name__ == "__main__":
    test_connection()