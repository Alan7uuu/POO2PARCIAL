from tkinter import*
ventana= Tk ()
ventana.title("FORMULARIO DE USUARIOS")
ventana.geometry("300x400")
uno=Label(ventana, text="BIENVENIDO  Rellene los siguientes datos").pack()
uno=Label(ventana, text="NOº de Cuenta").pack()
unoaa=StringVar()
unoa=Entry(ventana,textvariable=unoaa).pack()
uno=Label(ventana, text="Titular:").pack()
unobb=StringVar()
unob=Entry(ventana,textvariable=unobb).pack()
uno=Label(ventana, text="Edad").pack()
unocc=StringVar()
unoc=Entry(ventana,textvariable=unocc).pack()
uno=Label(ventana,text="Saldo").pack()
unodd=StringVar()
unod=Entry(ventana,textvariable=unodd).pack()
botonregistro=Button(ventana, text="Registrar", bg="black", fg="white").pack()
ventana.mainloop()
ventanados= Tk ()
ventanados.title("MENU DE CAJA POPULAR")
ventanados.geometry("300x400")

