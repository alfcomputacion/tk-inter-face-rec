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
    tree.heading('nombre', text='NOMBRE')
    tree.heading('apellidos', text='APELLIDOS')
    tree.heading('t_nombre', text='NOMBRE TUTOR')
    tree.heading('t_apellidos', text='APELLIDOS TUTOR')
    tree.heading('telefono', text='TELEFONO')

    for contact in contact_information:

        fecha = contact[0].split('.')[0]
        entrada = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
        print("ENTRADA:")
        print(entrada)

        tree.insert('', tk.END, value=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            showinfo(title='Information', message=record)

    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')
