import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from mainproj.FaceRec import recognize_faces


def execute_btn():
    process = title_combobox.get()
    if process == 'Face Recognition':
        recognize_faces()


window = tk.Tk()
window.geometry("500x500")

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
