from xml.dom.minidom import Document, parse, parseString

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaArchivoSalida:
    def __init__(self, ruta):
        self.ruta = ruta

    def crear_archivo(self):
        try:
            with open(self.ruta, 'w') as archivo:
                pass
            print("Archivo creado o sobrescrito correctamente.")
        except Exception as e:
            print(f'!!! Error al crear_archivo !!!\n',e)