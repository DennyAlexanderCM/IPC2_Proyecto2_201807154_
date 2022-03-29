from graphviz import Digraph, Graph
#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#CLASE DE LA LISTA ENLAZADA DE LOS PISOS
class Lista_Nodos:
    def __init__(self):
        self.head = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head

    #AGREGAMOS LOS DATOS AL INICIO
    def add(self , data):
        nodo = Node(data)
        if not self.emply():
            self.head = nodo
        else:
            nodo.next = self.head
            self.head = nodo
    
    def print(self):
        aux = self.head
        while aux:
            print(aux.data)
            aux = aux.next
        
    def cleanlist(self):
        self.head = None
    
    def buscarMayor(self):
        aux = self.head
        menor = aux
        while aux:
            if aux.next:
                if menor.data.value > aux.next.data.value:
                    menor = aux.next
            else:
                return menor.data
            aux = aux.next

    
    def deleteFirst(self):
        if self.head.next != None:
            self.head = self.head.next


"""lista = Lista_Nodos()
lista.add(1)
lista.add(2)
lista.add(3)
lista.add(4)
lista.deleteFirst()
lista.print()
lista.cleanlist()
lista.print()"""

