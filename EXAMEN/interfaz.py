from tkinter import*
from tkinter import ttk
from logica import*

ventana= Tk ()
ventana.title("GENERADOR DE MATRICULA")
ventana.geometry("500x300")
a=Label(ventana, text="Ingresar Nombre:").pack()
unoa=StringVar()
unoaa=Entry(ventana,textvariable=unoa).pack()
a=Label(ventana, text="Ingresar Apellido Paterno:").pack()
unob=StringVar()
unobb=Entry(ventana,textvariable=unob).pack()
a=Label(ventana, text="Ingresar Apelldo Materno:").pack()
unoc=StringVar()
unocc=Entry(ventana,textvariable=unoc).pack()
a=Label(ventana, text="Ingresar Año de Nacimiento:").pack()
unod=StringVar()
unodd=Entry(ventana,textvariable=unod).pack()
a=Label(ventana, text="Ingresar Carrera:").pack()
unoe=StringVar()
unoee=Entry(ventana,textvariable=unoe).pack()
#funciones
axc=logica()
def generar():
    axc.clave(unoa.get(),unob.get(),unoc.get(),unod.get(),unoe.get())
    

    
    

#Botones
BotonGuardar=Button(ventana,text="Generar",bg="black", fg="white",command=generar).pack()



ventana.mainloop()