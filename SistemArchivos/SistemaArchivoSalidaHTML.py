import os

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *

class SistemaArchivoHTML:
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos
        self.ruta = None
    
    def creararchivoHTML(self):
        try:
            print("\n"+'#'*10+"[ sistema HTML ]"+"*"*10)
            self.colainvernaderos.desplegar()
            print('\n>> Creando archivo HTML')

            print('\n>> guardando en salidaH.html')
            self.guardarHTML('holamundo')
            print("#"*30)
        except Exception as e:
            print('!!! Error al crear archivo HTML!!!\n',e)
        
    def guardarHTML(self,contenido):
        try:
            print('>> Guardando HTML')
            self.ruta = 'salidaH.html'
            with open(self.ruta, 'wb') as archivo:
                archivo.write(contenido.encode('utf-8'))
            print(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            print("!!! Error al crear el archivo DOC!!!\n",e)
