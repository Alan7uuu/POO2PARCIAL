import random
from tkinter import Tk


def consulta():
    for _ in range(random.randint(1, 13)):
        yield random.choices(range(1, 200), k=2)


def nueva_consulta():
    cursor = consulta()
    clientes_tab.clear()
    for row in cursor:
        clientes_tab.add_row(row)


t3 = tk.Tk()
clientes_headers = ["foo", "bar"]
clientes_tab = Table(
    t3, title="ENTRADAS DE MERCADERIAS", headers=clientes_headers
    )
clientes_tab.pack()
tk.Button(t3, text="Nueva consulta", command=nueva_consulta).pack()

t3.mainloop()