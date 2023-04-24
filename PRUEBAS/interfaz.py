from logica import*
a=logica()
def gen():
    a.generar_contrasena()
def cop():
    contraseña=a.copiar_contrasena()
    texto_entry.delete(0, tk.END)
    texto_entry.insert(0, contraseña)

# Crear la ventana
ventana = tk.Tk()

# Crear el Entry
texto_entry = tk.Entry(ventana)
texto_entry.pack()

# Crear el botón de generación de contraseña
boton_generar = tk.Button(ventana, text="Generar contraseña", command=cop)
boton_generar.pack()

# Iniciar el loop principal de la ventana
ventana.mainloop()