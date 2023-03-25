from tkinter import*
from tkinter import ttk
import tkinter as tk
from controladorBD import* 
#1 presentamos los archivos
#2 crear un objeto de la clase controlador 
controlador=controladorBD()

#3.funcion para disparar el boton
def ejecutainsert():
    controlador.guardarusuario(varnom.get(), varcorr.get(), varcontra.get())
#ventana  inicial

ventana= Tk ()
ventana.title("CRUD USUARIOS")
ventana.geometry("500x400")
#ventana dentro de la ventana
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
#subpestañas generadas
pestaña1=ttk.Frame(ventana2)
pestaña2=ttk.Frame(ventana2)
pestaña3=ttk.Frame(ventana2)
pestaña4=ttk.Frame(ventana2)
#pestaña1 formulario usuarios
titulo=Label(pestaña1,text="Registro de usuarios",fg='blue',font=("modern",18)).pack()
varnom=tk.StringVar()
titulo=Label(pestaña1,text="Nombre",fg='red',font=("modern",14)).pack()
txtnom=Entry(pestaña1,textvariable=varnom).pack()
varcorr=tk.StringVar()
titulo=Label(pestaña1,text="Correo",fg='red',font=("modern",14)).pack()
txtccorr=Entry(pestaña1,textvariable=varcorr).pack()
varcontra=tk.StringVar()
titulo=Label(pestaña1,text="Contraseña",fg='red',font=("modern",14)).pack()
txtcontra=Entry(pestaña1,textvariable=varcontra).pack()
botonregistro=Button(pestaña1,text="Realizar Registro",command=ejecutainsert).pack()
#pestaña2
ventana2.add(pestaña1,text='Registro de Datos')
ventana2.add(pestaña2,text='Buscar Usuario')
ventana2.add(pestaña3,text='Consultar Usuario')
ventana2.add(pestaña4,text='Actualizar Usuario')

#ejecutor de ventana
ventana.mainloop()