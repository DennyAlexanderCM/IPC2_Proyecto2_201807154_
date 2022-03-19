from xml.dom import minidom
from graphviz import Digraph, Graph
from ciudad import Ciudad
from LinkedList import LinkedList
from Robot import *

def pedirNumeroEntero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce una opción: "))
            correcto=True
        except ValueError:
            print('¡Error, introduce un numero entero!')
    return num  

def menuMision(mapas, robots):
    a = mapas.length()
    b = robots.length()

    end = False
    selection = 0

    while(not end):
        print("\n********** MISIONES **********\n 1. Rescate\n 2. Extraccón de recursos\n 3. Regresar")
        selection = pedirNumeroEntero()
        if selection == 1:
            if b != 0:
                aux = robots.head
                i = 1
                print("\n****** SELECCIONAR ROBOT ******")
                while aux:
                    robotType = aux.data.getTipo()
                    if robotType == "ChapinRescue":
                        print(" "+str(i) +". "+ aux.data.getNombre())
                        i += 1
                    aux = aux.next
            else:
                print("Sin robots disponibles")
            seleccion = pedirNumeroEntero()

        elif selection == 2:
            if b != 0:
                aux = robots.head
                i = 1
                print("\n****** SELECCIONAR ROBOT ******")
                while aux:
                    robotType = aux.data.getTipo()
                    if robotType == "ChapinFighter":
                        print(" "+str(i) +". "+ aux.data.getNombre())
                        i += 1
                    aux = aux.next
            else:
                print("Sin robots disponibles")
            seleccion = pedirNumeroEntero()
        elif selection == 3:
            end = True
        else:
            print("Ingrese una opción correcta")

def buscarRobots(data):
    #CREAMOS LISTA AUXILIAR
    listaRobots = LinkedList()
    doc = minidom.parse(data)
    rootNode = doc.documentElement
    #OBTENEMOS LOS OBJETOS ROBOTS DEL ARCHIVO XML
    robots = rootNode.getElementsByTagName("robot")
    #RECORREMOS LA LISTA
    for robot in robots:
        date = robot.getElementsByTagName("nombre")[0]
        robotName = date.firstChild.data
        robotType = date.getAttribute("tipo")
        if robotType == "ChapinFighter":
            capacidad = date.getAttribute("capacidad")
            aux = RobotChapinFighter(robotName, robotType, capacidad)
            listaRobots.append(aux)
        elif robotType == "ChapinRescue":
            aux = RobotChapinRescue(robotName, robotType)
            listaRobots.append(aux)
        else:
            print("Tipo de robot no reconocido: " + robotType)
    return listaRobots

def lecturaArchivosXml(data):
    listaCiudades = LinkedList()
    doc = minidom.parse(data)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    # LISTAMOS TODAS LAS CIUDADADES
    ciudades = rootNode.getElementsByTagName("ciudad")
    #RECORREMOS LA LISTA DE CIUDADES
    for ciudad in ciudades:
        #CREAMOS EL OBJETO CIUDAD QUE CONTRENDRA TODOS LOS DATOS DE CADA MAPA
        city = Ciudad()
        date = ciudad.getElementsByTagName("nombre")[0]
        #NOMBRE DE LA CIUDAD
        name = date.firstChild.data
        #FILAS
        filas = int(date.getAttribute("filas"))
        #COLUMNAS
        columnas = int(date.getAttribute("columnas"))
        #EDITAMOS LOS ELEMENTOS DE CADA CIUDAD
        #NOMBRE
        city.setName(name)
        #FILAS
        city.setFilas(filas)
        #COLUMNAS
        city.setColumnas(columnas)
        print(name, filas, columnas)

        leerFilas = ciudad.getElementsByTagName("fila")
        leerUnidadesMilitares = ciudad.getElementsByTagName("unidadMilitar")
        for elemento in leerFilas:
            countCol = 0
            numero = elemento.getAttribute("numero")
            elementosFila = elemento.firstChild.data
            for caracter in elementosFila:
                if caracter == "*":
                   print("Tipo: intr Fila: "+ numero + " columna: "+str(countCol))
                elif caracter == " ":
                    print("Tipo: tran Fila: "+ numero + " columna: "+str(countCol))
                elif caracter == "E":
                    print("Tipo: Entrada Fila: "+ numero + " columna: "+str(countCol))
                elif caracter == "C":
                   print("Tipo: Civil Fila: "+ numero + " columna: "+str(countCol))
                elif caracter == "R":
                    print("Tipo: Recurso Fila: "+ numero + " columna: "+str(countCol))
                countCol +=1

        for elemento in leerUnidadesMilitares:
            fila = elemento.getAttribute("fila")
            columna = elemento.getAttribute("columna") 
            vida = elemento.firstChild.data
            print(fila, columna, vida)
        listaCiudades.append(city)
    
    return listaCiudades

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