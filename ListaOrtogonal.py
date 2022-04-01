from ciudad import Ciudad
from pila import Lista_Nodos
from graphviz import Digraph, Graph
import numpy as np
#CABEZA PRINCIPAL
class Nodo_Head():
    def __init__(self, position):
        #DEFINE LA POSICION EN LA FILA O COLUMNA
        self.position= position
        self.nref = None
        self.pref = None
        #APUNTA A LOS NODOS DE LA MATRIZ
        self.access = None

#LISTA QUE CONTEDRA LOS ENCABEZADOS DE LA FILA Y COLUMNA DE LA MATRIZ
class Lista_Encabezado():
    def __init__(self):
        self.start_node: Nodo_Head = None
        self.final_node: Nodo_Head = None

    def insert_node(self, node: Nodo_Head):

        #SE VERIFICA SI LA LISTA ESTA VACÍA
        if self.start_node == None:
            self.start_node = node
            self.final_node = node
        #EN CASO CONTRARIO
        else:
            if node.position < self.start_node.position:   
                node.nref = self.start_node
                self.final_node.pref = node
                self.start_node = node
                
            elif node.position > self.final_node.position:
                self.final_node.nref = node
                node.pref = self.final_node
                self.final_node = node
            else:
                aux: Nodo_Head = self.start_node 
                while aux:
                    if (node.position < aux.position):
                        node.nref = aux
                        node.pref = aux.pref
                        aux.pref.nref = node
                        aux.pref = node
                        break
                    aux = aux.nref                

    def printHead(self):
        aux = self.start_node
        while aux:
            print(aux.position)
            aux = aux.nref

    def getHead(self, position):
        aux = self.start_node

        while aux:
            if position == aux.position:
                return aux
            aux = aux.nref
        return None

class Nodo_Contendor():
    def __init__(self, x, y, data):
        self.data = data
        self.value = 0
        self.anterior = None
        self.visited = False
        self.camino = False
        self.positionX = x
        self.positionY = y
        self.up = None
        self.down = None
        self.right = None
        self.left = None

class Lista_Ortogonal():
    def __init__(self):
        #LISTA DE ENCABEZADOS DEL EJE Y
        self.filas = Lista_Encabezado()
        #LISTA DE ENCABEZADOS DEL EJE X
        self.columnas = Lista_Encabezado()
        self.entradas = 0
        self.recursos = 0
        self.civiles = 0
    
    def restablecerDatos(self):
        aux = self.filas.start_node
        while aux:
            pivote:Nodo_Contendor = aux.access
            while pivote:
                pivote.anterior = None
                pivote.camino = False
                pivote.visited = False
                pivote = pivote.right
            aux = aux.nref

    #MÉTODO PARA INGRESAR UN NUEVO NODO EN LA POSICION X Y Y
    def insert(self, pos_x, pos_y, data):
        #SE CREA EL NODO QUE CONTENDRA EL DATO
        nuevo = Nodo_Contendor(pos_x, pos_y, data)
        nodo_X = self.columnas.getHead(pos_x)
        nodo_Y = self.filas.getHead(pos_y)

        if nodo_Y == None:
            nodo_Y = Nodo_Head(pos_y)
            nodo_Y.access = nuevo
            self.filas.insert_node(nodo_Y)
        else:
            if nuevo.positionX < nodo_Y.access.positionX:
                nuevo.right = nodo_Y.access
                nodo_Y.access.left = nuevo
                nodo_Y.access = nuevo
            else:
                tmp : Nodo_Contendor = nodo_Y.access
                while tmp:
                    if nuevo.positionX < tmp.positionX:
                        nuevo.right = tmp
                        nuevo.left = tmp.right
                        tmp.left.right = nuevo
                        tmp.left = nuevo
                        break
                    elif nuevo.positionX == tmp.positionX and nuevo.positionY == tmp.positionY:
                        """nuevo.left = tmp.left
                        tmp.left.right = nuevo
                        tmp.left = nuevo"""
                        tmp.left.right = nuevo
                        nuevo.left = tmp.left
                        nuevo.right = tmp.right
                        if tmp.right != None:
                            tmp.right.left = nuevo
                        break
                    else:
                        if tmp.right == None:
                            tmp.right = nuevo
                            nuevo.left = tmp
                            break
                    tmp = tmp.right

        if nodo_X == None:
            nodo_X = Nodo_Head(pos_x)
            nodo_X.access = nuevo
            self.columnas.insert_node(nodo_X)
        else:
            if nuevo.positionY < nodo_X.access.positionY:
                nuevo.down = nodo_X.access              
                nodo_X.access.up = nuevo
                nodo_X.acceso = nuevo
            else:
                tmp : Nodo_Contendor = nodo_X.access
                while tmp:
                    if nuevo.positionY < tmp.positionY:
                        nuevo.down = tmp
                        nuevo.up = tmp.up
                        tmp.up.down = nuevo
                        tmp.up = nuevo
                        break
                    elif nuevo.positionX == tmp.positionX and nuevo.positionY == tmp.positionY:
                        tmp.up.down = nuevo
                        nuevo.up = tmp.up
                        nuevo.down = tmp.down
                        if tmp.down != None:
                            tmp.down.up = nuevo
                        """nuevo.down = tmp
                        nuevo.up = tmp.up
                        tmp.up.down = nuevo
                        tmp.up = nuevo"""

                        break
                    else:
                        if tmp.down == None:
                            tmp.down = nuevo
                            nuevo.up = tmp
                            break
                    tmp = tmp.down 

    def imprimirLista(self):
        aux = self.filas.start_node
        while aux:
            txt=""
            pivote:Nodo_Contendor = aux.access
            while pivote:
                txt += str(pivote.data)+str(pivote.positionX)+str(pivote.positionY)
                pivote = pivote.right
            print(txt)
            aux = aux.nref
        print("fin")
    
    def copyList(self):
        lista = Lista_Ortogonal()
        aux = self.filas.start_node
        while aux:
            pivote:Nodo_Contendor = aux.access
            while pivote:
                lista.insert(pivote.data,pivote.positionX, pivote.positionY, pivote.data)
                pivote = pivote.right
            aux = aux.nref
        return lista
    
    def searchNode(self, positionX, positionY):
        aux_1 = self.filas.start_node
        aux_2 = self.columnas.start_node
        data = None

        while aux_1:
            if aux_1.position == positionY:
                pivote:Nodo_Contendor = aux_1.access
                while pivote:
                    if pivote.positionX == positionX:
                        return pivote
                    pivote = pivote.right
            aux_1 = aux_1.nref
        return None
    
    def buscarEntradas(self):
        aux_1 = self.filas.start_node
        i = 1
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                if pivote.data == "E":
                    print(" " + str(i) +". Posicion X: " + str(pivote.positionX) + " Posicion Y: " +  str(pivote.positionY))
                    i += 1
                pivote = pivote.right
            aux_1 = aux_1.nref
    
    def buscarUnidadCivil(self):
        aux_1 = self.filas.start_node
        i = 1
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                if pivote.data == "C":
                    print(" " + str(i) +". Posicion X: " + str(pivote.positionX) + " Posicion Y: " +  str(pivote.positionY))
                    i += 1
                pivote = pivote.right
            aux_1 = aux_1.nref
    
    def buscarRecursos(self):
        aux_1 = self.filas.start_node
        i = 1
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                if pivote.data == "R":
                    print(" " + str(i) +". Posicion X: " + str(pivote.positionX) + " Posicion Y: " +  str(pivote.positionY))
                    i += 1
                pivote = pivote.right
            aux_1 = aux_1.nref
    
    def buscarEntrada(self, posicion):
        aux_1 = self.filas.start_node
        i = 1
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                if pivote.data == "E":
                    if i == posicion:
                        return pivote
                    i += 1
                pivote = pivote.right
            aux_1 = aux_1.nref
        return None

    def buscarRecurso(self, posicion):
        aux_1 = self.filas.start_node
        i = 1
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                if pivote.data == "R":
                    if i == posicion:
                        return pivote
                    i += 1
                pivote = pivote.right
            aux_1 = aux_1.nref
        return None
    
    def buscarCivil(self, posicion):
        aux_1 = self.filas.start_node
        i = 1
        while aux_1:
            pivote:Nodo_Contendor = aux_1.access
            while pivote:
                if pivote.data == "C":
                    if i == posicion:
                        return pivote
                    i += 1
                pivote = pivote.right
            aux_1 = aux_1.nref
        return None
    


    def searchRute(self, A: Nodo_Contendor, B: Nodo_Contendor, robot):
        #Contendra la lista de nodos por analizar
        listaActiva = Lista_Nodos()
        #contendra la lista de nodos descartados
        listaCerrada = Lista_Nodos()
        aux_1: Nodo_Contendor = A
        aux_1.visited = True
        #meta
        end = False
        
        if robot.getTipo() == "ChapinFighter":
            vidaInicial = robot.getCapacidad()
            vidaFinal = robot.getCapacidad()
            while (not end):
                if aux_1.left != None and aux_1.left.data != "*" and aux_1.left.visited != True:
                    if not (isinstance(aux_1.left.data, int)):
                        h = self.valueF(aux_1.left, B)
                        aux = aux_1.left
                        aux.visited = True
                        aux.anterior = aux_1
                        aux.value = h
                        listaActiva.insert(aux)
                    else:
                        if vidaInicial > aux_1.left.data:
                            if vidaFinal > aux_1.left.data:
                                h = self.valueF(aux_1.left, B)
                                aux = aux_1.left
                                aux.visited = True
                                aux.anterior = aux_1
                                aux.value = h
                                vidaFinal = (vidaFinal - aux_1.left.data)
                                listaActiva.insert(aux)

                if aux_1.right != None and aux_1.right.data != "*" and aux_1.right.visited != True:
                    if not(isinstance(aux_1.right.data, int)):
                        h = self.valueF(aux_1.right, B)
                        aux = aux_1.right
                        aux.visited = True
                        aux.anterior = aux_1
                        aux.value = h
                        listaActiva.insert(aux)
                    else:
                        if vidaInicial > aux_1.right.data:
                            if vidaFinal > aux_1.right.data:
                                h = self.valueF(aux_1.right, B)
                                aux = aux_1.right
                                aux.visited = True
                                aux.anterior = aux_1
                                aux.value = h
                                vidaFinal = (vidaFinal - aux_1.right.data)
                                listaActiva.insert(aux)
                    
                if aux_1.down != None and aux_1.down.data != "*" and aux_1.down.visited != True:
                    if not(isinstance(aux_1.down.data, int)):
                        h = self.valueF(aux_1.down, B)
                        aux = aux_1.down
                        aux.visited = True
                        aux.anterior = aux_1
                        aux.value = h
                        success = True
                        listaActiva.insert(aux)
                    else:
                        if vidaInicial > aux_1.down.data:
                            if vidaFinal > aux_1.down.data:
                                h = self.valueF(aux_1.down, B)
                                aux = aux_1.down
                                aux.visited = True
                                aux.anterior = aux_1
                                aux.value = h
                                vidaFinal = (vidaFinal - aux_1.down.data)
                                listaActiva.insert(aux)
    
                if aux_1.up != None and aux_1.up.data != "*" and aux_1.up.visited != True:
                    if not(isinstance(aux_1.up.data, int)):
                        h = self.valueF(aux_1.up, B)
                        aux = aux_1.up
                        aux.visited = True
                        aux.anterior = aux_1
                        aux.value = h
                        success = True
                        listaActiva.insert(aux)
                    else:
                        if vidaInicial > aux_1.up.data:
                            if vidaFinal > aux_1.up.data:
                                h = self.valueF(aux_1.up, B)
                                aux = aux_1.up
                                aux.visited = True
                                aux.anterior = aux_1
                                aux.value = h
                                vidaFinal = (vidaFinal - aux_1.up.data)
                                listaActiva.insert(aux)

                listaActiva.deleteData(aux_1.value)
                if listaActiva.emply():
                    aux_1 = listaActiva.datoMenor()
                    if aux_1!= None:
                        if aux_1.positionX == B.positionX and aux_1.positionY == B.positionY:
                            A.visited = False
                            B.visited = False
                            end = True
                            aux_3:Nodo_Contendor = aux_1
                            while aux_3:
                                aux_3.camino = True
                                print(aux_3.positionX, aux_3.positionY)
                                aux_3 = aux_3.anterior
                            A.camino = False
                            B.camino = False
                    else:
                        print("Sin ruta encontrada")
                else:
                    print("Sin ruta encontrada")
                    break
        else:
            while (not end):
                success = False
                if aux_1 != None:
                    if aux_1.left != None and aux_1.left.data != "*" and aux_1.left.visited != True:
                        if not (isinstance(aux_1.left.data, int)):
                            h = self.valueF(aux_1.left, B)
                            aux = aux_1.left
                            aux.visited = True
                            aux.anterior = aux_1
                            aux.value = h
                            success = True
                            listaActiva.insert(aux)

                    if aux_1.right != None and aux_1.right.data != "*" and aux_1.right.visited != True:
                        if not(isinstance(aux_1.right.data, int)):
                            h = self.valueF(aux_1.right, B)
                            aux = aux_1.right
                            aux.visited = True
                            aux.anterior = aux_1
                            aux.value = h
                            success = True
                            listaActiva.insert(aux)
                    
                    if aux_1.down != None and aux_1.down.data != "*" and aux_1.down.visited != True:
                        if not(isinstance(aux_1.down.data, int)):
                            h = self.valueF(aux_1.down, B)
                            aux = aux_1.down
                            aux.visited = True
                            aux.anterior = aux_1
                            aux.value = h
                            success = True
                            listaActiva.insert(aux)
    
                    if aux_1.up != None and aux_1.up.data != "*" and aux_1.up.visited != True:
                        if not(isinstance(aux_1.up.data, int)):
                            h = self.valueF(aux_1.up, B)
                            aux = aux_1.up
                            aux.visited = True
                            aux.anterior = aux_1
                            aux.value = h
                            success = True
                            listaActiva.insert(aux)
                    listaActiva.deleteData(aux_1.value)
                    if listaActiva.emply():
                        aux_1 = listaActiva.datoMenor()
                        if aux_1!= None:
                            if aux_1.positionX == B.positionX and aux_1.positionY == B.positionY:
                                    A.visited = False
                                    B.visited = False
                                    end = True
                                    aux_3:Nodo_Contendor = aux_1
                                    while aux_3:
                                        aux_3.camino = True
                                        print(aux_3.positionX, aux_3.positionY)
                                        aux_3 = aux_3.anterior
                                    A.camino = False
                                    B.camino = False
                        else:
                            print("Sin ruta encontrada")
                    else:
                        print("Sin ruta encontrada")
                        break

    def valueF(self, nodoA: Nodo_Contendor, nodoB: Nodo_Contendor):
        valor = 0
        a = nodoA.positionX - nodoB.positionX
        b = nodoA.positionY - nodoB.positionY
        a = np.abs(a)
        b = np.abs(b)
        valor = a+b
        return valor
    
    def createGraph(self, mapa:Ciudad):
        aux_1 = self.filas.start_node
        aux_2 = self.columnas.start_node
        s = Digraph('html_table')
        s.attr(label='Ciudad: '+ mapa.getName(), fontsize='40 ')
        txt=""
        position = 0
        #imprimir envabezado X
        
        if aux_2 != None:
            txt +='<TR><TD bgcolor="white" border="1"></TD>'
            while aux_2:
                txt += '<TD bgcolor="white" border="1"><b><font point-size="20">' +str(aux_2.position)+'</font></b></TD>'
                aux_2 = aux_2.nref
            txt += '</TR>'


        if aux_1 != None:
            while aux_1:
                txt +='<TR><TD bgcolor="white" border="1"><b><font point-size="20">'+ str(aux_1.position) +'</font></b></TD>'
                pivote:Nodo_Contendor = aux_1.access
                while pivote:
                    if pivote.camino == True:
                        txt +='<TD bgcolor="yellow" border="1"></TD>'
                    elif pivote.data == "*":
                        txt +='<TD bgcolor="black" border="1"></TD>'
                    elif pivote.data == " ":
                        txt +='<TD bgcolor="white" border="1"></TD>'
                    elif pivote.data == "E":
                        txt +='<TD bgcolor="#357C3C" border="1"></TD>'
                    elif pivote.data == "C":
                        txt +='<TD bgcolor="#4D77FF" border="1"></TD>'
                    elif pivote.data == "R":
                        txt +='<TD bgcolor="#8FA69F" border="1"></TD>'
                    else:
                        txt +='<TD bgcolor="#890F0D" border="1"></TD>'
                    pivote = pivote.right
                aux_1 = aux_1.nref
                txt += '</TR>'
        s.node('tab', label='<<TABLE border="0" cellspacing="0" cellpadding="25">'+txt+'</TABLE>>', shape='none')
        s.render('Graficas/mapa.gv',format='jpg', view=True)
        print("Listo")
        self.restablecerDatos()
    
    def invertValue(self):
        aux = self.filas.start_node
        while aux:
            pivote:Nodo_Contendor = aux.access
            while pivote:
                pivote.visited = False
                pivote = pivote.right
            aux = aux.nref