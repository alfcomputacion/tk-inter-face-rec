import sqlite3
from datetime import datetime
import time


# fecha = datetime.now()

# time1 = fecha.strftime("%H:%M:%S")
# entrada = datetime.strptime(time1, "%H:%M:%S")
# print("hola", type(entrada))
# time_now = datetime.strptime("13:48:32", "%H:%M:%S")
# print("hello", type(time_now))

# if entrada > time_now:
#     print(str(entrada) + '  Salida')
# else:
#     print(str(time_now) + "  mas grande")

# fecha = input('Cual es la fecha?')
# print(fecha)
# print('esta es el tiempo de la fecha::::')
# print(fecha.time())
# 12569
con = sqlite3.connect('alumnos.db')
cursor = con.cursor()
con.execute("PRAGMA foreign_keys = ON")


def insertDataAlumno(matricula, nombre, apellidos, tel, t_nombre, t_apellidos):
    # params = (12569, 'arturo', 'padilla', 3235039491, 'Leticia', 'Rodriguez')
    params = (matricula, nombre, apellidos, tel, t_nombre, t_apellidos)

    con.execute('''
                INSERT INTO alumno(
                matricula, nombre,
                apellidos, tel,
                t_nombre, t_apellidos)
                VALUES
                (?, ?, ?, ?, ?, ?)
                ''', params)
    con.commit()
    print('Datos guardados')


# WORKING INSERT entrada tiene que ser un parametro
salida_entrada = 'SALIDA'


def insertDataAsistencia(matricula, fecha):
    # PONER ESTE CODIGO EN EL SENDTEXT
    # f = datetime.now()
    no_mseconds = fecha.split('.')[0]
    entrada = datetime.strptime(no_mseconds, "%Y-%m-%d %H:%M:%S")
##################### MODIFY#################################
    fecha = datetime.now()
    time1 = fecha.strftime("%H:%M:%S")
    entrada = datetime.strptime(time1, "%H:%M:%S")

    # print("hola", type(entrada))
    time_now = datetime.strptime("13:48:32", "%H:%M:%S")
    # print("hello", type(time_now))

    if entrada > time_now:
        salida_entrada = 'ENTRADA'
    else:
        salida_entrada = 'SALIDA'

#     print(str(entrada) + '  Salida')
# else:
#     print(str(time_now) + "  mas grande")
#################### END MODIFY################################

    # END PONER ESTE CODIGO EN EL SENDTEXT

    params = (entrada, salida_entrada, matricula)
    insert = 'INSERT INTO asistencia VALUES(?, ?, ?)'

    cursor.execute(insert, params)
    con.commit()
    print('Datos guardados exitosamente.')
    # WHERE fecha BETWEEN '2023-10-10' AND '2023-10-16'
    # fecha_inicio = '2023-10-10'
    # fecha_final = '2023-10-16'
    # matricula = 1569


def selectStatement(select='SELECT * FROM asistencia', params=None):
    selector = len(params)
    pass

    if params != None:
        params
        match selector:
            case 1:
                select = "SELECT fecha, entrada, mat_ID, tel FROM asistencia INNER JOIN alumno on alumno.matricula = asistencia.mat_ID WHERE mat_ID = ?"
            case 2:
                select = "SELECT fecha, entrada, mat_ID, tel FROM asistencia INNER JOIN alumno on alumno.matricula = asistencia.mat_ID WHERE DATE(fecha) BETWEEN ? AND ?"
            case 3:
                select = "SELECT fecha, entrada, mat_ID, nombre, apellidos, t_nombre, t_apellidos, tel FROM asistencia INNER JOIN alumno on alumno.matricula = asistencia.mat_ID WHERE mat_ID = ? AND DATE(fecha) BETWEEN ? AND ?"

    cursor.execute(select, params)
    results = cursor.fetchall()

    print(f"Matricula Nombre Apellidos")
    # entrada = ''
    for i, result in enumerate(results, 1):

        print(f"{result[0]} | {result[1]} | {result[2]}")

    return results
# print(results)


def selectAlumno():
    res = con.execute("SELECT matricula, nombre, apellidos From alumno")
    results = res.fetchall()
    print(results)
    print(f"Matricula Nombre Apellidos")
    for i, result in enumerate(results, 1):
        print(f"{result[0]} | {result[1]} | {result[2]}")
