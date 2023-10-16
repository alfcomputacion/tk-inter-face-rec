import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from mainproj.FaceRec import recognize_faces
from mainproj.utils.sendText import read_file
from mainproj.utils.table import generate_table

contact_information = [('1234', 'Jose', 'Rosas', '13235039494'),('2321', 'John', 'Doe', '13235039494')]
def execute_btn():
    process = title_combobox.get()
    if process == 'Face Recognition':
        recognize_faces()
    elif process == 'Reportes':

        #open a report function
        print('Reports')

        read_file("Lista_alumnos_4_10_2023_.json")

def start_facerec():
    recognize_faces()

def start_reports():
    table_window = Toplevel()
    table_window.title('Datos de alumnos')
    table_window.iconbitmap("favicon.ico")
    generate_table(contact_information, table_window=table_window )

window = tk.Tk()

window.geometry("500x500")
#Menu starts here
menubar = Menu(window)
#file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='REPORTES', command=start_reports)
filemenu.add_command(label='Face Recognition', command=start_facerec)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
menubar.add_cascade(label='File', menu=filemenu)
#ends filemenu

window.config(menu=menubar)

window.geometry("600x500")

window.title("*FACE REC PROJECT*")
window.iconbitmap("favicon.ico")


frame = tk.Frame(window)
frame.pack()

# user info
user_info_frame = tk.LabelFrame(frame, text="Selecciona una opcion")
user_info_frame.grid(row=0, column=0)


title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=[
                              "Reportes", "Face Recognition"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=0, column=2)

button = tk.Button(frame, text="Enter", command=execute_btn)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

my_img = ImageTk.PhotoImage(Image.open("maya-1-2.png"))
my_label = Label(image=my_img)
my_label.pack()

window.mainloop()
