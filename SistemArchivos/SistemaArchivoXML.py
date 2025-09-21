from xml.dom.minidom import Document, parse


class SistemaArchivo:
    def __init__(self, ruta):
        self.ruta = ruta

    def leer_archivo(self):
        try:
            with open(self.ruta, 'r') as archivo:
                contenido = archivo.read()
                print("# -----[ Lectura texto XML]-----")
                print(contenido)
                print("# -----[ Fin lectura texto XML]-----")
            return contenido
        except:
            print("¡¡¡ [ERROR] No se pudo leer el archivo !!!")

    def analizar_xml(self):
        try:
            #[1]Leer archivo texto
            texto_archivo = self.leer_archivo()
            return texto_archivo
            #[/1]
        except:
            print("¡¡¡ [ERROR] No se pudo analizar el archivo XML !!!")
            return None