

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
            return redirect(url_for('inicio'))
        elif request.method == 'GET':
            return render_template('subirArchivo.html')
    except Exception as e:
        print('!!! Error en subirarchivo() !!!\n',e)




#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)

