import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from mainproj.FaceRec import recognize_faces
from mainproj.utils.sendText import read_file


def execute_btn():
    process = title_combobox.get()
    if process == 'Face Recognition':
        recognize_faces()
    elif process == 'Reportes':
<<<<<<< HEAD
        #open a report function
        print('Reports')
=======
        read_file("Lista_alumnos_4_10_2023_.json")
>>>>>>> 5fc4263aa4ec4807262a5fdbdaae9609a3cf35fd

def start_facerec():
    recognize_faces()

def start_reports():
    print('reports')

window = tk.Tk()
<<<<<<< HEAD
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
=======
window.geometry("600x500")
>>>>>>> 5fc4263aa4ec4807262a5fdbdaae9609a3cf35fd

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
