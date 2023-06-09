from logica import *
import threading
import tkinter as tk

conexion=logicap()

def entrada():
    conexion.registraentrada(nombrei.get(),areai.get(),noserie.get(),cantidadi.get(),fechaentrada.get())
def formato():
    return conexion.consulta_entradas()
def actualizar_entradas():
    for uno in entradas.get_children():
            entradas.delete(uno)
    datose=formato()
    for m, row in enumerate(datose):
            entradas.insert("", "end", text=str(m+1), values=row)
    if datose==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
def nuev3() :
    prueba5=threading.Thread(target=actualizar_entradas)
    prueba5.start()
def eliminacion():
    conexion.eliminar_entradas(id1.get())
def actuali():
    conexion.Actualizar_Entradas(i.get(),n.get(),a.get(),s.get(),c.get(),f.get())
def buscar():
    usuario1=conexion.buscarentrada(idd2.get())
    for usu in usuario1:
        cadena1="ID: "+str(usu[0])+" ,"+"Nombre: "+ str( usu[1])+", "+ "AreA: "+str(usu[2])+" ,"+"Noº de serie: "+ str(usu[3])+ ","+"Cantidad: "+str(usu[4])+", "+ "Fecha de Entrada: "+str(usu[5])
    if(usuario1):
      print(cadena1)
    else:
        messagebox.showinfo("usuario no encontrado","usuario no existe en la BD")
    textenc.insert(tk.INSERT,cadena1)
#ventana inventario 

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()


# registrar entrada

inventario = Frame(note,width=400,height=400)
inventario.pack(expand=True,fill='both')
inventario.configure(bg='#00BFBF')
note.add(inventario,text="registrar en el inventario")

texto=Label(inventario,text="nombre")
texto.place(x=20, y=20)
nombrei=StringVar()
nombre5=Entry(inventario,textvariable=nombrei)
nombre5.place(x=110, y=20)

texto=Label(inventario,text="area")
texto.place(x=20, y=60)
areai=StringVar()
areai1=Entry(inventario,textvariable=areai)
areai1.place(x=110, y=60)

texto=Label(inventario,text="no. de serie")
texto.place(x=20, y=100)
noserie=StringVar()
noserie1=Entry(inventario,textvariable=noserie)
noserie1.place(x=110, y=100)

texto=Label(inventario,text="cantidad")
texto.place(x=20, y=140)
cantidadi=StringVar()
cantidad1=Entry(inventario,textvariable=cantidadi)
cantidad1.place(x=110, y=140)

texto=Label(inventario,text="fecha entrada")
texto.place(x=20, y=180)
fechaentrada=StringVar()
fechae=Entry(inventario,textvariable=fechaentrada)
fechae.place(x=110, y=180)


boton=Button(inventario,text="agregar",command=entrada)
boton.place(x=150, y=220)

#consultar inventario
consulta = Frame(note,width=400,height=400)
consulta.pack(expand=True,fill='both')
consulta.configure(bg='#BFBF00')
note.add(consulta,text="Consultar Inventario")
col=('id','nombre', 'area','serie','cantidad','fecha')
entradas=ttk.Treeview(consulta,col=col ,show='headings' ,height=20)
entradas.heading('id', text='ID',anchor=CENTER)
entradas.heading('nombre',text='Nombre',anchor=CENTER)
entradas.heading('area',text='Area',anchor=CENTER)
entradas.heading('serie', text='Serie',anchor=CENTER)
entradas.heading('cantidad', text='Cantidad',anchor=CENTER)
entradas.heading('fecha', text='Fechaa',anchor=CENTER)
entradas.pack(padx=10, pady=10)
datose=formato()
for m, row in enumerate(datose):
    entradas.insert('', 'end' , text=str(m+1), values =row)
    if datose==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
botonconsulentradas=Button(consulta,text="consultar",command=nuev3).pack()
#eliminar entradas
elime = Frame(note,width=400,height=400)
elime.pack(expand=True,fill='both')
elime.configure(bg='#FFE4C4')
note.add(elime,text="Eliminar Entrada")
titulo=Label(elime,text="Ingrese ID a Eliminar").pack()
id1=StringVar()
id11=Entry(elime,textvariable=id1).pack()
Botonelimi=Button(elime,text="Eliminar Entrada",command=eliminacion).pack()
#Actualizar datos
actu = Frame(note,width=400,height=400)
actu.pack(expand=True,fill='both')
actu.configure(bg='#D3D3D3')
note.add(actu,text="Actualizar Entrada")
texto=Label(actu,text="ingrese los datos").pack()
texto=Label(actu,text="Id a Actualizar").pack()
i=StringVar()
ii=Entry(actu,textvariable=i).pack()
texto=Label(actu,text="Nombre a Actualizar").pack()
n=StringVar()
nn=Entry(actu,textvariable=n).pack()
texto=Label(actu,text="Area a Actualizar").pack()
a=StringVar()
aa=Entry(actu,textvariable=a).pack()
texto=Label(actu,text="Serie a Actualizar").pack()
s=StringVar()
ss=Entry(actu,textvariable=s).pack()
texto=Label(actu,text="Cantidad a Actualizar").pack()
c=StringVar()
cc=Entry(actu,textvariable=c).pack()
texto=Label(actu,text="Fecha a Actualizar").pack()
f=StringVar()
ff=Entry(actu,textvariable=f).pack()
botonactu=Button(actu,text="Actualizar",command=actuali).pack()

#Buscar Usuario
buscador = Frame(note,width=400,height=400)
buscador.pack(expand=True,fill='both')
buscador.configure(bg='#00FA9A')
note.add(buscador,text="Buscar Entrada")
texto=Label(buscador,text="ingrese el ID a buscar").pack()
idd2=StringVar()
idd=Entry(buscador,textvariable=idd2).pack()
textenc=tk.Text(buscador,height=5,width=100)
textenc.pack()
botonbuscar=Button(buscador,text="Buscador",command=buscar).pack()
ventana.mainloop()