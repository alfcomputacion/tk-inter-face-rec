import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def generate_table(contact_information, table_window):
    columns = ('matricula','nombre', 'apellidos', 'telefono' )

    tree = ttk.Treeview(table_window, columns=columns, show='headings')

    tree.heading('matricula', text='Matricula')
    tree.heading('nombre', text='Nombre')
    tree.heading('apellidos', text='Apellidos')
    tree.heading('telefono', text='Telefono')

    for contact in contact_information:
        tree.insert('', tk.END, value=contact)

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            showinfo(title='Information', message=','.join(record))
    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')