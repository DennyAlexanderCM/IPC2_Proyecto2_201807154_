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
        self.visited = False
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

    def imprimirLista2(self):
        aux = self.columnas.start_node
        while aux:
            txt=""
            pivote = aux.access
            while pivote:
                txt += str(pivote.data) +", "
                pivote = pivote.down
            print(txt)
            aux = aux.nref
    
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
        listaActiva = Lista_Nodos()
        listaNodos = Lista_Nodos()
        aux_1: Nodo_Contendor = A
        aux_1.visited = True
        #meta
        aux_2: Nodo_Contendor = B
        end = False
        
        if robot.getTipo() == "ChapinFighter":
            while (not end):
                success = False
                if aux_1.left != None and aux_1.left.data != "*" and aux_1.left.visited != True:
                    if isinstance(aux_1.left.data, int):
                        if robot.getCapacidad() > aux_1.left.data:
                            robot.setReduceCapacidad(aux_1.left.data)
                            f = self.valueF(aux_1.left, aux_2)
                            aux = aux_1.left
                            aux.value = f
                            success = True
                            listaNodos.add(aux)
                            
                    else:
                        f = self.valueF(aux_1.left, aux_2)
                        aux = aux_1.left
                        aux.value = f
                        success = True
                        listaNodos.add(aux)

                if aux_1.right != None and aux_1.right.data != "*" and aux_1.right.visited != True:
                    if isinstance(aux_1.right.data, int):
                        if robot.getCapacidad() > aux_1.right.data:
                            #robot.setReduceCapacidad(aux_1.right.data)
                            f = self.valueF(aux_1.right, aux_2)
                            aux = aux_1.right
                            aux.value = f
                            success = True
                            listaNodos.add(aux)
                    else:
                        f = self.valueF(aux_1.right, aux_2)
                        aux = aux_1.right
                        aux.value = f
                        success = True
                        listaNodos.add(aux)
                if aux_1.down != None and aux_1.down.data != "*" and aux_1.down.visited != True:
                    if isinstance(aux_1.down.data, int):
                        if robot.getCapacidad() > aux_1.down.data:
                            robot.setReduceCapacidad(aux_1.down.data)
                            f = self.valueF(aux_1.down, aux_2)
                            aux = aux_1.down
                            aux.value = f
                            success = True
                            listaNodos.add(aux)
                    else:
                        f = self.valueF(aux_1.down, aux_2)
                        aux = aux_1.down
                        aux.value = f
                        success = True
                        listaNodos.add(aux)
                if aux_1.up != None and aux_1.up.data != "*" and aux_1.up.visited != True:
                    if isinstance(aux_1.up.data, int):
                        if robot.getCapacidad() > aux_1.up.data:
                            robot.setReduceCapacidad(aux_1.up.data)
                            f = self.valueF(aux_1.up, aux_2)
                            aux = aux_1.up
                            aux.value = f
                            success = True
                            listaNodos.add(aux)
                    else:
                        f = self.valueF(aux_1.up, aux_2)
                        aux = aux_1.up
                        aux.value = f
                        success = True
                        listaNodos.add(aux)
                
                if success == False:
                    listaActiva.deleteFirst()
                    aux_1 = listaActiva.head.data
                else:
                    x = listaNodos.buscarMayor()
                    listaNodos.cleanlist()
                    x.visited = True
                    listaActiva.add(x)
                    aux_1 = x
                    print(x.value, aux_1.positionX, aux_1.positionY)
                if aux_1.value == 1:
                    A.visited = False
                    B.visited = False
                    print(robot.getCapacidad())
                    end = True
        else:
            while (not end):
                success = False
                if aux_1.left != None and aux_1.left.data != "*" and aux_1.left.visited != True:
                    if not (isinstance(aux_1.left.data, int)):
                        f = self.valueF(aux_1.left, aux_2)
                        aux = aux_1.left
                        aux.value = f
                        success = True
                        listaNodos.add(aux)

                if aux_1.right != None and aux_1.right.data != "*" and aux_1.right.visited != True:
                    if not(isinstance(aux_1.right.data, int)):
                        f = self.valueF(aux_1.right, aux_2)
                        aux = aux_1.right
                        aux.value = f
                        success = True
                        listaNodos.add(aux)
                if aux_1.down != None and aux_1.down.data != "*" and aux_1.down.visited != True:
                    if not(isinstance(aux_1.down.data, int)):
                        f = self.valueF(aux_1.down, aux_2)
                        aux = aux_1.down
                        aux.value = f
                        success = True
                        listaNodos.add(aux)
                if aux_1.up != None and aux_1.up.data != "*" and aux_1.up.visited != True:
                    if not(isinstance(aux_1.up.data, int)):
                        f = self.valueF(aux_1.up, aux_2)
                        aux = aux_1.up
                        aux.value = f
                        success = True
                        listaNodos.add(aux)
                
                if success == False:
                    listaActiva.deleteFirst()
                    aux_1 = listaActiva.head.data
                else:
                    x = listaNodos.buscarMayor()
                    listaNodos.cleanlist()
                    x.visited = True
                    listaActiva.add(x)
                    aux_1 = x
                    print(x.value, aux_1.positionX, aux_1.positionY)
                if aux_1.value == 1:
                    A.visited = False
                    B.visited = False
                    end = True
        

    def valueF(self, nodoA: Nodo_Contendor, nodoB: Nodo_Contendor):
        valor = 0
        a = np.abs(nodoA.positionX) - np.abs(nodoB.positionX)
        b = np.abs(nodoA.positionY) - np.abs(nodoB.positionY)
        a = np.abs(a)
        b = np.abs(b)
        valor = a+b
        return valor+1
    
    def createGraph(self):
        aux_1 = self.filas.start_node
        aux_2 = self.columnas.start_node
        s = Digraph('html_table')
        s.attr(label='Hola esta es una prueba\nHello')
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
                    if pivote.visited == True:
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
    
    def invertValue(self):
        aux = self.filas.start_node
        while aux:
            pivote:Nodo_Contendor = aux.access
            while pivote:
                pivote.visited = False
                pivote = pivote.right
            aux = aux.nref