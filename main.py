from SistemArchivos.SistemaArchivoXML import SistemaArchivo




#Leer Archivo XML
ruta = 'G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\entrada.xml'
sistema_archivo = SistemaArchivo(ruta)
invernaderos = sistema_archivo.segmentar_archivo()
print("\n"*5,"?"*80)
invernaderos.desplegar()











