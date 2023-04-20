from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#CLASE
class logicap:
    
    def __init__(self) -> None:
        pass
    
    
    #conexion 
    
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/ALAN777/Documents/GitHub/POOS181.1/POO2PARCIAL/exmane3parcial/BDImportaciones.db")
            print("conectado a la base BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("no se pudo conectar")
    def guardarregistro (self,mercancia,pais):
        
       conx=self.conexionBD()
       
       if (mercancia == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Mercancia")
       if (pais == "" ):
           messagebox.showwarning("aviso","falto ingresar el dato Pais")    
       else:
           
           cursor=conx.cursor()
           datos=(mercancia,pais)
           qrisert="insert into TB_Europa (Mercancia,Pais) values (?,?)"
           
           cursor.execute(qrisert,datos)
           conx.commit()
           conx.close
           messagebox.showinfo("exito","usuario guardado")
    def eliminar_registro(self,id):
        conx=self.conexionBD()
        cursor=conx.cursor()
        if id == "":
            messagebox.showinfo("Aviso","Falto ingresar el ID")
        else:
            a=messagebox.askyesno("Alerta","Desea borrar registro de la bd")
            if a:
                cursor.execute("DELETE FROM TB_Europa WHERE IDImpo=?", (id,))
                conx.commit()
                conx.close()
            else: 
                pass
    """def consultar(self,pais):
        conx=self.conexionBD()
        cursor=conx.cursor()
        selectQry="select * from TB_Europa where Pais="+pais
        cursor.execute(selectQry)
        rsUsuario=cursor.fetchall()
        messagebox.showinfo("Tu consulta es",f'los datos dentro son es"{selectQry}"')
        conx.close()
        return rsUsuario"""