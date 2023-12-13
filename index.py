import tkinter as tk
from tkinter import ttk


def inicio(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="Inicio")
    
    index = ttk.Frame(pestania)
    index.grid(row=0, column=0, sticky="nsew")

    # Configurar las columnas y filas para que se expandan
    pestania.columnconfigure(0, weight=1)
    pestania.rowconfigure(0, weight=1)
    index.columnconfigure(0, weight=1)
    index.rowconfigure(0, weight=1)
    label_fadeco = tk.Label(index, text="FADECO")
    label_fadeco.grid(row=0, column=0, pady=10, sticky="nsew")