from pspymethods import MethodSCRIPTDevice
import logging

# Configuración básica del logging para registrar información y errores.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obtener_datos_pstrace(port="COM3", script_path="script.mscr"):
    """
    Conecta con el dispositivo a través del puerto especificado y utiliza un script para obtener datos de PSTrace.
    
    Parámetros:
        port (str): Puerto COM a utilizar (por defecto "COM3").
        script_path (str): Ruta al archivo de script que se enviará al dispositivo (por defecto "script.mscr").
        
    Retorna:
        list o None: Lista de diccionarios con los datos obtenidos o None en caso de error.
        
    Manejo de errores:
        - Captura errores en la conexión, en la lectura del script o durante la comunicación con el dispositivo,
          registrando el error y retornando None.
    """
    try:
        # Instanciar el dispositivo utilizando el puerto especificado.
        # Este paso abre la conexión serial al dispositivo que se encuentra en el puerto indicado.
        device = MethodSCRIPTDevice(port=port)
        logging.info("Dispositivo instanciado en el puerto %s.", port)
        
        # Leer el contenido del script desde el archivo indicado.
        try:
            with open(script_path, "r") as f:
                script = f.read()
            logging.info("Script leído correctamente desde %s.", script_path)
        except FileNotFoundError:
            logging.error("El archivo de script no se encontró en la ruta: %s", script_path)
            return None
        except Exception as fe:
            logging.error("Error al leer el archivo de script: %s", fe)
            return None
        
        # Enviar el script al dispositivo para que se ejecute y se inicie la adquisición de datos.
        device.send_script(script)
        logging.info("Script enviado al dispositivo.")
        
        # Leer los datos que el dispositivo retorna tras ejecutar el script.
        # Se espera que 'data' sea una lista de diccionarios con la información procesada.
        data = device.read_data()
        logging.info("Datos recibidos de PS Trace.")
        return data
        
    except Exception as e:
        logging.error("Error obteniendo datos de PS Trace: %s", e)
        return None

if __name__ == "__main__":
    # Ejecutar la función de obtención de datos para pruebas.
    datos = obtener_datos_pstrace()
    logging.info("Datos obtenidos: %s", datos)
