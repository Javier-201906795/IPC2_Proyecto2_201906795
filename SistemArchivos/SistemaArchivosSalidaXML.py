from xml.dom.minidom import Document, parse, parseString

from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *


class SistemaArchivoSalida:
    def __init__(self, ruta):
        self.ruta = ruta
        self.colainvernaderos = None
        self.doc = None
        self.root = None
        self.listaInvernaderos = None
        self.listaplanes = None

        self.invernaderoactual = None
        self.nuevasinstruccionesinv = None
    
    def asignarcolainvernadero(self, colainver):
        self.colainvernaderos = colainver
        #Imprimir valores
        print("\n"+'*-'*10+"[ Invernaderos Salida XML ]"+"*-"*10)
        self.colainvernaderos.desplegar()
        print("\n"+'/'*10+"[ Fin Invernaderos Salida XML ]"+"/"*10)

    def crear_archivo(self, contenido):
        try:
            with open(self.ruta, 'wb') as archivo:
                archivo.write(contenido)
            print(">> Archivo creado o sobrescrito correctamente.\n")
        except Exception as e:
            print(f'!!! Error al crear_archivo !!!\n',e)
    
    
    def creararchivoDOC(self):
        try:
            print('Creando Doc and root')
            self.doc = Document()
            self.root = self.doc.createElement('datoSalida')
            self.doc.appendChild(self.root)
        except Exception as e:
            print("!!! Error al crear el archivo DOC!!!\n",e)
    
    def agregarinvernaderos(self):
        try:
            doc = self.doc
            
            #Recorre invernaderos
            if (self.colainvernaderos.tamano() > 0):
                for i in range(0,self.colainvernaderos.tamano()):
                    if i <=0:
                        inv = self.colainvernaderos.primero
                    else:
                        inv = inv.siguiente
                    #Obtener datos
                    invern = inv.valor
                    nombre = invern.nombre
                    ##Datos invernadero
                    invernadero = doc.createElement('invernadero')
                    invernadero.setAttribute("nombre", f"{nombre}")
                    self.listaInvernaderos.appendChild(invernadero)

                    #Lista Planes
                    self.listaplanes = doc.createElement('listaPlanes')
                    invernadero.appendChild(self.listaplanes)

        except Exception as e:
            print("!!! Error al agregarinvernaderos!!!\n ",e)
    

    def obtenerinvernaderactual(self,numeroinvernadero):
        try:
            for i in range(0,int(numeroinvernadero)):
                if i <=0:
                    invernaderoL = self.colainvernaderos.primero
                else:
                    invernaderoL = invernaderoL.siguiente
                invernaderodata = invernaderoL.valor
                #Almacenar
                self.invernaderoactual = invernaderodata
        
        except Exception as e:
            print("!!! Error al obtenerinvernaderactual!!!\n",e)

    def obtenerinstrucciones(self):
        try:
            #COPIA LAS INSTRUCCIONES antes que sean sobreescritas
            instruccionesinv = self.invernaderoactual.colainstrucciones
            self.nuevasinstruccionesinv = Cola()
            for i in range (0,instruccionesinv.tamano()):
                if i <=0:
                    colaL = instruccionesinv.primero
                else:
                    colaL = colaL.siguiente
                tiempomovimiento = colaL.valor
                nombretiempo = tiempomovimiento.tiemposeg
                colainstru = tiempomovimiento.colamovimientos
                #Crear nuevas colas
                nuevaColainstruciones = Cola()
                for j in range(0,colainstru.tamano()):
                    if j <=0:
                        instruL = colainstru.primero
                    else:
                        instruL = instruL.siguiente
                    instruccion = instruL.valor
                    accion = instruccion.accion
                    nombre = instruccion.nombre
                    #Agregar a nueva cola
                    nuevaColainstruciones.Push(Cmovimiento(nombre,accion))
                #Crea nueva cola
                self.nuevasinstruccionesinv.Push(Ctiempo(nombretiempo,nuevaColainstruciones))

            self.nuevasinstruccionesinv.desplegar()
        except Exception as e:
            print('!!! Error en btenerinstrucciones !!!',e)





    # def crear_movimientos_dron(self):
    #     try:
    #         print('> Creando movimientos dron')
    #         self.nuevasinstruccionesinv.desplegar()
    #         print()
    #         self.obtenerinstrucciones()
    #         self.nuevasinstruccionesinv.desplegar()
    #         #Obtener valores
    #         for i in range (0,int(self.invernaderoactual.tiempoOptimo)):
    #             print('i:',i)
    #             if i <=0:
    #                 instruccionL = self.nuevasinstruccionesinv.primero
    #             else:
    #                 instruccionL = instruccionL.siguiente
    #             instruccion = instruccionL.valor
    #             tiempotxt = instruccion.tiemposeg
    #             colainstrucciones = instruccion.colamovimientos
    #             print(f'-[ {tiempotxt} ]-')
    #             for h in range(0,colainstrucciones.tamano()):
    #                 if h <=0:
    #                     movimientoL = colainstrucciones.primero
    #                 else:
    #                     movimientoL = movimientoL.siguiente
    #                 movimiento = movimientoL.valor
    #                 nombredron = movimiento.nombre
    #                 acciondron = movimiento.accion
    #                 print(f'Nom: {nombredron} - Acc: {acciondron}')
    #                 self.nuevasinstruccionesinv.desplegar()
    #             print(f'-[FIN {tiempotxt} ]-')


    #     except Exception as e:
    #         print("!!! Error al crear movimientos !!!\n",e)





    def crear_plan(self, numeroinvernadero, nombreplan, numeroplan):
        try:
            print('#'*10+" [Crear PLAN ]"+"#"*10)
            print(f'numeroinvernadero: {numeroinvernadero} - numeroplan: {numeroplan} - nombreplan: {nombreplan}')
            doc = self.doc
            listaplanes = self.listaplanes
            #Obtner infomacion invernadero
            self.obtenerinvernaderactual(numeroinvernadero)
            #Guardar instrucciones antes que se sobreescriban
            self.obtenerinstrucciones()
            print(f'Creando plan el invernadero nuero: {numeroinvernadero}')
            #Modificar Invernadero
            Listainvernaderos = self.listaInvernaderos.getElementsByTagName('invernadero')
            for i in range(0,int(numeroinvernadero)):
                invernadero = Listainvernaderos[i]
                print("Nombre Invernadero: ", invernadero.getAttribute('nombre'))
                #Datos Planes
                plan = doc.createElement('plan')
                plan.setAttribute('nombre',f'{nombreplan}')
                listaplanes.appendChild(plan)

                #Tiempo optimo
                tiempoOptimo = doc.createElement('tiempoOptimoSegundos')
                plan.appendChild(tiempoOptimo)
                txt= doc.createTextNode(str(self.invernaderoactual.tiempoOptimo))
                tiempoOptimo.appendChild(txt)

                #aguaRequeridaLitros
                aguaRequerida = doc.createElement('aguaRequeridaLitros')
                plan.appendChild(aguaRequerida)
                txt= doc.createTextNode(str(self.invernaderoactual.aguaRequerida))
                aguaRequerida.appendChild(txt)

                #Fertilizante
                fertilizanteReq = doc.createElement('fertilizanteRequeridoGramos')
                plan.appendChild(fertilizanteReq)
                txt= doc.createTextNode(str(self.invernaderoactual.fertilizanteRequerido))
                fertilizanteReq.appendChild(txt)

                #Lista Eficiencia Drones
                efiDrones = doc.createElement('eficienciaDronesRegadores')
                plan.appendChild(efiDrones)

                #Dron
                lsdron = self.invernaderoactual.ListaDrones
                for j in range(0,lsdron.tamano()):
                    if j <=0:
                        dronl = lsdron.primero
                    else:
                        dronl = dronl.siguiente
                    dataDron = dronl.valor

                    Dron = doc.createElement('dron')
                    efiDrones.appendChild(Dron)
                    Dron.setAttribute('nombre',f'{dataDron.nombre}')
                    Dron.setAttribute('litrosAgua',f'{dataDron.aguautilizada}')
                    Dron.setAttribute('gramosFertilizante',f'{dataDron.fertilizanteutilizado}')

                #Lista instrucciones
                instrucciones = doc.createElement('instrucciones')
                plan.appendChild(instrucciones)

                #self.crear_movimientos_dron()

                

                #Tiempo
                planmovientos = None
                for m in range(0,int(numeroplan)):
                    if m <=0:
                        historicoplanL = self.invernaderoactual.historialmovimientos.primero
                    else:
                        historicoplanL = historicoplanL.siguiente
                    planmovientos = historicoplanL.valor
                    print("\n-----")
                    planmovientos.desplegar()
                    print("------\n")

                for n in range(0,int(planmovientos.tamano())):    
                    plan = planmovientos.Obtener(n+1)
                    
                    tiempo = self.doc.createElement('tiempo')
                    tiempo.setAttribute('segundos',f'{plan.tiemposeg}')
                    instrucciones.appendChild(tiempo)

                    #Movimiento
                    colamovi = plan.colamovimientos
                    print(f'> XML agregando Tiempo: {plan.tiemposeg}')
                    colamovi.desplegar()
                    print()
                    self.nuevasinstruccionesinv.desplegar()
                    
                    for l in range(0,colamovi.tamano()):
                        if l <= 0:
                            mov = colamovi.primero
                        else:
                            mov = mov.siguiente
                        movimientodata = mov.valor
                        movimiento = doc.createElement('dron')
                        tiempo.appendChild(movimiento)
                        movimiento.setAttribute('nombre',f'{movimientodata.nombre}')
                        movimiento.setAttribute('accion',f'{movimientodata.accion}')
                
                    #print(f"----Creando Movimiento {n+1}/{planmovientos.tamano()}---")

                # print('\n-----------')
                # self.nuevasinstruccionesinv.desplegar()
                # print('-----------\n')
                # maxciclo =int(self.invernaderoactual.tiempoOptimo)

                # #Agregar valores
                # for l in range(0, maxciclo):
                #     if l <=0:
                #         NuevacolaL = self.nuevasinstruccionesinv.primero
                #     else:
                #         NuevacolaL = NuevacolaL.siguiente
                #     Nuevacolainstrucciones = NuevacolaL.valor
                    
                #     print("----Movimiento---")
                #     Nuevacolainstrucciones.desplegar()

                #     tiempo = self.doc.createElement('tiempo')
                #     tiempo.setAttribute('segundos',f'{Nuevacolainstrucciones.tiemposeg}')
                #     instrucciones.appendChild(tiempo)

                #     #Movimiento
                #     colamovi = Nuevacolainstrucciones.colamovimientos
                #     self.nuevasinstruccionesinv.desplegar()
                    
                #     for l in range(0,colamovi.tamano()):
                #         if l <= 0:
                #             mov = colamovi.primero
                #         else:
                #             mov = mov.siguiente
                #         movimientodata = mov.valor
                #         movimiento = doc.createElement('dron')
                #         tiempo.appendChild(movimiento)
                #         movimiento.setAttribute('nombre',f'{movimientodata.nombre}')
                #         movimiento.setAttribute('accion',f'{movimientodata.accion}')
                #     print("----Fin Movimiento---")
        except Exception as e:
            print("!!! Error al crear plan!!!",e)


    def GuardarSalidaXML(self):
        try:
            # ==============================
            # Guardar en archivo XML
            # ==============================
            xml_str = self.doc.toprettyxml(indent=" ", encoding="UTF-8")
            self.crear_archivo(xml_str)
        except Exception as e:
            print('!!! Error en GuardarSalidaXML!!!',e)
    
    def segmentar_archivo_XML(self):
        try:
            #self.creararchivoDOC()
            doc = self.doc
            root = self.root
            
            self.listaInvernaderos = doc.createElement('listaInvernaderos')
            root.appendChild(self.listaInvernaderos)

            #self.agregarinvernaderos()



            #Lista invernaderos
            for i in range(0,self.colainvernaderos.tamano()):
                Inv = self.colainvernaderos.Obtener(i+1)
                #Datos invernadero
                invernadero = doc.createElement('invernadero')
                invernadero.setAttribute("nombre", f"{Inv.nombre}")
                self.listaInvernaderos.appendChild(invernadero)
                print('> creando invernadero: ',Inv.nombre)

                #Lista Planes
                listaplanes = doc.createElement('listaPlanes')
                invernadero.appendChild(listaplanes)

                for h in range(0,Inv.ListaPlanes.tamano()):
                    #Obtener informacion del historico movimientos
                    Movmientos = Inv.historialmovimientos.Obtener(h+1)
                    #Obtener informacion de Lista plantes
                    Planinfo = Inv.ListaPlanes.Obtener(h+1)
                    #Obtener tiempo optimo
                    TiempooptimoInv = Inv.historiatiempooptimo.Obtener(h+1)
                    #Obtener ferlitianzate y agua
                    aguaopt = Inv.historiaagua.Obtener(h+1)
                    fertopt = Inv.historaifertilizante.Obtener(h+1)
                    
                    print('\n---[Plan info]---')
                    Planinfo.desplegar()
                    print('---[Fin Plan info]---\n')

                    print('\n---[Movimientos]---')
                    Movmientos.desplegar()
                    print('---[Fin Movimientos]---\n')



                    #Datos Planes
                    plan = doc.createElement('plan')
                    plan.setAttribute('nombre',f'{Planinfo.nombre}')
                    listaplanes.appendChild(plan)

                    #Tiempo optimo
                    tiempoOptimo = doc.createElement('tiempoOptimoSegundos')
                    plan.appendChild(tiempoOptimo)
                    txt= doc.createTextNode(f'{TiempooptimoInv}')
                    tiempoOptimo.appendChild(txt)

                    #aguaRequeridaLitros
                    aguaRequerida = doc.createElement('aguaRequeridaLitros')
                    plan.appendChild(aguaRequerida)
                    txt= doc.createTextNode(f'{aguaopt}')
                    aguaRequerida.appendChild(txt)

                    #Fertilizante
                    fertilizanteReq = doc.createElement('fertilizanteRequeridoGramos')
                    plan.appendChild(fertilizanteReq)
                    txt= doc.createTextNode(f'{fertopt}')
                    fertilizanteReq.appendChild(txt)

                    #Lista Eficiencia Drones
                    efiDrones = doc.createElement('eficienciaDronesRegadores')
                    plan.appendChild(efiDrones)

                    #Dron
                    for j in range(0,3):
                        Dron = doc.createElement('dron')
                        efiDrones.appendChild(Dron)
                        Dron.setAttribute('nombre',f'DR{j}')
                        Dron.setAttribute('litrosAgua',f'{j+3}')
                        Dron.setAttribute('gramosFertilizante',f'{j*100}')

                    #Lista instrucciones
                    instrucciones = doc.createElement('instrucciones')
                    plan.appendChild(instrucciones)

                    #Tiempo
                    for k in range(0,1):
                        tiempo = doc.createElement('tiempo')
                        tiempo.setAttribute('segundos',f'{k}')
                        instrucciones.appendChild(tiempo)

                        #Movimiento
                        for l in range(0,3):
                            movimiento = doc.createElement('dron')
                            tiempo.appendChild(movimiento)
                            movimiento.setAttribute('nombre',f'DR{l}')
                            movimiento.setAttribute('accion',f'Adelante(H{i}P{l})')

            
            #Modificar Invernadero
            # lista = listaInvernaderos.getElementsByTagName('invernadero')
            # if len(lista) > 1:
            #     segundo = lista[1]                       # índice 1 -> segundo elemento
            #     print("Atributo nombre (A):", segundo.getAttribute('nombre'))
            

            # ==============================
            # Guardar en archivo XML
            # ==============================
            #xml_str = doc.toprettyxml(indent=" ", encoding="UTF-8")
            #self.crear_archivo(xml_str)

        except Exception as e:
            print(f'!!! Error al segmentar_archivo_XML !!!\n',e)