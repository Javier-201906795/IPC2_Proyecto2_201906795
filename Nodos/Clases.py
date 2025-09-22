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