import tkinter as tk
from tkinter import ttk
from funciones import (
    mostrar_datos_torno,
    mostrar_datos_,
    actualizar_pieza_torno,
    actualizar_caja_torno,
    mostrar_piezas_torno_terminado,
    pulido_cabezal,
    de_enbruto_a_torneado,
    mostrar_cajas_bruto,
    agregar_a_lista_tarea,
    stock_prearmado,
    actualizar_inventario,
    stock_prebases,
    varilla_para_soldar
)

tipo = ["330", "300", "250"]
tipos_de_maquinas = ["inox_330", "inox_300", "inox_250", "pintada_330", "pintada_300"]
cajas_torono = ["caja_torneado_330", "caja_torneado_300", "caja_torneado_250"]
piezas_a_torner_lista = [
    "manchon",
    "manchon_250",
    "eje_250",
    "eje",
    "rueditas",
    "tornillo_guia",
    "carros",
    "movimientos",
    "carros_250",
]
motores_finales330 = [
    "caja_torneado_330",
    "eje",
    "manchon",
    "ruleman_1",
    "ruleman_2",
    "corona_330",
    "seguer",
    "sinfin",
    "motores_220w",
]
modelo330 = {
    "caja_torneado_330": 1,
    "eje": 1,
    "manchon": 1,
    "ruleman_1": 1,
    "ruleman_2": 1,
    "corona_330": 1,
    "seguer": 1,
    "sinfin": 1,
    "motores_220w": 1,
}
motores_finales300 = [
    "caja_torneado_300",
    "eje",
    "manchon",
    "ruleman_1",
    "ruleman_2",
    "corona_300",
    "seguer",
    "sinfin",
    "motores_220w",
]
modelo300 = {
    "caja_torneado_300": 1,
    "eje": 1,
    "manchon": 1,
    "ruleman_1": 1,
    "ruleman_2": 1,
    "corona_300": 1,
    "seguer": 1,
    "sinfin": 1,
    "motores_220w": 1,
}
motores_finales250 = [
    "caja_torneado_250",
    "eje",
    "manchon",
    "ruleman_1",
    "ruleman_2",
    "corona_250",
    "seguer",
    "sinfin",
    "motores250_220w",
]
modelo250 = {
    "caja_torneado_250": 1,
    "eje": 1,
    "manchon": 1,
    "ruleman_1": 1,
    "ruleman_2": 1,
    "corona_250": 1,
    "seguer": 1,
    "sinfin": 1,
    "motores250_220w": 1,
}
piezas_a_augeriar_lista = ["cuadrado_regulador"]
piezas_lijadas = ["base_afilador_300", "base_afilador_330", "base_afilador_250", "carcaza_afilador" ]
piezas_prenza = ["guia_U", "eje_corto", "eje_largo"]
cabezal_inox = ["cabezal_inox"]
varillas_soldar = ["varilla_330", "varilla_300", "varilla_250"]


def mecanizado(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

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
    result.grid(row=3, column=0, padx=3, pady=3)

    caja3 = ttk.Frame(pestania)
    caja3.grid(row=2, column=1)

    torno = ttk.Frame(caja3)
    torno.grid(row=0, column=1)

    tk.Label(torno, text="Torno").grid(row=0, column=0)

    tk.Label(torno, text="Piezas Terminadas").grid(row=1, column=0)
    piezas_a_torner = ttk.Combobox(torno, values=piezas_a_torner_lista)
    piezas_a_torner.grid(row=2, column=0)

    tk.Label(torno, text="Cantidad").grid(row=1, column=1)
    cantidad_torneada = tk.Entry(torno)
    cantidad_torneada.grid(row=2, column=1)

    ttk.Button(
        torno,
        text="Enviar",
        command=lambda: actualizar_pieza_torno(
            piezas_a_torner,
            cantidad_torneada,
            result,
            "piezas_finales_defenitivas",
            arbol,
        ),
    ).grid(row=3, column=1)

    ttk.Separator(torno, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    stock_torno = tk.Frame(torno)
    stock_torno.grid(row=5, column=0)

    tk.Label(stock_torno, text="Stock del Torno").grid(row=0, column=0)
    ttk.Button(
        stock_torno,
        text="Stock Bruto",
        command=lambda: mostrar_datos_torno(arbol, "piezas_del_fundicion"),
    ).grid(row=1, column=0)
    ttk.Button(
        stock_torno,
        text="Stock Terminado",
        command=lambda: mostrar_piezas_torno_terminado(arbol),
    ).grid(row=1, column=1)

    ttk.Separator(torno, orient="horizontal").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    tk.Label(torno, text="Torneado de cajas").grid(row=7, column=0)
    tk.Label(torno, text="Cajas Terminadas").grid(row=8, column=0)
    caja_a_torner = ttk.Combobox(torno, values=cajas_torono)
    caja_a_torner.grid(row=9, column=0)

    tk.Label(torno, text="Cantidad").grid(row=8, column=1)
    cantidad_caja_torneada = tk.Entry(torno)
    cantidad_caja_torneada.grid(row=9, column=1)

    ttk.Button(
        torno,
        text="Enviar",
        command=lambda: de_enbruto_a_torneado(
            caja_a_torner, cantidad_caja_torneada, result
        ),
    ).grid(row=10, column=1)
    ttk.Button(
        torno, text="Stock Terminado", command=lambda: mostrar_datos_(arbol)
    ).grid(row=11, column=0)
    ttk.Button(
        torno, text="Stock Bruto", command=lambda: mostrar_cajas_bruto(arbol)
    ).grid(row=11, column=1)

    ttk.Separator(torno, orient="horizontal").grid(
        row=12, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    tk.Label(torno, text="Obsebaciones").grid(row=13, column=0)
    info_torno = tk.Text(torno, height=6, width=25)
    info_torno.grid(row=14, column=0, columnspan=1)
    tk.Button(
        torno, text="Enviar", command=lambda: agregar_a_lista_tarea(info_torno, result)
    ).grid(row=15, column=0, sticky="e")

#--------------------------------
        
    mecanizado_de_piezas = tk.Frame(pestania)
    mecanizado_de_piezas.grid(row=2, column=2)   
    
#____________________________________augeriado_______________________________________

    caja2 = tk.Frame(mecanizado_de_piezas)
    caja2.grid(row=2, column=2)
    
    tk.Label(caja2, text="Augeriado de Piezas").grid(row=0, column=0)
    
    tk.Label(caja2, text="Piezas Augeriadas").grid(row=1, column=0)
    piezas_a_augerias = ttk.Combobox(caja2, values=piezas_a_augeriar_lista)
    piezas_a_augerias.grid(row=2, column=0)

    tk.Label(caja2, text="Cantidad").grid(row=1, column=1)
    cantidad_augeriada = tk.Entry(caja2)
    cantidad_augeriada.grid(row=2, column=1)

    ttk.Button(
        caja2,
        text="Enviar",
        command=lambda: actualizar_pieza_torno(
            piezas_a_augerias,
            cantidad_augeriada,
            result,
            "piezas_finales_defenitivas",
            arbol,
        ),
    ).grid(row=3, column=1)

    ttk.Separator(caja2, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    
#=-==========================Lijado=============================
    
    caja3 = tk.Frame(mecanizado_de_piezas)
    caja3.grid(row=3, column=2)
    
    tk.Label(caja3, text="Lijado de Piezas").grid(row=0, column=0)
    
    tk.Label(caja3, text="Piezas lijada").grid(row=1, column=0)
    piezas_a_lijada = ttk.Combobox(caja3, values=piezas_lijadas)
    piezas_a_lijada.grid(row=2, column=0)

    tk.Label(caja3, text="Cantidad").grid(row=1, column=1)
    cantidad_lijada = tk.Entry(caja3)
    cantidad_lijada.grid(row=2, column=1)

    ttk.Button(
        caja3,
        text="Enviar",
        command=lambda: actualizar_pieza_torno(
            piezas_a_lijada,
            cantidad_lijada,
            result,
            "piezas_finales_defenitivas",
            arbol,
        ),
    ).grid(row=3, column=1)

    ttk.Separator(caja3, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    
#=----------------------------Prenza---------------------------------
    
    caja4 = tk.Frame(mecanizado_de_piezas)
    caja4.grid(row=4, column=2)
    
    tk.Label(caja4, text="Prenza").grid(row=0, column=0)
    
    tk.Label(caja4, text="Piezas Prenza").grid(row=1, column=0)
    piezas_a_prenza = ttk.Combobox(caja4, values=piezas_prenza)
    piezas_a_prenza.grid(row=2, column=0)

    tk.Label(caja4, text="Cantidad").grid(row=1, column=1)
    cantidad_prenza = tk.Entry(caja4)
    cantidad_prenza.grid(row=2, column=1)

    ttk.Button(
        caja4,
        text="Enviar",
        command=lambda: actualizar_pieza_torno(
            piezas_a_prenza,
            cantidad_prenza,
            result,
            "piezas_finales_defenitivas",
            arbol,
        ),
    ).grid(row=3, column=1)

    ttk.Separator(caja4, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    
    
#------------------------pulido en fabrica---------------------------
    
    caja5 = tk.Frame(mecanizado_de_piezas)
    caja5.grid(row=5, column=2)
    
    tk.Label(caja5, text="Pulido en fabrica").grid(row=0, column=0)
    
    tk.Label(caja5, text="Piezas a Pulir").grid(row=1, column=0)
    piezas_a_pulir = ttk.Combobox(caja5, values=cabezal_inox)
    piezas_a_pulir.grid(row=2, column=0)

    tk.Label(caja5, text="Cantidad").grid(row=1, column=1)
    cantidad_pulido = tk.Entry(caja5)
    cantidad_pulido.grid(row=2, column=1)

    ttk.Button(
        caja5,
        text="Enviar",
        command=lambda: actualizar_pieza_torno(
            piezas_a_pulir,
            cantidad_pulido,
            result,
            "piezas_finales_defenitivas",
            arbol,
        ),
    ).grid(row=3, column=1)

    ttk.Separator(caja5, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    
    tk.Label(caja5, text="Consulta de Cabezales").grid(row=5, column=0)
    
    tk.Button(caja5, text="Cabezales Sin Pulir").grid(row=6, column=0)
    tk.Button(caja5, text="Cabezales Pulidos").grid(row=6, column=1)
    
    ttk.Separator(caja5, orient="horizontal").grid(
        row=7, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    
#-----------------------SOLDADO EN FABRICA-----------------------------------------

    caja6 = tk.Frame(mecanizado_de_piezas)
    caja6.grid(row=6, column=2)
    
    tk.Label(caja6, text="Soldado en fabrica").grid(row=0, column=0)
    
    tk.Label(caja6, text="Piezas a soldar").grid(row=1, column=0)
    piezas_a_varilla = ttk.Combobox(caja6, values=varillas_soldar)
    piezas_a_varilla.grid(row=2, column=0)

    tk.Label(caja6, text="Cantidad").grid(row=1, column=1)
    cantidad_varilla = tk.Entry(caja6)
    cantidad_varilla.grid(row=2, column=1)

    ttk.Button(
        caja6,
        text="Enviar",
        command=lambda: varilla_para_soldar(cantidad_varilla, piezas_a_varilla.get(), result),
    ).grid(row=3, column=1)

    ttk.Separator(caja6, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    ) 

#-------------------------------------------
