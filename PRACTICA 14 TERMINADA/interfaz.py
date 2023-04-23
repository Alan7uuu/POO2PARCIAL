from tkinter import*
from tkinter import ttk
from logica import*

ventana= Tk ()
ventana.title("CAJA POPULAR DE LOS  USUARIOS")
ventana.geometry("500x300")
ventana2=ttk.Notebook(ventana)
ventana2.pack(fill='both', expand='yes')
pestaña1=ttk.Frame(ventana2)
pestaña2=ttk.Frame(ventana2)
pestaña2=ttk.Notebook(ventana2)
pestaña2.pack(fill='both', expand='yes')
operacion1=ttk.Frame(pestaña2)
operacion2=ttk.Frame(pestaña2)
operacion3=ttk.Frame(pestaña2)
operacion4=ttk.Frame(pestaña2)
ventana2.add(pestaña1,text='Registro de Datos')
ventana2.add(pestaña2,text='Operaciones')
pestaña2.add(operacion1,text='Consultar Saldo')
pestaña2.add(operacion2,text='Realizar Deposto')
pestaña2.add(operacion3,text='Realizar Retiro')
pestaña2.add(operacion4,text='Realizar transferencia')
# generar datos en registro
uno=Label(pestaña1, text="BIENVENIDO  Rellene los siguientes datos", fg='purple').pack()
uno=Label(pestaña1, text="NOº de Cuenta").pack()
unoaa=StringVar()
unoa=Entry(pestaña1,textvariable=unoaa).pack()
uno=Label(pestaña1, text="Titular:").pack()
unobb=StringVar()
unob=Entry(pestaña1,textvariable=unobb).pack()
uno=Label(pestaña1, text="Edad").pack()
unocc=StringVar()
unoc=Entry(pestaña1,textvariable=unocc).pack()
uno=Label(pestaña1,text="Saldo").pack()
unodd=StringVar()
unod=Entry(pestaña1,textvariable=unodd).pack()
#INTERFAZ DE OPERACIONES
#operacion 1
ops=Label(operacion1,text="Ingrese el NOº de cuenta:").pack()
consulta1=StringVar()
consulta11=Entry(operacion1,textvariable=consulta1).pack()
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
#lista guardar datos de registro

axc=logica()
def registro():
    axc.guardar(unoaa.get(),unobb.get(),unocc.get(),unodd.get()) 
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
#botones
botonregistro=Button(pestaña1, text="Registrar", bg="black", fg="white", command=registro).pack()
botonconsulta=Button(operacion1, text="Consultar saldo", bg="black", fg="white", command=consulta2).pack()
botondeposito=Button(operacion2, text="Realizar deposito", bg="black", fg="white", command=deposito).pack()
botonderetiro=Button(operacion3, text="Realizar retiro", bg="black", fg="white", command=retiro).pack()
botondetransferencia=Button(operacion4, text="Realizar transferencia", bg="black", fg="white", command=transf).pack()
#ejecucion de la interfaz
ventana.mainloop()

















#def consulta():
#a=str(bnombre.get())
#b=pbombre.index(a)
