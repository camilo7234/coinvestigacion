from PalmSens import MethodScript
import logging
import os

# Configuración básica del logging para registrar información y errores.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obtener_datos_pstrace(port="COM3", script_path="script.mscr"):
    """
    Conecta con el dispositivo (simulado) a través del puerto especificado y utiliza un script
    para obtener datos de PS Trace.

    Nota: Dado que la clase MethodScript es abstracta y no se puede instanciar directamente,
    primero se verifica que el archivo de script exista. Si no existe, retorna None.
    Si existe, se simulan los datos para propósitos de prueba.

    Parámetros:
        port (str): Puerto COM a utilizar (por defecto "COM3").
        script_path (str): Ruta al archivo de script que se enviará al dispositivo (por defecto "script.mscr").
        
    Retorna:
        list o None: Lista de diccionarios con los datos obtenidos o None en caso de error.
    """
    # Verificar si el archivo de script existe.
    if not os.path.exists(script_path):
        logging.error("El archivo de script no se encontró en la ruta: %s", script_path)
        return None

    try:
        try:
            dispositivo = MethodScript()
        except TypeError as te:
            if "cannot instantiate abstract class" in str(te):
                logging.warning("No se puede instanciar MethodScript (clase abstracta). Se simularán los datos.")
                # Como el archivo existe, simulamos la lectura de datos.
                return [{"medicion": 1, "valor": 3.14}, {"medicion": 2, "valor": 2.71}]
            else:
                raise te

        logging.info("Dispositivo (simulado) instanciado en el puerto %s.", port)
        
        # Intentar leer el contenido del script desde el archivo indicado.
        try:
            with open(script_path, "r") as f:
                script = f.read()
            logging.info("Script leído correctamente desde %s.", script_path)
        except Exception as fe:
            logging.error("Error al leer el archivo de script: %s", fe)
            return None
        
        # Simular el envío del script al dispositivo.
        # En un escenario real, se utilizaría: dispositivo.send_script(script)
        logging.info("Script enviado al dispositivo (simulado).")
        
        # Simular la lectura de datos del dispositivo.
        # En un escenario real, se llamaría a: data = dispositivo.read_data()
        data = [{"medicion": 1, "valor": 3.14}, {"medicion": 2, "valor": 2.71}]
        logging.info("Datos simulados recibidos de PS Trace.")
        return data
        
    except Exception as e:
        logging.error("Error obteniendo datos de PS Trace: %s", e)
        return None

if __name__ == "__main__":
    datos = obtener_datos_pstrace()
    logging.info("Datos obtenidos: %s", datos)
