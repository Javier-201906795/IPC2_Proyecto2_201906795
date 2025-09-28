import os

from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
from flask.json import jsonify

from SistemaCentral import SistemaCental



#Crear app
app = Flask(__name__)
#CORS
cors = CORS(app)




#Variables Globales
app.config['banderaArchivonuevo'] = False
app.config['sistema_central'] = None





@app.route('/',  methods=['GET'])
def inicio():
    print('>>> banderaArchivonuevo: ',app.config['banderaArchivonuevo'])
    return '<h1>Invernaderos</h1>'

@app.route('/resumen', methods=['GET'])
def resumen():
    return render_template('salidaH.html')

@app.route('/subirarchivo', methods=['GET','POST'])
def subirarchivo():
    try:
        print('> /subirarchivo')
        if request.method == 'POST':
            print('>> Reciviendo archivo')
            #Evaluar Archivo
            mensaje = ''
            if 'archivo' not in request.files:
                mensaje = '!! No se encontro el archivo !! '
                print(mensaje)
            #Archivo
            archivo = request.files['archivo']
            if archivo.filename == '':
                mensaje = '!! No se selecciono ningun archivo !!'
                print(mensaje)
            
            #Comprobar
            if mensaje == '':
                #Guardar Archivo
                ruta_archivo = os.path.join(os.getcwd(),'entrada.xml')
                archivo.save(ruta_archivo)
                print('>>> Se subio el archivo correctamente.')
                app.config['banderaArchivonuevo'] = True
            
            return redirect(url_for('inicio'))
        elif request.method == 'GET':
            return render_template('subirArchivo.html')
    except Exception as e:
        print('!!! Error en subirarchivo() !!!\n',e)

def corresistemacentral():
    print('>>> Inicio sistema central')
    
    sistema_central = app.config['sistema_central']
    #Asignar Ruta
    sistema_central.asignarruta('G:\\2020\\2020_USAC\\Semestre14(2025)\\IPC2\\1_Laboratorio\\8_PROYECTO2\\IPC2_Proyecto2_201906795\\entrada.xml')
    print('>>> sistema central1')
    #Extraer informacion del archivo XML
    sistema_central.extraerinformacionXML()
    print('>>> sistema central2')
    #Crear Reporte XML
    sistema_central.crearReportesXML()
    #Crear Reporte HTML
    sistema_central.crearArchivoHTML('templates\\salidaH.html')

    #Crear TDA
    sistema_central.crearTDA(5,1,1)


@app.route('/ejecutarprograma', methods=['GET'])
def ejecutarprograma():
    try:
        print('>>>> Ejecutando programa')
        #Iniciar sitema cental
        app.config['sistema_central']  = SistemaCental()
        #Ejecutar
        corresistemacentral()
        

        return '<h1>Ejecutando Programa</h1>'
    except Exception as e:
        print('!!! Error en ejecutarprograma() !!!\n',e)


#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)

