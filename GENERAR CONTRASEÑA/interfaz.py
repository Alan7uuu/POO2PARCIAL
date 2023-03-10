from tkinter import*
from logica import *
x=logica()
def ejecucion():
    x.generarcontraseña(ta.get(), uwu.get())
ventana= Tk ()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("300x400")

tam=Label(ventana, text="Ingrese la Longitud:").pack()
ta=StringVar()
tama=Entry(ventana,textvariable=ta ).pack()
tam=Label(ventana, text="ingrese el numero de la opcion deseada").pack()
tam=Label(ventana, text="1.mayusculas").pack()
tam=Label(ventana, text="2.minusculas").pack()
tam=Label(ventana, text="3.numerico").pack()
tam=Label(ventana, text="4.especial").pack()
tam=Label(ventana, text="5.todos los anterirores").pack()
uwu=StringVar()
opciones=Entry(ventana,textvariable=uwu).pack()

botonuno=Button(ventana, text="GENERAR CONTRASEÑA", bg="pink", command=ejecucion).pack()#botondos=Button(ventana, text="Contraseña Especiales", bg="yellow").pack()

ventana.mainloop()
