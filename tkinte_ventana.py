import tkinter as tk
from tkinter import ttk

from stock_chapa import crear_pestana_chapa
from fundidor import ventana_fundidor
from provedores import ventana_provedores
from mecanizado import mecanizado
from arnado import armado_final
from index import inicio

def crear_pestana(notebook, texto):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=texto)
    return frame

piezas_pedefinida = [
    "teletubi",
    "cuchilla",
    "motor",
    "vela",
    "planchada",
    "brazo",
    "afilador",
    "patas",
]

root = tk.Tk()
root.title("Mostrar Datos de la Base De Datos")
root.iconbitmap("img/FLogo.ico")
notebook = ttk.Notebook(root)

armado_final(notebook)
inicio(notebook)
mecanizado(notebook)
ventana_provedores(notebook)
ventana_fundidor(notebook)
crear_pestana_chapa(notebook)

notebook.pack()

root.mainloop()
