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
#Iniciar sitema cental
app.config['sistema_central']  = SistemaCental()
app.config['invsel'] = None
app.config['plansel'] = None
app.config['tiempo']=None





@app.route('/',   methods=['GET','POST'])
def inicio():
    try:
        print('>>> banderaArchivonuevo: ',app.config['banderaArchivonuevo'])
        if request.method == 'GET':
            baneraArchivo = app.config['banderaArchivonuevo']
            return render_template('index.html')
        elif request.method == 'POST':
            print('>> inicio() reciviendo form')
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
                baneraArchivo = app.config['banderaArchivonuevo']
            return render_template('index.html', baneraArchivo=baneraArchivo)
    except Exception as e:
        print('!!! Error FLASK inicio() !!!\n',e)

@app.route('/resumen', methods=['GET'])
def resumen():
    return render_template('salidaH.html')


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
        
        #Ejecutar
        corresistemacentral()
        
        archivoProcesado = True
        return render_template('index.html', archivoProcesado=archivoProcesado)
    except Exception as e:
        print('!!! Error en ejecutarprograma() !!!\n',e)


def listanombres():
    sistema_central = app.config['sistema_central']
    print(sistema_central)
    listainvernaderos = sistema_central.ListarnombresInvernaderos()
    print(listainvernaderos)
    return listainvernaderos

@app.route('/selinvernadero',   methods=['GET','POST'])
def selinvernadero():
    try:
        print('>>>> Seleccionando invernadero')
        print('>>>>> Meotdo recivido: ',request.method)
        if request.method == 'GET':
            nombreInv = listanombres()
            print(nombreInv)
            return render_template('selInver.html', nombreInv=nombreInv)
        elif request.method == 'POST':
            invernadero = request.form.get("invernadero")  # o request.form["invernadero"]
            app.config['invsel'] = invernadero
            print("Invernadero:", invernadero)
            #return render_template('selfplan.html')
            return redirect(url_for('selplan'))
    except Exception as e:
        print('!!! Error en selinvernadero !!!\n',e)

def listaplanes():
    sistema_central = app.config['sistema_central']
    print(sistema_central)
    numinv = int(app.config['invsel'])
    print('>>>> Inv sel',numinv)
    listaplan = sistema_central.Listaplanes(numinv)
    return listaplan


def crearTDA(tiempo,plan):
    print('>> Creando TDAs')
    sistema_central = app.config['sistema_central']
    numinv = int(app.config['invsel'])
    print('>>>> Inv sel',numinv)
    listaplan = sistema_central.Listaplanes(numinv)
    print('creando tdad')
    sistema_central.crearTDA(int(tiempo),int(numinv),int(plan))
    print('creando tdad')

@app.route('/selplan',   methods=['GET','POST'])
def selplan():
    try:
        print('>>>> Seleccionando invernadero')
        print('>>>>> Meotdo recivido: ',request.method)
        if request.method == 'GET':
            
            lista = listaplanes()
            print(lista)
            return render_template('selfplan.html', lista=lista)
        elif request.method == 'POST':
            plan = request.form.get("plan")  
            tiempo = request.form.get("tiempo")
            print("Plan:", plan)
            print("Tiempo:", tiempo)
            app.config['plansel'] = plan
            app.config['tiempo']=tiempo
            crearTDA(tiempo,plan)
            return render_template('index.html')
    except Exception as e:
        print('!!! Error en selinvernadero !!!\n',e)



#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)

