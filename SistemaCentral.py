from SistemArchivos.SistemaArchivoXML import SistemaArchivo
from SistemArchivos.SistemaArchivosSalidaXML import SistemaArchivoSalida
from SistemaRiegos.SistemaRiegos import SistemaRiegos

class SistemaCental:
    def __init__(self):
        self.ruta = None
        self.sistema_archivo = None
        self.sistema_riego = None
        
    
    def asignarruta(self, ruta):
        self.ruta = ruta
    
    def extraerinformacionXML(self):
        #iniciar sistema archivos
        self.sistema_archivo = SistemaArchivo(self.ruta)
        #Convertir a Listas y Colas
        invernaderos = self.sistema_archivo.segmentar_archivo()
        #iniciar sistem riegos
        self.sistema_riego = SistemaRiegos(invernaderos)
        #Archivo Salida crear
        self.sistema_riego.CrearArchivoXML()
        self.sistema_riego.CrearListainvernaderoXML()
    
    def seleccionarinvernaderoconsola(self):
        print('>')
        #Selecciona un invernadero
        Colanombreinvernaderos = self.sistema_riego.ColasInvernaderos()
        #Imprime invernaderos
        for i in range(0,Colanombreinvernaderos.tamano()):
            nombre = Colanombreinvernaderos.Pop().nombre
        #Seleccion una opcion
        invernaderoselecionado = input("Numero de opcion: ")
        print(invernaderoselecionado)
        #Listar Planes
        ColaLista = self.sistema_riego.ColasPlanes(invernaderoselecionado)
        #Imprime Planes
        for i in range(0,ColaLista.tamano()):
            nombre = ColaLista.Pop().nombre
        #Seleccion una opcion
        planselecionado = input("Numero de opcion: ")
        #Obtener informacion
        self.sistema_riego.Obtenerinformacion(invernaderoselecionado,1)
        self.sistema_riego.Ejecutar_tiempo(9)
        self.sistema_riego.CreanplanXML()

        self.sistema_riego.Obtenerinformacion(invernaderoselecionado,2)
        self.sistema_riego.Ejecutar_tiempo(10)
        self.sistema_riego.CreanplanXML()

        self.sistema_riego.GuardarSalidaXML()

        



#Iniciar sitema cental
sistema_central = SistemaCental()
#Asignar Ruta
sistema_central.asignarruta('G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\entrada.xml')
#Extraer informacion del archivo XML
sistema_central.extraerinformacionXML()
#Seleccionar invernadero
sistema_central.seleccionarinvernaderoconsola()





# #Leer Archivo XML
# ruta = 'G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\entrada.xml'
# sistema_archivo = SistemaArchivo(ruta)
# #Convertir a Listas y Colas
# invernaderos = sistema_archivo.segmentar_archivo()
# #Pasar a SistemaRiegos
# sistema_riego = SistemaRiegos(invernaderos)
# #Selecciona un invernadero
# Colanombreinvernaderos = sistema_riego.ColasInvernaderos()
# #Imprime invernaderos
# for i in range(0,Colanombreinvernaderos.tamano()):
#     nombre = Colanombreinvernaderos.Pop().nombre
# #Seleccion una opcion
# invernaderoselecionado = input("Numero de opcion: ")
# print(invernaderoselecionado)
# #Listar Planes
# ColaLista = sistema_riego.ColasPlanes(invernaderoselecionado)
# #Imprime Planes
# for i in range(0,ColaLista.tamano()):
#     nombre = ColaLista.Pop().nombre
# #Seleccion una opcion
# planselecionado = input("Numero de opcion: ")

# #Archivo Salida crear
# sistema_riego.CrearArchivoXML()
# sistema_riego.CrearListainvernaderoXML()


# #Obtener informacion
# sistema_riego.Obtenerinformacion(invernaderoselecionado,1)
# sistema_riego.Ejecutar_tiempo(9)
# sistema_riego.CreanplanXML()

# sistema_riego.Obtenerinformacion(invernaderoselecionado,2)
# sistema_riego.Ejecutar_tiempo(10)
# sistema_riego.CreanplanXML()

# sistema_riego.GuardarSalidaXML()














