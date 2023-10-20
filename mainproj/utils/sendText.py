import json
import pywhatkit
import time
from datetime import datetime
from mainproj.utils.statementsdb import insertDataAsistencia
alumnos_list = []


def SendTxt(file):
    with open(file, 'r') as lista:
        alumnos_list = json.load(lista)
        # print(alumnos_list)
# ***********************************************************************************************
    ahorita = datetime.now()
    checa_hora = ahorita.strftime('%H:%M:%S')
    entrada = datetime.strptime(checa_hora, "%H:%M:%S")

    checa_hora = entrada.time()

    hora_entrada = datetime.strptime("09:10:00", "%H:%M:%S")
    hora_entrada = hora_entrada.time()

    hora_salida = datetime.strptime("13:20:00", "%H:%M:%S")
    hora_salida = hora_salida.time()

    if checa_hora <= hora_entrada:
        salida_entrada = 'ENTRO'
    elif checa_hora > hora_entrada and checa_hora < hora_salida:
        salida_entrada = 'LLEGO TARDE'
    elif checa_hora > hora_salida:
        salida_entrada = 'SALIO'
# ***********************************************************************************************
    for i in range(0, len(alumnos_list['Alumno'])):
        print(alumnos_list['Alumno'][i]['matricula'])
        matricula = alumnos_list['Alumno'][i]['matricula']
        fecha = alumnos_list['Alumno'][i]['hora']
        number = str(alumnos_list['Alumno'][i]['tel_contacto'])
        nombre = alumnos_list['Alumno'][i]['nombre']
        apellido = alumnos_list['Alumno'][i]['apellidos']
        nombrecompleto = nombre + ' ' + apellido
        pywhatkit.sendwhatmsg_instantly(
            "+" + number, 'Buen día, el estudiante: ' + nombrecompleto + ' ' + salida_entrada + ' al CECyT 22 ', wait_time=5, close_time=5)
        insertDataAsistencia(matricula, fecha)
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
