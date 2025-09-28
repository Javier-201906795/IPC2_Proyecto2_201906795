import os

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *

class SistemaArchivoHTML:
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos
        self.ruta = None
        self.txthtml = ''
    
    def creararchivoHTML(self):
        try:
            print("\n"+'#'*10+"[ sistema HTML ]"+"*"*10)
            self.colainvernaderos.desplegar()
            print('\n>> Creando archivo HTML')
            #incio documento html
            self.HTMLencabezado()

            #Contenido invernaderos
            for i in range(0,self.colainvernaderos.tamano()):
                invernadero = self.colainvernaderos.Obtener(i+1)
                #obtener numero plan
                planes = invernadero.ListaPlanes

                #Recorre invernadero y Planes
                maxplanes = planes.tamano()
                for j in range(0,maxplanes):
                    self.crearinvernadero(invernadero, j+1)



            #pie de pagina 
            self.HTMLpie()

            print('\n>> guardando en salidaH.html')
            self.guardarHTML('holamundo')
            print("#"*30)
        except Exception as e:
            print('!!! Error al crear archivo HTML!!!\n',e)
        
    def guardarHTML(self,contenido):
        try:
            print('>> Guardando HTML')
            self.ruta = 'salidaH.html'
            with open(self.ruta, 'wb') as archivo:
                archivo.write(self.txthtml.encode('utf-8'))
            print(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            print("!!! Error al crear el archivo DOC!!!\n",e)

    

    def crearinvernadero(self,Inv, numero):
        try:
            Inv.desplegar()
            print('>>> Creando invernadero')
            #Inicio
            self.txthtml +='''\n  <div id="invernaderos">\n   <div class="invernadero">
            
            '''
            #Titulo
            nombreInv = Inv.nombre
            #Planes
            plannombre = Inv.ListaPlanes.Obtener(numero).nombre


            self.txthtml +=f'''      <header class="hero d-flex align-items-center bg-white border-bottom rounded-top">
          <div class="container">
            <div class="row align-items-center">
              <div class="col-md-8">
                <h1 class="h2 mb-1"><span class="text-primary">{nombreInv}</span></h1>
                <p class="mb-0 text-muted">Resumen visual del <strong>Plan: {plannombre}</strong></p>
              </div>
              <div class="col-md-4 text-md-end mt-3 mt-md-0">
              </div>
            </div>
          </div>
        </header>'''



            #Final
            self.txthtml += '\n   </div>\n  </div>'

        except Exception as e:
            print('!!! Error en crearinvernadero !!!\n',e)




    
    def HTMLencabezado(self):
        print('>>> Creando Encabezado html')
        self.txthtml += """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Invernaderos — Plan Semana 3</title>

  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    /* Pequeños ajustes estéticos */
    .hero {
      height: 28vh;
      min-height: 160px;
    }
    .metric {
      font-size: 1.25rem;
      font-weight: 600;
    }
    .drone-badge {
      min-width: 72px;
      display:inline-block;
    }

    /* Separador entre invernaderos */
    .invernadero {
      margin-bottom: 1.5rem;
    }
  </style>
</head>
<body class="bg-light">

  <!-- NAVBAR -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
      <a class="navbar-brand" href="#">Invernaderos</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMain">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navMain">
        <ul class="navbar-nav ms-auto">
          
        </ul>
      </div>
    </div>
  </nav>

  
  <main class="container py-4">"""
        
    def HTMLpie(self):
        print('>>> Creando Pie de pagina html')
        self.txthtml += """
        
  </main>

  <!-- FOOTER -->
  <footer class="bg-white border-top py-3">
    <div class="container d-flex justify-content-between">
      <small class="text-muted">Javier Ricardo Yllescas Barrios - <strong>201906795</strong></small>
    </div>
  </footer>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js"></script>
</body>
</html>"""

