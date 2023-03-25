from tkinter import messagebox
import sqlite3
import bcrypt
class controladorBD:
    def __init__(self):
        pass
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/ALAN777/Documents/GitHub/POOS181.1/POO2PARCIAL/tkinterSQLite/DBusuarios.db")
            print("conexion ala BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se pudo conectar ala BD")
    def guardarusuario(self,nom,corr,contra):
        #1.usamos una conexion
        conx= self.conexionBD()
        #2.Validar parametros vacios
        if (nom== "" or corr== "" or contra==""):
            messagebox.showwarning("aguas","formulario incompleto")
        else:
            
            
            #3.preparamos cursor,datos,querySQL
            cursor=conx.cursor()
            conH=self.encriptarCon(contra)
            
            datos=(nom,corr,conH)
            qrInsert="insert into TBRegistrados(nombre,correo,contra) values (?,?,?)"
            
            #4. ejecutar insert y cerramos conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("exito","usuario guardado")
    def encriptarCon(self,contra):
        conPlana= contra
        conPlana=conPlana.encode()  #convertimos con a bytes
        sal=bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa
    
            
        
        
  