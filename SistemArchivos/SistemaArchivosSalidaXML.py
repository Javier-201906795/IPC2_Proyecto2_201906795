from xml.dom.minidom import Document, parse, parseString

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaArchivoSalida:
    def __init__(self, ruta):
        self.ruta = ruta
        self.colainvernaderos = None
        self.doc = None
        self.root = None
    
    def asignarcolainvernadero(self, colainver):
        self.colainvernaderos = colainver
        #Imprimir valores
        print("\n"+'*-'*10+"[ Invernaderos Salida XML ]"+"*-"*10)
        self.colainvernaderos.desplegar()
        print("\n"+'/'*10+"[ Fin Invernaderos Salida XML ]"+"/"*10)

    def crear_archivo(self, contenido):
        try:
            with open(self.ruta, 'wb') as archivo:
                archivo.write(contenido)
            print(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            print(f'!!! Error al crear_archivo !!!\n',e)
    
    
    def creararchivoDOC(self):
        try:
            print('Creando Doc and root')
            self.doc = Document()
            self.root = self.doc.createElement('datoSalida')
            self.doc.appendChild(self.root)
        except Exception as e:
            print("!!! Error al crear el archivo DOC!!!\n",e)
    
    def segmentar_archivo_XML(self):
        try:
            self.creararchivoDOC()
            doc = self.doc
            root = self.root
            
            listaInvernaderos = doc.createElement('listaInvernaderos')
            root.appendChild(listaInvernaderos)

            #Lista invernaderos
            for i in range(0,1):
                #Datos invernadero
                invernadero = doc.createElement('invernadero')
                invernadero.setAttribute("nombre", f"Invernadero {i}")
                listaInvernaderos.appendChild(invernadero)

                #Lista Planes
                listaplanes = doc.createElement('listaPlanes')
                invernadero.appendChild(listaplanes)

                for h in range(0,1):
                    #Datos Planes
                    plan = doc.createElement('plan')
                    plan.setAttribute('nombre',f'Semana{h}')
                    listaplanes.appendChild(plan)

                    #Tiempo optimo
                    tiempoOptimo = doc.createElement('tiempoOptimoSegundos')
                    plan.appendChild(tiempoOptimo)
                    txt= doc.createTextNode('8')
                    tiempoOptimo.appendChild(txt)

                    #aguaRequeridaLitros
                    aguaRequerida = doc.createElement('aguaRequeridaLitros')
                    plan.appendChild(aguaRequerida)
                    txt= doc.createTextNode('5')
                    aguaRequerida.appendChild(txt)

                    #Fertilizante
                    fertilizanteReq = doc.createElement('fertilizanteRequeridoGramos')
                    plan.appendChild(fertilizanteReq)
                    txt= doc.createTextNode('500')
                    fertilizanteReq.appendChild(txt)

                    #Lista Eficiencia Drones
                    efiDrones = doc.createElement('eficienciaDronesRegadores')
                    plan.appendChild(efiDrones)

                    #Dron
                    for j in range(0,3):
                        Dron = doc.createElement('dron')
                        efiDrones.appendChild(Dron)
                        Dron.setAttribute('nombre',f'DR{j}')
                        Dron.setAttribute('litrosAgua',f'{j+3}')
                        Dron.setAttribute('gramosFertilizante',f'{j*100}')

                    #Lista instrucciones
                    instrucciones = doc.createElement('instrucciones')
                    plan.appendChild(instrucciones)

                    #Tiempo
                    for k in range(0,1):
                        tiempo = doc.createElement('tiempo')
                        tiempo.setAttribute('segundos',f'{k}')
                        instrucciones.appendChild(tiempo)

                        #Movimiento
                        for l in range(0,3):
                            movimiento = doc.createElement('dron')
                            tiempo.appendChild(movimiento)
                            movimiento.setAttribute('nombre',f'DR{l}')
                            movimiento.setAttribute('accion',f'Adelante(H{i}P{l})')

            

            

            # ==============================
            # Guardar en archivo XML
            # ==============================
            xml_str = doc.toprettyxml(indent=" ", encoding="UTF-8")
            self.crear_archivo(xml_str)

        except Exception as e:
            print(f'!!! Error al segmentar_archivo_XML !!!\n',e)