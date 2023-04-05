from tkinter import messagebox
import sqlite3
import bcrypt
from tkinter import ttk
import tkinter as tk
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
            cursor= conx.cursor()
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
        conPlana=conPlana.encode()
        #convertimos con a bytes
        sal=bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa
    #metodo buscar un usuario
    def consultarusuario(self,id):
        #1.Preparar una conexion
        conx=self.conexionBD()
        #2.verificar si el parametro ID contiene algo
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID es invalido o esta vacio")
            conx.close()
        else:
            try:
                #3.preparar cursor y el query
                cursor=conx.cursor()
                selectQry="select * from TBRegistrados where id="+id
                #4.ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario=cursor.fetchall()
                conx.close()
                return rsUsuario
            except sqlite3.OperationalError:
                print("Error de consulta")
    #Prectica 17 se realizara una funcion la cual al ejecutar el programa mostrara dentro de una tabla los registros dentro de la BD
                
    def imprimir(self):
       # se accede primero ala conexion generada anteriormente reutilizando dicha funcion
        conx=self.conexionBD()
        # se genera un cursor
        cursor=conx.cursor()
       
        # se prepera el Query
        
        selectQry="select id,nombre,correo,contra from TBRegistrados"
        # se ejecutara la consulta realizada
        cursor.execute(selectQry)
        resultado=cursor.fetchall()
        #se cierra la conexion
        conx.close()
        # dichos datos se tomaran y almacenaran en una lista para mandarlos llamar cuando se desee
        registros=[]
        for row in resultado:
            registros.append(list(row))
            
        # se beden regresar los datos de la lista para asi poder asiganarles una funcion dentro del boton para actualizarr los datos
       
        return registros   
        
    def eliminar_registro(self,id):
        conx=self.conexionBD()
        cursor=conx.cursor()
        cursor.execute("DELETE FROM TBRegistrados WHERE id=?", (id,))
        messagebox.askyesno("Alerta","Desea borrar registro de la bd")
        conx.commit()
        conx.close()
        
    def modificar(self,id,nombre,correo,contraseña):
        if(id == ""):
            messagebox.showwarning("Cuidado","El ID no se encuentra en la base de datos")
       
        else:
            try:
        
                nom=nombre
                cor=correo
                contra=contraseña
            
                conx=self.conexionBD()
                cursor=conx.cursor()
                cursor.execute("UPDATE TBRegistrados SET nombre=?, correo=?, contra=? WHERE id=?", (nom, cor, contra,id))
                messagebox.showinfo("Realizado","Se a realizado la actualizacion de datos")
                conx.commit()
                conx.close()
            except sqlite3.OperationalError:
                messagebox.showerror("Error","no se pudieron realizar los cambios")
        

    
        
        
        
        # dichos datos se tomaran y almacenaran en una lista para mandarlos llamar cuando se desee
    
        
        
   

        
           

