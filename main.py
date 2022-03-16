from functions import*

def run():
    end = False
    selection = 0

    while not end:
        print("\n========= Menú =========\n 1. Cargar Configuración\n 2. Seleccionar piso y patrón\n 3. Pisos cargados\n 4. Salir")
        selection = pedirNumeroEntero()
        if selection == 1:
            #OBTENEMOS LA RUTA DEL ARCHIVO
            rute = leerArchivo()
            #ANALIZAMOS LOS DATOS DEL ARCHIVO DE ENTRADA
            lecturaArchivosXml(rute)

        elif selection == 2:
            pass
        elif selection == 3:
            pass
            
        elif selection == 4:
            print("Finalizando programa...")
            end = True
        else:
            print("Intente de nuevo") 

#Método incial
if __name__ == '__main__':
    run()