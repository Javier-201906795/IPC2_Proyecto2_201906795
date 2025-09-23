class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def obtenerDato(self):
        return self.valor

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,valor):
        self.valor = valor

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente