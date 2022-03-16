from xml.dom import minidom
from graphviz import Digraph, Graph
from tkinter.filedialog import askopenfilename
from tkinter import Tk
from ciudad import Ciudad
from LinkedList import LinkedList

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('¡Error, introduce un numero entero!')
    return num  

def leerArchivo():
    root = Tk()
    #obtenemos la direccion local del archivo
    root = askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
    if root != "":
        return root
    return None

def lecturaArchivosXml(data):
    listCiudades = LinkedList()
    doc = minidom.parse(data)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    #listPisos.setName(rootNode.nodeName)
    # LISTAMOS TODAS LAS CIUDADADES
    ciudades = rootNode.getElementsByTagName("ciudad")
    #RECORREMOS LA LISTA DE CIUDADES
    for ciudad in ciudades:
        #CREAMOS EL OBJETO CIUDAD QUE CONTRENDRA TODOS LOS DATOS DE CADA MAPA
        city = Ciudad()
        #NOMBRE DE LA CIUDAD
        name = ciudad.getElementsByTagName("nombre")[0].firstChild.data
        #FILAS
        filas = ciudad.getElementsByTagName("nombre")[0].getAttribute("filas")
        #COLUMNAS
        columnas = ciudad.getElementsByTagName("nombre")[0].getAttribute("columnas")
        #EDITAMOS LOS ELEMENTOS DE CADA CIUDAD
        #NOMBRE
        city.setName(name)
        #FILAS
        city.setFilas(filas)
        #COLUMNAS
        city.setColumnas(columnas)
        print(name, filas, columnas)

        filas = ciudad.getElementsByTagName("fila")
        for i in filas:
            print(i.firstChild.data)
        
        listCiudades.append(city)

def graphPatter(tile, patern):
    position = 0
    txt = ""
    #filas
    R = int(tile.getR())
    #columnas
    C = int(tile.getC())
    s = Digraph('html_table' )
    for i in range(R):
        txt +="<TR>"
        for j in range(C):
            if patern[position] == "W":
                txt+='<TD bgcolor="white" border="2"></TD>'
            else:
                txt += '<TD bgcolor="black" border="2"></TD>'
            position +=1
        txt += "</TR>"

    s.node('tab', label='<<TABLE border="0" cellspacing="2" cellpadding="30">'+txt+'</TABLE>>', shape='box')
    s.render('Graficas/Pisos.gv',format='jpg', view=True)