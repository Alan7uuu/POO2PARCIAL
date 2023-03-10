import random 
from tkinter import messagebox
class logica():
    def __init__(self):
        self.__mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__minusculas="abcdefghijklmnopqrstuvwxyz"
        self.__numerico="0123456789"
        self.__especial="!@#$%^&*()_+-={}|[]\\:\";'<>?,./"
    def generarcontraseña(self, tamaño,opciones):
        tamaño2=int(tamaño)
        opciones2=str(opciones)
        if (opciones2) ==str("1"):
            contra=[random.choice(self.__mayusculas) for i in range(tamaño2)]
            messagebox.askokcancel("contraseña", f'"su contraseña es:"{contra}"')
        elif opciones2==str(2):
            contra=[random.choice(self.__minusculas) for i in range(tamaño2)]
            messagebox.askokcancel("contraseña", f'"su contraseña es:"{contra}"')
        elif opciones2==str(3):
            contra=[random.choice(self.__numerico) for i in range(tamaño2)]
            messagebox.askokcancel("contraseña", f'"su contraseña es:"{contra}"')
        elif opciones2==str(4):
            contra=[random.choice(self.__especial) for i in range(tamaño2)]
            messagebox.askokcancel("contraseña", f'"su contraseña es:"{contra}"')
        elif opciones2==str(5):
            contra=[random.choices(self.__mayusculas+self.__especial+self.__minusculas+self.__numerico) for i in range(tamaño2)]
            messagebox.askokcancel("contraseña", f'"su contraseña es:"{contra}"')
        
        