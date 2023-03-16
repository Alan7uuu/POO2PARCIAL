from tkinter import messagebox
#daTOS DE 2 CUENTRA PREDEFINIDOS
user=["4321"]
saldoo=[]
#donde se almacenaran los datos del usuario
usuario=[]
saldo=[]
class logica:

    def __init__(self):
        self
    def guardar (self,unoaa,unobb,unocc,unodd):
        uno=str(unoaa)
        dos=str(unobb)
        tres=str(unocc)
        cuatro=int(unodd)
        usuario.append(uno)
        usuario.append(dos)
        usuario.append(tres)
        usuario.append(saldo)
        saldo.append(cuatro)
#crear una consulta 
        
        
    def consulta (self):
        uno=sum(saldo)
        messagebox.showinfo(f'su total disponible es: "{uno}"')
        
    def depositar(self, consulta4):
        sumar=int(consulta4)
        saldo.append(sumar)
        messagebox.showinfo( "deposito realizado")
    def retirar(self,consulta6):
        restar=int(consulta6)
        neg=(-restar)
        saldo.append(neg)
        messagebox.showinfo("se realizo el retiro")
        
    def transferencia (self,consulta8,consulta10):
        if (str(consulta8) == str("4321")):
            aa=int(consulta10)
            bb=(-aa)
            saldo.append(bb)
            saldoo.append(aa)
            messagebox.showinfo("deposito realizado")
        else:
            messagebox.showerror("no se realizo el deposito")