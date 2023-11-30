import tkinter as tk
from tkinter import ttk
from funciones import mostrar_datos_torno, mostrar_datos_ , actualizar_pieza_torno, actualizar_caja_torno, mostrar_piezas_torno_terminado, pulido_cabezal, de_enbruto_a_torneado, mostrar_cajas_bruto, agregar_a_lista_tarea

tipo = ["330", "300", "250"]
tipos_de_maquinas = ["inox_330", "inox_300", "Inox_250", "pintada_330", "pintada_300"]
cajas_torono = ["caja_torneado_330", "caja_torneado_300", "caja_torneado_250"]
piezas_a_torner_lista = ["manchon", "manchon_250", "eje_250", "eje", "rueditas", "tornillo_guia", "carros", "movientos", "carros_250" ]


def mecanizado(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(row=0, column=0, padx=10, pady=10,)

    notebook.add(pestania, text="Mecanizado")
    tk.Label(pestania, text="Mecanizado").grid(row=1, column=0, columnspan=4)
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
    
    tk.Label(torno, text="Piezas Terminadas").grid(row=1 , column=0)
    piezas_a_torner = ttk.Combobox(torno, values=piezas_a_torner_lista)
    piezas_a_torner.grid(row=2, column=0)
    
    tk.Label(torno, text="Cantidad").grid(row=1,column=1)
    cantidad_torneada = tk.Entry(torno)
    cantidad_torneada.grid(row=2, column=1)
    
    ttk.Button(torno, text="Enviar", command=lambda: actualizar_pieza_torno(piezas_a_torner, cantidad_torneada, result, "piezas_finales_defenitivas", arbol)).grid(row=3, column=1)
    
    ttk.Separator(torno, orient="horizontal").grid(row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5)    
    
    stock_torno = tk.Frame(torno)
    stock_torno.grid(row=5, column=0)
    
    tk.Label(stock_torno, text="Stock del Torno").grid(row=0, column=0)
    ttk.Button(stock_torno, text="Stock Bruto", command=lambda: mostrar_datos_torno(arbol, "piezas_del_fundicion")).grid(row=1, column=0)
    ttk.Button(stock_torno, text="Stock Terminado", command=lambda: mostrar_piezas_torno_terminado(arbol)).grid(row=1, column=1)    
    
    ttk.Separator(torno, orient="horizontal").grid(row=6, column=0, sticky="ew", columnspan=2, padx=5, pady=5)    
    
    tk.Label(torno, text="Torneado de cajas").grid(row=7, column=0)
    tk.Label(torno, text="Cajas Terminadas").grid(row=8 , column=0)
    caja_a_torner = ttk.Combobox(torno, values=cajas_torono)
    caja_a_torner.grid(row=9, column=0)
    
    tk.Label(torno, text="Cantidad").grid(row=8,column=1)
    cantidad_caja_torneada = tk.Entry(torno)
    cantidad_caja_torneada.grid(row=9, column=1)
    
    ttk.Button(torno, text="Enviar", command=lambda: de_enbruto_a_torneado(caja_a_torner, cantidad_caja_torneada, result)).grid(row=10, column=1)
    ttk.Button(torno, text="Stock Terminado", command=lambda: mostrar_datos_(arbol)).grid(row=11, column=0)   
    ttk.Button(torno, text="Stock Bruto", command=lambda: mostrar_cajas_bruto(arbol)).grid(row=11, column=1)   
    

    ttk.Separator(torno, orient="horizontal").grid(row=12, column=0, sticky="ew", columnspan=2, padx=5, pady=5)        
    
    tk.Label(torno, text="Obsebaciones").grid(row=13, column=0)
    info_torno = tk.Text(torno, height=6, width=25)
    info_torno.grid(row=14, column=0, columnspan=1)
    tk.Button(torno, text="Enviar", command= lambda: agregar_a_lista_tarea(info_torno, result)).grid(row=15, column=0, sticky="e")
    
    caja2 = ttk.Frame(pestania)
    caja2.grid(row=2, column=2)
    
    armado_de_caja = ttk.Frame(caja2)
    armado_de_caja.grid(row=0, column=0)
 
    tk.Label(armado_de_caja, text="Armado de cajas").grid(row=0, column=0)
    
    tk.Label(armado_de_caja, text="Stock de Motores").grid(row=1, column=0)
    tk.Button(armado_de_caja, text="Motores").grid(row=1, column=1)
    
    ttk.Separator(armado_de_caja, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="ew", pady=5, padx=5)
    
    tk.Label(armado_de_caja, text="Consultas de Piezas Para Armar Motores").grid(row=3, column=0)
    tk.Button(armado_de_caja, text="Mostrar").grid(row=3, column=1)
    
    ttk.Separator(armado_de_caja, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=5, padx=5)
    
    tk.Label(armado_de_caja, text="Cantidad Posible de Cajas Terminadas").grid(row=5, column=0)
    botonera = ttk.Frame(armado_de_caja)
    botonera.grid(row=6, column=0, columnspan=3)
    
    tk.Button(botonera, text="330").grid(row=12, column=0)
    tk.Button(botonera, text="300").grid(row=12, column=1)
    tk.Button(botonera, text="250").grid(row=12, column=2)

    ttk.Separator(armado_de_caja, orient="horizontal").grid(row=7, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    ttk.Label(armado_de_caja, text="Morotes Terminados").grid(row=8, column=0)
    
    checkbox = ttk.Frame(armado_de_caja)
    checkbox.grid(row=9, column=0, columnspan=2)
    
    modelo = tk.IntVar()
    modelo.set(1)
    
    tk.Radiobutton(checkbox, text="330", variable=modelo, value=1).grid(row=0, column=0)
    tk.Radiobutton(checkbox, text="300", variable=modelo, value=2).grid(row=0, column=1)
    tk.Radiobutton(checkbox, text="250", variable=modelo, value=3).grid(row=0, column=2)
    
    tk.Label(armado_de_caja, text="Cantidad").grid(row=10, column=0)
    motores_terminado_cantidad = tk.Entry(armado_de_caja)
    motores_terminado_cantidad.grid(row=10, column=1)
    ttk.Button(armado_de_caja, text="Enviar").grid(row=11, column=1)

    ttk.Separator(armado_de_caja, orient="horizontal").grid(row=12, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    afiladores = ttk.Frame(caja2)
    afiladores.grid(row=13, column=0)
    
    tk.Label(afiladores, text="Afiladores").grid(row=0, column=0)
    tk.Label(afiladores, text="Stock de Afiladores Terminados").grid(row=1, column=0)
    tk.Button(afiladores, text="Mostrar").grid(row=1, column=1)
    
    ttk.Separator(afiladores, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(afiladores, text=" Stock De Piezas para afiladores").grid(row=3, column=0)
    tk.Button(afiladores, text="Mostrar").grid(row=3, column=1)
    
    ttk.Separator(afiladores, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(afiladores, text="Cantidad Terminada").grid(row=5, column=0)
    cantidad_entrada_afilador = tk.Entry(afiladores)
    cantidad_entrada_afilador.grid(row=6, column=0)
    tk.Button(afiladores, text="Enviar").grid(row=6, column=1)
    
    ttk.Separator(afiladores, orient="horizontal").grid(row=7, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    
    pulido_en_fabrica = ttk.Frame(caja2)
    pulido_en_fabrica.grid(row=14, column=0)
    
    tk.Label(pulido_en_fabrica, text="Cabezales a pulir").grid(row=0, column=0, columnspan=2)
    tk.Label(pulido_en_fabrica, text="Cantidad").grid(row=1, column=0)
    cantidad_cabezales_pulir = tk.Entry(pulido_en_fabrica)
    cantidad_cabezales_pulir.grid(row=1, column=1)
    tk.Button(pulido_en_fabrica, text="Enviar", command= lambda: pulido_cabezal(cantidad_cabezales_pulir, result)).grid(row=2, column=1)
    
    ttk.Separator(pulido_en_fabrica, orient="horizontal").grid(row=3, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    caja4 = ttk.Frame(pestania)
    caja4.grid(row=2, column=3)
    
    pre_armado = tk.Frame(caja4)
    pre_armado.grid(row=0, column=0)
    
    tk.Label(pre_armado, text="Pre Armado").grid(row=1, column=0)
    
    ttk.Separator(pre_armado, orient="horizontal").grid(row=2, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(pre_armado, text="Stock De Piezas Pre Armado").grid(row=3, column=0)
    tk.Button(pre_armado, text="Stock").grid(row=3, column=1)

    ttk.Separator(pre_armado, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", pady=5, padx=5)
    
    tk.Label(pre_armado, text="Bases Terminandas 'sin Motor'").grid(row=5, column=0)
    
    tk.Label(pre_armado, text="Tipo").grid(row=6, column=0)
    tk.Label(pre_armado, text="Cantidad").grid(row=6, column=1)
    
    tipo_pre_armado = ttk.Combobox(pre_armado, values=tipos_de_maquinas)
    tipo_pre_armado.grid(row=7, column=0)
    cantidad_pre_armado_base = tk.Entry(pre_armado)
    cantidad_pre_armado_base.grid(row=7, column=1)
    
    tk.Button(pre_armado, text="Enviar").grid(row=8, column=1)
    
    ttk.Separator(pre_armado, orient="horizontal").grid(row=9, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(pre_armado, text="Stock de bases pre Armadas").grid(row=10, column=0)
    tk.Button(pre_armado, text="Stock").grid(row=10, column=1)
    
    ttk.Separator(pre_armado, orient="horizontal").grid(row=11, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(pre_armado, text="Bases Terminadas con motores").grid(row=12, column=0)
    
    tk.Label(pre_armado, text="Tipo").grid(row=13, column=0)
    tk.Label(pre_armado, text="Cantidad").grid(row=13, column=1)
    
    tipo_pre_armado_final = ttk.Combobox(pre_armado, values=tipos_de_maquinas)
    tipo_pre_armado_final.grid(row=14, column=0)
    cantidad_pre_armado_base_final = tk.Entry(pre_armado)
    cantidad_pre_armado_base_final.grid(row=14, column=1)

    tk.Button(pre_armado, text="Enviar").grid(row=15, column=1)

    ttk.Separator(pre_armado, orient="horizontal").grid(row=16, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(pre_armado, text="Stock de bases Terminadas").grid(row=17, column=0)
    tk.Button(pre_armado, text="Stock").grid(row=17, column=1)
    
    ttk.Separator(pre_armado, orient="horizontal").grid(row=18, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

    tk.Label(pre_armado, text="Obsebaciones").grid(row=19, column=0)
    info_pre_armado = tk.Text(pre_armado, height=6, width=25)
    info_pre_armado.grid(row=20, column=0, columnspan=1)
    tk.Button(pre_armado, text="Enviar").grid(row=21, column=0, sticky="e")
    