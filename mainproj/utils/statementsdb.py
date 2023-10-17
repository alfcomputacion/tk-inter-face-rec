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
    con.execute('''
                INSERT INTO alumno(
                matricula, nombre,
                apellidos, tel,
                t_nombre, t_apellidos)
                VALUES
                (1569, 'jose', 'rosas', 3235039491, 'martha', 'sanchez')
                ''')
    con.commit()
    cursor.close()
    con.close()

# WORKING INSERT entrada tiene que ser un parametro
salida_entrada = 'entrada'

# nw = datetime.now()
# hrs = nw.hour
# mins = nw.minute
# secs = nw.second
# zero = datetime.timedelta(seconds = secs+mins*60+hrs*3600)
# st = nw - zero # this take me to 0 hours.
# time1 = st + datetime.timedelta(seconds=10*3600+30*60) # this gives 10:30 AM
# time1 = fecha.time()
# time2 = datetime.strptime('07:40:59', '%H::%M::%S').time()
# print(time1)
# print(time2)

# if time > time2:
#     salida_entrada = 'salida'
# print(salida_entrada)
def insertDataAsistencia():
    params = ('2023-10-07', salida_entrada, 1569)
    insert = 'INSERT INTO asistencia VALUES(?, ?, ?)'
    cursor.execute(insert, params)
    con.commit()
    # WHERE fecha BETWEEN '2023-10-10' AND '2023-10-16'
    fecha_inicio = '2023-10-10'
    fecha_final = '2023-10-16'
    matricula = 1569
    cursor.close()
    con.close()


def selectStatement(select='SELECT * FROM asistencia', params=''):

    # if select != 'x':
    #     # select = "SELECT * FROM asistencia"
    #     select_by_fecha = "SELECT fecha, entrada, mat_ID, tel FROM asistencia INNER JOIN alumno on alumno.matricula = asistencia.mat_ID WHERE fecha BETWEEN {fecha_inicio} AND {fecha_final}"
    #     select_by_matricula = "SELECT fecha, entrada, mat_ID, tel FROM asistencia INNER JOIN alumno on alumno.matricula = asistencia.mat_ID WHERE mat_ID = {matricula}"

    cursor.execute(select, params)
    results = cursor.fetchall()

    print(f"Matricula Nombre Apellidos")
    # entrada = ''
    for i, result in enumerate(results, 1):

        print(f"{result[0]} | {result[1]} | {result[2]}")
    cursor.close()
    con.close()
    return results
# print(results)

def selectAlumno():
    res = con.execute("SELECT matricula, nombre, apellidos From alumno")
    results = res.fetchall()
    print(results)
    print(f"Matricula Nombre Apellidos")
    for i, result in enumerate(results, 1):
        print(f"{result[0]} | {result[1]} | {result[2]}")
    cursor.close()
    con.close()



# selectStatement("SELECT fecha, entrada, mat_ID, tel FROM asistencia INNER JOIN alumno on alumno.matricula = asistencia.mat_ID WHERE fecha BETWEEN {fecha_inicio} AND {fecha_final}")
