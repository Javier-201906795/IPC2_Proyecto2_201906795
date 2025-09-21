from xml.dom.minidom import Document, parse, parseString


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

    def convertir_xml_a_Dom(self):
        try:
            #[1]Leer archivo texto
            texto_archivo = self.leer_archivo()
            # Convertir el texto en un objeto DOM
            dom = parseString(texto_archivo)
            return dom
            #[/1]
        except Exception as e:
            print("¡¡¡ [ERROR] No se pudo convertir a archivo DOM - XML !!!")
            print(f"Detalles del error: {e}")
            return None