from SistemArchivos.SistemaArchivoXML import SistemaArchivo
from SistemArchivos.SistemaArchivosSalidaXML import SistemaArchivoSalida
from SistemaRiegos.SistemaRiegos import SistemaRiegos
from SistemArchivos.SistemaArchivoSalidaHTML import SistemaArchivoHTML
from SistemArchivos.SistemaArchivoTDAs import SistemaTDAs

class SistemaCental:
    def __init__(self):
        self.ruta = None
        self.sistema_archivo = None
        self.sistema_riego = None
        self.sistema_archivoHTML = None
        self.sistema_TDAs = None
        self.Colainvernaderos = None


    
    def asignarruta(self, ruta):
        self.ruta = ruta
    
    def extraerinformacionXML(self):
        #iniciar sistema archivos
        self.sistema_archivo = SistemaArchivo(self.ruta)
        #Convertir a Listas y Colas
        invernaderos = self.sistema_archivo.segmentar_archivo()
        #iniciar sistem riegos
        self.sistema_riego = SistemaRiegos(invernaderos)
        
    
    # def seleccionarinvernaderoconsola(self):
    #     print('>')
    #     #Selecciona un invernadero
    #     Colanombreinvernaderos = self.sistema_riego.ColasInvernaderos()
    #     #Imprime invernaderos
    #     for i in range(0,Colanombreinvernaderos.tamano()):
    #         nombre = Colanombreinvernaderos.Pop().nombre
    #     #Seleccion una opcion
    #     invernaderoselecionado = input("Numero de opcion: ")
    #     print(invernaderoselecionado)
    #     #Listar Planes
    #     ColaLista = self.sistema_riego.ColasPlanes(invernaderoselecionado)
    #     #Imprime Planes
    #     for i in range(0,ColaLista.tamano()):
    #         nombre = ColaLista.Pop().nombre
    #     #Seleccion una opcion
    #     planselecionado = input("Numero de opcion: ")
    #     #Obtener informacion
    #     self.sistema_riego.Obtenerinformacion(invernaderoselecionado,1)
    #     self.sistema_riego.Ejecutar_tiempo(9)
    #     self.sistema_riego.CreanplanXML()

    #     self.sistema_riego.Obtenerinformacion(invernaderoselecionado,2)
    #     self.sistema_riego.Ejecutar_tiempo(10)
    #     self.sistema_riego.CreanplanXML()

    #     self.sistema_riego.GuardarSalidaXML()

    def crearReportesXML(self):
        try:
            #Obtener cola invernaderos
            self.Colainvernaderos = self.sistema_riego.obtenercolainvernadero()
            #Recorrer invernaderos
            for i in range(0,self.Colainvernaderos.tamano()):
                #obtener inverdadero
                invernaderoS = self.Colainvernaderos.Obtener(i+1)
                invernaderoS.desplegar()
                #obtener planes
                colaplanes = self.sistema_riego.ColasPlanes(str(i+1))
                colaplanes.desplegar()
                
                #Obtener info
                for j in range(0,colaplanes.tamano()):
                    self.sistema_riego.Obtenerinformacion(i+1,j+1)
                    self.sistema_riego.Ejecutar_tiempo(12)

            #Archivo Salida crear
            self.sistema_riego.CrearArchivoXML()

            self.sistema_riego.AlmacenarContenidoXML()

            # self.sistema_riego.CrearListainvernaderoXML()
            # self.sistema_riego.CrearXML()


            #Guardar XML
            self.sistema_riego.GuardarSalidaXML()



        except Exception as e:
            print('!!! Error al crear reportes xml !!!\n',e) 


    def crearArchivoHTML(self):
        #Incializar
        self.sistema_archivoHTML = SistemaArchivoHTML(self.Colainvernaderos)
        #Crear archivo
        self.sistema_archivoHTML.creararchivoHTML()

    def crearTDA(self, tiempo):
        print('> Crear TDA en Tiempo: ',tiempo)
        self.sistema_TDAs = SistemaTDAs()
        self.sistema_TDAs.hola


#Iniciar sitema cental
sistema_central = SistemaCental()
#Asignar Ruta
sistema_central.asignarruta('G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\entrada2.xml')
#Extraer informacion del archivo XML
sistema_central.extraerinformacionXML()
#Crear Reporte XML
sistema_central.crearReportesXML()
#Crear Reporte HTML
sistema_central.crearArchivoHTML()

#Crear TDA
sistema_central.crearTDA(5)


















