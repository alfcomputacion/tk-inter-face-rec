import sqlite3
from datetime import time, datetime


fecha = datetime.now()

# fecha = input('Cual es la fecha?')
# print(fecha)
print(time)

con = sqlite3.connect('alumnos.db')
cursor = con.cursor()
con.execute("PRAGMA foreign_keys = ON")


def insertDataAlumno():
    params = (12569, 'jose', 'rosas', 3235039491, 'martha', 'sanchez')

    con.execute('''
                INSERT INTO alumno(
                matricula, nombre,
                apellidos, tel,
                t_nombre, t_apellidos)
                VALUES
                (?, ?, ?, ?, ?, ?)
                ''', params)
    con.commit()


# WORKING INSERT entrada tiene que ser un parametro
salida_entrada = 'entrada'


def insertDataAsistencia():
    params = ('2023-10-07', salida_entrada, 1569)
    insert = 'INSERT INTO asistencia VALUES(?, ?, ?)'

    cursor.execute(insert, params)
    con.commit()
    # WHERE fecha BETWEEN '2023-10-10' AND '2023-10-16'
    fecha_inicio = '2023-10-10'
    fecha_final = '2023-10-16'
    matricula = 1569


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
