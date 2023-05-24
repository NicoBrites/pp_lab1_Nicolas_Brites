import json
import re
import os

def leer_archivo(string_de_archivo_json):
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


def parcial_app(lista_jugadores):
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

def listar_jugadores(lista_jugadores):

    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]
    lista_retorno = []
    indice = 0
    for jugadores in lista_para_trabajar:

        print("{0}) {1} - {2}".format(indice, jugadores["nombre"], jugadores["posicion"]))
        indice += 1


# Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas,
#  incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales,
#  promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, 
# robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

# def seleccionar_jugador(lista_jugadores):
     
#      while True:
#         opcion = input("Ingrese el indice del jugador (antes listado, de 1 a 13):") # QUE FORMATO ???
#         if re.match(r"[0-9]{2}$",opcion):
#             if opcion >= 0 or opcion < 14:
#                 for indice in range(lista_jugadores):
#                     if indice == opcion:
                        

#             else:
#                 print("No existe el indice ingresado")
#         else:
#             print("Formato invalido. Intente de nuevo.")

# parcial_app(leer_archivo(r"C:\Users\AdministraGod\Downloads\dt.json"))

