import sys
sys.path.append('sdk/PSPythonSDK/')
from pspython import pspymethods

# Confirmamos la importación exitosa del módulo
print("El SDK de PalmSens se importó correctamente.")

# Listamos los atributos y funciones disponibles en pspymethods para verificar su contenido.
print("Atributos disponibles en pspymethods:")
for attr in dir(pspymethods):
    print(attr)
