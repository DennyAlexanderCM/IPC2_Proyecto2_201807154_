from xml.dom import minidom
from graphviz import Digraph, Graph
from ciudad import Ciudad
from LinkedList import LinkedList
from Robot import *
from ListaOrtogonal import Lista_Ortogonal

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

#MENÚ SECUNDARIO
def menuMision(robots, mapas):
    #OBTENEMOS LA CANTIDAD DE OBJETOS EN LA LISTA
    b = robots.length()
    end = False

    while(not end):
        print("\n********** MISIONES **********\n 1. Rescate\n 2. Extraccón de recursos\n 3. Regresar")
        selection = pedirNumeroEntero()
        if selection == 1:
            if b != 0:
                aux = robots.head
                i = 0
                print("\n****** SELECCIONAR ROBOT ******")
                while aux:
                    robotType = aux.data.getTipo()
                    if robotType == "ChapinRescue":
                        i += 1
                        print(" "+str(i) +". "+ aux.data.getNombre())
                    aux = aux.next
                robotSeleccionado = pedirNumeroEntero()
                if robotSeleccionado <= i and robotSeleccionado > 0:
                    print(robotSeleccionado, i)
                    mapaCiudad = seleccionarMapa(mapas)
                else:
                    print("¡Ingrese una opción correcta!")#robotS = robots.searchData("ChapinRescue", robotSeleccionado)

            else:
                print("Sin robots disponibles")
            
        elif selection == 2:
            if b != 0:
                aux = robots.head
                i = 0
                print("\n****** SELECCIONAR ROBOT ******")
                while aux:
                    robotType = aux.data.getTipo()
                    if robotType == "ChapinFighter":
                        i += 1
                        print(" "+str(i) +". "+ aux.data.getNombre())
                    aux = aux.next
                robotSeleccionado = pedirNumeroEntero()
                if robotSeleccionado <= i and robotSeleccionado > 0:
                    mapaCiudad = seleccionarMapa(mapas)
                else:
                    print("¡Ingrese una opción correcta!") 
                #robotS = robots.searchData("ChapinFighter", robotSeleccionado)
            else:
                print("Sin robots disponibles")
            
        elif selection == 3:
            end = True
        else:
            print("Ingrese una opción correcta")

def seleccionarMapa(mapas):
    end = False
    while(not end):
        print("\n****** SELECCIONAR CIUDAD ******")
        mapas.printDates()
        selection = pedirNumeroEntero()
        if mapas.length() >= selection and selection > 0:
            seleccionado = mapas.searchData2(selection)
            end = True
            return seleccionado
        else:
            print("¡Ingrese una opción correcta!") 

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

def lecturaArchivoXml(data):
    listaCiudades = LinkedList()
    doc = minidom.parse(data)
    # Elemento raíz del documento
    rootNode = doc.documentElement
    # LISTAMOS TODAS LAS CIUDADADES
    ciudades = rootNode.getElementsByTagName("ciudad")
    #RECORREMOS LA LISTA DE CIUDADES
    for ciudad in ciudades:
        mapa = Lista_Ortogonal()
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
        #print(name, filas, columnas)

        leerFilas = ciudad.getElementsByTagName("fila")
        leerUnidadesMilitares = ciudad.getElementsByTagName("unidadMilitar")
        for elemento in leerFilas:
            countCol = 0
            numero = elemento.getAttribute("numero")
            elementosFila = elemento.firstChild.data
            for caracter in elementosFila:
                if caracter == "*":
                    mapa.insert(int(numero), int(countCol),caracter)
                elif caracter == " ":
                    mapa.insert(int(numero), int(countCol),caracter)
                elif caracter == "E":
                    mapa.insert(int(numero), int(countCol),caracter)
                elif caracter == "C":
                    mapa.insert(int(numero), int(countCol),caracter)
                elif caracter == "R":
                    mapa.insert(int(numero), int(countCol),caracter)
                countCol +=1

        for elemento in leerUnidadesMilitares:
            fila = elemento.getAttribute("fila")
            columna = elemento.getAttribute("columna") 
            vida = elemento.firstChild.data
            mapa.insert(int(fila), int(columna), int(vida))
            #print(fila, columna, vida)
        city.setMapa(mapa)
        mapa.imprimirLista2()
        listaCiudades.append(city)
    print("Datos Cargados Correctamente")
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