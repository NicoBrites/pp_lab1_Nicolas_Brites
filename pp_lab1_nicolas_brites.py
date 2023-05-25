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
    E)Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,\n\
    ordenado por nombre de manera ascendente.\n\
    F)Permitir al usuario ingresar el nombre de un jugador y \n\
    mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.\n\
    G)Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n\
    H)Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n\
    I)Calcular y mostrar el jugador con el mayor porcentaje de asistencias totales.\n\
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
            calcular_y_mostrar_promedios(lista_jugadores)
        elif opcion == "F": 
            buscar_logros_por_nombre(lista_jugadores, salon_de_la_fama = True)
        elif opcion == "G": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "rebotes_totales")
        elif opcion == "H": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "porcentaje_tiros_de_campo")
        elif opcion == "I": 
            calcular_y_mostrar_jugador_mayor(lista_jugadores, "asistencias_totales")
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

def listar_jugadores(lista_jugadores:list) -> str:   #1
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


def seleccionar_jugador(lista_jugadores): #2
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
    
def guardar_estadisticas_csv(exportar_CSV): #3
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

def buscar_logros_por_nombre(lista_jugadores, salon_de_la_fama = False):# 4 y 6
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
                        Chris|MullinChristian|Laettner)",opcion.capitalize()
                        )and salon_de_la_fama == False:
                if opcion.capitalize() in jugadores["nombre"]:
                    imprimir_logros_jugadores(jugadores)
                    flag_break = 1
            elif re.match(r"(Michael|Jordan|Magic|Johnson|Larry|Bird|Scottie|Pippen|David|\
                        Robinson|Patrick|Ewing|Karl|Malone|John|Stockton|Clyde|Drexler|\
                        Chris|MullinChristian|Laettner)",opcion.capitalize()
                        )and salon_de_la_fama == True:
                if opcion.capitalize() in jugadores["nombre"]:
                    imprimir_logros_jugadores(jugadores, True)
                    flag_break = 1
            else:
                print("Escribio cualquier cosa, escriba el nombre de un jugador.")
                break

        if flag_break == 1:
            break 
                
def imprimir_logros_jugadores(jugadores, salon_de_la_fama = False): # 4 y 6
    '''
    imprime los logros del jugador pedido (ahorra 3 lineas de codigo por jugador al ejercicio anterior)
    Recibe una lista de jugadores
    devuelve Nada, solo imprime
    '''
    if salon_de_la_fama == False:
        retorno = "\n".join(jugadores["logros"])
    else:
        retorno = jugadores["logros"][-1]
    print(jugadores["nombre"])
    print(retorno)  


# Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente.   

def ivan_sort_diccionarios_promedios(lista:list , clave:str, clave_estadisticas:str, up = True , longitud_nombre = False): #SORT PARA EL 5 , 6 , 7 , 8 , 9
    '''
    El algoritmo de ordenamiento, recibe una lista y varios parametros y los ordena en orden dependiendo los parametros ingresado,
    Si es up seria de mayor a menor o viceversa y longitud es si cuenta los caracteres del string o no
    recibe una lista de cosas, una clave para saber que clave del dicc comparar, up es un bool y log nombre es un bool
    devuelve Nada, ( la funcion solo ordena )
    '''
    rango_a = len(lista)
    flag_swap = True


    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            if up == True and longitud_nombre == False and float(lista[indice_A][clave][clave_estadisticas]
               ) > float(lista[indice_A+1][clave][clave_estadisticas]) \
                or up == False and longitud_nombre == False and float(lista[indice_A][clave][clave_estadisticas]
                 ) < float(lista[indice_A+1][clave][clave_estadisticas]):
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True

            if up == True and longitud_nombre == True and len(lista[indice_A][clave][clave_estadisticas]
                ) > len(lista[indice_A+1][clave][clave_estadisticas])\
                or up == False and longitud_nombre == True and len(lista[indice_A][clave][clave_estadisticas]
                  ) < len(lista[indice_A+1][clave][clave_estadisticas]):
                lista[indice_A], lista[indice_A+1] = lista[indice_A+1], lista[indice_A]
                flag_swap = True

def calcular_y_mostrar_promedios(lista_jugadores): # 5

    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:]
    acumulador = 0

    for jugador in lista_para_trabajar:
        valor = jugador["estadisticas"]["promedio_puntos_por_partido"]
        acumulador += valor

    promedio = acumulador / len(lista_para_trabajar)

    print("El promedio total de puntos por partido de todo el Dream Team es : {0}".format(round(promedio,2)))
    print("Y el promedio de cada jugador ordenado de manera ascendente es:")

    ivan_sort_diccionarios_promedios(lista_para_trabajar,"estadisticas", "promedio_puntos_por_partido", True, False)

    for jugador in lista_para_trabajar:
        print("{0}  | Promedio de puntos por partido: {1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"]))
    


#Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
#Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
#Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.


def calcular_y_mostrar_jugador_mayor(lista_jugadores, clave_estadistica): # 7 , 8 y 9

    lista_para_trabajar = []
    lista_para_trabajar = lista_jugadores[:] 

    if clave_estadistica == "rebotes_totales":
        ivan_sort_diccionarios_promedios(lista_para_trabajar, "estadisticas", "rebotes_totales", False, False)

        print("{0} | Rebotes totales : {1}".format(lista_para_trabajar[0]["nombre"],
                                                    lista_para_trabajar[0]["estadisticas"]["rebotes_totales"]))
    elif clave_estadistica == "porcentaje_tiros_de_campo":
        ivan_sort_diccionarios_promedios(lista_para_trabajar, "estadisticas", "porcentaje_tiros_de_campo", False, False)

        print("{0} | Porcentaje de tiros de campo : {1}".format(lista_para_trabajar[0]["nombre"],
                                                    lista_para_trabajar[0]["estadisticas"]["porcentaje_tiros_de_campo"]))
    elif clave_estadistica == "asistencias_totales":
        ivan_sort_diccionarios_promedios(lista_para_trabajar, "estadisticas", "asistencias_totales", False, False)

        print("{0} | Asistencias totales : {1}".format(lista_para_trabajar[0]["nombre"],
                                                    lista_para_trabajar[0]["estadisticas"]["asistencias_totales"]))



parcial_app(leer_archivo(r"C:\Users\AdministraGod\Downloads\dt.json"))



