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

    def desplegar(self):
        print(f"ID: {self.id} - Nombre: {self.nombre}")

    def EsIgualALLave(self, id):
        return self.id == id


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