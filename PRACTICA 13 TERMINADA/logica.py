import random 
from tkinter import messagebox
import tkinter as tk


class logica:
    
    lista=[]
    
    def __init__(self):
        
        self.__caracteres="abcdefghijklmnñopqrstuvwxyz"
        self.__numeros="1234567890"
        self.__especiales="@!#$%&/=?¡¿'¿´+*-|°¬"
        self.__mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    def generar (self,tam,mayus,espec):
        a=int(tam)
        c=str(espec)
        d=str(mayus)
        
        if (c == "si"):
            b = [random.choices(self.__especiales +self.__caracteres+self.__numeros) for i in range(a)]
            messagebox.askokcancel("contraseña",f'la contraseña es"{b}"')
            
        elif (d == "si"):
            b = [random.choices(self.__mayusculas+self.__numeros+self.__caracteres) for i in range(a)]
            messagebox.askokcancel("contraseña",f'la contraseña es"{b}"')
            
        elif (d == "si" and  c== "si"):
            b = [random.choices(self.__mayusculas+self.__numeros+self.__caracteres+self.__especiales) for i in range(a)]
            messagebox.askokcancel("contraseña",f'la contraseña es"{b}"')
          
            
        else:
            b = [random.choice(self.__caracteres) for i in range(a)]
            f=print( messagebox.askokcancel("contraseña",f'la contraseña es"{b}"'))
            if f == True:
                print("si")
        return b
        
    def comprobar (self,tam,mayus,espec):
        a=int(tam)
        c=str(espec)
        d=str(mayus)
        if c=="si" and d=="" and a==8:
            messagebox.showinfo("Aviso","Su contraseña cuenta con una seguridad MODERADO")
        elif c=="" and d=="si" and a==8:
            messagebox.showinfo("Aviso","Su contraseña cuenta con una seguridad MODERADO")
        elif c=="" and d=="" and a <=8:
            messagebox.showinfo("Aviso","Su contraseña cuenta con una seguridad BAJA")
        elif c=="si" and d=="si" and a >8 :
            messagebox.showinfo("Aviso","Su contraseña cuenta con una seguridad FUERTE")
        else:
            pass
    
        
       
