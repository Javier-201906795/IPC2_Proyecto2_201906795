from SistemArchivos.SistemaArchivoXML import SistemaArchivo
from SistemArchivos.SistemaArchivosSalidaXML import SistemaArchivoSalida
from SistemaRiegos.SistemaRiegos import SistemaRiegos



#Leer Archivo XML
ruta = 'G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\entrada.xml'
rutaSalida = 'G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\salida.xml'
sistema_archivo = SistemaArchivo(ruta)
sistema_archivo_salida = SistemaArchivoSalida(rutaSalida)
#Convertir a Listas y Colas
invernaderos = sistema_archivo.segmentar_archivo()
#Pasar a SistemaRiegos
sistema_riego = SistemaRiegos(invernaderos)
#Selecciona un invernadero
Colanombreinvernaderos = sistema_riego.ColasInvernaderos()
#Imprime invernaderos
for i in range(0,Colanombreinvernaderos.tamano()):
    nombre = Colanombreinvernaderos.Pop().nombre
#Seleccion una opcion
invernaderoselecionado = input("Numero de opcion: ")
print(invernaderoselecionado)
#Listar Planes
ColaLista = sistema_riego.ColasPlanes(invernaderoselecionado)
#Imprime Planes
for i in range(0,ColaLista.tamano()):
    nombre = ColaLista.Pop().nombre
#Seleccion una opcion
planselecionado = input("Numero de opcion: ")
#Obtener informacion
#sistema_riego.Obtenerinformacion(invernaderoselecionado,1)
#sistema_riego.Ejecutar_tiempo(9)
sistema_riego.Obtenerinformacion(invernaderoselecionado,2)
sistema_riego.Ejecutar_tiempo(10)

#Sistema Salida XML
#sistema_archivo_salida.asignarcolainvernadero(sistema_riego.obtenercolainvernaderos())
#sistema_archivo_salida.segmentar_archivo_XML()













