from tkinter import*
from tkinter import ttk
import tkinter as tk
import threading
from controladorBD import* 
#1 presentamos los archivos
#2 crear un objeto de la clase controlador 
controlador=controladorBD()

#3.funcion para disparar el boton
def ejecutainsert():
    controlador.guardarusuario(varnom.get(), varcorr.get(), varcontra.get())
#disparar funcion en boton de busqueda
def ejecutaselectu():
    usuario= controlador.consultarusuario(varbus.get())
    for usu in usuario:
        cadena=str(usu[0])+" "+ usu[1]+" "+ usu[2]+" "+ str(usu[3])
    if(usuario):
       print(cadena)
    else:
        messagebox.showinfo("usuario no encontrado","usuario no existe en la BD")
    textenc.insert(tk.INSERT,cadena)
    
def tabla():
    return controlador.imprimir()
def actualizar_tabla():
    for uno in a.get_children():
            a.delete(uno)
    registros=tabla()
    for b, row in enumerate(registros):
            a.insert("", "end", text=str(b+1), values=row)
    if registros==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
def nuevo() :
    prueba1=threading.Thread(target=actualizar_tabla)
    prueba1.start()
def eli():
    controlador.eliminar_registro(eliminarid.get())

#ventana  inicial

ventana= Tk ()
ventana.title("CRUD USUARIOS")
ventana.geometry("700x500")
#ventana dentro de la ventana
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
#subpestañas generadas
pestaña1=ttk.Frame(ventana2)
pestaña2=ttk.Frame(ventana2)
pestaña3=ttk.Frame(ventana2)
pestaña4=ttk.Frame(ventana2)
pestaña5=ttk.Frame(ventana2)

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
#pestaña2 Buscar Usuario
titulo=Label(pestaña2,text="Buscar Usuario",fg='blue',font=("modern",18)).pack()
varbus=tk.StringVar()
idlib=Label(pestaña2,text="Identificador de usuario",fg='red',font=("modern",14)).pack()
txtbus=Entry(pestaña2,textvariable=varbus).pack()
botonbus=Button(pestaña2,text="Buscar",command=ejecutaselectu).pack()
subbus=Label(pestaña2,text="Encontrado:", fg='blue',font=("modern",15)).pack()
textenc=tk.Text(pestaña2,height=5,width=52)
textenc.pack()
#Pestaña 3
titulo=Label(pestaña3,text="Consulta de Usuarios",fg='blue',font=("modern",18)).pack()
Botoncons=Button(pestaña3,text="Actualizar Tabla", command=nuevo).pack()
#se generara el formato de la tabla con las columnas correspondientes
a=ttk.Treeview(pestaña3,height=50, col=('Nombre', 'Correo','Contraseña'))
a.heading('#0', text='ID',anchor=CENTER)
a.heading('#1', text='Nombre',anchor=CENTER)
a.heading('#2', text='Correo',anchor=CENTER)
a.heading('#3', text='Contraseña',anchor=CENTER)
a.pack(padx=4, pady=4)
registros=tabla()
for b, row in enumerate(registros):
    a.insert('', 'end' , text=str(b+1), values =row)
    # se usa un if para en caso de estar vacia arroje un mensaje de que la base esta vacia.
    if registros==[]:
        messagebox.showinfo("Error","La Base de Datos esta vacia.")
# pestaña 4
titulo=Label(pestaña4,text="Actualizar datos del usuario",fg='blue',font=("modern",22)).pack()
titulo=Label(pestaña4,text="Ingrese ID que desee cambiar",fg='red',font=("modern",18)).pack()
nuevoid=tk.StringVar()
nuevoid2=Entry(pestaña4,textvariable=nuevoid).pack()
titulo=Label(pestaña4,text="Ingrese nuevo Nombre",fg='red',font=("modern",18)).pack()
nuevonom=tk.StringVar()
nuevonom2=Entry(pestaña4,textvariable=nuevonom).pack()
titulo=Label(pestaña4,text="Ingrese Nuevo Correo",fg='red',font=("modern",18)).pack()
nuevocorr=tk.StringVar()
nuevocorr2=Entry(pestaña4,textvariable=nuevocorr).pack()
titulo=Label(pestaña4,text="Ingrese nueva contraseña",fg='red',font=("modern",18)).pack()
nuevacontra=tk.StringVar()
nuevacontra2=Entry(pestaña4,textvariable=nuevacontra).pack()
botoncambiar=Button(pestaña4,text="Realizar cambios").pack()
#PESTAÑA 5 ELIMINAR
titulo=Label(pestaña5,text="Eliminar datos del usuario",fg='blue',font=("modern",22)).pack()
titulo=Label(pestaña5,text="Ingrese ID que desee eliminar",fg='red',font=("modern",18)).pack()
eliminarid=tk.StringVar()
eliminarid2=Entry(pestaña5,textvariable=eliminarid).pack()
botoneliminar=Button(pestaña5,text="Eliminar",command=eli).pack()


#AÑADIR VENTAna
ventana2.add(pestaña1,text='Registro de Datos')
ventana2.add(pestaña2,text='Buscar Usuario')
ventana2.add(pestaña3,text='Consultar Usuario')
ventana2.add(pestaña4,text='Actualizar Usuario')
ventana2.add(pestaña5,text='Eliminar usuario')

#ejecutor de ventana
ventana.mainloop()