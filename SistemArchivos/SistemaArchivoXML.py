from xml.dom.minidom import Document, parse


class SistemaArchivo:
    def __init__(self, ruta):
        self.ruta = ruta

    def leer_archivo(self):
        with open(self.ruta, 'r') as archivo:
            contenido = archivo.read()
            print("> -----[ Lectura texto XML]-----")
            print(contenido)
            print("> -----[ Fin lectura texto XML]-----")
        return contenido