import tkinter as tk
from tkinter import ttk
from funciones import consulta_bases_terminadas, consulta_insumos, consulta_piezas, consulta_afiladores

tipo = ["Inox 330", "Inox 300", "Inox 250", "Pintada 300", "Pintada 250"]

i330 = ["brazo_330", "cubrecuchilla_330", "velero", "perilla_brazo", "cabezal_I", "teletubi_330", "chuchilla_330", "cuadrado_regulador", "vela_final_330", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "planchada_final_330", "varilla_brazo_330", "resorte_brazo", "tapa_afilador", "pipas", "tubo_manija", "afilador_final", "perilla_cubrecuchilla", "perilla_afilador", "base_afilador_330", "base_pre_armada330inox", "piedras_afilador" ]
i300 = ["brazo_300", "cubrecuchilla_300", "velero", "perilla_brazo", "cabezal_I", "teletubi_300", "chuchilla_300", "cuadrado_regulador", "vela_final_300", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "planchada_final_300", "varilla_brazo_300", "resorte_brazo", "tapa_afilador", "pipas", "tubo_manija", "afilador_final", "perilla_cubrecuchilla", "perilla_afilador", "base_afilador_300", "base_pre_armada300inox", "piedras_afilador" ]
i250 = ["brazo_250", "cubrecuchilla_250", "velero", "perilla_brazo", "cabezal_I", "teletubi_300", "chuchilla_250", "cuadrado_regulador", "vela_final_250", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "planchada_final_250", "varilla_brazo_250", "resorte_brazo", "tapa_afilador_250", "pipas", "tubo_manija_250", "afilador_final", "perilla_cubrecuchilla", "perilla_afilador", "base_afilador_250", "base_pre_armada250inox", "piedras_afilador" ]

p330 = ["brazo_330", "cubrecuchilla_330", "velero", "perilla_brazo", "cabezal_pintura", "teletubi_330", "chuchilla_330", "cuadrado_regulador", "vela_final_330", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "planchada_final_330", "varilla_brazo_330", "resorte_brazo", "tapa_afilador", "pipas", "tubo_manija", "afilador_final", "perilla_cubrecuchilla", "perilla_afilador", "base_afilador_330", "base_pre_armada330pint", "piedras_afilador" ]
p300 = ["brazo_300", "cubrecuchilla_300", "velero", "perilla_brazo", "cabezal_pintura", "teletubi_300", "chuchilla_300", "cuadrado_regulador", "vela_final_300", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "planchada_final_300", "varilla_brazo_300", "resorte_brazo", "tapa_afilador", "pipas", "tubo_manija", "afilador_final", "perilla_cubrecuchilla", "perilla_afilador", "base_afilador_300", "base_pre_armada300pint", "piedras_afilador" ]


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

    mostrar = tk.Label(caja1, text="Mostrar Datos")
    mostrar.grid(row=1, column=0) 

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

    tk.Button(botonesgrup, text="Insumos", command= lambda: consulta_insumos(arbol, mostrar)).grid(row=0, column=0)
    tk.Button(botonesgrup, text="Afiladores", command=lambda: consulta_afiladores(arbol, mostrar)).grid(row=0, column=1)
    tk.Button(botonesgrup, text="Base Prearmadas", command=lambda: consulta_bases_terminadas(arbol, mostrar)).grid(row=0, column=2)
    tk.Button(botonesgrup, text="Piezas", command= lambda: consulta_piezas(arbol, mostrar)).grid(row=0, column=3)

    ttk.Separator(caja2, orient="horizontal").grid(row=2, column=0, sticky="ew", columnspan=2, padx=5, pady=5)
    

    tk.Label(caja2, text="Maquinas Armadas en el día ").grid(row=3, column=0)
    tk.Label(caja2, text="Tipo").grid(row=4, column=0)
    tipo_seleccionado = ttk.Combobox(caja2, values=tipo, state="readonly")
    tipo_seleccionado.grid(row=4, column=1)
    tk.Label(caja2, text="Cantidad").grid(row=5, column=0)
    cantidad = tk.Entry(caja2)
    cantidad.grid(row=5, column=1)
    ttk.Button(caja2, text="ENVIAR").grid(row=6, column=1)

    ttk.Separator(caja2, orient="horizontal").grid(row=7, column=0, sticky="ew", columnspan=2, padx=5, pady=5)
