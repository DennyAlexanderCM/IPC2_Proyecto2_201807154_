#CLASE NODO
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#CLASE DE LA LISTA ENLAZADA DE LOS PISOS
class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    #VERIFICAMOS SI LA LISTA ESTA VACÍA
    def emply(selft):
        return selft.head
    
    #AGREGAMOS LOS DATOS AL FINAL
    def append(selft, data):
        nodo = Node(data)
        if not selft.emply():
            selft.head = nodo
            selft.last = nodo
        else:
            selft.last.next = nodo
            selft.last = nodo
    
    #RETORNAR EL NÚMERO DE ELEMENTOS
    def length(selft):
        n = 0
        i = selft.head
        while i:
            i = i.next
            n+=1
        return n