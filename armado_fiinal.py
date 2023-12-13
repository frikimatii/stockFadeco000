import tkinter as tk
from tkinter import ttk
from funciones import (mostrar)

def armado_final(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="Armado Final")
    tk.Label(pestania, text="Armado Final").grid(row=1, column=0, columnspan=4)
    caja1 = ttk.Frame(pestania)
    caja1.grid(row=2, column=0)

    tk.Label(caja1, text="Mostrar Datos").grid(row=1, column=0)

    arbol = ttk.Treeview(caja1, columns=("Pieza", "Cantidad", "Modelo"))
    arbol.heading("Pieza", text="Pieza")
    arbol.heading("Cantidad", text="Cantidad")
    arbol.heading("Modelo", text="Modelo")
    arbol.column("#0", width=0, stretch=tk.NO)
    arbol.column("Pieza", anchor=tk.W, width=170)
    arbol.column("Cantidad", anchor=tk.W, width=90)
    arbol.column("Modelo", anchor=tk.W, width=90)
    arbol.config(height=20)
    arbol.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")

    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, padx=3, pady=3)
    
    caja2 = ttk.Frame(pestania)
    caja2.grid(row=2, column=1)
    
    tk.Label(caja2, text="Consultas De...").grid(row=0, column=0)
    
    botonesgrup = tk.Frame(caja2)
    botonesgrup.grid(row=1, column=0)
    
    tk.Button(botonesgrup, text="Insumos").grid(row=0,column=0)
    tk.Button(botonesgrup, text="Afiladores").grid(row=0,column=1)
    tk.Button(botonesgrup, text="Base Prearmadas").grid(row=0,column=2)
    tk.Button(botonesgrup, text="Piezas").grid(row=0,column=3)
    
    ttk.Separator(caja2, orient="horizontal").grid(row=2, column=0, sticky="ew", columnspan=2, padx=5, pady=5)
    
    tk.Label(caja2, text="Consulta de maquinas para armar").grid(row=3, column=0)
    
    btnposible = tk.Frame(caja2)
    btnposible.grid(row=4, column=0)
    
    tk.Button(btnposible, text="Inox 330").grid(row=0,column=0)
    tk.Button(btnposible, text="Inox 300").grid(row=0,column=1)
    tk.Button(btnposible, text="Inox 250").grid(row=0,column=2)
    tk.Button(btnposible, text="Pintada 300").grid(row=1,column=0)
    tk.Button(btnposible, text="Pintada 250").grid(row=1,column=2)
    
    
    