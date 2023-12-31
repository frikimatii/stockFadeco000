import tkinter as tk
from tkinter import ttk

from stock_chapa import crear_pestana_chapa
from fundidor import ventana_fundidor
from provedores import ventana_provedores
from mecanizado import mecanizado

from index import inicio
from parte_armado import seccion_armado


def crear_pestana(notebook, texto):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=texto)
    return frame



root = tk.Tk()
root.title("Mostrar Datos de la Base De Datos")
root.iconbitmap("img/FLogo.ico")
notebook = ttk.Notebook(root)


inicio(notebook)

ventana_fundidor(notebook)
crear_pestana_chapa(notebook)
ventana_provedores(notebook)
mecanizado(notebook)
seccion_armado(notebook)

notebook.pack()

root.mainloop()
