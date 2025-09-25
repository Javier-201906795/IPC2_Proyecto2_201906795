from Nodos.Lista import Lista

from Nodos.Cola import Cola
from Nodos.Clases import *

class InfoNodo():
    
    def desplegar():
        pass
    
    def EsIgualALLave():
        pass


############################################################

class CDron (InfoNodo):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.hilera = None
        self.planta = 0
    
    def asignarPlanta(self,planta):
        self.planta = planta

    def asignarHilera(self, hilera):
        self.hilera = hilera
    
    def desplegar(self):
        print(f"ID: {self.id} - Nombre: {self.nombre} - Hilera Asignada: {self.hilera} - Planta: P{self.planta}")

    def EsIgualALLave(self, id):
        return self.id == id
    


############################################################

class CPlanta (InfoNodo):
    def __init__(self, hilera, posicion, litrosAgua, gramosFertilizante, nombre):
        self.hilera = hilera
        self.posicion = posicion
        self.litrosAgua = litrosAgua
        self.gramosFertilizante = gramosFertilizante
        self.nombre = nombre
    
    def desplegar(self):
        print(f"Hilera: {self.hilera} - Posicion: {self.posicion} - Litros Agua: {self.litrosAgua} - Gramos Fertilizante: {self.gramosFertilizante} - Nombre Planta: {self.nombre}")
    
    def EsIgualALLave(self, nombre):
        return self.nombre == nombre


############################################################

class CAsignacionPlan (InfoNodo):
    def __init__ (self, hilera, planta):
        self.hilera = hilera
        self.planta = planta
    
    def desplegar(self):
        print(f"Hilera: {self.hilera} - Planta: {self.planta}")
    
    def EsIgualALLave(self, hilera):
        return self.hilera == hilera


############################################################

class CPlanRiego (InfoNodo):
    def __init__ (self, nombre, colaplan):
        self.nombre = nombre
        self.colaplan = colaplan

    def desplegar(self):
        
        print(f"-----[Plan Riego: {self.nombre}]----")
        self.colaplan.desplegar()
        print(f"-----[FIN Plan Riego {self.nombre}]----")

############################################################
class CInvernadero (InfoNodo):
    def __init__(self, nombre, numeroHilera, plantasXHilera, ListaPlantas, ListaPlanes, ListaDrones):
        self.nombre = nombre
        self.numeroHilera = numeroHilera
        self.plantasXHilera = plantasXHilera
        self.ListaPlantas = ListaPlantas
        self.ListaPlanes = ListaPlanes
        self.ListaDrones = ListaDrones

        self.colainstrucciones = Cola()
    
    def EsIgualALLave(self, nombre):
        return self.nombre == nombre
    
    def desplegar(self):
        print("/"*120)
        print(f'nombre: {self.nombre} - numero hileras: {self.numeroHilera} - plantas por hilera: {self.plantasXHilera}')
        print("-------------- [Lista Plantas] --------------")
        self.ListaPlantas.desplegar()
        print("-------------- [Fin Lista Plantas] --------------")
        print("-------------- [Lista Planes] -----------------")
        self.ListaPlanes.desplegar()
        print("------------- [Fin Lista Planes] --------------")
        print("-------------- [Lista Drones] -----------------")
        self.ListaDrones.desplegar()
        print("-------------- [Fin Lista Planes] -----------------")
        print("/"*120)
    
############################################################
class Cnombreinvernadero (InfoNodo):
    def __init__(self, nombre,opcion):
        self.nombre = nombre
        self.opcion = opcion

    def desplegar(self):
        print(f'Opcion: {self.opcion}) Nombre: {self.nombre}')       
    
    def EsIgualALLave(self, nombre):
        return self.nombre == nombre    

############################################################
class Cnombreplan (InfoNodo):
    def  __init__(self, nombre, opcion):
        self.nombre = nombre
        self.opcion = opcion

    def desplegar(self):
        print(f'Opcion: {self.opcion}) Nombre: {self.nombre}')       
    
    def EsIgualALLave(self, nombre):
        return self.nombre == nombre  


############################################################

class Ctiempo(InfoNodo):
    def __init__(self, tiemposeg, colamovimientos):
        self.tiemposeg = tiemposeg
        self.colamovimientos = colamovimientos

    def desplegar(self):
        print(f'\nTiempo: {self.tiemposeg}')
        if self.colamovimientos.tamano() == 0:
            print('- No hay elemento en movimientos')
        else:
            self.colamovimientos.desplegar()
    
    def asignarcolamovimientos(self, colamov):
        self.colamovimientos = colamov

############################################################

class Cmovimiento(InfoNodo):
    def __init__(self, nombre, accion):
        self.nombre = nombre
        self.accion = accion
    
    def desplegar(self):
        print(f'Movimiento -> Nombre: {self.nombre} - Accion: {self.accion}')