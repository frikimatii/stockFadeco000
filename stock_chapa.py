import tkinter as tk
from tkinter import ttk
from funciones import (
    actualizar_pieza,
    eliminar_pieza,
    mostrar_datos,
    mostrar_datos_chapa,
    consulta_de_piezas,
    consulta_cabezales,
    stock_chapa,
    agregar_pieza_chapas,
    eliminar_pieza_chapas,
    agregar_portaeje,
    eliminar_portaeje,
    sort_column,
    calcular_maquinas,
    agregar_piezas_faltantes,
    eliminar_piezas_faltante,
    ensamble_de_maquinas_soldadas
    
)



piezas_pedefinida_chapas_base = [
    "chapa_principal_330",
    "lateral_L_330",
    "lateral_R_330",
    "chapa_principal_300",
    "lateral_L_300",
    "lateral_R_300",
]

base_inox_330 = [
    ("chapa_principal_330", 1),
    ("lateral_L_330", 1),
    ("lateral_R_330", 1),
    ("varilla_330", 1),
    ("planchuela_330", 1),
    ("portaeje", 1),
    ("arandela", 1)
]

base_inox_300 = [
    ("chapa_principal_300", 1),
    ("lateral_L_300", 1),
    ("lateral_R_300", 1),
    ("varilla_300", 1),
    ("planchuela_300", 1),
    ("portaeje", 1),
    ("arandela", 1)
]

base_pintada_330 = [
    ("chapa_principal_330", 1),
    ("lateral_L_330", 1),
    ("lateral_R_330", 1),
    ("varilla_330", 1),
    ("planchuela_330", 1),
    ("portaeje", 1),
    ("arandela", 1)
]

base_pintada_300 = [
    ("chapa_principal_300", 1),
    ("lateral_L_300", 1),
    ("lateral_R_300", 1),
    ("varilla_300", 1),
    ("planchuela_300", 1),
    ("portaeje", 1),
    ("arandela", 1)
]

cabezal_final = ["chapa_U_cabezal", "tapa_cabezal", "bandeja_cabezal"]

piezas_restante = [
    "planchuela_330",
    "varilla_330",
    "planchuela_300",
    "varilla_300",
    "portaeje",
    "arandela"]

pieza_faltante = ["portaeje", "arandela"]


def crear_pestana_chapa(notebook):
    pestana_chapa = ttk.Frame(notebook)
    pestana_chapa.grid(
        row=3,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestana_chapa, text="Stock de Chapa")

    box1 = ttk.Frame(pestana_chapa)
    box1.grid(row=0, column=0, pady=5, padx=5)

    ttk.Label(box1, text="Tabla de Chapas", font=("Arial", 10, "bold")).grid(
        row=0, column=0, padx=5, pady=5
    )
    subtitulo = ttk.Label(box1, text="")
    subtitulo.grid(row=1, column=0, padx=5, pady=5)

    tabla_chapa = ttk.Treeview(box1, columns=("Pieza", "Cantidad", "Modelo", "Tipo"))
    tabla_chapa.heading("Pieza", text="Pieza", command=lambda: sort_column(tabla_chapa, "Pieza", False))
    tabla_chapa.heading("Cantidad", text="Cantidad", command=lambda: sort_column(tabla_chapa, "Cantidad", False))
    tabla_chapa.heading("Modelo", text="Modelo", command=lambda: sort_column(tabla_chapa, "Modelo", False))
    tabla_chapa.heading("Tipo", text="Tipo", command=lambda: sort_column(tabla_chapa, "Tipo", False))
    tabla_chapa.column("#0", width=0, stretch=tk.NO)
    tabla_chapa.column("Pieza", anchor=tk.W, width=150)
    tabla_chapa.column("Cantidad", anchor=tk.W, width=50)
    tabla_chapa.column("Modelo", anchor=tk.W, width=50)
    tabla_chapa.column("Tipo", anchor=tk.W, width=50)
    tabla_chapa.config(height=25)
    tabla_chapa.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")

    lista_acciones = tk.Listbox(box1, width=60)
    lista_acciones.grid(row=4, column=0, )

    box2 = ttk.Frame(pestana_chapa)
    box2.grid(row=0, column=1, padx=5, pady=5, sticky="ne")

    titulo = ttk.Label(box2, text="Stock de Chapas", font=("Arial", 17, "bold")).grid(
        row=0, column=1, padx=5, pady=5, sticky="e"
    )
    ttk.Label(box2, text="Total de Piezas").grid(row=1, column=0, padx=5, sticky="e")
    btn_stock = ttk.Button(
        box2,
        text="Stock Total",
        command=lambda: mostrar_datos_chapa(tabla_chapa, "chapa", subtitulo),
    ).grid(row=1, column=1, padx=5, sticky="w")

    ttk.Separator(box2, orient="horizontal").grid(
        row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )
    
    pieza_agregar_chapa = ttk.Frame(box2)
    pieza_agregar_chapa.grid(row=3, column=0, padx=7)

    ttk.Label(pieza_agregar_chapa, text="Agregar Piezas ", font=("Arial", 10, "bold")).grid(row=0, column=1,pady=5, sticky="w")

    tipo_var = tk.IntVar()
    tipo_var.set(1)
    
    acero_radio_agregar = tk.Radiobutton(pieza_agregar_chapa, text="Acero", variable=tipo_var, value=1)
    acero_radio_agregar.grid(row=1, column=0)
    chapa_radio_agregar = tk.Radiobutton(pieza_agregar_chapa, text="Pintura", variable=tipo_var, value=2)
    chapa_radio_agregar.grid(row=1, column=1)    
    
    ttk.Label(pieza_agregar_chapa, text="Agregar Pieza").grid(row=2, column=0, pady=5)
    lista_agregar_chapa = ttk.Combobox(pieza_agregar_chapa, values=piezas_pedefinida_chapas_base, state="readonly")
    lista_agregar_chapa.grid(row=2, column=1,pady=5)    
    
    ttk.Label(pieza_agregar_chapa, text="Cantidad").grid(row=3, column=0, sticky="nw", pady=5)
    cantidad_agregar = ttk.Entry(pieza_agregar_chapa)
    cantidad_agregar.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_agregar = ttk.Button(pieza_agregar_chapa, text="Agregar", command= lambda: agregar_pieza_chapas(tipo_var,lista_agregar_chapa, cantidad_agregar, tabla_chapa, "chapa", lista_acciones))
    btn_agregar.grid(row=4, column=1, sticky="ne", pady=5)
    
    pieza_eliminar_chapa = ttk.Frame(box2)
    pieza_eliminar_chapa.grid(row=3, column=1, padx=7)
    
    ttk.Label(pieza_eliminar_chapa, text="Elimiar Pieza", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", pady=5)
    
    
    tipo_var_d = tk.IntVar()
    tipo_var_d.set(1)
    
    tipo_var_d = tk.IntVar()
    tipo_var_d.set(1)
    acero_radio_eliminar = tk.Radiobutton(pieza_eliminar_chapa, text="Acero", variable=tipo_var_d, value=1)
    acero_radio_eliminar.grid(row=1, column=0)
    chapa_radio_eliminar = tk.Radiobutton(pieza_eliminar_chapa, text="Pintura", variable=tipo_var_d, value=2)
    chapa_radio_eliminar.grid(row=1, column=1)
    
    ttk.Label(pieza_eliminar_chapa, text="Elimiar Pieza").grid(row=2, column=0, pady=5)
    lista_eliminar_chapa = ttk.Combobox(pieza_eliminar_chapa, values=piezas_pedefinida_chapas_base, state="readonly")
    lista_eliminar_chapa.grid(row=2, column=1, pady=5)
    
    ttk.Label(pieza_eliminar_chapa, text="Cantidad").grid(row=3, column=0, pady=5, sticky="nw")    
    cantidad_elimimar = ttk.Entry(pieza_eliminar_chapa)
    cantidad_elimimar.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_eliminar = ttk.Button(pieza_eliminar_chapa, text="Eliminar", command= lambda: eliminar_pieza_chapas(tipo_var_d, lista_eliminar_chapa, cantidad_elimimar, tabla_chapa, "chapa", lista_acciones))
    btn_eliminar.grid(row=4, column=1, sticky="ne", pady=5)
    
    ttk.Separator(box2, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    ttk.Label(box2, text="Consultas", font=("Arial", 10, "bold")).grid(row=5, column=1, padx=5, sticky="e")
    stock_pintada = ttk.Button(box2,text="Stock De Inox",command=lambda: stock_chapa(tabla_chapa, "acero", subtitulo))
    stock_pintada.grid(row=6, column=0, padx=5, sticky="e")

    stock_acero = ttk.Button(box2,text="Stock De Pintura", command=lambda: stock_chapa(tabla_chapa, "pintura", subtitulo))
    stock_acero.grid(row=6, column=1, padx=5, sticky="w")

    ttk.Separator(box2, orient="horizontal").grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    ttk.Separator(box2, orient="horizontal").grid(row=19, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
#____________________________________________________________________________________________

    ttk.Label(box2, text="Consulta Piezas de maquinas", font=("Arial", 10, "bold")).grid(row=8,column=1, pady=5, padx=5, sticky="e")
    piezas_330_acero = ttk.Button(box2,text="Inox 330",command=lambda: consulta_de_piezas(tabla_chapa, "acero", "330", subtitulo))
    piezas_330_acero.grid(row=9, column=0, padx=5, pady=5, sticky="e")

    piezas_300_acero = ttk.Button(box2,text="Pintura 330",command=lambda: consulta_de_piezas(tabla_chapa, "pintura", "330", subtitulo))
    piezas_300_acero.grid(row=9, column=1, padx=5, pady=5, sticky="w")

    piezas_330_pintura = ttk.Button(box2, text="Inox 300",command=lambda: consulta_de_piezas(tabla_chapa, "acero", "300", subtitulo))
    piezas_330_pintura.grid(row=10, column=0, padx=5, pady=5, sticky="e")

    piezas_300_pintura = ttk.Button(box2,text="Pintura 300",command=lambda: consulta_de_piezas(tabla_chapa, "pintura", "300", subtitulo))
    piezas_300_pintura.grid(row=10, column=1, padx=5, pady=5, sticky="w")

    ttk.Separator(box2, orient="horizontal").grid(row=11, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    ttk.Label(box2, text="Stock de Cabezales", font=("Arial", 10, "bold")).grid(row=12, column=1, pady=5, padx=5, sticky="e")
    
    stock_cabezales_totalAcero = ttk.Button(box2,text="Cabezales Chapa negra",command=lambda: consulta_cabezales(tabla_chapa, "pintura", "cabezal", subtitulo))
    stock_cabezales_totalAcero.grid(row=17, column=1, padx=5, pady=5, sticky="w")
    stock_cabezales_totalChapa = ttk.Button(box2,text="Cabezales Inox",command=lambda: consulta_cabezales(tabla_chapa, "acero", "cabezal", subtitulo))
    stock_cabezales_totalChapa.grid(row=17, column=0, padx=5, pady=5, sticky="e")

    pieza_agregar_cabezal = ttk.Frame(box2)
    pieza_agregar_cabezal.grid(row=18, column=0, padx=7)

    ttk.Label(pieza_agregar_cabezal, text="Agregar Piezas ", font=("Arial", 10, "bold")).grid(row=0, column=1,pady=5, sticky="w")

    tipo_var_c = tk.IntVar()
    tipo_var_c.set(1)
    
    
    acero_radio_agregar = tk.Radiobutton(pieza_agregar_cabezal, text="Acero", variable=tipo_var_c, value=1)
    acero_radio_agregar.grid(row=1, column=0)
    chapa_radio_agregar = tk.Radiobutton(pieza_agregar_cabezal, text="Pintura", variable=tipo_var_c, value=2)
    chapa_radio_agregar.grid(row=1, column=1)    
    
    ttk.Label(pieza_agregar_cabezal, text="Agregar Pieza").grid(row=2, column=0, pady=5)
    lista_agregar_cabezal = ttk.Combobox(pieza_agregar_cabezal, values=cabezal_final, state="readonly")
    lista_agregar_cabezal.grid(row=2, column=1,pady=5)    
    
    ttk.Label(pieza_agregar_cabezal, text="Cantidad").grid(row=3, column=0, sticky="nw", pady=5)
    cantidad_agregar_cabezal = ttk.Entry(pieza_agregar_cabezal)
    cantidad_agregar_cabezal.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_agregar_cabezal = ttk.Button(pieza_agregar_cabezal, text="Agregar", command= lambda: agregar_pieza_chapas(tipo_var_c,lista_agregar_cabezal, cantidad_agregar_cabezal, tabla_chapa, "chapa", lista_acciones))
    btn_agregar_cabezal.grid(row=4, column=1, sticky="ne", pady=5)
    
    pieza_eliminar_cabezal = ttk.Frame(box2)
    pieza_eliminar_cabezal.grid(row=18, column=1, padx=7)
    
    ttk.Label(pieza_eliminar_cabezal, text="Elimiar Pieza", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", pady=5)
    
    tipo_var_ce = tk.IntVar()
    tipo_var_ce.set(1)
    
    tipo_var_ce = tk.IntVar()
    tipo_var_ce.set(1)
    acero_radio_eliminar = tk.Radiobutton(pieza_eliminar_cabezal, text="Acero", variable=tipo_var_ce, value=1)
    acero_radio_eliminar.grid(row=1, column=0)
    chapa_radio_eliminar = tk.Radiobutton(pieza_eliminar_cabezal, text="Pintura", variable=tipo_var_ce, value=2)
    chapa_radio_eliminar.grid(row=1, column=1)
    
    ttk.Label(pieza_eliminar_cabezal, text="Elimiar Pieza").grid(row=2, column=0, pady=5)
    lista_eliminar_cabezal = ttk.Combobox(pieza_eliminar_cabezal, values=cabezal_final, state="readonly")
    lista_eliminar_cabezal.grid(row=2, column=1, pady=5)
    
    ttk.Label(pieza_eliminar_cabezal, text="Cantidad").grid(row=3, column=0, pady=5, sticky="nw")    
    cantidad_elimimar_cabezal = ttk.Entry(pieza_eliminar_cabezal)
    cantidad_elimimar_cabezal.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_eliminar_cabezal = ttk.Button(pieza_eliminar_cabezal, text="Eliminar", command= lambda: eliminar_pieza_chapas(tipo_var_ce, lista_eliminar_cabezal, cantidad_elimimar_cabezal, tabla_chapa, "chapa", lista_acciones))
    btn_eliminar_cabezal.grid(row=4, column=1, sticky="ne", pady=5)
    
    ttk.Separator(box2, orient="horizontal").grid(row=19, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    
    
    #_________________________________________________________________________________________________
    
    box3 = ttk.Label(pestana_chapa)
    box3.grid(row=0, column=3, pady=5, padx=5, sticky="nw")
    
    ttk.Label(box3, text="Agregado de Pieza Faltantes", font=("Arial", 9, "bold")).grid(row=0, column=1, pady=5)
    
    pieza_agregar_v_p = ttk.Frame(box3)
    pieza_agregar_v_p.grid(row=2, column=0, padx=7)

    ttk.Label(pieza_agregar_v_p, text="Agregar Piezas ", font=("Arial", 10, "bold")).grid(row=0, column=1,pady=5, sticky="w")  
    
    ttk.Label(pieza_agregar_v_p, text="Agregar Pieza").grid(row=2, column=0, pady=5)
    lista_agregar_v_p = ttk.Combobox(pieza_agregar_v_p, values=piezas_restante, state="readonly")
    lista_agregar_v_p.grid(row=2, column=1,pady=5)    
    
    ttk.Label(pieza_agregar_v_p, text="Cantidad").grid(row=3, column=0, sticky="nw", pady=5)
    cantidad_agregar_v_p = ttk.Entry(pieza_agregar_v_p)
    cantidad_agregar_v_p.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_agregar_v_p = ttk.Button(pieza_agregar_v_p, text="Agregar", command= lambda:  agregar_piezas_faltantes(lista_agregar_v_p,cantidad_agregar_v_p,tabla_chapa , lista_acciones, "chapa"))
    btn_agregar_v_p.grid(row=4, column=1, sticky="ne", pady=5)
    
    #--------#
    
    pieza_eliminar_v_p = ttk.Frame(box3)
    pieza_eliminar_v_p.grid(row=2, column=1, padx=7)
    
    ttk.Label(pieza_eliminar_v_p, text="Elimiar Pieza", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w", pady=5)
    
    ttk.Label(pieza_eliminar_v_p, text="Elimiar Pieza").grid(row=2, column=0, pady=5)
    lista_eliminar_v_p = ttk.Combobox(pieza_eliminar_v_p, values=piezas_restante, state="readonly")
    lista_eliminar_v_p.grid(row=2, column=1, pady=5)
    
    ttk.Label(pieza_eliminar_v_p, text="Cantidad").grid(row=3, column=0, pady=5, sticky="nw")    
    cantidad_elimimar_v_p = ttk.Entry(pieza_eliminar_v_p)
    cantidad_elimimar_v_p.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_eliminar_v_p = ttk.Button(pieza_eliminar_v_p, text="Eliminar", command=lambda: eliminar_piezas_faltante(lista_eliminar_v_p.get(), cantidad_elimimar_v_p.get(), tabla_chapa, lista_acciones, "chapa"))
    btn_eliminar_v_p.grid(row=4, column=1, sticky="ne", pady=5)
    
    ttk.Separator(box3, orient="horizontal").grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

    #-------------------#
    
    ttk.Label(box3, text="Soldador", font=("Arial", 17, "bold")).grid(row=5, column=1, padx=5, pady=5, sticky="e")    
    
    ttk.Label(box3, text="Stock Del Soldador").grid(row=6, column=0, padx=5, sticky="e")
    btn_stock_soldador = ttk.Button(box3, text="Stock").grid(row=6, column=1, padx=5, sticky="w")
    
    ttk.Separator(box3, orient="horizontal").grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    
    ttk.Label(box3, text="Cantidad de maquina posibles").grid(row=9, column=1)
    
    caja_botones = ttk.Frame(box3)
    caja_botones.grid(row=9, column=0)
    
    tipo_base_acero = "acero"
    tipo_base_pintura = "pintura"

    btn_i_330 = ttk.Button(caja_botones, text="Inox 330", command=lambda: ensamble_de_maquinas_soldadas(base_inox_330, "acero 330", lista_acciones, tipo_base_acero)).grid(row=1, column=0)
    btn_i_300 = ttk.Button(caja_botones, text="Inox 300", command=lambda: ensamble_de_maquinas_soldadas(base_inox_300, "acero 300", lista_acciones, tipo_base_acero)).grid(row=1, column=1)
    btn_p_330 = ttk.Button(caja_botones, text="Pint 330", command=lambda: ensamble_de_maquinas_soldadas(base_pintada_330, "pintada 330", lista_acciones, tipo_base_pintura)).grid(row=1, column=2)
    btn_p_300 = ttk.Button(caja_botones, text="Pint 300", command=lambda: ensamble_de_maquinas_soldadas(base_pintada_300, "pintada 300", lista_acciones, tipo_base_pintura)).grid(row=1, column=3)
    
    ttk.Separator(box3, orient="horizontal").grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
