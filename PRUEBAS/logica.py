import random
import tkinter as tk
import string
class logica:
    def __init__(self):
        pass
    def generar_contrasena(self):
        longitud = 10
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
        return contrasena
    def copiar_contrasena(self):
        contraseña=self.copiar_contrasena
        
