import json
import re
import os

def leer_archivo(string_de_archivo_json:str):
    '''
    La funcion lee un json y lo devuelve como una lista
    Recibe: una direccion de donde se encuentra el archivo
    Devuelve: el archivo transformado a lista
    '''
    lista= []
    with open(string_de_archivo_json, "r") as archivo:
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

    lista_exportar_CSV = []
    flag = 0
    while True:
        opcion = menu_principal_parcial()

        if opcion == "A":
            lista_exportar_CSV = listar_jugadores(lista_jugadores)
            flag = 1
        elif opcion == "B":
            lista_exportar_CSV = seleccionar_jugador(lista_jugadores)
            flag = 2
        elif opcion == "C":
            flag = 3
        elif opcion == "D":
            pass
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

def listar_jugadores(lista_jugadores:list):
    '''
    Muestra por consola la lista de jugadores en el formato pedido
    Recibe una lista de jugadores
    devuelve nada, solo imprime
    '''
    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]
    lista_retorno = []
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
            break
        else:
            print("Formato invalido o no existe el indice. Intente de nuevo.")

    
# Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
#  permite al usuario guardar las estadísticas de ese jugador en un archivo CSV.
#  El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,
#  puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido,
#  asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, 
# porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
    

parcial_app(leer_archivo(r"C:\Users\AdministraGod\Downloads\dt.json"))

