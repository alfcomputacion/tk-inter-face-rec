import sqlite3
from datetime import datetime
import time

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


def insertDatosAsistencia(matricula, fecha):
    # PONER ESTE CODIGO EN EL SENDTEXT
    # f = datetime.now()
    print(fecha)
    no_mseconds = fecha.split('.')[0]
    print(no_mseconds)
    entrada = datetime.strptime(no_mseconds, "%Y-%m-%d %H:%M:%S")

    checa_hora = entrada.time()

    hora_entrada = datetime.strptime("09:10:00", "%H:%M:%S")
    hora_entrada = hora_entrada.time()

    hora_salida = datetime.strptime("13:20:00", "%H:%M:%S")
    hora_salida = hora_salida.time()

    if checa_hora <= hora_entrada:
        salida_entrada = 'ENTRADA'
    elif checa_hora > hora_entrada and checa_hora < hora_salida:
        salida_entrada = 'RETARDO'
    elif checa_hora > hora_salida:
        salida_entrada = 'SALIDA'

    # if checa_hora > hora_entrada and checa_hora < hora_salida:
       # print(checa_hora, ' es mayor que  ', hora_entrada)
       # salida_entrada = 'SALIDA'
   # else:
      #  print(checa_hora, ' es MENOR que ', hora_entrada)

       # salida_entrada = 'ENTRADA'

    # END PONER ESTE CODIGO EN EL SENDTEXT

    params = (entrada, salida_entrada, matricula)
    insert = 'INSERT INTO asistencia VALUES(?, ?, ?)'

    cursor.execute(insert, params)
    con.commit()
    print('Datos guardados exitosamente.')


def selectSentencia(select='SELECT * FROM asistencia', params=None):
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
