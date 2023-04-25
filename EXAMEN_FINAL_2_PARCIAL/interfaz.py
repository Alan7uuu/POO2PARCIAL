
from tkinter import *
from tkinter import ttk
from logica import*
import tkinter as tk
x=logica()
def enteros__romanos():
    x.arabigo__romano(arabigg.get())
    
def romanos_arabigos():
    x.romano__arabigo(roma.get())
ventana= Tk ()
ventana.title("Convertidor de Numeros")
ventana.geometry("600x600")
ventana.configure(bg='#00FA9A')
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
pestaña1=ttk.Frame(ventana2)
pestaña1=ttk.Notebook(ventana2)
pestaña1.pack(fill='both', expand='yes')
pestaña2=ttk.Frame(ventana2)
pestaña2=ttk.Notebook(ventana2)
pestaña2.pack(fill='both', expand='yes')
ventana2.add(pestaña2,text='Numeros Romanos a Arabigos')
ventana2.add(pestaña1,text='Numeros Arabigos a Romanos')
Titulo=Label(pestaña1,text="Ingrese Datos Solicitados",fg="blue").pack()
Titulo=Label(pestaña1,text="Ingrese Numero desea convertir ").pack()
arabigg=tk.IntVar()
arabigo=Entry(pestaña1,textvariable=arabigg).pack()
Titulo=Label(pestaña2,text="Ingrese Datos Solicitados",fg="red").pack()
Titulo=Label(pestaña2,text="Ingrese Numero desea convertir ").pack()
roma=tk.StringVar()
romano=Entry(pestaña2,textvariable=roma).pack()

botonuno=Button(pestaña2,text="Convertir",bg="blue",command=romanos_arabigos).pack()
botondos=Button(pestaña1,text="Convertir",bg="red",command=enteros__romanos).pack()



ventana.mainloop()