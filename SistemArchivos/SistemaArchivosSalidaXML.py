from xml.dom.minidom import Document, parse, parseString

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaArchivoSalida:
    def __init__(self, ruta):
        self.ruta = ruta

    def crear_archivo(self, contenido):
        try:
            with open(self.ruta, 'wb') as archivo:
                archivo.write(contenido)
            print(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            print(f'!!! Error al crear_archivo !!!\n',e)
    
    def segmentar_archivo_XML(self):
        try:
            doc = Document()
            root = doc.createElement('datoSalida')
            doc.appendChild(root)

            campo = doc.createElement("campo")
            campo.setAttribute("id", "1")
            campo.setAttribute("nombre", "2")
            root.appendChild(campo)

            # ==============================
            # Guardar en archivo XML
            # ==============================
            xml_str = doc.toprettyxml(indent=" ", encoding="UTF-8")
            self.crear_archivo(xml_str)

        except Exception as e:
            print(f'!!! Error al segmentar_archivo_XML !!!\n',e)