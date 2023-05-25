import json
import re
import os

#NOMBRE:NICOLAS BRITES

def leer_archivo(string_de_archivo_json:str):
    '''
    La funcion lee un json y lo devuelve como una lista
    Recibe: una direccion de donde se encuentra el archivo
    Devuelve: el archivo transformado a lista
    '''
    lista= []
    with open(string_de_archivo_json, "r", encoding='utf-8') as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]
 
    return lista

def imprimir_menu():
    '''
    imprime el menu para este desafio
    recibe nada
    devuelve el menu impreso
    '''
    mensaje = "\
    A) Mostrar la lista de todos los jugadores del Dream Team.\n\
    B) Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas.\n\
    C) Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario\n\
    guardar las estadísticas de ese jugador en un archivo CSV.\n\
    D)Permitir al usuario buscar un jugador por su nombre y mostrar sus logros\n\
    Z) Salir de la aplicacion.\
    _____________________________________________________________________________________________________________________\
    "
    print(mensaje)

def menu_principal_parcial():
    '''
    La función imprime el menu y solicita al usuario que ingrese un numero, valida si es un valor valido o no
    Recibe: nada
    Devuelve: el numero ingresado pasado a int, o -1 si no puede
    '''
    imprimir_menu()
    opcion = input("Ingrese la opción deseada: ")
    if re.match(r"^[a-zA-Z]{1}$", opcion):
        return opcion.upper()
    else:
        return -1


def parcial_app(lista_jugadores:list):
    '''
    La función inicia la app
    Recibe: La lista de personajes
    Devuelve: la ejecucion del programa en si, eligiendo que hacer en el menu
    '''

    exportar_CSV = ""
    while True:
        opcion = menu_principal_parcial()

        if opcion == "A":
            listar_jugadores(lista_jugadores)
        elif opcion == "B":
            exportar_CSV = seleccionar_jugador(lista_jugadores)
        elif opcion == "C":
            guardar_estadisticas_csv(exportar_CSV)
        elif opcion == "D":
            buscar_logros_por_nombre(lista_jugadores)
        elif opcion == "E": 
            pass
        elif opcion == "Z":
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        clear_console()

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

# Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta

def listar_jugadores(lista_jugadores:list) -> str:
    '''
    Muestra por consola la lista de jugadores en el formato pedido
    Recibe una lista de jugadores
    devuelve un string con los datos para imprimir el csv
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]

    indice = 1
    for jugadores in lista_para_trabajar:

        print("{0}) {1} - {2}".format(indice, jugadores["nombre"], jugadores["posicion"]))
        indice += 1


# Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas,
#  incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales,
#  promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, 
# robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.


def seleccionar_jugador(lista_jugadores):
    '''
    Muestra las estadisticas completas de un jugador, el cual lo ingresa el usuario
    Recibe una lista de jugadores
    devuelve nada, solo imprime
    '''
    while True:
        opcion = input("Ingrese el indice del jugador (antes listado, de 0 a 13):") # QUE FORMATO ???
        if opcion.isdigit() and (int(opcion) >=0 and int(opcion) <13):

            for indice in range(len(lista_jugadores)):
                if indice+1 == int(opcion):
                    
                    mensaje = "\
    {0} \n\
    Temporadas : {1}\n\
    Puntos totales: {2}\n\
    Promedio puntos por partido: {3}\n\
    Rebotes totales: {4}\n\
    Promedio rebotes por partido: {5}\n\
    Asistencias totales: {6}\n\
    Promedio asistencias por partido: {7}\n\
    Robos totales: {8}\n\
    Bloqueos totales: {9}\n\
    Porcentaje_tiros_de_campo: {10}\n\
    Porcentaje_tiros_libres: {11}\n\
    Porcentaje_tiros_triples: {12}"
                    mensaje = mensaje.format(lista_jugadores[indice]["nombre"], lista_jugadores[indice]["estadisticas"]["temporadas"],
                                            lista_jugadores[indice]["estadisticas"]["puntos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_puntos_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["rebotes_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["asistencias_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["robos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["bloqueos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_libres"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_triples"], end= "\n") 
                    print(mensaje)
                    
                    imprimir_csv = "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}"
                    imprimir_csv = imprimir_csv.format(lista_jugadores[indice]["nombre"],lista_jugadores[indice]["posicion"],
                                            lista_jugadores[indice]["estadisticas"]["temporadas"],
                                            lista_jugadores[indice]["estadisticas"]["puntos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_puntos_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["rebotes_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_rebotes_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["asistencias_totales"],
                                            lista_jugadores[indice]["estadisticas"]["promedio_asistencias_por_partido"],
                                            lista_jugadores[indice]["estadisticas"]["robos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["bloqueos_totales"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_de_campo"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_libres"],
                                            lista_jugadores[indice]["estadisticas"]["porcentaje_tiros_triples"])

            break
        else:
            print("Formato invalido o no existe el indice. Intente de nuevo.")

    return imprimir_csv

    
# Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
#  permite al usuario guardar las estadísticas de ese jugador en un archivo CSV.
#  El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
#  puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido,
#  asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, 
# porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
    
def guardar_estadisticas_csv(exportar_CSV):
    '''
    Guarda la info pedida en formato csv
    Recibe un string con los datos para exportar
    devuelve Nada
    '''
    if exportar_CSV != "":
        exportar_CSV_separado = exportar_CSV.split(",")
        nombre_de_archivo = "{0}.csv".format(exportar_CSV_separado[0])

        # if len(exportar_CSV) != 0 or nombre_de_archivo != -1:
        #     nombre_de_archivo_csv_guardar = "./SEGUNDO PARCIAL/{0}".format(nombre_de_archivo)
        with open(nombre_de_archivo, "w") as archivo:
                archivo.write(exportar_CSV)
     
    else:
        print("Todavia seleccionaste un jugador en el punto anterior")    


# Permitir al usuario buscar un jugador por su nombre y mostrar sus logros,
#  como campeonatos de la NBA, participaciones en el All-Star y pertenencia
#  al Salón de la Fama del Baloncesto, etc.

def buscar_logros_por_nombre(lista_jugadores):
    '''
    Le pide al usuario ingresar un nombre y mostar los logros del jugador que pide
    Recibe una lista de jugadores
    devuelve Nada, solo imprime
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]
    flag_break = 0

    while True:
        opcion = input("Ingrese el nombre del jugador: ") # QUE FORMATO ???
        for jugadores in lista_para_trabajar:

            if re.match(r"(Michael|Jordan|Magic|Johnson|Larry|Bird|Scottie|Pippen|David|\
                        Robinson|Patrick|Ewing|Karl|Malone|John|Stockton|Clyde|Drexler|\
                        Chris|MullinChristian|Laettner)",opcion.capitalize()):
                if opcion.capitalize() in jugadores["nombre"]:
                    imprimir_logros_jugadores(jugadores)
                    flag_break = 1
            else:
                print("Escribio cualquier cosa, escriba el nombre de un jugador.")
                break

        if flag_break == 1:
            break 
                
def imprimir_logros_jugadores(jugadores):
    '''
    imprime los logros del jugador pedido (ahorra 3 lineas de codigo por jugador al ejercicio anterior)
    Recibe una lista de jugadores
    devuelve Nada, solo imprime
    '''
    retorno = "\n".join(jugadores["logros"])
    print(jugadores["nombre"])
    print(retorno)  

# Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.   



parcial_app(leer_archivo(r"C:\Users\AdministraGod\Downloads\dt.json"))

