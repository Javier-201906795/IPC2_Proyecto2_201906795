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

        self.Tiempoactual = 0
        self.Tiempomax = 0

        self.DronRegando = False

        self.ColaHilerasIndividualIndividual = Cola()

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

            self.Tiempoactual = 0
            self.Tiempomax = 0

            self.DronRegando = False

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


            #Colas por Hilera
            Colainstrucciones = self.PlanSel.colaplan
            #Cola hileras separadas
            self.ColaHilerasIndividual = Cola()
            for i in range(0,int(self.InvnumeroHilera)):
                nuevaCola = Cola()
                #Buscar elementos para hilera
                Buscar = f'H{i+1}'
                for j in range(0,Colainstrucciones.tamano()):
                    if j <= 0:
                        instruccion = Colainstrucciones.primero
                    else:
                        instruccion = instruccion.siguiente
                    hil = instruccion.valor.hilera
                    pla = instruccion.valor.planta
                    #print(f'hilera: {hil}, planta{pla}')
                    #Compara valores si igual a la hilera buscada
                    if hil == Buscar:
                        #Guardar en nuevaCola
                        nuevaCola.Push(CAsignacionPlan(hil,pla))
                #Almacenar hilera
                self.ColaHilerasIndividual.Push(nuevaCola)
            
            print("\n -------[nuevas colas de hileras ]-------")
            print(f'> Numero colas hileras: {self.ColaHilerasIndividual.tamano()}')
            self.ColaHilerasIndividual.desplegar()
                        
            

            print("\n\n")



        except Exception as e:
            print("!!! Error al Obtener informacion de invernadero y planes !!!\n",e)




    def Ejecutar_instruccion(self, instruccion):
        try:
            hilera = instruccion.hilera
            planta = instruccion.planta
            
            print("\n"+"-"*50)
            print(f">> Instruccion: {hilera} - {planta}")

            #Aumentar tiempo
            self.Tiempoactual +=1
            print(f'>>> Tiempo Actual: {self.Tiempoactual} - Tiempo Maximo: {self.Tiempomax}')
            print()
            
            #Restricciones
            #Un dron riega a la vez
            #Sigue el orden de riego
            print(f'Dron Regando: {self.DronRegando}')

            #Mover Drones
            if self.Tiempoactual == 1:
                #Mover Todos los Drones
                for i in range(0,self.InvListaDrones.tamano()):
                    if i <= 0:
                        dron = self.InvListaDrones.primero
                    else:
                        dron = dron.siguiente
                    
                    plantaactual = dron.valor.planta
                    #Mover Dron
                    dron.valor.asignarPlanta(int(plantaactual)+1)
                #Imprimir nuevo valores
                self.InvListaDrones.desplegar()
            else:
                if self.DronRegando == False:
                    #No hay drones regando avanazar
                    print("No hay drones regando, -> avanazar")
                    #Mover Todos los Drones
                    for i in range(0,self.InvListaDrones.tamano()):
                        if i <= 0:
                            dron = self.InvListaDrones.primero
                        else:
                            dron = dron.siguiente
                        plantaactual = dron.valor.planta
                        #Mover Dron si llego al final
                        if int(plantaactual) < int(self.InvplantasXHilera):
                            dron.valor.asignarPlanta(int(plantaactual)+1)
                    #Imprimir nuevo valores
                    self.InvListaDrones.desplegar()
            
            print("-"*50)
            print()
            return True

        except Exception as e:
            print(f"!!! Error al Ejecutar_instruccion: {instruccion} !!!\n",e)




    def Ejecutar_tiempo(self,tiempo):
        print("\n\n\n########################## [Sistema Riegos] ############################")
        print(">> Tiempo Max: ", tiempo)
        self.Tiempomax = tiempo
        try:
            #Obtener instrucciones
            self.PlanSel.desplegar()
            print()
            #Obtener drones
            self.InvListaDrones.desplegar()
            print()

            #Ejecutar instrucciones
            Nombreinstrucciones = self.PlanSel.nombre
            Colainstrucciones = self.PlanSel.colaplan
            max = Colainstrucciones.tamano()
            for i in range(0,max):
                instruccion = Colainstrucciones.Pop()
                #Ejecutar hasta completar
                completado = False
                while completado == False and (self.Tiempoactual) <= int(self.Tiempomax):
                    completado = self.Ejecutar_instruccion(instruccion)
                    print(f'tiempoa: {self.Tiempoactual} - tiempmax: {self.Tiempomax} - completado: {completado}')
            
            
                
            
        except Exception as e:
            print("!!! Error al ejecutar_tiempo !!!\n",e)
        print("########################## [FIN Sistema Riegos] ############################\n\n\n")
            
            
        