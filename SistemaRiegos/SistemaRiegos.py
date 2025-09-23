from SistemArchivos.SistemaArchivoXML import SistemaArchivo


class SistemaRiegos():
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos

    def desplegar(self):
        self.colainvernaderos.desplegar()
    
    def Ejecutar_tiempo(self,tiempo):
        print("Tiempo: ", tiempo)
        #Recorre invernaderos
        for i in range(0,self.colainvernaderos.tamano()):
            print("ciclo: ",i)
            #Obtener invernadero
            invernadero = self.colainvernaderos.Pop()
            
            
        