from mainproj.utils.statementsdb import insertDataAlumno
import json


def readandinsertData(file):
    with open(file, 'r') as lista:
        alumnos_list = json.load(lista)
        # print(alumnos_list)

    for i in range(0, len(alumnos_list['Alumno'])):
        print(alumnos_list['Alumno'][i]['matricula'])

        matricula = alumnos_list['Alumno'][i]['matricula']
        nombre = alumnos_list['Alumno'][i]['nombre']
        apellido = alumnos_list['Alumno'][i]['apellidos']
        tel = str(alumnos_list['Alumno'][i]['tel_contacto'])
        t_nombre = alumnos_list['Alumno'][i]['t_nombre']
        t_apellidos = alumnos_list['Alumno'][i]['t_apellidos']

        insertDataAlumno(matricula, nombre, apellido,
                         tel, t_nombre, t_apellidos)
