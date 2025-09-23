from SistemArchivos.SistemaArchivoXML import SistemaArchivo
from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaRiegos():
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos

    def desplegar(self):
        self.colainvernaderos.desplegar()

    def ListarInvernaderos(self):
        try:
            Colanombreinv = Cola()
            #Recorre invernaderos
            for i in range(0,self.colainvernaderos.tamano()):
                if i <=0:
                    invernadero = self.colainvernaderos.primero
                else:
                    invernadero = invernadero.siguiente
                nombreinv = invernadero.valor.nombre
                #Adjuntar en texto
                Colanombreinv.Push(Cnombreinvernadero(nombreinv, i + 1))
            
            return Colanombreinv
        except Exception as e:
            print("!!! Error al listar invernaderos !!!\n",e)

    


    def Ejecutar_tiempo(self,tiempo):
        print("\n\n\n########################## [Sistema Riegos] ############################")
        print(">> Tiempo: ", tiempo)
        #Recorre invernaderos
        for i in range(0,self.colainvernaderos.tamano()):
            print(">>> ciclo: ",i)
            #Obtener invernadero
            invernadero = self.colainvernaderos.Pop()
            #obtener datos
            nombre = invernadero.nombre
            numeroHilera = invernadero.numeroHilera
            plantasXHilera = invernadero.plantasXHilera
            ListaPlantas = invernadero.ListaPlantas
            ListaPlanes = invernadero.ListaPlanes
            ListaDrones = invernadero.ListaDrones
            print("\n\n ------------- [Planes] --------------")
            #Obtener Instrucciones
            for i in range(0,ListaPlanes.tamano()):
                if i <=0:
                    plan = ListaPlanes.primero
                else:
                    plan = plan.siguiente
                #Datos plan
                nombreplan = plan.valor.nombre
                colaplan = plan.valor.colaplan
                print(f'\nNombre plan: {nombreplan}')
                colaplan.desplegar()
            print("\n\n ------------- [Fin Planes] --------------")

        print("########################## [FIN Sistema Riegos] ############################\n\n\n")
            
            
        