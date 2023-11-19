import tkinter as tk
from tkinter import ttk

tipo = ["330", "300", "250"]

piezas_a_torner_lista = ["manchon", "manchon_250", "eje_250", "eje", "rueditas", "tornillo_guia", "carros", "movimientos", "carros_250" ]

def mecanizado(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(row=0, column=0, padx=10, pady=10,)

    notebook.add(pestania, text="Mecanizado")
    tk.Label(pestania, text="Mecanizado").grid(row=1, column=0, columnspan=3)
    caja1 = ttk.Frame(pestania)
    caja1.grid(row=2, column=0)
    
    tk.Label(caja1, text="mostrar Datos").grid(row=1, column=0)
    
    arbol = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    arbol.heading("Pieza", text="Pieza")
    arbol.heading("Cantidad", text="Cantidad")
    arbol.column("#0", width=0, stretch=tk.NO)
    arbol.column("Pieza", anchor=tk.W, width=170)
    arbol.column("Cantidad", anchor=tk.W, width=90)
    arbol.config(height=20)
    arbol.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")  
    
    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, padx=3,pady=3)
    
    
    caja3 = ttk.Frame(pestania)
    caja3.grid(row=2, column=1)
    
    torno = ttk.Frame(caja3)
    torno.grid(row=0, column=1)
    
    tk.Label(torno, text="Torno").grid(row=0, column=0)
    
    tk.Label(torno, text="Piezas").grid(row=1 , column=0)
    piezas_a_torner = ttk.Combobox(torno, values=piezas_a_torner_lista)
    piezas_a_torner.grid(row=2, column=0)
    
    tk.Label(torno, text="Cantidad").grid(row=1,column=1)
    cantidad_torneada = tk.Entry(torno)
    cantidad_torneada.grid(row=2, column=1)
    
    ttk.Button(torno, text="Enviar").grid(row=3, column=1)
    
    ttk.Separator(torno, orient="horizontal").grid(row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5)    
    
    stock_torno = tk.Frame(torno)
    stock_torno.grid(row=5, column=0)
    
    tk.Label(stock_torno, text="Stock del Torno").grid(row=0, column=0)
    ttk.Button(stock_torno, text="Stock Bruto").grid(row=1, column=0)
    ttk.Button(stock_torno, text="Stock Terminado").grid(row=1, column=1)    
    
    ttk.Separator(torno, orient="horizontal").grid(row=6, column=0, sticky="ew", columnspan=2, padx=5, pady=5)    
    
    tk.Label(torno, text="Obsebaciones").grid(row=7, column=0)
    info_torno = tk.Text(torno, height=6, width=25)
    info_torno.grid(row=8, column=0)
    tk.Button(torno, text="Enviar").grid(row=9, column=1)
    
    caja2 = ttk.Frame(pestania)
    caja2.grid(row=2, column=2)
    
    armado_de_caja = ttk.Frame(caja2)
    armado_de_caja.grid(row=0, column=0)
    
    tk.Label(armado_de_caja, text="Armado De Cajas").grid(row=0, column=0)
    
    botonera = ttk.Frame(armado_de_caja)
    botonera.grid(row=1, column=0)
    
    tk.Button(botonera, text="Stock Total").grid(row=0, column=0)
    tk.Button(botonera, text="Stock 330").grid(row=0, column=1)
    tk.Button(botonera, text="Stock 300").grid(row=0, column=2)
    tk.Button(botonera, text="Stock 250").grid(row=0, column=3)
    tk.Button(botonera, text="Stock Motores").grid(row=1, column=1, columnspan=4)
    
    tk.Label(botonera, text="posibilidade maquinas").grid(row=2, column=0)
    
    tk.Button(botonera, text="Stock Total").grid(row=3, column=0)
    tk.Button(botonera, text="330").grid(row=3, column=1)
    tk.Button(botonera, text="300").grid(row=3, column=2)
    tk.Button(botonera, text="250").grid(row=3, column=3)
    
    ttk.Separator(armado_de_caja, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5 )
    
    tk.Label(armado_de_caja, text="cajas terminadas").grid(row=3, column=0)
    
    tk.Label(armado_de_caja, text="Tipo").grid(row=4, column=0)
    tipo_de_caja = ttk.Combobox(armado_de_caja, values=tipo)
    tipo_de_caja.grid(row=5,column=0)
    
    tk.Label(armado_de_caja, text="Cantidad").grid(row=4, column=1)
    cantidad_entrada = tk.Entry(armado_de_caja)
    cantidad_entrada.grid(row=5, column=1)
    
    tk.Button(armado_de_caja, text="Enviar").grid(row=6, column=1)
    
    ttk.Separator(armado_de_caja, orient="horizontal").grid(row=7, column=0, columnspan=2, sticky="ew", padx=5, pady=5 )

    tk.Label(armado_de_caja, text="Observaciones").grid(row=8, column=0, )
    caja_texto = tk.Text(armado_de_caja, height=6 , width=25)
    caja_texto.grid(row=9, column=0, columnspan=2)
    
    tk.Button(armado_de_caja, text="Enviar").grid(row=10, column=0)