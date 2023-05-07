from tkinter import messagebox
class logica:
    def _init_(self):
        pass

    def arabigo__romano(self,arabi):
        if arabi >= 50:
            messagebox.showerror("Alerta", "Numero esta fuera de rango escoje uno entre 1 y 50")
        elif arabi ==0:
            messagebox.showerror("Alerta","No existe este numero en el sistema Romano ingrese uno entre 1 y 50")
        else:
            
            x = ["", "X", "XX", "XXX", "XL", "L"]
            i = ["", "I", "II", "III", "IV", "V",
                "VI", "VII", "VIII", "IX"]

            
            decenas = x[(arabi % 100) // 10]
            unidad = i[arabi % 10]
        
            respuesta = (decenas + unidad)
            messagebox.showinfo("alerta",f'la conversion es"{str(respuesta)}"')
 

    def romano__arabigo( self,roma):
        romano={"I": 1,"II":2, "III":3,"IV": 4,"V": 5,"VI":6,"VII":7,"VIII":8,"X": 9,"X": 10,"XI": 11,"XII":12, "XIII":13,"XIV": 14,"XV": 15,"XVI":16,"XVII":17,"XVIII":18,"XIX": 19,"XX": 20,"XXI": 21,"XXII":22, "XXIII":23,"XXIV": 24,"XXV": 25,"XXVI":26,"XXVII":27,"XXVIII":28,"XXIX": 29,"XXXX": 30,"XXXI": 31,"XXXII":32, "XXXIII":33,"XXXIV": 34,"XXXV": 35,"XXXVI":36,"XXXVII":37,"XXXVIII":38,"XXXIX": 39,"XL": 40,"XLI":41,"XLII":42,"XLIII":43,"XLIV":44,"XLV":45,"XLVI":46,"XLVII":47,"XLVIII":48,"XLIX":49,"L": 50}
        entero=0
        

        if roma =="VX" or roma =="VXX" or roma =="VXXx" or roma=="IIII" or roma=="VXXXXL" or roma=="XIIII":
                messagebox.showerror("Cuidado","La conversion no puede realizarse porque el numero no existe intente con otro")
        else:
            for i in range (len(roma)):
                if i > 0 and romano[roma[i]] > romano[roma[i - 1]]:
                    entero += romano[roma[i]] - 2 * romano[roma[i - 1]]
                else:
                    entero += romano[roma[i]]
            messagebox.showinfo("alerta",f'la conversion es"{entero}"')
          
    