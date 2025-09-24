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

        self.ColaHilerasIndividual = Cola()

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
            #self.ColaHilerasIndividual = Cola()
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
            banderainstruccioncompletada = False
            
            
            print("\n"+"-"*50)
            print(f">> Instruccion: {hilera} - {planta}")

            #Aumentar tiempo
            self.Tiempoactual +=1
            print(f'>>> Tiempo Actual: {self.Tiempoactual} - Tiempo Maximo: {self.Tiempomax}')
            print()
            
            #Restricciones
            #Un dron riega a la vez
            #Sigue el orden de riego

            #Validar si hay riego o no
            #Buscar Dron/Hilera comparo posicion Planta = posicion planta dron
            for i in range(0,self.InvListaDrones.tamano()):
                if i <= 0:
                    dron = self.InvListaDrones.primero
                else:
                    dron = dron.siguiente
                nombredron = dron.valor.nombre
                hildron = f'H{dron.valor.hilera}'
                plandron = f'P{dron.valor.planta}'
                #Encontrar Dron
                if hildron == hilera:
                    #Validar posicion
                    if plandron == planta:
                        print(f'>>>> Dron Regando, {nombredron}')
                        self.DronRegando = True
                        banderainstruccioncompletada = True
                        #Eliminar instruccion de cola individual
                        #Buscar en hileras
                        for h in range(1,int(hildron[1])+1):
                            if h <= 1:
                                bhilera = self.ColaHilerasIndividual.primero
                            else:
                                bhilera = bhilera.siguiente
                            colahilera = bhilera.valor
                        #Eliminar valor
                        colahilera.Pop()
                        
                        
                    else:
                        self.DronRegando = False


            print(f'Dron Regando: {self.DronRegando}')

            #Mover Drones
            if self.Tiempoactual == 1:
                #Mover Todos los Drones
                for j in range(0,self.InvListaDrones.tamano()):
                    if j <= 0:
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
                    #Mover Drones
                    for f in range(0,self.InvListaDrones.tamano()):
                        #DRON{f}
                        if f <= 0:
                            dron = self.InvListaDrones.primero
                        else:
                            dron = dron.siguiente
                        nombredron2 = dron.valor.nombre
                        plantaactual = dron.valor.planta
                        hileradron = dron.valor.hilera
                        #Mover Dron si NO llego al final
                        if int(plantaactual) < int(self.InvplantasXHilera):
                            #Mover si No esta en su posicion de riego
                            #Buscar en hilera
                            for g in range(0,int(hileradron)):
                                if g <= 0:
                                    hilera = self.ColaHilerasIndividual.primero
                                else:
                                    hilera = hilera.siguiente
                                colahilera = hilera.valor
                            #colahilera.desplegar()
                            #obtener primera posicion
                            if colahilera.primero != None:
                                posiciontope = colahilera.primero.valor.planta
                                posiciontope = int(posiciontope[1])
                                #Validar si mover o no
                                if plantaactual < posiciontope:
                                    #Mover dron
                                    dron.valor.asignarPlanta(int(plantaactual)+1)
                                else:
                                    print(f"Dron {nombredron2} llego a posicion -> esperar")
                    #Imprimir nuevo valores
                    self.InvListaDrones.desplegar()
                elif self.DronRegando == True:
                    print(f"Dron  regando. - {instruccion.hilera} - {instruccion.planta}")
                    #Mover Drones
                    for f in range(0,self.InvListaDrones.tamano()):
                        #DRON{f}
                        if f <= 0:
                            dron = self.InvListaDrones.primero
                        else:
                            dron = dron.siguiente
                        nombredron2 = dron.valor.nombre
                        plantaactual = dron.valor.planta
                        hileradron = dron.valor.hilera
                        #No mover Dron Regando
                        hileranotocar = instruccion.hilera[1]
                        if int(hileradron) == int(hileranotocar):
                            print('Dron Regando.')
                        else:
                            #Mover Dron si NO llego al final
                            if int(plantaactual) < int(self.InvplantasXHilera):
                                #Mover si No esta en su posicion de riego
                                #Buscar en hilera
                                for p in range(0,int(hileradron)):
                                    if p <= 0:
                                        hilera = self.ColaHilerasIndividual.primero
                                    else:
                                        hilera = hilera.siguiente
                                    colahilera = hilera.valor
                                #colahilera.desplegar()
                                if colahilera.primero != None:
                                    #obtener primera posicion
                                    posiciontope = colahilera.primero.valor.planta
                                    posiciontope = int(posiciontope[1])
                                    #Validar si mover o no
                                    if plantaactual < posiciontope:
                                        #Mover dron
                                        dron.valor.asignarPlanta(int(plantaactual)+1)
                                    else:
                                        print(f"Dron {nombredron2} llego a posicion -> esperar")
                    #Imprimir nuevo valores
                    self.InvListaDrones.desplegar()
                    
            
            print("-"*50)
            print()
            return banderainstruccioncompletada

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
            Colainstrucciones = self.PlanSel.colaplan
            max = Colainstrucciones.tamano()
            ultimoriegotiempo = 0
            for i in range(0,max):
                
                #Instruccion a ejecutar
                instruccion = Colainstrucciones.Pop()
                #Ejecutar hasta completar
                completado = False
                while completado == False and (self.Tiempoactual) < int(self.Tiempomax):
                    completado = self.Ejecutar_instruccion(instruccion)
                    print(f'tiempoa: {self.Tiempoactual} - tiempmax: {self.Tiempomax} - completado: {completado}')
                
            #Ya no hay instrucciones pero si tiempo
            if Colainstrucciones.tamano() <= 0:
                #Guardar tiempo ultimo riego
                ultimoriegotiempo = self.Tiempoactual
                
                #Terminar tiempo
                for h in range(self.Tiempoactual, self.Tiempomax):
                    self.Tiempoactual += 1
                    print(f"\n\n>>>> Se completaron todos los riegos, tiempoA: {self.Tiempoactual} - tiempmax: {self.Tiempomax} - tiempo ultimo riego: {ultimoriegotiempo}\n\n")
            
                
            
        except Exception as e:
            print("!!! Error al ejecutar_tiempo !!!\n",e)
        print("########################## [FIN Sistema Riegos] ############################\n\n\n")
            
            
        