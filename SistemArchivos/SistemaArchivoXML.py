from xml.dom.minidom import Document, parse, parseString

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaArchivo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.ListaDrones = Cola()
        self.ListaPlantas = Lista()
        self.ListaPlanes = Lista()
        self.ColaInvernaderos = Cola()
        self.BanderaErrores = False
        
        
        
        

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
                    try:
                        listadrones = item.getElementsByTagName("listaDrones")
                        for drones in listadrones:
                            print("#------------[Drones]-------------")
                            drone = drones.getElementsByTagName("dron")
                            
                            for d in drone:
                                iddron =  d.getAttribute('id')
                                nombredron = d.getAttribute('nombre')
                                #Almacenar Dron
                                self.ListaDrones.Push(CDron(iddron,nombredron))
                            self.ListaDrones.desplegar()
                            
                            #print(self.ListaDrones.primero.obtenerDato().id)
                            print("#------------[Fin Drones]-------------")
                    except Exception as e:
                        print("!!! ErrorXML no se encontro listaDrones !!!\n",e)
                        self.BanderaErrores = True
                    print("#---------------[Fin Lista Drones XML]-------------")


                    ##########################################################


                    print("#---------------[Lista Invernaderos XML]-------------")
                    try:
                        listainvernaderos = item.getElementsByTagName("listaInvernaderos")
                        for invernaderos in listainvernaderos:
                            print("#---------------[Invernaderos]-------------")
                            
                            try:
                                invernadero = invernaderos.getElementsByTagName("invernadero")
                                for inv in invernadero:
                                    nombreinvernadero = inv.getAttribute('nombre')
                                    print(f"#-------------[Invernadero {nombreinvernadero}]--------------")
                                    numeroHileras = inv.getElementsByTagName('numeroHileras')[0].firstChild.data
                                    plantasXhilera = inv.getElementsByTagName('plantasXhilera')[0].firstChild.data
                                    print("numero de hileras: ",numeroHileras)
                                    print("plantas por hilera: ",plantasXhilera)
                                    print("# -------[ Lista plantas ]-------")
                                    try:
                                        listaplantas = inv.getElementsByTagName('listaPlantas')[0]
                                        plantas = listaplantas.getElementsByTagName('planta')
                                        for planta in reversed(plantas):
                                            hileraplanta = planta.getAttribute('hilera')
                                            posicionplanta = planta.getAttribute('posicion')
                                            litrosAgua = planta.getAttribute('litrosAgua')
                                            gramosFertilizante = planta.getAttribute('gramosFertilizante')
                                            nombreplanta = planta.firstChild.data
                                            #print(f"Hilera: {hileraplanta} - Posicion: {posicionplanta} - Litros Agua: {litrosAgua} - Gramos Fertilizante: {gramosFertilizante} - Nombre Planta: {nombreplanta}")
                                            #Almacenar Planta
                                            self.ListaPlantas.agregar(CPlanta(hileraplanta,posicionplanta,litrosAgua, gramosFertilizante, nombreplanta))
                                        
                                        self.ListaPlantas.desplegar()
                                    except Exception as e:
                                        print("!!! ErrorXML en listaPlantas !!!\n",e)
                                        self.BanderaErrores = True
                                    print("# -------[ Fin Lista plantas ]-------")
                                    
                                    print("# -------------[ asignacionDrones ]-------------")
                                    
                                    try:
                                        ColaDronesInvernadero = Cola()

                                        #Nueva Lista drones para invernadero
                                        for i in range(0,self.ListaDrones.tamano()):
                                            #AgregarDato
                                            if i <=0 :
                                                datocola = self.ListaDrones.primero
                                            else:
                                                datocola = datocola.siguiente
                                            #guardar en cola nueva
                                            iddronnuevo = datocola.valor.id
                                            nombredronnuevo = datocola.valor.nombre
                                            ColaDronesInvernadero.Push(CDron(iddronnuevo,nombredronnuevo))

                                        ColaDronesInvernadero.desplegar()
                                    except Exception as e:
                                        print("!!! ErrorXML en listaDrones o en copia valores drones !!!\n",e)
                                        self.BanderaErrores = True
                                    
                                    try:
                                        asignacionDrones = inv.getElementsByTagName('asignacionDrones')[0]
                                        dronesAsignados = asignacionDrones.getElementsByTagName('dron')
                                        for dron in dronesAsignados:
                                            iddronasignacion = dron.getAttribute('id')
                                            hileraasignacion = dron.getAttribute('hilera')
                                            #print(f"id: {iddronasignacion} - hilera: {hileraasignacion}")
                                            #Buscar Dron
                                            item = ColaDronesInvernadero.buscar_item(iddronasignacion)
                                            item.asignarHilera(hileraasignacion)
                                            item.desplegar()
                                    except Exception as e:
                                        print("!!! ErrorXML en asignacionDrones !!!\n",e)
                                        self.BanderaErrores = True
                                        
                                    print("# -------------[ Fin asignacionDrones ]-------------")
                                    
                                    
                                    print("#-----------[ PlanRiego ]-----------")
                                    try:
                                        planesriego = inv.getElementsByTagName('planesRiego')[0]
                                        planes = planesriego.getElementsByTagName('plan')
                                        for plan in reversed(planes):
                                            nombreplan = plan.getAttribute('nombre')
                                            colaplan = plan.firstChild.data
                                            #print(f"Plan: {nombreplan} - Cola: {colaplan}")
                                            #Elimina espacios en blanco y separa por comas
                                            elementos = colaplan.split(',')
                                            ColaPlanesRiego = Cola()
                                            for elemento in elementos:
                                                item = elemento.strip()
                                                item2 = item.split('-')
                                                item2hilera = item2[0].strip()
                                                item2planta = item2[1].strip()
                                                #print(f'hilera: {item2hilera} - planta: {item2planta}')
                                                #Almacenar Asignacion Plan
                                                ColaPlanesRiego.Push(CAsignacionPlan(item2hilera, item2planta))
                                            #Almacen Plan Riego
                                            planriego = CPlanRiego(nombreplan,ColaPlanesRiego)
                                            #Almacenar en Lista
                                            self.ListaPlanes.agregar(planriego)
                                    
                                        self.ListaPlanes.desplegar()
                                    except Exception as e:
                                        print("!!! ErrorXML en planesRiego!!!\n",e)
                                        self.BanderaErrores = True


                                    print("#-----------[ Fin PlanRiegos ]-----------")

                                    try:
                                        if self.BanderaErrores == False:
                                            #Crear Invernadero
                                            Invernadero = CInvernadero(nombreinvernadero,numeroHileras,plantasXhilera,self.ListaPlantas,self.ListaPlanes, ColaDronesInvernadero)
                                            Invernadero.desplegar()
                                            #Almacenar invernadero
                                            self.ColaInvernaderos.Push(Invernadero)
                                        #Reiniciar Valores para nuevo Invernadero
                                        self.ListaPlantas = Lista()
                                        self.ListaPlanes = Lista()
                                        ColaDronesInvernadero = Cola()
                                        self.BanderaErrores = False
                                    except Exception as e:
                                        print("!!! ERORR AL CREAR INVERNADERO !!!\n Revise si el XML esta correctamente\n",e)
                                    
                                    print(f"#-------------[Fin Invernadero {nombreinvernadero}]--------------")
                            except Exception as e:
                                print("!!! Error en  invernadero !!!\n",e)
                            print("#---------------[Fin Invernaderos]-------------")
                            print()
                            print()
                            print("#"*10+"# [ Lista Invernaderos ] #"+ "#"*10)
                            self.ColaInvernaderos.desplegar()
                            print("#"*10+"# [ Fin Lista Invernaderos ] #"+ "#"*10)
                            print()
                    except Exception as e:
                        print("!!! ErrorXML en listaInvernaderos !!!\n",e)
                    print("#---------------[Fin Lista Invernaderos XML]-------------")


                    #Devolver Lista invernaderos
                    return self.ColaInvernaderos

            else:
                print("El objeto DOM, no se puede segmentar.")
                return None
        except Exception as e:
            print("¡¡¡ [ERROR] No se pudo segmentar el archivo !!!")
            print(f"Detalles del error: {e}")
            return None