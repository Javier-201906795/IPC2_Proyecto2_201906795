class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def obtenerDato(self):
        return self.valor

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,valor):
        self.valor = valor

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


########################################################################

class Lista:

    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def obtenerprimero(self):
        return self.primero

    def estaVacia(self):
        return self.primero == None

    def agregar(self,item):
        nuevo = Nodo(item)
        nuevo.asignarSiguiente(self.primero)
        self.primero = nuevo
        self.longitud += 1

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

    def eliminar(self,item):
        actual = self.primero
        previo = None
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato().EsIgualALLave(item):
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        if previo == None:
            if self.primero != None:
                self.primero = actual.obtenerSiguiente()
                print("Eliminado1")
        else:
            if encontrado:
                previo.asignarSiguiente(actual.obtenerSiguiente())
                print("Eliminado2")
            else:
                print("no encontrado")

    def obtener(self, indice):
        if indice < 0 or indice >= self.longitud:
            return None
        actual = self.primero
        for i in range(indice):
            actual = actual.siguiente
        return actual.valor
    
    def buscar_indice(self, id_buscar):
        # Busca el índice de un elemento por su id
        actual = self.primero
        indice = 0
        while actual:
            #Valida si existe el valor id y si si el id es igual
            if hasattr(actual.valor, 'id') and actual.valor.id == id_buscar:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1