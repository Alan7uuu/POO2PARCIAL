
from tkinter import *
from tkinter import ttk
from logica import*
x=logica()
def arabigos_romanos():
    x.arabigo__romano(arabi.get())
def romanos_arabigos():
    x.romano__arabigo(roma.get())
ventana= Tk ()
ventana.title("Convertidor de Numeros")
ventana.geometry("300x400")
ventana.configure(bg='#00FA9A')
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
pestaña1=ttk.Frame(ventana2)
pestaña1=ttk.Notebook(ventana2)
pestaña1.pack(fill='both', expand='yes')
pestaña2=ttk.Frame(ventana2)
pestaña2=ttk.Notebook(ventana2)
pestaña2.pack(fill='both', expand='yes')
ventana2.add(pestaña2,text='Numeros Romanos')
ventana2.add(pestaña1,text='Numeros Arabigos')
Titulo=Label(pestaña1,text="Ingrese Datos Solicitados",fg="blue").pack()
Titulo=Label(pestaña1,text="Ingrese Numero desea convertir ").pack()
arabi=StringVar()
arabigo=Entry(pestaña1,textvariable=arabi).pack()
Titulo=Label(pestaña2,text="Ingrese Datos Solicitados",fg="red").pack()
Titulo=Label(pestaña2,text="Ingrese Numero desea convertir ").pack()
roma=StringVar()
romano=Entry(pestaña2,textvariable=roma).pack()

botonuno=Button(pestaña2,text="Convertir",bg="blue",command=romanos_arabigos).pack()
botondos=Button(pestaña1,text="Convertir",bg="red",command=arabigos_romanos).pack()



ventana.mainloop()