import os

from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
from flask.json import jsonify



#Crear app
app = Flask(__name__)
#CORS
cors = CORS(app)

@app.route('/',  methods=['GET'])
def inicio():
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
            
            return redirect(url_for('inicio'))
        elif request.method == 'GET':
            return render_template('subirArchivo.html')
    except Exception as e:
        print('!!! Error en subirarchivo() !!!\n',e)




#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)

