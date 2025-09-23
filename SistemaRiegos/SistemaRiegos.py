from SistemArchivos.SistemaArchivoXML import SistemaArchivo
from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaRiegos():
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos
        self.InvernaderoSel = None
        self.PlanSel = None

        self.Invnombre = None
        self.InvnumeroHilera = None
        self.InvplantasXHilera = None
        self.InvListaPlantas = None
        self.InvListaDrones = None

    def desplegar(self):
        self.colainvernaderos.desplegar()

    def ColasInvernaderos(self):
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





    def ColasPlanes(self, opcion):
        try:

            print(f'>> Opcion seleccionada: {opcion}')
            #Buscar nombre invernadero
            #Recorre invernaderso
            invernadero = None
            for i in range(0,int(opcion)):
                if i <= 0:
                    invernadero = self.colainvernaderos.primero
                else:
                    invernadero = invernadero.siguiente
            #Datos invernadero
            nombre = invernadero.valor.nombre
            ListaPlanes = invernadero.valor.ListaPlanes
            
            #Cola nombres
            colanombresplanes = Cola()
            #Obtener Instrucciones
            nombreplan = None
            for i in range(0,ListaPlanes.tamano()):
                if i <=0:
                    plan = ListaPlanes.primero
                else:
                    plan = plan.siguiente
                #Datos plan
                nombreplan = plan.valor.nombre
                colanombresplanes.Push(Cnombreplan(nombreplan,i+1))
            
            return colanombresplanes

        except Exception as e:
            print("!!! Error al Listar Planes !!!")






    def Obtenerinformacion(self, numinv, numplan):
        try:
            print(f'\n>> Invernadero seleccionado: {numinv}  -  Plan seleccionado: {numplan}')
            #Reinicar valores
            self.InvernaderoSel = None
            self.PlanSel = None
            self.Invnombre = None
            self.InvnumeroHilera = None
            self.InvplantasXHilera = None
            self.InvListaPlantas = None
            self.InvListaDrones = None

            #Obtener invernadero
            invernaderodata = None
            for i in range(0,int(numinv)):
                if i <=0:
                    invernadero = self.colainvernaderos.primero
                else:
                    invernadero = invernadero.siguiente
                invernaderodata = invernadero.valor
            invernaderodata.desplegar()

            print()

            #Obtener plan
            ListaPlanes = invernaderodata.ListaPlanes
            Plan = None
            for i in range(0,int(numplan)):
                if i <=0:
                    plan = ListaPlanes.primero
                else:
                    plan = plan.siguiente
                #Datos plan
                Plan = plan.valor
            Plan.desplegar()

            #Almacenar informacion
            self.InvernaderoSel = invernaderodata
            self.PlanSel = Plan

            print()

            #Obtener Datos invernadero
            self.Invnombre = invernaderodata.nombre
            self.InvnumeroHilera = invernaderodata.numeroHilera
            self.InvplantasXHilera = invernaderodata.plantasXHilera
            self.InvListaPlantas = invernaderodata.ListaPlantas
            self.InvListaDrones = invernaderodata.ListaDrones
            

            print("\n\n")



        except Exception as e:
            print("!!! Error al Obtener informacion de invernadero y planes !!!\n",e)







    def Ejecutar_tiempo(self,tiempo):
        print("\n\n\n########################## [Sistema Riegos] ############################")
        print(">> Tiempo: ", tiempo)
        try:
            #Obtener instrucciones
            self.PlanSel.desplegar()
            print()
            #Obtener drones
            self.InvListaDrones.desplegar()
            print()

            
        except Exception as e:
            print("!!! Error al ejecutar_tiempo !!!\n",e)
        print("########################## [FIN Sistema Riegos] ############################\n\n\n")
            
            
        