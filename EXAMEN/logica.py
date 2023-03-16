import random
from tkinter import messagebox
nombre=[]
apellidopat=[]
apellidomat=[]
añonac=[]
carrera=[]
numeros="0123456789"
class logica:
    def __init__(self):
        self
    def guardar(self, unoa,unob,unoc,unod,unoe):
        a=str(unoa)
        b=str(unob)
        c=str(unoc)
        d=int(unod)
        e=str(unoe)
        nombre.append(a)
        apellidopat.append(b)
        apellidomat.append(c)
        añonac.append(d)
        carrera.append(e)

       
    def generar():
        tamaño=2
        
        
        mat=[random.choice(numeros)for i in range(tamaño)]
        matricula=mat
        messagebox.showinfo(f"matricula es:",{matricula} )
       
        
        
    
    