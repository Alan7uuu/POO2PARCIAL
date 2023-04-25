from tkinter import messagebox
def roman2int(romval):
        if romval == "VX" or romval == "IIII" or romval == "VVVV" or romval == "XXXX" or romval == "LLLL" or romval == "CCCC" or romval == "DDDD" or romval == "MMMM" or romval == "VV" :
            messagebox.showinfo("resultado", "no es un numero romano")
        else:
            romanos = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            total = 0
            prev = 0
            for letra in romval[::-1]:
                valor = romanos[letra]
                total += valor if valor >= prev else -valor
                prev = valor
            messagebox.showinfo("resultado", str(total))
            
            
roman2int('VX')