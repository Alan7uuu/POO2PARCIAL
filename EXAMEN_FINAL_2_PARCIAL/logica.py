from tkinter import messagebox
class logica:
    def _init_(self):
        self.romanos = {"I": 1,"IV": 4,"V": 5,"IX": 9,"X": 10,"XL": 40,"L": 50}
        self.arabigos = {1: "I",4: "IV", 5: "V",9: "IX", 10: "X", 40: "XL",50: "L"}

    def arabigo__romano(self,arabi):
        resultado = ""
        if arabi <51:
            for arabigo, romano in sorted(self.arabigos.items(), reverse=True):
                while arabi >= arabigo:
                    resultado += romano
                    arabi -= arabigo
                    messagebox.showinfo("Alerta",f'la conversion es es"{resultado}"')
        else:
            pass

    def romano__arabigo(self, roma):
        resultado = 0
        i = 0

        while i < len(roma):
            if i + 1 < len(roma) and self.romanos[roma[i]] < self.romanos[roma[i+1]]:
                resultado += self.romanos[roma[i+1]] - self.romanos[roma[i]]
                i += 2
            else:
                resultado += self.romanos[roma[i]]
                i += 1
        messagebox.showinfo("Alerta",f'la conversion es es"{resultado}"')
