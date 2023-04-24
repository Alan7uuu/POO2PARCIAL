from tkinter import*
from logica import *
import tkinter as tk
x=logica()

def generar2():
    b=x.generar(tamaño.get(),mayusculas.get(),especiales.get())
    contraseña1.set(b)
   

def fortaleza():
    x.comprobar(tamaño.get(),mayusculas.get(),especiales.get())

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
botonuno=Button(ventana, text="GENERAR CONTRASEÑA", bg="pink",command=generar2).pack()
botondos=Button(ventana, text="Comprobar Fortaleza", bg="pink",command=fortaleza).pack()

tam=Label(ventana, text="Su contraseña es:").pack()
contraseña1=StringVar()
contraseña = tk.Entry(ventana ,width=30,textvariable=contraseña1)
contraseña.pack()



ventana.mainloop()
