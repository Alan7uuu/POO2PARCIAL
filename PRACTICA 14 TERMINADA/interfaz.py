from tkinter import*
from tkinter import ttk
from logica import*

ventana= Tk ()
ventana.title("CAJA POPULAR DE LOS  USUARIOS")
ventana.geometry("500x300")
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
pestaña1=ttk.Frame(ventana2)
pestaña1=ttk.Notebook(ventana2)
pestaña1.pack(fill='both', expand='yes')
pestaña2=ttk.Frame(ventana2)
pestaña2=ttk.Notebook(ventana2)
pestaña2.pack(fill='both', expand='yes')
operacion1=ttk.Frame(pestaña2)
operacion2=ttk.Frame(pestaña2)
operacion3=ttk.Frame(pestaña2)
operacion4=ttk.Frame(pestaña2)
operacion5=ttk.Frame(pestaña2)
operacion6=ttk.Frame(pestaña1)
operacion7=ttk.Frame(pestaña1)


ventana2.add(pestaña2,text='Cuenta 1')
ventana2.add(pestaña1,text='Cuenta 2')
pestaña1.add(operacion6,text='Registro de datos')
pestaña1.add(operacion7,text='Consultar Saldo')
pestaña2.add(operacion5,text='Registro de datos')
pestaña2.add(operacion1,text='Consultar Saldo')
pestaña2.add(operacion2,text='Realizar Deposto')
pestaña2.add(operacion3,text='Realizar Retiro')
pestaña2.add(operacion4,text='Realizar transferencia')
# generar datos en registro
uno=Label(operacion5, text="BIENVENIDO  Rellene los siguientes datos", fg='purple').pack()
uno=Label(operacion5, text="NOº de Cuenta").pack()
unoaa=StringVar()
unoa=Entry(operacion5,textvariable=unoaa).pack()
uno=Label(operacion5, text="Titular:").pack()
unobb=StringVar()
unob=Entry(operacion5,textvariable=unobb).pack()
uno=Label(operacion5, text="Edad").pack()
unocc=StringVar()
unoc=Entry(operacion5,textvariable=unocc).pack()
uno=Label(operacion5,text="Saldo").pack()
unodd=StringVar()
unod=Entry(operacion5,textvariable=unodd).pack()
#INTERFAZ DE OPERACIONES
#operacion 1

#operacion 2
ops=Label(operacion2,text="Ingrese el NOº de cuenta:").pack()
consulta3=StringVar()
consulta33=Entry(operacion2,textvariable=consulta3).pack()
ops=Label(operacion2,text="Ingrese el la cantidad a depositar:").pack()
consulta4=StringVar()
consulta44=Entry(operacion2,textvariable=consulta4).pack()
#operacion 3
ops=Label(operacion3,text="Ingrese el NOº de cuenta:").pack()
consulta5=StringVar()
consulta55=Entry(operacion3,textvariable=consulta5).pack()
ops=Label(operacion3,text="Ingrese el nombre del titular:").pack()
consulta7=StringVar()
consulta77=Entry(operacion3,textvariable=consulta7).pack()
ops=Label(operacion3,text="Ingrese el la cantidad a retirar:").pack()
consulta6=StringVar()
consulta66=Entry(operacion3,textvariable=consulta6).pack()
#operacion 4
ops=Label(operacion4,text="Ingrese el NOº de cuenta:").pack()
consulta8=StringVar()
consulta88=Entry(operacion4,textvariable=consulta8).pack()
ops=Label(operacion4,text="Ingrese el la cantidad a transferir").pack()
consulta10=StringVar()
consulta1010=Entry(operacion4,textvariable=consulta10).pack()
#Registrar 2 cuenta
dos=Label(operacion6, text="BIENVENIDO  Rellene los siguientes datos", fg='purple').pack()
dos=Label(operacion6, text="NOº de Cuenta").pack()
dosaa=StringVar()
dosa=Entry(operacion6,textvariable=dosaa).pack()
dos=Label(operacion6, text="Titular:").pack()
dosbb=StringVar()
dosb=Entry(operacion6,textvariable=dosbb).pack()
dos=Label(operacion6, text="Edad").pack()
doscc=StringVar()
dosc=Entry(operacion6,textvariable=doscc).pack()
dos=Label(operacion6,text="Saldo").pack()
dosdd=StringVar()
dosd=Entry(operacion6,textvariable=dosdd).pack()
#lista guardar datos de registro


axc=logica()
def registro():
    axc.guardar(unoaa.get(),unobb.get(),unocc.get(),unodd.get()) 
def registro2():
    axc.guardar2(dosaa.get(),dosbb.get(),doscc.get(),dosdd.get()) 
# checar saldo
def consulta2():
    axc.consulta()
#deposito
def deposito():
    axc.depositar(consulta4.get())
#retiro
def retiro():
    axc.retirar( consulta6.get())
#transferencia
def transf():
    axc.transferencia(consulta8.get(),consulta10.get()),
def consultados():
    axc.consulta2()
#botones
botonregistro=Button(operacion5, text="Registrar", bg="black", fg="white", command=registro).pack()
botonregistro2=Button(operacion6, text="Registrar", bg="black", fg="white", command=registro2).pack()
botonconsulta=Button(operacion1, text="Consultar saldo", bg="black", fg="white", command=consulta2).pack()
botonconsulta2=Button(operacion7, text="Consultar saldo", bg="black", fg="white", command=consultados).pack()
botondeposito=Button(operacion2, text="Realizar deposito", bg="black", fg="white", command=deposito).pack()
botonderetiro=Button(operacion3, text="Realizar retiro", bg="black", fg="white", command=retiro).pack()
botondetransferencia=Button(operacion4, text="Realizar transferencia", bg="black", fg="white", command=transf).pack()
#ejecucion de la interfaz

ventana.mainloop()

















#def consulta():
#a=str(bnombre.get())
#b=pbombre.index(a)
