import random
from tkinter import messagebox
numero='1234567890'
año="2023"
class logica:
    
    """def aleatorio():
        mat=''
        for i in range(2):
            mat +=str(random.randint(0, 9))
            return mat"""
    def clave(self,nombre,apellidop,apellidom,nacimiento,carrera):
            aa= (nombre[0:1])
            bb=(apellidop[0:2])
            cc= (apellidom[0:2])
            dd= (nacimiento[-2:])
            ee= (carrera[0:3])
            ff= (año[-2:])
            ww=random.randint(0,9)
            xx=random.randint(0,9)
         
           

     
            messagebox.showinfo("error",f'la matricula es: "{aa}{bb}{cc}{dd}{ff}{ee}{ww}{xx}"')

        
      
    
       
        
        
    
    