from Nodos.Lista import Lista


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

    def asignarHilera(self, hilera):
        self.hilera = hilera
    
    def desplegar(self):
        print(f"ID: {self.id} - Nombre: {self.nombre} - Hilera Asignada: {self.hilera}")

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
    def __init__(self, nombre, numeroHilera, plantasXHilera, ListaPlantas, ListaAsignacionDrones):
        self.nombre = nombre
        self.numeroHilera = numeroHilera
        self.plantasXHilera = plantasXHilera
        self.ListaPlantas = ListaPlantas
        self.ListaAsignacionDrones = ListaAsignacionDrones
    
    
    
    
    
    def EsIgualALLave(self, nombre):
        return self.nombre == nombre