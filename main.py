from functions import*
from LinkedList import LinkedList
from tkinter.filedialog import askopenfilename
from tkinter import Tk

def run():
    end = False
    selection = 0
    mapas = LinkedList()
    robots = LinkedList()

    while not end:
        print("\n************ MENÚ ************\n 1. Cargar Configuración\n 2. Misiones\n 3. Salir")
        selection = pedirNumeroEntero()
        if selection == 1:
            #OBTENEMOS LA RUTA DEL ARCHIVO
            rute = Tk()
            #obtenemos la direccion local del archivo
            rute = askopenfilename(title= "Abrir Archivo", filetypes=(("Xml","*.xml"),("Todos los archivos","*.*")))
            #ANALIZAMOS LOS DATOS DEL ARCHIVO DE ENTRADA
            if rute != "":
                robots =  buscarRobots(rute)
                mapas = lecturaArchivosXml(rute)
            else:
                print("No se realizaron Cambios")

        elif selection == 2:
            
            if mapas.length() != 0:
                menuMision(mapas, robots)
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