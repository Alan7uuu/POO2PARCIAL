import tkinter
from tkinter import *
from Logica import *
a=Logica()
def inicio():
    a.iniciarsesion(corr.get(),con.get())
ventana= Tk ()
ventana.title("GENERADOR DE CONTRASEÑAS")
ventana.geometry("300x400")
ventana.configure(bg='#00FA9A')
Titulo=Label(ventana,text="Ingrese Datos Solicitados").pack()
Titulo=Label(ventana,text="Ingrese Correo Electronico").pack()
corr=StringVar()
corr2=Entry(ventana,textvariable=corr).pack()
Titulo=Label(ventana,text="Ingrese Contraseña").pack()
con=StringVar()
con2=Entry(ventana,show="**",textvariable=con).pack()
BotonIniciar=Button(ventana,text="Iniciar Secion",command=inicio).pack()


ventana.mainloop()