import json
import pywhatkit
import time
alumnos_list = []


def SendTxt(file):
    with open(file, 'r') as lista:
        alumnos_list = json.load(lista)
        # print(alumnos_list)

    for i in range(0, len(alumnos_list['Alumno'])):
        print(alumnos_list['Alumno'][i]['matricula'])

        number = str(alumnos_list['Alumno'][i]['tel_contacto'])
        nombre = alumnos_list['Alumno'][i]['nombre']
        apellido = alumnos_list['Alumno'][i]['apellidos']
        nombrecompleto = nombre + ' ' + apellido
        pywhatkit.sendwhatmsg_instantly(
            "+" + number, 'Hi, ' + nombrecompleto + ' was in today.', wait_time=5, close_time=5)

        time.sleep(5)


def read_file(file):
    with open(file, 'r') as lista:
        alumnos_list = json.load(lista)
    # print(alumnos_list)
    print('MENSAJES ENVIADOS EL DIA ' + file)
    for i in range(0, len(alumnos_list['Alumno'])):

        number = str(alumnos_list['Alumno'][i]['tel_contacto'])
        nombre = alumnos_list['Alumno'][i]['nombre']
        apellido = alumnos_list['Alumno'][i]['apellidos']
        nombrecompleto = nombre + ' ' + apellido

        print('Matricula: ' + alumnos_list['Alumno'][i]['matricula'])
        print('Nombre: ' + nombrecompleto)
        print('Tel: ' + number)
        print('matricula: ' + alumnos_list['Alumno'][i]['hora'] + '\n')
