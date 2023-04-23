from tkinter import messagebox
#daTOS DE 2 CUENTRA PREDEFINIDOS
user=["777"]
saldoo=[]
#donde se almacenaran los datos del usuario
usuario=[]
saldo=[]
class logica:

    def __init__(self):
        self
    def guardar (self,unoaa,unobb,unocc,unodd):
        if unoaa =="" and unobb=="" and unocc=="" and unodd=="":
            messagebox.showinfo("Alerta","No se pueden reistrar campos vacios")
        elif unoaa =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Noº de cuenta")
        elif unoaa =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Titular")
        elif unoaa =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Edad")
        elif unoaa =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Saldo")
        else:
            uno=str(unoaa)
            dos=str(unobb)
            tres=str(unocc)
            cuatro=int(unodd)
            usuario.append(uno)
            usuario.append(dos)
            usuario.append(tres)
            usuario.append(saldo)
            saldo.append(cuatro)
            messagebox.showinfo("Usuario","Seguardo exitosamente el Usuario")
        
        
    def consulta (self):
            uno=sum(saldo)
            messagebox.showinfo("Consulta",f'su total disponible es: "{uno}"')
    
    
        
    def depositar(self, consulta4):
        sumar=int(consulta4)
        saldo.append(sumar)
        messagebox.showinfo( "Realizado","deposito realizado")
    def retirar(self,consulta6):
        restar=int(consulta6)
        neg=(-restar)
        saldo.append(neg)
        messagebox.showinfo("Realizado","se realizo el retiro")
        
    def transferencia (self,consulta8,consulta10):
        if (str(consulta8) == str("777")):
            aa=int(consulta10)
            bb=(-aa)
            saldo.append(bb)
            saldoo.append(aa)
            messagebox.showinfo("Realizado","deposito realizado")
        else:
            messagebox.showerror("Error","El numero de usuario no existe")