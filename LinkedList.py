#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head
    
    #AGREGAMOS LOS DATOS AL INICIO
    def add(selft , data):
        nodo = Node(data)
        if not selft.emply():
            selft.head = nodo
            selft.last = nodo
        else:
            nodo.next = selft.head
            selft.head = nodo      

    #AGREGAMOS LOS DATOS AL FINAL
    def append(self, data):
        nodo = Node(data)
        if not self.emply():
            self.head = nodo
            self.last = nodo
        else:
            self.last.next = nodo
            self.last = nodo
    
    #RETORNAR EL NÚMERO DE ELEMENTOS
    def length(self):
        n = 0
        i = self.head
        while i:
            i = i.next
            n+=1
        return n
    
    def printDates(self):
        aux = self.head
        i = 1
        while aux:
            print(" "+ str(i) +". "+ aux.data.getName())
            aux = aux.next
            i += 1
    
    def searchData(self, tipo, seleccion):
        aux = self.head
        i = 1
        while aux:
            if aux.data.getTipo() == tipo:
                if seleccion  == i:
                    #print(aux.data.getNombre())
                    return aux.data
                i += 1
            aux = aux.next
        
        
    def searchData2(self, posicion):
        aux = self.head
        i = 1
        while aux:
            if posicion  == i:
                #print(aux.data.getNombre())
                return aux.data
            i += 1
            aux = aux.next

class LinkedListRobots:
    def __init__(self):
        self.ChapinFighter = False
        self.ChapinRescue = False
        self.head = None
        self.last = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head  

    #AGREGAMOS LOS DATOS AL FINAL
    def append(self, data):
        nodo = Node(data)
        if not self.emply():
            self.head = nodo
            self.last = nodo
        else:
            self.last.next = nodo
            self.last = nodo
    
    #RETORNAR EL NÚMERO DE ELEMENTOS
    def length(self):
        n = 0
        i = self.head
        while i:
            i = i.next
            n+=1
        return n
    
    def printDates(self):
        aux = self.head
        i = 1
        while aux:
            print(" "+ str(i) +". "+ aux.data.getName())
            aux = aux.next
            i += 1
    
    def searchData(self, tipo, seleccion):
        aux = self.head
        i = 1
        while aux:
            if aux.data.getTipo() == tipo:
                if seleccion  == i:
                    print(aux.data.getNombre())
                    return aux.data
                i += 1
            aux = aux.next
