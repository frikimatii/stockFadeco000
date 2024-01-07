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
    pestania = ttk.Frame(notebook)
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="session Provedores")

    caja1 = ttk.Frame(pestania)
    caja1.grid(row=0, column=0, padx=5, pady=5)

    tk.Label(caja1, text="PROVEDORES").grid(row=0, column=0)
    tk.Label(caja1, text=" Tabla de datos").grid(row=1, column=0, sticky="w")
    arbol = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    arbol.heading(
        "Pieza", text="Pieza", command=lambda: sort_column(arbol, "Pieza", False)
    )
    arbol.heading(
        "Cantidad",
        text="Cantidad",
        command=lambda: sort_column_numeric(arbol, "Cantidad", False),
    )
    arbol.column("#0", width=0, stretch=tk.NO)
    arbol.column("Pieza", anchor=tk.W, width=170)
    arbol.column("Cantidad", anchor=tk.W, width=90, command=lambda: sort_column(arbol, "Cantidad", False))
    arbol.config(height=20)
    arbol.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")

    arbol.tag_configure("#ff6868", background="#ff6868")
    arbol.tag_configure("#87ff79", background="#87ff79")

    
    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, padx=3, pady=3)

    caja2 = ttk.Frame(pestania)
    caja2.grid(row=0, column=1)

    tk.Label(caja2, text="Pulidor").grid(row=0, column=0, sticky="w")
    # ----------------------------------------------------------------#
    tk.Label(caja2, text="Envios A Carmelo").grid(row=1, column=0)
    tk.Label(caja2, text="Pieza").grid(row=2, column=0, sticky="w")
    tk.Label(caja2, text="Cantidad").grid(row=2, column=1)

    pieza_predeterminadas = ttk.Combobox(caja2, values=piezas_carmelo)
    pieza_predeterminadas.grid(row=3, column=0)

    cantidad_agregar_carmelo = tk.Entry(caja2, width=10)
    cantidad_agregar_carmelo.grid(row=3, column=1)

    tk.Button(
        caja2,
        text="Enviar Piezas",
        command=lambda: enviar_piezas_a_pulido(
            pieza_predeterminadas,
            cantidad_agregar_carmelo,
            "carmelo_pulido",
            arbol,
            result,
        ),
    ).grid(row=4, column=1)

    # ___________________consulta stock____________________________________#
    tk.Label(caja2, text="Consultas De Stock").grid(row=5, column=0, sticky="w")

    tk.Button(
        caja2,
        text="Stock Total",
        command=lambda: mostrar_datos(arbol, "carmelo_pulido"),
    ).grid(row=6, column=0, columnspan=2)

    botonera = ttk.Frame(caja2)
    botonera.grid(row=7, column=0, columnspan=2)

    tk.Button(
        botonera,
        text="Stock 330",
        command=lambda: mostrar_datos_especifico("carmelo_pulido", "330", arbol),
    ).grid(row=0, column=0)
    tk.Button(
        botonera,
        text="Stock 300",
        command=lambda: mostrar_datos_especifico("carmelo_pulido", "300", arbol),
    ).grid(row=0, column=1)
    tk.Button(
        botonera,
        text="Resto De Piezas",
        command=lambda: mostrar_datos_especifico("carmelo_pulido", "all", arbol),
    ).grid(row=0, column=2)

    # _---------------------------------------------------------#
    tk.Label(caja2, text="Piezas Resibidas").grid(row=8, column=0)
    tk.Label(caja2, text="Pieza").grid(row=9, column=0, sticky="w")
    tk.Label(caja2, text="Cantidad").grid(row=9, column=1)

    pieza_predeterminadas1 = ttk.Combobox(caja2, values=piezas_carmelo)
    pieza_predeterminadas1.grid(row=10, column=0)

    cantidad_piezas_terminadas_carmelo = tk.Entry(caja2, width=10)
    cantidad_piezas_terminadas_carmelo.grid(row=10, column=1)

    tk.Button(
        caja2,
        text="Piezas Terminadas",
        command=lambda: mover_piezas_a_stock_pulidas(
            pieza_predeterminadas1,
            cantidad_piezas_terminadas_carmelo,
            "carmelo_pulido",
            "piezas_finales_defenitivas",
            arbol,
            result,
        ),
    ).grid(row=11, column=1)

    # ------------------------------------------------------------------------------#
    ttk.Separator(caja2, orient="horizontal").grid(
        row=12, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    tk.Label(caja2, text="Envios A Maxi").grid(row=13, column=0)
    tk.Label(caja2, text="Pieza").grid(row=14, column=0, sticky="w")
    tk.Label(caja2, text="Cantidad").grid(row=14, column=1)

    pieza_predeterminadas2 = ttk.Combobox(caja2, values=piezas_maxi)
    pieza_predeterminadas2.grid(row=15, column=0)

    cantidad_agregar_maxi = tk.Entry(caja2, width=10)
    cantidad_agregar_maxi.grid(row=15, column=1)

    tk.Button(
        caja2,
        text="Enviar Piezas",
        command=lambda: enviar_piezas_a_pulido(
            pieza_predeterminadas2, cantidad_agregar_maxi, "maxi_pulido", arbol, result
        ),
    ).grid(row=16, column=1)

    # ___________________consulta stock_________________________________________#
    tk.Label(caja2, text="Consultas De Stock").grid(row=17, column=0, sticky="w")

    tk.Button(
        caja2, text="Stock Total", command=lambda: mostrar_datos(arbol, "maxi_pulido")
    ).grid(row=18, column=0, columnspan=2)

    botonera = ttk.Frame(caja2)
    botonera.grid(row=19, column=0, columnspan=2)

    tk.Button(
        botonera,
        text="Stock 300",
        command=lambda: mostrar_datos_especifico("maxi_pulido", "330", arbol),
    ).grid(row=0, column=0)
    tk.Button(
        botonera,
        text="Stock 330",
        command=lambda: mostrar_datos_especifico("maxi_pulido", "300", arbol),
    ).grid(row=0, column=1)
    tk.Button(
        botonera,
        text="Resto De Piezas",
        command=lambda: mostrar_datos_especifico("maxi_pulido", "250", arbol),
    ).grid(row=0, column=2)

    # _---------------------------------------------------------#
    tk.Label(caja2, text="Piezas Resibidas").grid(row=20, column=0)
    tk.Label(caja2, text="Pieza").grid(row=21, column=0, sticky="w")
    tk.Label(caja2, text="Cantidad").grid(row=21, column=1)

    pieza_predeterminadas4 = ttk.Combobox(caja2, values=piezas_maxi)
    pieza_predeterminadas4.grid(row=22, column=0)

    cantidad_piezas_terminadas_maxi = tk.Entry(caja2, width=10)
    cantidad_piezas_terminadas_maxi.grid(row=22, column=1)

    tk.Button(
        caja2,
        text="Piezas Terminadas",
        command=lambda: mover_piezas_a_stock_pulidas(
            pieza_predeterminadas4,
            cantidad_piezas_terminadas_maxi,
            "maxi_pulido",
            "piezas_finales_defenitivas",
            arbol,
            result,
        ),
    ).grid(row=23, column=1)

    # ------------------------------------------------------------------------------#
    ttk.Separator(caja2, orient="horizontal").grid(
        row=245, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    caja3 = ttk.Frame(pestania)
    caja3.grid(row=0, column=2)

    # 0000----------------------------BUEN HOMBRE ------------------------------------#
    tk.Label(caja3, text="Envios A Buen Hombre").grid(row=1, column=0)
    tk.Label(caja3, text="Pieza").grid(row=2, column=0, sticky="w")
    tk.Label(caja3, text="Cantidad").grid(row=2, column=1)

    pieza_predeterminadas5 = ttk.Combobox(caja3, values=pieza_buen_hombre)
    pieza_predeterminadas5.grid(row=3, column=0)

    cantidad_agregar_buen_hombre = tk.Entry(caja3, width=10)
    cantidad_agregar_buen_hombre.grid(row=3, column=1)

    tk.Button(caja3,
            text="Enviar Piezas",
            command=lambda: enviar_piezas_a_pulido(
            pieza_predeterminadas5,
            cantidad_agregar_buen_hombre,
            "buen_hombre_pulido",
            arbol,
            result,
        ),
    ).grid(row=4, column=1)

    # ___________________consulta stock_________________________________________#
    tk.Label(caja3, text="Consultas De Stock").grid(row=5, column=0, sticky="w")

    tk.Button(caja3, text="Stock Total", command=lambda: mostrar_datos(arbol, "buen_hombre_pulido")).grid(row=6, column=0, columnspan=2)

    botonera = ttk.Frame(caja3)
    botonera.grid(row=7, column=0, columnspan=2)

    tk.Button(
        botonera,
        text="Stock 300",
        command=lambda: mostrar_datos_especifico("buen_hombre_pulido", "330", arbol),
    ).grid(row=0, column=0)
    tk.Button(
        botonera,
        text="Stock 330",
        command=lambda: mostrar_datos_especifico("buen_hombre_pulido", "300", arbol),
    ).grid(row=0, column=1)
    tk.Button(
        botonera,
        text="Resto De Piezas",
        command=lambda: mostrar_datos_especifico("buen_hombre_pulido", "all", arbol),
    ).grid(row=0, column=2)

    # _------------------------------------- --------------------#
    tk.Label(caja3, text="Piezas Resibidas").grid(row=8, column=0)
    tk.Label(caja3, text="Pieza").grid(row=9, column=0, sticky="w")
    tk.Label(caja3, text="Cantidad").grid(row=9, column=1)

    pieza_predeterminadas6 = ttk.Combobox(caja3, values=pieza_buen_hombre)
    pieza_predeterminadas6.grid(row=10, column=0)

    cantidad_piezas_terminadas_buen_hombre = tk.Entry(caja3, width=10)
    cantidad_piezas_terminadas_buen_hombre.grid(row=10, column=1)

    tk.Button(caja3,
        text="Piezas Terminadas",
        command=lambda: mover_piezas_a_stock_pulidas(
        pieza_predeterminadas6,
        cantidad_piezas_terminadas_buen_hombre,
        "buen_hombre_pulido",
        "piezas_finales_defenitivas",
        arbol,
        result,
        ),).grid(row=11, column=1)

    ttk.Separator(caja3, orient="horizontal").grid(
        row=12, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )


    # -----------------------------------stock en fabrica-------------------------------------------#

    botonera2 = ttk.Frame(caja3)
    botonera2.grid(row=13, column=0, columnspan=2)

    tk.Label(botonera2, text="Stock en Fabrica").grid(row=0, column=0)
    tk.Button(
        botonera2,
        text="Stock Total Bruto",
        command=lambda: mostrar_datos(arbol, "piezas_del_fundicion"),
    ).grid(row=1, column=0)
    tk.Button(
        botonera2,
        text="Stock Total Pulido",
        command=lambda: mostrar(arbol, "piezas_finales_defenitivas", "pulido"),
    ).grid(row=1, column=1)

    ttk.Separator(botonera2, orient="horizontal").grid(
        row=3, column=0, columnspan=3, sticky="ew", padx=5, pady=5
    )

    tk.Label(caja3, text="Niquelado").grid(row=14, column=1)
    tk.Button(
        caja3,
        text="Stock en bruto",
        command=lambda: mostrar(arbol, "piezas_del_fundicion", "niquelado"),
    ).grid(row=15, column=0)
    tk.Button(
        caja3,
        text="Stock niquelado",
        command=lambda: mostrar(arbol, "piezas_finales_defenitivas", "niquelado"),
    ).grid(row=15, column=1)
    tk.Label(caja3, text="Piezas").grid(row=16, column=0)
    lista_piezas = ttk.Combobox(caja3, values=niquelado)
    lista_piezas.grid(row=16, column=1)
    tk.Label(caja3, text="Cantidad").grid(row=17, column=0)
    cantidad_a_niquelar = tk.Entry(caja3)
    cantidad_a_niquelar.grid(row=17, column=1)

    tk.Button(
        caja3,
        text="Enviar",
        command=lambda: envios_de_bruto_a_pulido(
            lista_piezas.get(), cantidad_a_niquelar, result, arbol, "niquelado"
        ),
    ).grid(row=18, column=1, columnspan=2)

    ttk.Separator(caja3, orient="horizontal").grid(
        row=19, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    caja4 = tk.Frame(pestania)
    caja4.grid(row=0, column=3)

    tk.Label(caja4, text="Pintura").grid(row=0, column=1, columnspan=2)

    tk.Button(
        caja4,
        text="Stock en fabrica",
        command=lambda: mostrar(arbol, "piezas_del_fundicion", "pintor"),
    ).grid(row=1, column=0)
    tk.Button(
        caja4,
        text="Stock en Pintura",
        command=lambda: mostrar(arbol, "piezas_finales_defenitivas", "pintor"),
    ).grid(row=1, column=1)

    tk.Label(caja4, text="envios de base").grid(row=2, column=1)

    tk.Label(caja4, text="Tipo").grid(row=3, column=0)
    modelo = ttk.Combobox(caja4, values=modelo_piezas)
    modelo.grid(row=4, column=0)

    tk.Label(caja4, text="Cantidad").grid(row=3, column=1)
    enviar_a_pintura = tk.Entry(caja4)
    enviar_a_pintura.grid(row=4, column=1)

    tk.Button(
        caja4,
        text="Enviar",
        command=lambda: envios_de_bruto_a_pulido(
            modelo.get(), enviar_a_pintura, result, arbol, "pintor"
        ),
    ).grid(row=5, column=1)

    tk.Label(caja4, text="envios de cabezales").grid(row=6, column=1)

    cantidad_cabezales = tk.Entry(caja4)
    cantidad_cabezales.grid(row=7, column=0)

    tk.Button(
        caja4,
        text="enviar",
        command=lambda: envios_de_bruto_a_pulido(
            "cabezal_pintura", cantidad_cabezales, result, arbol, "pintor"
        ),
    ).grid(row=7, column=1)

    ttk.Separator(caja4, orient="horizontal").grid(
        row=8, column=0, columnspan=2, sticky="ew", padx=5, pady=5
    )

    tk.Label(caja4, text="Observaciones").grid(row=14, column=0, sticky="w")
    caja_texto = tk.Text(caja4, height=6, width=30)
    caja_texto.grid(row=15, column=0, columnspan=2)
    tk.Button(
        caja4, text="Enviar", command=lambda: agregar_a_lista_tarea(caja_texto, result)
    ).grid(row=16, column=1, sticky="e")
