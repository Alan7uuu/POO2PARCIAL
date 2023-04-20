from logica import *
import threading 
import tkinter as tk
x=logicap()
ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")
def registrar():
    x.guardarregistro(merca1.get(),pais.get())
def eliminar():
    x.eliminar_registro(id.get())
"""def consultacion():
    x.consultar(paa.get())"""

#VENTANA

note= ttk.Notebook(ventana)
note.pack()
registro = Frame(note,width=400,height=400)
registro.pack(expand=True,fill='both')
note.add(registro,text="Registro")

titulo=Label(registro,text="Ingrese Datos solicitados").pack()
titulo=Label(registro,text="Ingrese la Mercancia").pack()
merca1=StringVar()
merca2=Entry(registro,textvariable=merca1).pack()
titulo=Label(registro,text="Ingrese el Pais").pack()
pais=StringVar()
pais2=Entry(registro,textvariable=pais).pack()
Botonreg=Button(registro,text="Registrar",command=registrar).pack()
eliminar2 = Frame(note,width=400,height=400)
eliminar2.pack(expand=True,fill='both')
note.add(eliminar2,text="Eliminar")
titulo=Label(eliminar2,text="Ingrese el ID a eliminar").pack()
id=StringVar()
id2=Entry(eliminar2,textvariable=id).pack()
BotonEli=Button(eliminar2,text="Eliminar",command=eliminar).pack()

"""consultar = Frame(note,width=400,height=400)
consultar.pack(expand=True,fill='both')
note.add(consultar,text="consultar")
titulo=Label(consultar,text="Ingrese el Pais").pack()
paa=StringVar()
paa2=Entry(consultar,textvariable=paa).pack()
Botonconsu=Button(consultar,text="consultar",command=consultacion).pack()"""

ventana.mainloop()
