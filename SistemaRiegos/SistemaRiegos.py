from SistemArchivos.SistemaArchivoXML import SistemaArchivo


class SistemaRiegos():
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos

    def desplegar(self):
        self.colainvernaderos.desplegar()
    
    def Ejecutar_tiempo(self,tiempo):
        print("\n\n\n########################## [Sistema Riegos] ############################")
        print(">> Tiempo: ", tiempo)
        #Recorre invernaderos
        for i in range(0,self.colainvernaderos.tamano()):
            print(">>> ciclo: ",i)
            #Obtener invernadero
            invernadero = self.colainvernaderos.Pop()
            #obtener datos
            nombre = invernadero.nombre
            numeroHilera = invernadero.numeroHilera
            plantasXHilera = invernadero.plantasXHilera
            ListaPlantas = invernadero.ListaPlantas
            ListaPlanes = invernadero.ListaPlanes
            ListaDrones = invernadero.ListaDrones
            print("\n\n ------------- [Instrucciones] --------------")
            #Obtener Instrucciones
            for i in range(0,ListaPlanes.tamano()):
                if i <=0:
                    plan = ListaPlanes.primero
                else:
                    plan = plan.siguiente
                #Datos plan
                nombreplan = plan.valor.nombre
                colaplan = plan.valor.colaplan
                print(f'\nNombre plan: {nombreplan}')
                colaplan.desplegar()
            print("\n\n ------------- [Fin Instrucciones] --------------")

        print("########################## [FIN Sistema Riegos] ############################\n\n\n")
            
            
        