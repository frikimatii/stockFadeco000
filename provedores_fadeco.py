import tkinter as tk
from tkinter import ttk
from funciones import (
    enviar_piezas_a_pulido,
    mostrar_datos,
    mover_piezas_a_stock_pulidas,
    mostrar_datos_especifico,
    agregar_a_lista_tarea,
    mostrar,
    envios_de_bruto_a_pulido,
    sort_column,
    sort_column_numeric,
    envios_de_bruto_a_niquelar,
    envios_de_niquelado_a_fabrica,
    envios_pulido_a_fabrica,
    envios_pulido_a_fabrica_cabezal,
    envios_de_bruto_cabezal,
    
)
 
modelo_piezas = ["base_pintada_330", "base_pintada_300"]  
niquelado = [
    "eje_rectificado",
    "varilla_brazo_330",
    "varilla_brazo_300",
    "varilla_brazo_250",
    "tubo_manija",
    "tubo_manija_250",
    "palanca_afilador"
]
piezas_carmelo = [
    "brazo_330",#
    "brazo_300",#
    "brazo_250",#
    "cubrecuchilla_330",#
    "cubrecuchilla_300",#
    "cubrecuchilla_250",#
    "teletubi_330",#
    "teletubi_300",#
    "teletubi_250",#
    "vela_final_330",#
    "vela_final_300",#
    "vela_final_250",#
    "planchada_final_330",#
    "planchada_final_300",#
    "planchada_final_250",#
    "tapa_afilador",#
    "velero",#
    "aro_numerador",#
    "tapa_afilador_250",#
    "caja_torneado_330",#
    "caja_torneado_300",#
    "caja_torneado_250",#
    "inox_330",#
    "inox_300",#
    "inox_250"#
]
piezas_maxi = [
    "brazo_330",#
    "brazo_300",#
    "brazo_250",#
    "cubrecuchilla_330",#
    "cubrecuchilla_300",#
    "cubrecuchilla_250",#
    "teletubi_330",#
    "teletubi_300",#
    "teletubi_250",#
    "vela_final_330",#
    "vela_final_300",#
    "vela_final_250",#
    "planchada_final_330",#
    "planchada_final_300",#
    "planchada_final_250",#
    "tapa_afilador",#
    "velero",#
    "aro_numerador",#
    "tapa_afilador_250",#
    "caja_torneado_330",#
    "caja_torneado_300",#
    "caja_torneado_250",#
    "inox_330",#
    "inox_300",#
    "inox_250"#
]
pieza_buen_hombre =  [
    "brazo_330",#
    "brazo_300",#
    "brazo_250",#
    "cubrecuchilla_330",#
    "cubrecuchilla_300",#
    "cubrecuchilla_250",#
    "teletubi_330",#
    "teletubi_300",#
    "teletubi_250",#
    "vela_final_330",#
    "vela_final_300",#
    "vela_final_250",#
    "planchada_final_330",#
    "planchada_final_300",#
    "planchada_final_250",#
    "tapa_afilador",#
    "velero",#
    "aro_numerador",#
    "tapa_afilador_250",#
    "caja_torneado_330",#
    "caja_torneado_300",#
    "caja_torneado_250",#
    "inox_330",#
    "inox_300",#
    "inox_250"#
]
cabezal = ["cabezal_pintura"]


def ventana_provedores(notebook):
    pestania = ttk.Frame(notebook, style='Color.TFrame')
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="session Provedores")

    notebook.style = ttk.Style()
    notebook.style.configure('Color.TFrame', background='#192965', radius=20, borderwidth=10) 
    notebook.style.configure('WhiteOnRed.TLabel', background='#192965', foreground='#c1c1c1')  
    notebook.style.configure('WhiteOnRed.TEntry', fieldbackground='black', foreground='black')  
    notebook.style.configure('WhiteOnRed.TCombobox', fieldbackground='#192965', foreground='white')  
    notebook.style.configure("Estilo9.TButton", font=("Verdana", 7, "bold"), padding=(2, 2))
    notebook.style.configure("Separador1.TSeparator", background="yellow")
    notebook.style.configure("Separador2.TSeparator", background="blue")
    notebook.style.configure("Estilo2.TButton", background="green", padding=2)
    notebook.style.configure("Estilo5.TButton", font=("Arial", 7, "bold"))
    notebook.style.configure("Estilo4.TButton", background="yellow", padding=7)

 


    caja1 = ttk.Frame(pestania, style='Color.TFrame')
    caja1.grid(row=0, column=0, sticky="n")
    
    ttk.Label(caja1, text="Provedores", style="WhiteOnRed.TLabel", font=("Verdana", 30, "bold")).grid(row=0, column=0)
    info = ttk.Label(caja1, text=" Tabla de datos", style="WhiteOnRed.TLabel")
    info.grid(row=1, column=0, sticky="w")
    arbol = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    arbol.heading(
        "Pieza", text="Pieza")
    arbol.heading(
        "Cantidad",
        text="Cantidad",
        command=lambda: sort_column_numeric(arbol, "Cantidad", False),
    )
    arbol.column("#0", width=0, stretch=tk.NO)
    arbol.column("Pieza", anchor=tk.W, width=170)
    arbol.column("Cantidad", anchor=tk.W, width=90)
    arbol.config(height=25)
    arbol.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")

    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, padx=3, pady=3)

#----------------------Carmelo-------------------------------------
    
    box2 = ttk.Frame(pestania, style='Color.TFrame')
    box2.grid(row=0, column=1, sticky="n",pady=27, padx=10)
    
    
    ttk.Label(box2, text="Carmelo", style="WhiteOnRed.TLabel",font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2)
    
    ttk.Label(box2, text="Envios A Carmelo", style="WhiteOnRed.TLabel",font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
    ttk.Label(box2, text="Pieza", style="WhiteOnRed.TLabel",).grid(row=2, column=0, sticky="ew")
    ttk.Label(box2, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=2, column=1, sticky="ew")

    pieza_predeterminadas = ttk.Combobox(box2, values=piezas_carmelo, state="readonly")
    pieza_predeterminadas.grid(row=3, column=0, sticky="w")

    cantidad_agregar_carmelo = ttk.Entry(box2, width=10 ,style='WhiteOnRed.TEntry')
    cantidad_agregar_carmelo.grid(row=3, column=1, sticky="w")

    tk.Button(
        box2,
        text="Enviar Piezas",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: enviar_piezas_a_pulido(
            pieza_predeterminadas,
            cantidad_agregar_carmelo,
            "carmelo_pulido",
            arbol,
            result,info
        ),
    ).grid(row=4, column=1,pady=5, sticky="w")
    
    ttk.Separator(box2, orient="horizontal", style="Separador2.TSeparator").grid(
    row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    
    ttk.Label(box2, text="Piezas Resibidas", style="WhiteOnRed.TLabel",font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w")
    ttk.Label(box2, text="Pieza", style="WhiteOnRed.TLabel",).grid(row=7, column=0, sticky="w")
    ttk.Label(box2, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=7, column=1, sticky="ew")

    pieza_predeterminadas1 = ttk.Combobox(box2, values=piezas_carmelo, state="readonly")
    pieza_predeterminadas1.grid(row=8, column=0, sticky="w")

    cantidad_piezas_terminadas_carmelo = ttk.Entry(box2, width=10,style='WhiteOnRed.TEntry')
    cantidad_piezas_terminadas_carmelo.grid(row=8, column=1, sticky="w")

    tk.Button(
        box2,
        text="Piezas Terminadas",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: mover_piezas_a_stock_pulidas(
            pieza_predeterminadas1,
            cantidad_piezas_terminadas_carmelo,
            "carmelo_pulido",
            "piezas_finales_defenitivas",
            arbol,
            result,info
        ),
    ).grid(row=9, column=1, pady=5, sticky="w")
    
    ttk.Separator(box2, orient="horizontal", style="Separador2.TSeparator").grid(
    row=10, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    
    ttk.Label(box2, text="Consultas De Stock", style="WhiteOnRed.TLabel",).grid(row=11, column=0, sticky="w")

    ttk.Button(
        box2,
        text="Stock Total",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos(arbol, "carmelo_pulido", info),
    ).grid(row=12, column=0, columnspan=2)

    botonera = ttk.Frame(box2, style='Color.TFrame')
    botonera.grid(row=13, column=0, columnspan=2)

    ttk.Button(
        botonera,
        text="Stock 330",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("carmelo_pulido", "330", arbol, info),
    ).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(
        botonera,
        text="Stock 300",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("carmelo_pulido", "300", arbol, info),
    ).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(
        botonera,
        text="Resto De Piezas",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("carmelo_pulido", "250", arbol, info),
    ).grid(row=0, column=2, padx=5, pady=5)

    ttk.Separator(box2, orient="horizontal", style="Separador1.TSeparator").grid(
    row=14, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    
#-----------------------Maxi-------------------------------------------

    box3 = ttk.Frame(pestania, style='Color.TFrame')
    box3.grid(row=0, column=2, sticky="n",pady=25)

    ttk.Label(box3, text="Maxi", style="WhiteOnRed.TLabel",font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2)

    ttk.Label(box3, text="Envios A Maxi", style="WhiteOnRed.TLabel",font=("Arial", 10, "bold")).grid(row=1, column=0,sticky="w")
    ttk.Label(box3, text="Pieza", style="WhiteOnRed.TLabel",).grid(row=2, column=0, sticky="ew")
    ttk.Label(box3, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=2, column=1, sticky="ew")

    pieza_predeterminadas2 = ttk.Combobox(box3, values=piezas_maxi, state="readonly")
    pieza_predeterminadas2.grid(row=3, column=0,sticky="w")

    cantidad_agregar_maxi = ttk.Entry(box3, width=10,style='WhiteOnRed.TEntry')
    cantidad_agregar_maxi.grid(row=3, column=1, sticky="w")

    tk.Button(
        box3,
        text="Enviar Piezas",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: enviar_piezas_a_pulido(
            pieza_predeterminadas2, cantidad_agregar_maxi, "maxi_pulido", arbol, result,info
        ),
    ).grid(row=4, column=1,padx=5, sticky="w")

    ttk.Separator(box3, orient="horizontal", style="Separador2.TSeparator").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )
    
    ttk.Label(box3, text="Piezas Resibidas", style="WhiteOnRed.TLabel",font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w")
    ttk.Label(box3, text="Pieza", style="WhiteOnRed.TLabel",).grid(row=7, column=0, sticky="w")
    ttk.Label(box3, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=7, column=1, sticky="ew")

    pieza_predeterminadas4 = ttk.Combobox(box3, values=piezas_maxi,state="readonly")
    pieza_predeterminadas4.grid(row=8, column=0, sticky="w")

    cantidad_piezas_terminadas_maxi = ttk.Entry(box3, width=10,style='WhiteOnRed.TEntry')
    cantidad_piezas_terminadas_maxi.grid(row=8, column=1, sticky="w")

    tk.Button(
        box3,
        text="Piezas Terminadas",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: mover_piezas_a_stock_pulidas(
            pieza_predeterminadas4,
            cantidad_piezas_terminadas_maxi,
            "maxi_pulido",
            "piezas_finales_defenitivas",
            arbol,
            result,info
        ),
    ).grid(row=9, column=1,padx=5,sticky="w")
    ttk.Separator(box3, orient="horizontal", style="Separador2.TSeparator").grid(row=10, column=0, columnspan=2, sticky="ew", padx=5, pady=5)


    ttk.Label(box3, text="Consultas De Stock", style="WhiteOnRed.TLabel",).grid(row=11, column=0, sticky="w")

    ttk.Button(
        box3, text="Stock Total", style = "Estilo9.TButton", command=lambda: mostrar_datos(arbol, "maxi_pulido", info)
    ).grid(row=12, column=0, columnspan=2)

    botonera = ttk.Frame(box3, style='Color.TFrame')
    botonera.grid(row=13, column=0, columnspan=2)

    ttk.Button(
        botonera,
        text="Stock 300",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("maxi_pulido", "330", arbol, info),
    ).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(
        botonera,
        text="Stock 330",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("maxi_pulido", "300", arbol, info),
    ).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(
        botonera,
        text="Resto De Piezas",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("maxi_pulido", "250", arbol, info),
    ).grid(row=0, column=2, padx=5, pady=5)
    
    ttk.Separator(box3, orient="horizontal", style="Separador1.TSeparator").grid(row=14, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    
    box1 = ttk.Frame(pestania, style='Color.TFrame')
    box1.grid(row=0, column=3, sticky="n",pady=25)

    ttk.Label(box1, text="Buen Hombre", style="WhiteOnRed.TLabel",font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2)
    
    # 0000----------------------------BUEN HOMBRE ------------------------------------#
    
    ttk.Label(box1, text="Envios A Buen Hombre", style="WhiteOnRed.TLabel",font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w")
    ttk.Label(box1, text="Pieza", style="WhiteOnRed.TLabel").grid(row=2, column=0, sticky="ew")
    ttk.Label(box1, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=2, column=1, sticky="ew")

    pieza_predeterminadas5 = ttk.Combobox(box1, values=pieza_buen_hombre ,state="readonly")
    pieza_predeterminadas5.grid(row=3, column=0, sticky="w")

    cantidad_agregar_buen_hombre = ttk.Entry(box1, width=10,style='WhiteOnRed.TEntry')
    cantidad_agregar_buen_hombre.grid(row=3, column=1, sticky="w")

    tk.Button(box1,
            text="Enviar Piezas",
            background="green",
            foreground="white",
            padx=10,
            pady=4,
            font=('Helvetica', 8, "bold"),
            command=lambda: enviar_piezas_a_pulido(
            pieza_predeterminadas5,
            cantidad_agregar_buen_hombre,
            "buen_hombre_pulido",
            arbol,
            result,info
        ),
    ).grid(row=4, column=1,padx=5, sticky="w")

    ttk.Separator(box1, orient="horizontal", style="Separador2.TSeparator").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    ttk.Label(box1, text="Piezas Resibidas", style="WhiteOnRed.TLabel",font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w")
    ttk.Label(box1, text="Pieza", style="WhiteOnRed.TLabel").grid(row=7, column=0, sticky="w")
    ttk.Label(box1, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=7, column=1, sticky="ew")

    pieza_predeterminadas6 = ttk.Combobox(box1, values=pieza_buen_hombre, state="readonly")
    pieza_predeterminadas6.grid(row=8, column=0, sticky="w")

    cantidad_piezas_terminadas_buen_hombre = ttk.Entry(box1, width=10,style='WhiteOnRed.TEntry')
    cantidad_piezas_terminadas_buen_hombre.grid(row=8, column=1, sticky="w")

    tk.Button(box1,
        text="Piezas Terminadas",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: mover_piezas_a_stock_pulidas(
        pieza_predeterminadas6,
        cantidad_piezas_terminadas_buen_hombre,
        "buen_hombre_pulido",
        "piezas_finales_defenitivas",
        arbol,
        result,info
        ),).grid(row=9, column=1,padx=5, sticky="w")

    ttk.Separator(box1, orient="horizontal", style="Separador2.TSeparator").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    ttk.Label(box1, text="Consultas De Stock", style="WhiteOnRed.TLabel",).grid(row=11, column=0, sticky="w")

    ttk.Button(box1, text="Stock Total"  ,style = "Estilo9.TButton",command=lambda: mostrar_datos(arbol, "buen_hombre_pulido", info)).grid(row=12, column=0, columnspan=2)

    botonera = ttk.Frame(box1, style='Color.TFrame')
    botonera.grid(row=13, column=0, columnspan=2)

    ttk.Button(
        botonera,
        text="Stock 300",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("buen_hombre_pulido", "330", arbol, info),
    ).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(
        botonera,
        text="Stock 330",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("buen_hombre_pulido", "300", arbol, info),
    ).grid(row=0, column=1, padx=5, pady=5)
    ttk.Button(
        botonera,
        text="Resto De Piezas",
        style = "Estilo9.TButton",
        command=lambda: mostrar_datos_especifico("buen_hombre_pulido", "250", arbol, info),
    ).grid(row=0, column=2, padx=5, pady=5)

    ttk.Separator(box1, orient="horizontal", style="Separador1.TSeparator").grid(
        row=14, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )
    
    

    
#0000000000000000000000000niquelado0000000000000000000000000000000000000

    box5 = ttk.Frame(box2, style='Color.TFrame')
    box5.grid(row=16, column=0 ,columnspan=3)
    
    ttk.Label(box5, text="Niquelado", style="WhiteOnRed.TLabel",font=("Arial", 20, "bold")).grid(row=0, column=1, columnspan=1)
    
    ttk.Button(
        box5,
        text="Stock en bruto",
        style="Estilo2.TButton",
        command=lambda: mostrar(arbol, "piezas_del_fundicion", "niquelado", info),
    ).grid(row=1, column=0, padx=1, pady=1)
    
    ttk.Button(
        box5,
        text="Stock en fabrica",
        style="Estilo2.TButton",
        command=lambda: mostrar(arbol, "piezas_finales_defenitivas", "niquelado", info),
    ).grid(row=1, column=1, padx=1, pady=1)
    
    ttk.Button(
        box5,
        text="Stock en niquelado",
        style="Estilo2.TButton",
        command= lambda: mostrar(arbol, "pieza_retocadas", "niquelado", info)
    ).grid(row=1, column=2, padx=1, pady=1)
    
    ttk.Label(box5, text="Piezas A Niquelar", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=2, column=0, columnspan=2)
    ttk.Label(box5, text="Piezas", style="WhiteOnRed.TLabel").grid(row=3, column=0, sticky="w")
    
    lista_piezas = ttk.Combobox(box5, values=niquelado, state="readonly")
    lista_piezas.grid(row=3, column=1, sticky="w")
    
    ttk.Label(box5, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=4, column=0, sticky="w")
    
    cantidad_a_niquelar = ttk.Entry(box5,style='WhiteOnRed.TEntry')
    cantidad_a_niquelar.grid(row=4, column=1, sticky="w",pady=5)

    tk.Button(
        box5,
        text="Enviar",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: envios_de_bruto_a_niquelar(
            lista_piezas.get(), cantidad_a_niquelar, result, arbol, "niquelado"
        ),
    ).grid(row=5, column=1, columnspan=2, padx=5, pady=5,sticky="w")

    ttk.Separator(box5, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    ttk.Label(box5, text="Piezas Terminadas", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=2)
    ttk.Label(box5, text="Piezas", style="WhiteOnRed.TLabel").grid(row=8, column=0, sticky="w")
    
    lista_piezas_nique = ttk.Combobox(box5, values=niquelado, state="readonly")
    lista_piezas_nique.grid(row=8, column=1, sticky="w")
    
    ttk.Label(box5, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=9, column=0, sticky="w")
    
    cantidad_a_niquelado = ttk.Entry(box5,style='WhiteOnRed.TEntry')
    cantidad_a_niquelado.grid(row=9, column=1, sticky="w" ,pady=5)

    tk.Button(
        box5,
        text="Resivido",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: envios_de_niquelado_a_fabrica(lista_piezas_nique.get(),cantidad_a_niquelado ,result, arbol, "niquelado")
        ).grid(row=10, column=1, columnspan=2, padx=5, pady=5, sticky="w")

    ttk.Separator(box5, orient="horizontal", style="Separador2.TSeparator").grid(
        row=11, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )    
    
    
#30000000000000000000000000000000Pintura000000000000000000000000000000000000000000000
    
    box6 = ttk.Frame(box3, style='Color.TFrame')
    box6.grid(row=17, column=0, columnspan=3)
    
    ttk.Label(box6, text="Pintura", style="WhiteOnRed.TLabel",font=("Arial", 20, "bold")).grid(row=0, column=1, columnspan=1)

    ttk.Button(
        box6,
        text="Stock en fabrica",
        style="Estilo2.TButton",
        command=lambda: mostrar(arbol, "piezas_del_fundicion", "pintor", info),
    ).grid(row=1, column=0)
    ttk.Button(
        box6,
        text="Stock Terminado",
        style="Estilo2.TButton",
        command=lambda: mostrar(arbol, "piezas_finales_defenitivas", "pintor", info),
    ).grid(row=1, column=1)
    ttk.Button(
        box6,
        text="Stock en Pintura",
        style="Estilo2.TButton",
        command=lambda: mostrar(arbol, "pieza_retocadas", "pintor", info),
    ).grid(row=1, column=2)

    ttk.Separator(box6, orient="horizontal", style="Separador2.TSeparator").grid(
        row=2, column=0, columnspan=3, sticky="ew", padx=5, pady=5
    )
    ttk.Label(box6, text="Envios A Pintura",font=("Arial", 12, "bold"), style="WhiteOnRed.TLabel").grid(row=3, column=0, columnspan=2)

    ttk.Label(box6, text="Tipo", style="WhiteOnRed.TLabel",).grid(row=4, column=0, sticky="ew")
    modelo = ttk.Combobox(box6, values=modelo_piezas,state="readonly")
    modelo.grid(row=4, column=1, sticky="w")

    ttk.Label(box6, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=5, column=0, sticky="ew")
    enviar_a_pintura = ttk.Entry(box6, width=10, style='WhiteOnRed.TEntry', )
    enviar_a_pintura.grid(row=5, column=1, sticky="ew", pady=2)

    tk.Button(
        box6,
        text="Enviar Bases",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: envios_de_bruto_a_pulido(
            modelo.get(), enviar_a_pintura, result, arbol, "pintor"
        ),
    ).grid(row=6, column=1)
    
    ttk.Label(box6, text="Envios de cabezales",font=("Arial", 11, "bold"), style="WhiteOnRed.TLabel",).grid(row=7, column=0)

    cantidad_cabezales = ttk.Entry(box6, width=10,style='WhiteOnRed.TEntry')
    cantidad_cabezales.grid(row=7, column=1, pady=5, sticky="s")

    tk.Button(
        box6,
        text="Enviar Cabezales",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        command=lambda: envios_de_bruto_cabezal("cabezal_pintura", cantidad_cabezales, result, arbol, "pintor"),
        font=('Helvetica', 8, "bold")).grid(row=9, column=1, columnspan=1)

    ttk.Separator(box6, orient="horizontal", style="Separador2.TSeparator").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    ttk.Label(box6, text="Bases Resibidas",font=("Arial", 12, "bold"), style="WhiteOnRed.TLabel",).grid(row=11, column=0, columnspan=2)

    ttk.Label(box6, text="Tipo", style="WhiteOnRed.TLabel",).grid(row=12, column=0)
    modelo_pintur = ttk.Combobox(box6, values=modelo_piezas, state="readonly")
    modelo_pintur.grid(row=12, column=1)

    ttk.Label(box6, text="Cantidad", style="WhiteOnRed.TLabel",).grid(row=13, column=0)
    resibe_a_pintura = ttk.Entry(box6, width=10, style='WhiteOnRed.TEntry')
    resibe_a_pintura.grid(row=13, column=1, sticky="ew", pady=3)

    tk.Button(
        box6,
        text="Cantida Resibida",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: envios_pulido_a_fabrica(modelo_pintur.get(),resibe_a_pintura, result, arbol, "pintor" )
    ).grid(row=14, column=1, pady=2)

    ttk.Label(box6, text="Cabezales Resividos", style="WhiteOnRed.TLabel",).grid(row=15, column=0, sticky="s")

    cantidad_resibida_cabezales = ttk.Entry(box6, width=10,style='WhiteOnRed.TEntry')
    cantidad_resibida_cabezales.grid(row=15, column=1, pady=5)

    tk.Button(
        box6,
        text="Resivir Cabzales",
        background="blue",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: envios_pulido_a_fabrica_cabezal("cabezal_pintura", cantidad_resibida_cabezales, result, arbol, "pintor")
    ).grid(row=16, column=1)

    ttk.Separator(box6, orient="horizontal", style="Separador2.TSeparator").grid(
        row=17, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )


#(((((((((((((((((((((((((((((((((((((Stock )))))))))))))))))))))))))))))))))))))
    box4 = ttk.Frame(box1, style='Color.TFrame')
    box4.grid(row=16, column=0, sticky="n", columnspan=2)
    

    botonera2 = ttk.Frame(box4, style='Color.TFrame')
    botonera2.grid(row=0, column=0, columnspan=2)

    ttk.Label(botonera2, text="Stock en Fabrica",font=("Arial", 18, "bold"), style="WhiteOnRed.TLabel").grid(row=0, column=0,columnspan=2)
    ttk.Button(
        botonera2,
        style="Estilo5.TButton",
        text="Stock Total Bruto",
        command=lambda: mostrar_datos(arbol, "piezas_del_fundicion", info),
    ).grid(row=1, column=0, padx=3, pady=5)
    ttk.Button(
        botonera2,
        style="Estilo5.TButton",
        text="Stock Total Pulido",
        command=lambda: mostrar(arbol, "piezas_finales_defenitivas", "pulido", info),
    ).grid(row=1, column=1, padx=3, pady=5)

    ttk.Separator(botonera2, orient="horizontal", style="Separador2.TSeparator").grid(
        row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

#99999999999999999999999999999999999Observaciones ###############################################

    box7 = ttk.Frame(box1, style='Color.TFrame')
    box7.grid(row=17, column=0, columnspan=2)
    
    ttk.Label(box7, text="Observaciones", style="WhiteOnRed.TLabel",font=("Arial", 15, "bold")).grid(row=0, column=1, sticky="w")
    caja_texto = tk.Text(box7, height=6, width=30,)
    caja_texto.grid(row=1, column=1, columnspan=1)
    ttk.Button(
        box7, text="Enviar", style="Estilo4.TButton", command=lambda: agregar_a_lista_tarea(caja_texto, result)
    ).grid(row=2, column=1, sticky="e", pady=5, padx=5)
