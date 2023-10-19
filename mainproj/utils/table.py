import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime


def generate_table(contact_information, table_window):
    columns = ('fecha', 'entrada', 'matricula', 'nombre',
               'apellidos', 't_nombre', 't_apellidos', 'telefono')

    tree = ttk.Treeview(table_window, columns=columns, show='headings')

    tree.heading('fecha', text='FECHA')
    tree.heading('entrada', text='ENTRADA/SALIDA')
    tree.heading('matricula', text='MATRICULA')
    tree.heading('nombre', text='MATRICULA')
    tree.heading('apellidos', text='MATRICULA')
    tree.heading('t_nombre', text='MATRICULA')
    tree.heading('t_apellidos', text='APELLIDOS')
    tree.heading('telefono', text='TELEFONO')

    for contact in contact_information:

        # time_now = datetime.strftime(contact[0], "%H:%M:%S")
        # print(time_now)
        # **********************************
        fecha = contact[0].split('.')[0]
        entrada = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
        print("ENTRADA:")
        print(entrada)
        # print("hola", type(entrada))
        # time_now = datetime.strptime("13:48:32", "%H:%M:%S")
        # print("hello", type(time_now))

        # if entrada > time_now:
        #     print(str(entrada) + '  Salida')
        # else:
        #     print(str(time_now) + "  mas grande")
# **********************************

        tree.insert('', tk.END, value=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            showinfo(title='Information', message=record)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')
