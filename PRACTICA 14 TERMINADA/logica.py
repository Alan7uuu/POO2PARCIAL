from tkinter import messagebox
#daTOS DE 2 CUENTRA PREDEFINIDOS
usuario2=[]
saldo2=[]
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
        elif unobb =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Titular")
        elif unocc =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Edad")
        elif unodd =="":
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
        
    
    def guardar2 (self,dosaa,dosbb,doscc,dosdd):
        if dosaa =="" and dosbb=="" and doscc=="" and dosdd=="":
            messagebox.showinfo("Alerta","No se pueden reistrar campos vacios")
        elif dosaa =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Noº de cuenta")
        elif dosbb =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Titular")
        elif doscc =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Edad")
        elif dosdd =="":
            messagebox.showinfo("Alerta","Falto ingresar dato Saldo")
        else:
            uno2=str(dosaa)
            dos2=str(dosbb)
            tres2=str(doscc)
            cuatro2=int(dosdd)
            usuario2.append(uno2)
            usuario2.append(dos2)
            usuario2.append(tres2)
            usuario2.append(saldo2)
            saldo2.append(cuatro2)
            messagebox.showinfo("Usuario","Se guardo exitosamente el Usuario")
    def transferencia (self,consulta8,consulta10):
        if (str(consulta8) == str(usuario2[0])):
            aa=int(consulta10)
            bb=(-aa)
            cc=(+aa)
            saldo.append(bb)
            saldo2.append(cc)
            messagebox.showinfo("Realizado","deposito realizado")
        else:
            pass
    def consulta2 (self):
            dos=sum(saldo2)
            messagebox.showinfo("Consulta",f'su total disponible es: "{dos}"')
        
        
         