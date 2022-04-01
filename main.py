from functions import*
from LinkedList import LinkedList, LinkedListRobots
from tkinter.filedialog import askopenfilename
from tkinter import Tk
def run():
    end = False
    selection = 0
    mapas = LinkedList()
    robots = LinkedListRobots()

    while not end:
        print("\n************ MENÚ ************\n 1. Cargar Configuración\n 2. Misiones\n 3. Salir")
        selection = pedirNumeroEntero()
        if selection == 1:
            #OBTENEMOS LA RUTA DEL ARCHIVO
            rute = askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
            #ANALIZAMOS LOS DATOS DEL ARCHIVO DE ENTRADA
            if rute != "":
                #ENLISTA LOS ROBOTS ENCONTRADOS EN EL ARCHIVO XML
                robots =  buscarRobots(rute)
                #ENLISTA LAS CIUDADES ENCONTRADAS EN EL ARCHIVO XML
                mapas = lecturaArchivoXml(rute)
            else:
                print("No se realizaron Cambios")

        elif selection == 2:
            #VERIFICA SI LA LISTA DE CONTIENE MAPAS   
            if mapas.length() != 0:
                robot = menuMision(robots)
                if robot:
                    ciudad = seleccionarMapa(mapas, robot.getTipo())
                    buscarRuta(ciudad, robot)
            else:
                print("Sin datos")
            
        elif selection == 3:
            print("Finalizando programa...")
            end = True
        else:
            print("Ingrese una opción correcta") 

#Método incial
if __name__ == '__main__':
    run()