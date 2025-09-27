
from Nodos.Nodo import Nodo

class Cola:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacia(self):
        return self.primero == None

    def Push(self,item):
        nuevo = Nodo(item)
        
        if self.primero != None: 
            self.ultimo.asignarSiguiente(nuevo)
        else:
            self.primero = nuevo
            
        self.ultimo = nuevo
            
    def tamano(self):
        actual = self.primero
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def desplegar(self):
        actual = self.primero
        while actual != None:
            actual.obtenerDato().desplegar()
            actual = actual.obtenerSiguiente()

    def buscar(self,item):
        actual = self.primero
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado
    
    def buscar_item(self,item):
        actual = self.primero
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = actual.obtenerDato()
            else:
                actual = actual.obtenerSiguiente()

        return encontrado

    def Pop(self):
        primerotemp = self.primero
        if self.primero != None:
            self.primero.obtenerDato().desplegar()                    
            self.primero = self.primero.obtenerSiguiente()
        else:
            print("Cola esta vacia")
            return None
            
        return primerotemp.obtenerDato()

    def Obtener(self,numero):
        max = self.tamano()
        if numero <= max:
            for i in range(0,numero):
                if i <=0:
                    item = self.primero
                else:
                    item = item.siguiente
                itemvalor = item.valor
            return itemvalor
        else:
            return None