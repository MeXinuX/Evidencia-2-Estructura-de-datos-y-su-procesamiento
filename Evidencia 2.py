#################### IMPORTACION DE LIBRERIAS REQUERIDAS ####################

from ast import While
from curses.ascii import isspace

#Esta libreria la importamos para realizar validaciones
import re

#Esta libreria la importamos para realizar validacion de fecha posible al momento de hacer una reservacion
import datetime

#Esta libreria la importamos para la creacion de animaciones
import time

#Esta libreria la importamos para la creacion de animaciones
import sys

#Esta libreria la importamos para el uso de CSV
import os

#Esta libreria la importamos para el uso de CSV
import csv

#Esta LIbreria la Importamos para el manejo de excel
import pandas as pd

####!!! ESTA LIBRERIA NO VIENE POR DEFECTO EN PYTHON HAY QUE INSTALARLA !!! ####
from tqdm import tqdm #Esta libreria la importamos para la creacion de animaciones
from time import sleep #Esta libreria la importamos para la creacion de animaciones


#COLORES PARA LA IMPRESION DE TEXTO EN PANTALLA
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[35m'

turno = ""
turno_posible = {'M':'Matutino', 'V':'Vespertino', 'N':'Nocturno'}

#################### CREACION DE FUNCIONES PARA LAS ANIMACIONES ####################
def create_client_animation():#Animacion De Creacion de un Cliente
    numero = 100
    print(GREEN + "\n Registrando Nuevo Cliente")
    for i in tqdm(range(numero)):
        sleep(0.01)
    sleep(0)
    os.system('clear')

def exit_animation():#Animacion de cerrado de programa
    sys.stdout.write('\rSaliendo')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo.')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo..')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo...')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo....')
    time.sleep(0.2)
    sys.stdout.write(RED + '\rPrograma Cerrado!\n' + BLACK)

def search_animation():
    sys.stdout.write('\rBuscando Eventos En esa Fecha')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha.')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha..')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha...')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha....')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha    ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha.   ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha..  ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha... ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha....')
    time.sleep(0.3)
    sys.stdout.write('\r                                 \n')

def load_animation():#Animacion de carga de archivos
    sys.stdout.write('\rCargando')
    time.sleep(0.3)
    sys.stdout.write('\rCargando.')
    time.sleep(0.3)
    sys.stdout.write('\rCargando..')
    time.sleep(0.3)
    sys.stdout.write('\rCargando...')
    time.sleep(0.3)
    sys.stdout.write('\rCargando....')
    time.sleep(0.3)
    sys.stdout.write('\rCargando    ')
    time.sleep(0.3)
    sys.stdout.write('\rCargando.   ')
    time.sleep(0.3)
    sys.stdout.write('\rCargando..'  )
    time.sleep(0.3)
    sys.stdout.write('\rCargando... ')
    time.sleep(0.3)
    sys.stdout.write('\rCargando....')
    time.sleep(0.2)
    sys.stdout.write(GREEN + '\r¡Carga De Información Completada!\n' + BLACK)

def mostrar_reservaciones(fecha_consulta):
    prueba_lista =[]
    for clave,valores in reservaciones.items():
        if fecha_consulta == valores[0][0]:
            prueba_lista.append(valores)

    print('*' * 80)
    print("* FECHA\t\tTURNO\t\tCLIENTE\t\tID SALA\t\tNOMBRE DE SALA *")
    print('*' * 80)
    if  prueba_lista:
        for reserva in prueba_lista:
            print(f"{reserva[0][0]}\t\t{reserva[0][1]}\t\t{reserva[1]}\t\t{reserva[2]}\t\t{reserva[3]}")
    else:
        print("                 No hay reservaciones para esta fecha ")



clientes = {} #LLAVE: ID CLIENTE ,VALORES: NOMBRE DEL CLIENTE
salas = {} #LLAVE: ID DE LA SALA, VALORES: NOMBRE DE LA SALA, CUPO DE LA SALA
reservaciones ={} #LLAVE: FOLIO DE RESERVACION, VALORES: FECHA DE RESERVACION,TURNO,ID CLIENTE,ID SALA,NOMBRE DE LA SALA,CUPO

file_clientes = "Clientes.csv"
file_salas = "Salas.csv"
file_reservaciones = "Reservaciones.csv"


if (os.path.exists(file_clientes) and os.path.exists(file_salas)):
    os.system('clear')#LIMPIEZA DE PANTALLA
    #RECUPERACION DE DATOS DE ARCHIVO CSV DE CLIENTES
    with open('Clientes.csv', mode='r') as file_clientes:
        reader = csv.reader(file_clientes)
        next(reader, None)
        writer = csv.writer(file_clientes)
        clientes = {int(rows[0]):rows[1] for rows in reader}

    #RECUPERACION DE DATOS DE ARCHIVO CSV DE SALAS
    with open('Salas.csv', mode='r') as file_salas:
        reader = csv.reader(file_salas)
        next(reader, None)
        writer = csv.writer(file_salas)
        salas = {int(rows[0]):rows[2] for rows in reader}

    #RECUPERACION DE DATOS DE ARCHIVO CSV DE RESERVACIONES
    with open('Reservaciones.csv', mode='r') as file_reservaciones:
        reader = csv.reader(file_reservaciones)
        next(reader, None)
        writer = csv.writer(file_reservaciones)
        for rows in reader:
            reservaciones[int(rows[0])] = [(rows[1],rows[2]),int(rows[3]),int(rows[4]),rows[5]]
    print(reservaciones)
    print("Se Encontro Informacion Previa ")
    load_animation()
else:
    os.system('clear')
    print("Esta Es La Primera Ejecucion del Programa.")
while True:
    print(BLACK + """\n
     -----------Menú de opciones----------
    |  1) Reservaciones                    |
    |  2) Reportes                         |
    |  3) Registrar Una Sala               |
    |  4) Registrar Nuevo Cliente          |
    |  5) Salir                            |
     -------------------------------------""")
    option_menu = input("\nIngresa una opción del menú: ")

    if not option_menu in "12345":
        print(RED + "Opción no disponible, intenta de nuevo." + BLACK)
        os.system('clear')
        continue

    if option_menu == "5":
        os.system('clear')

        #CREACION DE ARCHIVO CSV PARA CLIENTES
        with open('Clientes.csv', 'w') as file_clientes:
            writer = csv.writer(file_clientes)
            writer.writerow(["ID CLIENTE","NOMBRE"])
            for clave,valor in clientes.items():
                writer.writerow([clave, valor])

        #CREACION DE ARCHIVO CSV PARA SALAS
        with open('Salas.csv', 'w') as file_salas:
            writer = csv.writer(file_salas)
            writer.writerow(["ID SALA","NOMBRE DE SALA","CUPO"])
            for clave,valor in salas.items():
                writer.writerow([clave, valor[0],valor[1]])

        #CREACION DE ARCHIVO CSV PARA RESERVACIONES
        with open('Reservaciones.csv', 'w') as file_reservaciones:
            writer = csv.writer(file_reservaciones)
            writer.writerow(["Folio Reservacion","Fecha Reservacion","Turno","ID Sala","ID Cliente","Nombre Del Evento"])
            for clave,valor in reservaciones.items():
                writer.writerow([clave, valor[0][0],valor[0][1],valor[1],valor[2],valor[3]])

        exit_animation()
        break

    if option_menu =="1":
        while True:
            print(BLACK + """\n
                ------------------Menú de opciones----------------
                |1) Registrar Nueva Reservacion.                    |
                |2) Cambiar Nombre De La Reservacion.               |
                |3) Consultar Disponibilidad De Sala Para Una Fecha.|
                |4) Salir                                           |
                --------------------------------------------------""")
            submenu = input("\nIngresa una opción del menú: ")

            if not submenu in "1234":
                print(RED + "Opción no disponible, intenta de nuevo." + BLACK)
                os.system('clear')
                continue

            if submenu =="4":
                os.system('clear')
                break

            if submenu =="1":
                if not salas:
                    print("No existe ninguna sala, favor de registrar una sala. \n")
                    continue

                while True:
                    numero_cliente = input("Ingrese su ID cliente:  ")
                    if numero_cliente == "":
                        print("Debe ingresar un ID \n")
                        continue

                    if (not re.match("^[0-9]*$", numero_cliente)):
                        print("El ID del cliente debe ser un número, intente de nuevo. \n")
                        continue

                    numero_cliente = int(numero_cliente)
                    if numero_cliente not in clientes.keys():
                        print("No se encontró su ID de cliente, favor de registrarse como cliente \n")
                        break

                    while True:
                        print(f"*SALAS DISPONIBLES*\nID SALA\t\tNOMBRE DE SALA\t\tCUPO")
                        #print(salas[salas.keys()])

                        for clave,valor in salas.items():
                            print(clave,"\t\t",valor[0],"\t\t",valor[1])

                        sala = input("Seleccione una sala:  ")

                        if sala == "":
                            print("Debe seleccionar una sala. \n")
                            continue

                        if(not re.match("^[0-9]*$",sala)):
                            print("El ID de la sala es un número, intente de nuevo. \n")
                            continue

                        sala = int(sala)

                        if sala not in salas.keys():
                            print("No hay una sala con ese ID. \n")
                            continue
                        break

                    while True:
                        fecha_reservacion = input("Ingrese la fecha deseada con el formato (dd/mm/aaaa): \n")
                        if fecha_reservacion == "":
                            print("Debe ingresar una fecha. \n")
                            continue

                        if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_reservacion)):
                            print("La fecha debe tener el formato(dd/mm/aaaa). \n")
                            continue

                        try:
                            fecha_reservacion = datetime.datetime.strptime(fecha_reservacion,"%d/%m/%Y").date()
                        except:
                            print("La fecha ingresada no es una fecha válida, intente de nuevo. \n")
                            continue

                        fecha_actual = (datetime.date.today())
                        limite_fecha = (fecha_reservacion - fecha_actual).days
                        if limite_fecha <=2:
                            print("Se necesitan más de 2 días de anticipación. \n")
                            continue
                        #mostrar_reservaciones(fecha_reservacion)
                        break

                    while True:
                        turno = input( """\n
                        ----------Turnos----------
                        (M)Matutino
                        (V)Vespertino
                        (N)Nocturno
                        --------------------------\nSeleccione un turno:  """).upper()

                        if turno == "":
                            print("Debe Seleccionar un turno. \n")
                            continue

                        if turno not in "MVN":
                            print("Debes seleccionar una opción disponible en el menú, intenta de nuevo. \n")
                            continue
                        if turno == "M":
                            turno="Matutino"
                        if turno == "V":
                            turno="Vespertino"
                        if turno == "N":
                            turno="Nocturno"
                        fecha_reservada = ""
                        turno_reservado = ""
                        for clave,valor in reservaciones.items():
                            if fecha_reservacion == valor[0][0] and turno == valor[0][1]:
                                fecha_reservada = valor[0][0]
                                turno_reservado = valor[0][1]
                        if fecha_reservacion == fecha_reservada and turno == turno_reservado:
                            print("Ya existe una reservación en ese turno, favor de ingresar otro turno. \n")
                            continue
                        break

                    while True:
                        nombre_evento = input("Ingrese el nombre del evento:  ").title()
                        if nombre_evento == "":
                            print("Debe ingresar un nombre del evento. \n")
                            continue
                        if nombre_evento.isspace():
                            print("Debe ingresar un nombre del evento. \n")
                            continue

                        folio_reservacion = max(reservaciones.keys(), default=0) + 1
                        reservaciones[folio_reservacion] = [(fecha_reservacion,turno),sala,numero_cliente,nombre_evento]
                        print("Folio Reservacion        Fecha Reservacion       Turno       ID Sala     ID Cliente      Nombre Del Evento")
                        print(folio_reservacion,"               ",fecha_reservacion,"           ",turno,"           ",sala,"            ",numero_cliente,"       ",nombre_evento)
                        break
                    break

            if submenu =="2":
                os.system('clear')
                while True:
                    if not reservaciones:
                        print(RED +"No Existe Ninguna Reservacion Favor de Realizar una." +BLACK)
                        break

                    folio = input("Ingrese El Folio De Reservacion: ")
                    if folio == "":
                        print(RED + "Debe Ingresar El Folio De Reservacion." + BLACK)
                        continue
                    if folio.isspace():
                        print(RED + "Debe Ingresar El Folio De Reservacion." + BLACK)
                        continue
                    if(not re.match("^[0-9]*$",folio)):
                        print(RED + "El Folio De Reservacion Debe Ser Un Numero." + BLACK)
                        continue
                    folio = int(folio)
                    if folio not in reservaciones.keys():
                        print(RED + "No Existe Una Reservacion Con ese Folio" + BLACK)
                        break

                    print("NOMBRE DEL EVENTO\n",reservaciones[folio][3])

                    while True:
                        nuevo_nombre = input("Ingrese El Nuevo Nombre De Su Evento: ").title()
                        if nuevo_nombre == "":
                            print(RED + "Debe Ingresar Un Nombre Del Evento." + BLACK)
                            continue
                        if nuevo_nombre.isspace():
                            print(RED + "Debe Ingresar Un Nombre Del Evento." + BLACK)
                            continue

                        nombre_antiguo = reservaciones[folio][3]
                        reservaciones[folio][3] = nuevo_nombre
                        print("Se modifico el nombre del evento.")
                        print(f"Nombre Anterior: {nombre_antiguo}\nNombre Nuevo: {nuevo_nombre}")
                        break
                    break

            if submenu =="3":
                if not salas:
                    print("No Existe Ninguna Sala.Por Favor Registra Una.")
                    break

                while True:
                    fecha_consulta = input('¿Qué fecha desea consultar?: ')
                    if fecha_consulta == "":
                        print("Debe Ingresar una Fecha.")
                        continue
                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print("La fecha debe tener el formato(dd/mm/aaaa)")
                        continue

                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print("La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo.")
                        continue

                    lista_encontrados = []
                    reservaciones_posibles = []

                    for clave,datos in reservaciones.items():
                        sala, fecha, turno = (datos[2], datos[0][0], datos[0][1])
                        if fecha == fecha_consulta:
                            lista_encontrados.append((sala, turno))

                    reservas_encontradas = set(lista_encontrados)

                    for sala in salas.keys():
                        for turno in turno_posible.values():
                            reservaciones_posibles.append((sala,turno))
                    combinaciones_reservas_posibles = set((reservaciones_posibles))

                    salas_turnos_posibles = set((combinaciones_reservas_posibles - reservas_encontradas))
                    print(f"Las salas disponibles para la {fecha_consulta.strftime('%d/%m/%Y')} son: \n")
                    print('ID SALA   TURNO')
                    for sala in salas_turnos_posibles:
                        print(f'{sala}')
                    break

    if option_menu == "2":
        os.system('clear')
        while True:
            print(BLACK + """\n
             ------------------Menú de opciones----------------
            |1) Mostrar Reservaciones.                        |
            |2) Exportar Reservaciones A Excel.               |
            |3) Salir.                                        |
             --------------------------------------------------""")
            submenu = input("\nIngresa una opción del menú: ")

            if submenu not in "123":
                print(RED + "Opción no disponible, intenta de nuevo." + BLACK)
                os.system('clear')
                continue

            if submenu == "3":
                break

            if submenu == "1":
                while True:
                    fecha_consulta = input('¿Qué fecha desea consultar?: ')
                    if fecha_consulta == "":
                        print(RED + "Debe Ingresar una Fecha." + BLACK)
                        continue
                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED + "La fecha debe tener el formato(dd/mm/aaaa)." + BLACK)
                        continue

                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo." + BLACK)
                        continue
                    search_animation()
                    mostrar_reservaciones(fecha_consulta)
                    break
            if submenu =="2":
                prueba_lista =[]

                while True:
                    fecha_consulta = input('¿Qué fecha desea consultar?: ')
                    if fecha_consulta == "":
                        print("Debe Ingresar una Fecha.")
                        continue
                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print("La fecha debe tener el formato(dd/mm/aaaa)")
                        continue

                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print("La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo.")
                        continue

                    for clave,valores in reservaciones.items():
                        if fecha_consulta == valores[0][0]:
                            prueba_lista.append(valores)

                    lista_para_excel = []
                    for valor in prueba_lista:
                        fecha = valor[0][0]
                        turno = valor[0][1]
                        id_sala = valor[1]
                        id_cliente = valor[2]
                        nombre_reserva = valor[3]
                        lista_para_excel.append((fecha,turno,id_sala,id_cliente,nombre_reserva))

                    print('*' *75)
                    print("FECHA\t\tTURNO\t\tCLIENTE\t\tID SALA\t\tNOMBRE DE SALA")
                    print('*' *75)
                    if  prueba_lista:
                        reservaciones_DataFrame = pd.DataFrame(lista_para_excel)
                        reservaciones_DataFrame.columns = ["Fecha", "Turno", "ID Sala", "ID Cliente", "Nombre del evento"]
                        reservaciones_excel = reservaciones_DataFrame.to_excel("REPORTES.xlsx")
                    else:
                        print("                 No hay reservaciones para exportar a excel en esa fecha ")
                    break

    if option_menu == "3":
        os.system('clear')
        while True:
            nombre_sala = input("Ingrese el nombre de la sala:  ").title()
            if nombre_sala == "":
                print(RED + "Debe Ingresar Un Nombre A La Sala. \n" + BLACK)
                continue

            if nombre_sala.isspace():
                print(RED + "Debe Ingresar Un Nombre A La Sala. \n" + BLACK)
                continue


            nombre_existente = "" #Preguntar como puede ser una forma mas pythonica
            for clave,valor in salas.items():
                if nombre_sala == valor[0]:
                    nombre_existente = valor[0]

            if nombre_sala == nombre_existente:
                print(RED + "Ya existe una sala con ese nombre, Registre otro Nombre" + BLACK)
                continue

            while True:
                cupo_sala = ""
                try:
                    cupo_sala = int(input("Ingrese el cupo de la sala:  "))
                except:
                    if cupo_sala == "":
                        print(RED + "Debe Ingresar El Cupo De La Sala \n" + BLACK)
                        continue
                    if cupo_sala.isspace():
                        print(RED + "Debe Ingresar El Cupo De La Sala \n" + BLACK)
                        continue
                    print(RED + "Solamente se aceptan números \n" + BLACK)
                    continue
                else:
                    id_sala = max(salas.keys(), default=0) + 1
                    salas[id_sala]= [nombre_sala,cupo_sala]
                    print("Nombre De La Sala: "+ GREEN , nombre_sala)
                    print(BLACK +"Id Sala: "+ GREEN , id_sala)
                    print(BLACK +"Cupo: "+ GREEN , cupo_sala)
                    break
            break

    if option_menu == "4":
        os.system('clear')
        while True:
            nombre_cliente = input("Ingrese su nombre: ").title()

            if nombre_cliente == "":#REVISAR ESPACIADO PARA EVITAR QUE EL USUARIO INGRESE NUMEROS Y PUEDA INGRESAR SOLO LETRAS
                print(RED + "El nombre No Puede Quedar Vacio. \n" + BLACK)
                continue

            if nombre_cliente.isspace():
                print(RED + "El nombre No Puede Quedar Vacio. \n" + BLACK)
                continue

            if (not re.match("^[a-zA-Z_ ]*$", nombre_cliente)):#Expresion Regular para validar que el usuario solamente ingrese palabras y no numeros con espacios
                print(RED + "El Nombre solo pueden ser Letras, Intente de Nuevo" + BLACK)
                continue
            else:
                id_cliente = max(clientes.keys(), default=0) + 1
                clientes[id_cliente] = nombre_cliente #EVITAR LA CONVERSION A STRING HASTA , MANDAR A IMPRIMIR
                create_client_animation()
                print(BLACK + "Nombre Del Cliente: "  + GREEN, nombre_cliente)
                print(BLACK + "ID cliente: " + GREEN ,id_cliente)
                break
