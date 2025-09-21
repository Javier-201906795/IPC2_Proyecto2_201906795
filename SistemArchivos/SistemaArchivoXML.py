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
    
    def segmentar_archivo(self):
        try:
            Dom = self.convertir_xml_a_Dom()
            if Dom is not None:

                configuracion = Dom.getElementsByTagName("configuracion")
                for item in configuracion:
                    print("#---------------[Configuracion XML]-------------")
                    print(item.toxml())
                    print("#---------------[Fin Configuracion XML]-------------")
                    ##########################################################
                    print("#---------------[Lista Drones XML]-------------")
                    listadrones = item.getElementsByTagName("listaDrones")
                    for drones in listadrones:
                        print("#------------[Drones]-------------")
                        drone = drones.getElementsByTagName("dron")
                        for d in drone:
                            iddron =  d.getAttribute('id')
                            nombredron = d.getAttribute('nombre')
                            print(f"id: {iddron} - nombre: {nombredron}")
                        print("#------------[Fin Drones]-------------")
                    print("#---------------[Fin Lista Drones XML]-------------")

            else:
                print("El objeto DOM, no se puede segmentar.")
                return None
        except Exception as e:
            print("¡¡¡ [ERROR] No se pudo segmentar el archivo !!!")
            print(f"Detalles del error: {e}")
            return None