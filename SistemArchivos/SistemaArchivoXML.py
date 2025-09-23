from xml.dom.minidom import Document, parse, parseString

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaArchivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ListaDrones = Lista()
        
        

    def leer_archivo(self):
        try:
            with open(self.ruta, 'r') as archivo:
                contenido = archivo.read()
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
                        
                        for d in reversed(drone):
                            iddron =  d.getAttribute('id')
                            nombredron = d.getAttribute('nombre')
                            #Almacenar Dron
                            self.ListaDrones.agregar(CDron(iddron,nombredron))
                        self.ListaDrones.desplegar()
                        
                        #print(self.ListaDrones.primero.obtenerDato().id)
                        print("#------------[Fin Drones]-------------")
                    print("#---------------[Fin Lista Drones XML]-------------")
                    ##########################################################
                    print("#---------------[Lista Invernaderos XML]-------------")
                    listainvernaderos = item.getElementsByTagName("listaInvernaderos")
                    for invernaderos in listainvernaderos:
                        print("#---------------[Invernaderos]-------------")
                        
                        invernadero = invernaderos.getElementsByTagName("invernadero")
                        for inv in invernadero:
                            nombreinvernadero = inv.getAttribute('nombre')
                            print(f"#-------------[Invernadero {nombreinvernadero}]--------------")
                            numeroHileras = inv.getElementsByTagName('numeroHileras')[0].firstChild.data
                            plantasXhilera = inv.getElementsByTagName('plantasXhilera')[0].firstChild.data
                            print("numero de hileras: ",numeroHileras)
                            print("plantas por hilera: ",plantasXhilera)
                            print("# -------[ Lista plantas ]-------")
                            listaplantas = inv.getElementsByTagName('listaPlantas')[0]
                            plantas = listaplantas.getElementsByTagName('planta')
                            for planta in plantas:
                                hileraplanta = planta.getAttribute('hilera')
                                posicionplanta = planta.getAttribute('posicion')
                                litrosAgua = planta.getAttribute('litrosAgua')
                                gramosFertilizante = planta.getAttribute('gramosFertilizante')
                                nombreplanta = planta.firstChild.data
                                print(f"Hilera: {hileraplanta} - Posicion: {posicionplanta} - Litros Agua: {litrosAgua} - Gramos Fertilizante: {gramosFertilizante} - Nombre Planta: {nombreplanta}")
                                #print(planta.toxml())
                            print("# -------[ Fin Lista plantas ]-------")
                            print("# -------------[ asignacionDrones ]-------------")
                            asignacionDrones = inv.getElementsByTagName('asignacionDrones')[0]
                            dronesAsignados = asignacionDrones.getElementsByTagName('dron')
                            for dron in dronesAsignados:
                                iddronasignacion = dron.getAttribute('id')
                                hileraasignacion = dron.getAttribute('hilera')
                                print(f"id: {iddronasignacion} - hilera: {hileraasignacion}")
                            print("# -------------[ Fin asignacionDrones ]-------------")
                            print("#-----------[ PlanRiego ]-----------")
                            planesriego = inv.getElementsByTagName('planesRiego')[0]
                            planes = planesriego.getElementsByTagName('plan')
                            for plan in planes:
                                nombreplan = plan.getAttribute('nombre')
                                colaplan = plan.firstChild.data
                                print(f"Plan: {nombreplan} - Cola: {colaplan}")
                                #Elimina espacios en blanco y separa por comas
                                elementos = colaplan.split(',')
                                for elemento in elementos:
                                    item = elemento.strip()
                                    print(item)
                                
                            print("#-----------[ Fin PlanRiegos ]-----------")
                            print(f"#-------------[Fin Invernadero {nombreinvernadero}]--------------")
                        print("#---------------[Fin Invernaderos]-------------")
                    print("#---------------[Fin Lista Invernaderos XML]-------------")
            else:
                print("El objeto DOM, no se puede segmentar.")
                return None
        except Exception as e:
            print("¡¡¡ [ERROR] No se pudo segmentar el archivo !!!")
            print(f"Detalles del error: {e}")
            return None