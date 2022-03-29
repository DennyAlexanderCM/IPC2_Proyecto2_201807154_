from ast import Return
from pickle import NONE
from xml.dom import minidom
from ciudad import Ciudad
from LinkedList import LinkedList, LinkedListRobots
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
def menuMision(robots: LinkedListRobots):
    #OBTENEMOS LA CANTIDAD DE OBJETOS EN LA LISTA
    b = robots.length()
    end = False

    while(not end):
        print("\n********** MISIONES **********\n 1. Rescate\n 2. Extraccón de recursos\n 3. Regresar")
        selection = pedirNumeroEntero()
        if selection == 1:
            if b != 0 and robots.ChapinRescue:
                aux = robots.head
                i = 0
                print("\n******* SELECCIONAR ROBOT *******\n>> ROBOTS DISPONIBLES")
                while aux:
                    robotType = aux.data.getTipo()
                    if robotType == "ChapinRescue":
                        i += 1
                        print("  "+str(i) +". "+ aux.data.getNombre())
                    aux = aux.next
                selection = pedirNumeroEntero()

                if selection <= i and selection > 0:
                    return robots.searchData("ChapinRescue", selection)
                else:
                    print("¡Ingrese una opción correcta!")#robotS = robots.searchData("ChapinRescue", robotSeleccionado)
            else:
                print("Sin robots disponibles")
                return None
            
        elif selection == 2:
            if b != 0 and robots.ChapinFighter:
                aux = robots.head
                i = 0
                print("\n******* SELECCIONAR ROBOT *******\n>> ROBOTS DISPONIBLES")
                while aux:
                    robotType = aux.data.getTipo()
                    if robotType == "ChapinFighter":
                        i += 1
                        print("  "+str(i) +". "+ aux.data.getNombre())
                    aux = aux.next
                selection = pedirNumeroEntero()
                if selection <= i and selection > 0:
                    return robots.searchData("ChapinFighter", selection)
                    
                else:
                    print("¡Ingrese una opción correcta!") 
            else:
                print("Sin robots disponibles")
                return None
        elif selection == 3:
            end = True
        else:
            print("Ingrese una opción correcta")

def seleccionarMapa(mapas, tipo):
    end = False
    while(not end):
        print("\n****** SELECCIONAR CIUDAD ******")
        #SE IMPRIMEN EL NOMBRE DE LOS MAPAS CARGADOS AL SISTEMA
        mapas.printDates()
        selection = pedirNumeroEntero()
        if mapas.length() >= selection and selection > 0:
            seleccionado = mapas.searchData2(selection)
            if tipo == "ChapinRescue":
                if seleccionado.unidadCivil != False:
                    end = True
                    return seleccionado
                else:
                    print("!Mapa sin unidadesciviles!")
                    end = True
                    return None
            elif tipo == "ChapinFighter":
                if seleccionado.recurso != False:
                    end = True
                    return seleccionado
                else:
                    print("!Mapa sin recursos disponibles!")
                    end = True
                    return None
        else:
            print("¡Ingrese una opción correcta!")

def buscarRuta(mapa, robot):
    #IMPRIME UNA LISTA CON LAS ENTRADAS DISPONIBLES
    ciudad:Lista_Ortogonal = mapa.mapa
    end = False
    A = None
    B = None
    
    if ciudad.entradas > 1:
        while(not end):
            print("\n>>> ENTRADAS DE: " + mapa.getName())
            ciudad.buscarEntradas()
            seleccionar = pedirNumeroEntero()
            if ciudad.entradas >= seleccionar and seleccionar > 0:
                #NOS DEVUELVE EL NODO QUE CONTINE LOS DATOS DE LA ENTRADA
                A = ciudad.buscarEntrada(seleccionar)
                end = True
            else:
                print("¡Ingrese una opción correcta!")
    elif ciudad.entradas == 1:
        #NOS DEVUELVE EL NODO QUE CONTINE LOS DATOS DE LA ENTRADA
        A = ciudad.buscarEntrada(1)
        print(">>Entrada EN: (" + str(A.positionX) + ", " + str(A.positionY) + ")")
    else:
        print("Sin entradas disponible")
    
    #BUSCAR LOS RECURSOS O LOS CIVILES DEL MAPA
    if robot.getTipo() == "ChapinFighter":
        if ciudad.recursos > 1:
            end = False
            while (not end):
                print("\n>>> RECURSOS DE: " + mapa.getName())
                ciudad.buscarRecursos()
                seleccionar = pedirNumeroEntero()
                if ciudad.recursos >= seleccionar and seleccionar > 0:
                   B = ciudad.buscarRecurso(seleccionar)
                   end = True
        else:
            B = ciudad.buscarRecurso(1)
    else:
        if ciudad.civiles > 1:
            end = False
            while (not end):
                print("\n>>> CIVILES EN: " + mapa.getName())
                ciudad.buscarUnidadCivil()
                seleccionar = pedirNumeroEntero()
                if ciudad.civiles >= seleccionar and seleccionar > 0:
                   B = ciudad.buscarCivil(seleccionar)
                   end = True
        else:
            B = ciudad.buscarCivil(1)
            
    ciudad.searchRute(A, B, robot)
    ciudad.createGraph()

def buscarRobots(data):
    #CREAMOS LISTA AUXILIAR
    listaRobots = LinkedListRobots()
    doc = minidom.parse(data)
    # Elemento raíz del documento
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
            listaRobots.ChapinFighter = True
            aux = RobotChapinFighter(robotName, robotType, int(capacidad))
            listaRobots.append(aux)
        elif robotType == "ChapinRescue":
            listaRobots.ChapinRescue = True
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
                    mapa.insert(int(countCol), int(numero), caracter)
                elif caracter == " ":
                    mapa.insert(int(countCol), int(numero), caracter)
                elif caracter == "E":
                    mapa.entradas += 1
                    mapa.insert(int(countCol), int(numero), caracter)
                elif caracter == "C":
                    city.setUnidadCivil(True)
                    mapa.civiles += 1
                    mapa.insert(int(countCol), int(numero), caracter)
                elif caracter == "R":
                    city.setRecurso(True)
                    mapa.recursos += 1
                    mapa.insert(int(countCol), int(numero), caracter)
                countCol +=1
        if len(leerUnidadesMilitares) > 0:
            
            for elemento in leerUnidadesMilitares:
                fila = elemento.getAttribute("fila")
                columna = elemento.getAttribute("columna") 
                vida = elemento.firstChild.data
                mapa.insert(int(columna), int(fila), int(vida))
                #print(fila, columna, vida)
        city.setMapa(mapa)
        listaCiudades.append(city)
    print("Datos Cargados Correctamente")
    return listaCiudades

