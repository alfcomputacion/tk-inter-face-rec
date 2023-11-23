import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from mainproj.FaceRec import reconociendo_caras
from mainproj.utils.tabla import generar_tabla
from mainproj.utils.creartablas import conectar_tabla
from tkcalendar import DateEntry
from mainproj.utils.sentenciasdb import selectSentencia

conectar_tabla()


def empezar_reconocimiento():
    reconociendo_caras()


def generar_reporte():
    tabla_ventana = Toplevel()
    tabla_ventana.title('Datos de alumnos')
    tabla_ventana.iconbitmap("favicon.ico")

    matricula = matricula_entry.get()
    inicio = desdeCal.get_date()
    final = hastaCal.get_date()

    parametros = (matricula, inicio, final)
    resultados = selectSentencia(params=parametros)

    generar_tabla(resultados, ventana_tabla=tabla_ventana)


ventana = tk.Tk()
ventana.geometry("2800x1500")
instrucciones = Label(
    ventana, text="""Para generar el reporte en un rango de fechas \n 
    solo selecciona el rango con dos fechas distintas.""")
instrucciones.pack()
# Menu starts here


def fechas():
    return desdeCal.get_date()


# MATRICULA
matricula_lab = Label(ventana, text="Matricula: ")
matricula_lab.pack()
matricula_entry = Entry(ventana, text="Matricula", font=40)
matricula_entry.pack()

# CALENDAR
desde_label = Label(ventana, text="SELECCIONA FECHA DESDE: ")
desde_label.pack()
desdeCal = DateEntry(ventana, selectmode='day')
desdeCal.pack()

hasta_label = Label(ventana, text="SELECCIONA FECHA HASTA: ")
hasta_label.pack()
hastaCal = DateEntry(ventana, selectmode='day')
hastaCal.pack()

ventana.title("*FACE REC PROJECT*")
ventana.iconbitmap("favicon.ico")


marco = tk.Frame(ventana)
marco.pack()

reportebtn = tk.Button(marco, text="Generar Reporte",
                       fg='white', bg='green', command=generar_reporte)

reportebtn.pack(side=LEFT, padx=10, pady=10)
carasbtn = tk.Button(marco, text="Reconocimiento Facial", fg='white', bg='blue',
                     command=empezar_reconocimiento)

carasbtn.pack(side=LEFT, padx=10, pady=10)
cerrarbtn = tk.Button(marco, text="Cerrar", fg='white', bg='red',
                      command=ventana.quit)

cerrarbtn.pack(side=LEFT, padx=10, pady=10)

my_img = ImageTk.PhotoImage(Image.open("maya-1-2.png"))

my_label = Label(image=my_img)
my_label.pack()

ventana.mainloop()
