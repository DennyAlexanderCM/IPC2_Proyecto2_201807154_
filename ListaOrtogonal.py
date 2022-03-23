#CABEZA PRINCIPAL
from sqlite3 import Date


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
        self.positionX = x
        self.positionY = y
        self.up = None
        self.down = None
        self.right = None
        self.left = None

class Lista_Ortogonal():
    def __init__(self):
        #LISTA DE ENCABEZADOS DEL EJE X
        self.filas = Lista_Encabezado()
        #LISTA DE ENCABEZADOS DEL EJE Y
        self.columnas = Lista_Encabezado()

    #MÉTODO PARA INGRESAR UN NUEVO NODO EN LA POSICION X Y Y
    def insert(self, pos_x, pos_y, data):
        #SE CREA EL NODO QUE CONTENDRA EL DATO
        nuevo = Nodo_Contendor(pos_x, pos_y, data)
        nodo_X = self.filas.getHead(pos_x)
        nodo_Y = self.columnas.getHead(pos_y)

        if nodo_X == None:
            nodo_X = Nodo_Head(pos_x)
            nodo_X.access = nuevo
            self.filas.insert_node(nodo_X)
        else:
            if nuevo.positionY < nodo_X.access.positionY:
                nuevo.right = nodo_X.access
                nodo_X.access.left = nuevo
                nodo_X.access = nuevo
            else:
                tmp : Nodo_Contendor = nodo_X.access
                while tmp:
                    if nuevo.positionY < tmp.positionY:
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

        if nodo_Y == None:
            nodo_Y = Nodo_Head(pos_y)
            nodo_Y.access = nuevo
            self.columnas.insert_node(nodo_Y)
        else:
            if nuevo.positionX < nodo_Y.access.positionX:
                nuevo.down = nodo_Y.access              
                nodo_Y.access.up = nuevo
                nodo_Y.acceso = nuevo
            else:
                tmp : Nodo_Contendor = nodo_Y.access
                while tmp:
                    if nuevo.positionX < tmp.positionX:
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
            pivote = aux.access
            while pivote:
                txt += str(pivote.data) +", "
                pivote = pivote.right
            print(txt)
            aux = aux.nref

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