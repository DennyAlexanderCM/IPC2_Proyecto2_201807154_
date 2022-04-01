#CLASE NODO
from numpy import insert


class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

#CLASE DE LA LISTA ENLAZADA DE LOS PISOS
class Lista_Nodos:
    def __init__(self):
        self.head = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(self):
        return self.head

    #AGREGAMOS LOS DATOS AL INICIO
    def insert(self , data):
        nodo = Node(data)
        if not self.emply():
            self.head = nodo
        else:
            nodo.nref = self.head
            self.head.pref = nodo
            self.head = nodo
    
    def deleteData(self, data):
        if not(self.emply):
            print("The list has no element to delete")
            return 
        if self.head.nref is None:
            if self.head.data.value == data:
                self.head = None
            else:
                print("Item not found")
            return 

        if self.head.data.value == data:
            self.head = self.head.nref
            self.head.pref = None
            return

        n = self.head
        while n.nref is not None:
            if n.data.value == data:
                break;
            n = n.nref
        
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data.value == data:
                n.pref.nref = None
            else:
                print("Element not found")
    
    def print(self):
        aux = self.head
        while aux:
            print(aux.data)
            aux = aux.nref
        
    def cleanlist(self):
        self.head = None
    
    def datoMenor(self):
        aux = self.head
        menor = aux
        if self.emply:
            while aux:
                if aux.nref:
                    if menor.data.value > aux.nref.data.value:
                        menor = aux.nref
                else:
                    return menor.data
                aux = aux.nref
        else:
            return None


