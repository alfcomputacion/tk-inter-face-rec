import sqlite3
import os.path


def conectar_tabla():
    con = sqlite3.connect('../../alumnos.db')

    query = ('''
        CREATE TABLE IF NOT EXISTS alumno
            (matricula INTEGER PRIMARY KEY, 
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL, 
            tel TEXT NOT NULL,
            t_nombre TEXT NOT NULL, 
            t_apellidos TEXT NOT NULL);''')
    con.execute(query)

    query = ('''
        CREATE TABLE IF NOT EXISTS asistencia
            (fecha TEXT NOT NULL,
            entrada TEXT NOT NULL,
            mat_ID INTEGER NOT NULL,
            FOREIGN KEY(mat_ID) REFERENCES alumno(matricula)
            );''')
    con.execute(query)

    # cur.executescript("""
    #     BEGIN;
    #     CREATE TABLE alumno(firstname, lastname, age);
    #     CREATE TABLE book(title, author, published);
    #     CREATE TABLE publisher(name, address);
    #     COMMIT;
    # """)

    con.close()
