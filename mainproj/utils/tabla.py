import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime


def generar_tabla(inf_contacto, ventana_tabla):
    columns = ('fecha', 'entrada', 'matricula', 'nombre',
               'apellidos', 't_nombre', 't_apellidos', 'telefono')

    arbol = ttk.Treeview(ventana_tabla, columns=columns, show='headings')

    arbol.heading('fecha', text='FECHA')
    arbol.heading('entrada', text='ENTRADA/SALIDA')
    arbol.heading('matricula', text='MATRICULA')
    arbol.heading('nombre', text='NOMBRE')
    arbol.heading('apellidos', text='APELLIDOS')
    arbol.heading('t_nombre', text='NOMBRE TUTOR')
    arbol.heading('t_apellidos', text='APELLIDOS TUTOR')
    arbol.heading('telefono', text='TELEFONO')

    for contacto in inf_contacto:

        fecha = contacto[0].split('.')[0]
        entrada = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
        print("ENTRADA:")
        print(entrada)

        arbol.insert('', tk.END, value=contacto)

    def articulo_seleccionado(event):
        for articulo_seleccionado in arbol.selection():
            articulo = arbol.item(articulo_seleccionado)
            registro = articulo['values']
            showinfo(title='Information', message=registro)

    arbol.bind('<<arbolviewSelect>>', articulo_seleccionado)

    arbol.grid(row=0, column=0, sticky='nsew')
