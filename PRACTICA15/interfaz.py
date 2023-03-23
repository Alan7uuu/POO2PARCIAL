from tkinter import*
from tkinter import ttk


ventana= Tk ()
ventana.title("CRUD USUARIOS")
ventana.geometry("500x300")
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
pestaña1=ttk.Frame(ventana2)
pestaña2=ttk.Frame(ventana2)
pestaña3=ttk.Frame(ventana2)
pestaña4=ttk.Frame(ventana2)
ventana2.add(pestaña1,text='Registro de Datos')
ventana2.add(pestaña2,text='Buscar Usuario')
ventana2.add(pestaña3,text='Consultar Usuario')
ventana2.add(pestaña4,text='Actualizar Usuario')
ventana.mainloop()