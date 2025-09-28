import os


from Nodos.Lista import Lista
from Nodos.Cola import Cola
from Nodos.Clases import *



class SistemaTDAs:
    def __init__(self):
        self.dot_text = ''
        self.colainstrucciones = None
    
    def asignarcolainstrucciones(self, cola):
        try:
            self.colainstrucciones = cola
            print('>>> TDAs Recibiendo cola instrucciones')
            print()
            self.colainstrucciones.desplegar()
            print()
        except Exception as e:
            print('!!! Error en  asignarcolainstrucciones!!!\n',e)

        
   
    
    def crearTDAs(self, tiempo):
        try:
            print('>> TDAs Creando TDAs para T: ',tiempo)
            #Crear contenido
            self.crearContenidoDot()
            #Crear archivo
            self.creararchivoDot()
        except Exception as e:
            print('!!! Error en crearTDAs !!!')
    
    def crearContenidoDot(self):
        try:
            print('>> TDAs Creando archivo')
            self.dot_text += '''digraph ColaPacientes {
    graph [rankdir=LR];
    node [shape=box, style=filled, fillcolor=lightyellow, fontname="Helvetica"];

    
'''
            #Ciclos
            
            self.dot_text += '''
    n1 [label="H1-P2"];
    n2 [label="H2-P1"];
    n3 [label="H2-P2"];
    n4 [label="H3-P3"];
    n5 [label="H1-P4"];


'''

            self.dot_text += '''
    n1 -> n2;
    n2 -> n3;
    n3 -> n4;
    n4 -> n5;

'''
            #FIN Ciclos
            self.dot_text += '''
}
'''

        except Exception as e:
            print('!!! Error en  crearContenidoDot!!!\n',e)

    def creararchivoDot(self):
        try:
            # Guardar el archivo .dot
            with open("1_Grafica.dot", "w", encoding="utf-8") as f:
                f.write(self.dot_text)

            print(">> Archivo 1_Grafica.dot generado")

            #Crear Imagen
            try:
                os.system(f"dot -Tpng 1_Grafica.dot -o 1_TDAs.png")
                print(f">>Imagen 1_TDAs.png generada")
            except:
                print("!! Error al crear imagen ¡¡¡")
        
        except Exception as e:
            print('!!! Error en  creararchivoDot!!!',e)