from tkinter import*
from logica import *
import tkinter as tk
x=logica()
def generar():
    alan=x.generar(tamaño.get(),mayusculas.get(),especiales.get())
    
ventana= Tk ()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("300x400")

tam=Label(ventana, text="Ingrese la Longitud:").pack()
tamaño= tk.StringVar()
tamaño.set('8')
tamaño1=tk.Entry(ventana,textvariable=tamaño).pack()
tam=Label(ventana, text="Tendra caracteres especiales:").pack()
especiales=StringVar()
especiales2=Entry(ventana,textvariable=especiales).pack()
tam=Label(ventana, text="Contendra mayusculas:").pack()
mayusculas=StringVar()
mayusculas2=Entry(ventana,textvariable=mayusculas).pack()
tam=Label(ventana, text="Su contraseña es:").pack()
contraseña1=tk.StringVar
contraseña = tk.Entry(ventana ,width=30,textvariable=contraseña1)
contraseña.configure(text=generar)
contraseña.pack()
botonuno=Button(ventana, text="GENERAR CONTRASEÑA", bg="pink",command=generar).pack()

ventana.mainloop()
