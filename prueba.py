import tkinter as tk

# Crear ventana y widget Entry
ventana = tk.Tk()
entry_resultado = tk.Entry(ventana)

# Definir la función
def mi_funcion():
    # Realizar cálculos y devolver el resultado
    resultado = "hola mundo"
    return resultado

# Obtener el resultado de la función y mostrarlo en el widget Entry
resultado = mi_funcion()
entry_resultado.insert(0, str(resultado))

# Mostrar la ventana
entry_resultado.pack()
ventana.mainloop()