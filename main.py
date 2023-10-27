import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from mainproj.FaceRec import recognize_faces
from mainproj.utils.sendText import read_file
from mainproj.utils.table import generate_table
from mainproj.utils.alumnoform import readandinsertData
from tkcalendar import DateEntry

import asyncio

from mainproj.utils.statementsdb import selectStatement, insertDataAlumno, insertDataAsistencia

# conexion BASE DE DATOS
con = sqlite3.connect('alumnos.db')
cursor = con.cursor()

fecha_inicio = '2023-10-01'
fecha_final = '2023-10-16'
params = (fecha_inicio, fecha_final)


con.execute("PRAGMA foreign_keys = ON")

contact_information = [(1234, 'Jose', 'Rosas', '13235039494'),
                       ('2321', 'John', 'Doe', '13235039494')]


def start_facerec():
    recognize_faces()


def start_reports():
    table_window = Toplevel()
    table_window.title('Datos de alumnos')
    table_window.iconbitmap("favicon.ico")

    matricula = matricula_entry.get()
    inicio = desdeCal.get_date()
    final = hastaCal.get_date()

    parametros = (matricula, inicio, final)
    results = selectStatement(params=parametros)

    generate_table(results, table_window=table_window)


window = tk.Tk()

window.geometry("800x600")
instrucciones = Label(
    window, text="Para generar el reporte en un rango de fechas \n solo selecciona el rango con dos fechas distintas.")
instrucciones.pack()
# Menu starts here


def fechas():
    return desdeCal.get_date()


# MATRICULA
matricula_lab = Label(window, text="Matricula: ")
matricula_lab.pack()

matricula_entry = Entry(window, text="Matricula", font=40)
matricula_entry.pack()
# CALENDAR
desde_label = Label(window, text="SELECCIONA FECHA DESDE: ")
desde_label.pack()

desdeCal = DateEntry(window, selectmode='day')
desdeCal.pack()

hasta_label = Label(window, text="SELECCIONA FECHA HASTA: ")

hasta_label.pack()
hastaCal = DateEntry(window, selectmode='day')
hastaCal.pack()

# MENU
menubar = Menu(window)
# file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='REPORTES', command=start_reports)
filemenu.add_command(label='Face Recognition', command=start_facerec)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
menubar.add_cascade(label='File', menu=filemenu)
# ends filemenu

window.config(menu=menubar)

window.geometry("600x500")

window.title("*FACE REC PROJECT*")
window.iconbitmap("favicon.ico")


frame = tk.Frame(window)
frame.pack()

button = tk.Button(frame, text="Generar Reporte", command=start_reports)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

my_img = ImageTk.PhotoImage(Image.open("maya-1-2.png"))
my_label = Label(image=my_img)
my_label.pack()
# insertDataAlumno(11111, "Brissa", "Gandarilla",
#  526562151452, "Senora Brissa", "Hernandez")
# insertDataAsistencia(11111)
# readandinsertData('Lista_alumnos_17_10_2023_.json')

window.mainloop()
