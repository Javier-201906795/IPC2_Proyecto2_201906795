

from flask import Flask, request, render_template
from flask_cors import CORS
from flask.json import jsonify

#Crear app
app = Flask(__name__)
#CORS
cors = CORS(app)

@app.route('/',  methods=['GET'])
def inicio():
    return '<h1>Invernaderos</h1>'




#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)

