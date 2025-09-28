import os

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *

class SistemaArchivoHTML:
    def __init__(self, colainvernaderos):
        self.colainvernaderos = colainvernaderos
        self.ruta = None
        self.txthtml = ''
        self.idmovimientos = 1
    
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

            #Titulo
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
        </header>

        <section class="row g-4 mt-3">'''
            
            #Resumen invernadero
            self.HTMLTitulosResumen(Inv,numero)

            
        
            self.HTMLDronesResumen(Inv,numero)

            self.HTMLListamovimientos(Inv,numero)

            




            #Final
            self.txthtml += '\n      </section>\n   </div>\n  </div>'

        except Exception as e:
            print('!!! Error en crearinvernadero !!!\n',e)

    def HTMLListamovimientos(self, Inv, numero):
        try:
            print('>>> Lista movimientos')

            #Inicio
            self.txthtml += '''          <div class="col-12">
            <div class="card shadow-sm">
              <div class="card-body">
                <h5 class="card-title mb-3">Instrucciones por tiempo</h5>
                <p class="text-muted small mb-3">Acciones planificadas por segundo</p>

                <div class="accordion" id="accordionInstrucciones-Peten">

'''

            #Intermedio
            colamovimientos = Inv.historialmovimientos.Obtener(numero)
            for i in range(0,colamovimientos.tamano()):
            #for i in range(0,1):
                movimiento = colamovimientos.Obtener(i+1)
                nombre = movimiento.tiemposeg 
                mov = movimiento.colamovimientos
                self.idmovimientos += 1
                #Titulos tiempo
                self.txthtml += f'''
                    <!-- tiempo 1 -->
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="heading{self.idmovimientos}-Peten">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{self.idmovimientos}-Peten">
                            Tiempo — {nombre} s
                        </button>
                        </h2>
                        <div id="collapse{self.idmovimientos}-Peten" class="accordion-collapse collapse" data-bs-parent="#accordionInstrucciones-Peten">
                        <div class="accordion-body">

                    '''
                #Movmientos
                self.txthtml += f'''
                            <div class="row gy-2">
                            
                    '''
                for j in range(0,mov.tamano()):
                    dron = mov.Obtener(j+1)
                    dronnombre = dron.nombre
                    dronaccion = dron.accion
                    tamanobloq = int(12/mov.tamano())
                    self.txthtml += f'''
                                <div class="col-md-{tamanobloq}">
                                    <div class="card card-sm">
                                    <div class="card-body p-2 d-flex justify-content-between align-items-center">
                                        <div>
                                        <div class="small text-muted">{dronnombre}</div>
                                        <div class="fw-bold">{dronaccion}</div>
                                        </div>
                                    </div>
                                    </div>
                                </div>

                        '''
                    
                self.txthtml += f'''
                            
                            </div><!-- /.row -->
                    '''
                #Final
                self.txthtml += f'''
                        </div>
                        </div>
                    </div>
                    '''
            
            #Final
            self.txthtml += '''
            
                </div><!-- /.accordion -->
              </div>
            </div>
          </div>'''

        except Exception as e:
            print('!!! Error en HTMLListamovimientos !!!\n',e)

    def HTMLDronesResumen(self,Inv,numero):
        try:
            print('Lista drones')
            #Inicio
            self.txthtml += '''          <div class="col-lg-8">
            <div class="card shadow-sm">
              <div class="card-body">
                <h5 class="card-title">Eficiencia — Drones regadores</h5>
                <p class="text-muted small mb-3">Litros de agua y gramos de fertilizante por dron</p>

                <div class="table-responsive">
                  <table class="table table-sm align-middle">
                    <thead class="table-light">
                      <tr>
                        <th>Dron</th>
                        <th class="text-end">Litros de agua</th>
                        <th class="text-end">Fertilizante (g)</th>
                      </tr>
                    </thead>
                    <tbody>
                      '''
            
            #Lista Drones
            coladrones = Inv.historialdrones.Obtener(numero)
            for i in range(0,coladrones.tamano()):
                drondata = coladrones.Obtener(i+1)
                self.txthtml += f'''
                        <tr>
                            <td>{drondata.nombre}</td>
                            <td class="text-end">{drondata.aguautilizada}</td>
                            <td class="text-end">{drondata.fertilizanteutilizado}</td>
                        </tr>
                        '''

            #Final
            self.txthtml += '''
                      
                    </tbody>
                  </table>
                </div>

                <div class="mt-3">
                </div>
              </div>
            </div>
          </div>'''
        
            

            
        except Exception as e:
            print('!!! Error en HTMLDronesResumen !!!\n',e)


    def HTMLTitulosResumen(self,Inv,numero):
        try:
            print(f'>>> Creando Titulos resumen invernadero {Inv.nombre}')
            #Resumen invernadero
            tiempooptimo = Inv.historiatiempooptimo.Obtener(numero)
            aguareq = Inv.historiaagua.Obtener(numero)
            fertilreq = Inv.historaifertilizante.Obtener(numero)


            self.txthtml += f'''          <div class="col-lg-4">
            <div class="card shadow-sm">
              <div class="card-body">
                <h5 class="card-title">Parámetros del plan</h5>
                <div class="d-flex flex-column gap-2 mt-3">
                  <div class="d-flex justify-content-between align-items-center">
                    <div>
                      <div class="text-muted small">Tiempo óptimo (s)</div>
                      <div class="metric">{tiempooptimo}</div>
                    </div>
                    <div><span class="badge bg-secondary">tiempo</span></div>
                  </div>

                  <div class="d-flex justify-content-between align-items-center">
                    <div>
                      <div class="text-muted small">Agua requerida (L)</div>
                      <div class="metric">{aguareq} L</div>
                    </div>
                    <div><span class="badge bg-primary">agua</span></div>
                  </div>

                  <div class="d-flex justify-content-between align-items-center">
                    <div>
                      <div class="text-muted small">Fertilizante requerido (g)</div>
                      <div class="metric">{fertilreq} g</div>
                    </div>
                    <div><span class="badge bg-warning text-dark">fertilizante</span></div>
                  </div>
                </div>
              </div>
            </div>
          </div>'''


        
        except Exception as e:
            print('!!! Error en HTMLTitulosResumen!!!\n',e)

    
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

