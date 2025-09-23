from SistemArchivos.SistemaArchivoXML import SistemaArchivo


class SistemaRiegos():
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos

    def desplegar(self):
        self.colainvernaderos.desplegar()