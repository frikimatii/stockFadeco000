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
    varilla_para_soldar,
    mostrar_datos_mecanizado,
    varilla_soldador,
    sort_column,
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
cabezal_inox = ["cabezal_inox", "cabezal_250"]
varillas_soldar = ["varilla_330", "varilla_300", "varilla_250"]


def mecanizado(notebook):
    pestania = ttk.Frame(notebook, style='Color.TFrame')
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )
    
    
    notebook.style = ttk.Style()
    notebook.style.configure('Color.TFrame', background='#192965', radius=20, borderwidth=10)  # Puedes ajustar el color
    notebook.style.configure('WhiteOnRed.TLabel', background='#192965', foreground='white')  # Puedes ajustar el color
    notebook.style.configure('WhiteOnRed.TEntry', fieldbackground='black', foreground='black')  # Puedes ajustar el color
    notebook.style.configure('WhiteOnRed.TCombobox', fieldbackground='#192965', foreground='white')  # Puedes ajustar el color
    notebook.style.configure("Estilo4.TButton", foreground='#192965', background="yellow", borderwidth=10)   
    notebook.style.configure("Separador2.TSeparator", background="blue")
    notebook.style.configure("Separador1.TSeparator", background="yellow")

        

    notebook.add(pestania, text="Mecanizado")
    
    ttk.Label(pestania, text="Mecanizado", style="WhiteOnRed.TLabel", font=("Verdana", 30, "bold")).grid(row=1, column=0, columnspan=4)
    caja1 = ttk.Frame(pestania, style='Color.TFrame')
    caja1.grid(row=2, column=0, sticky="n")

    info = ttk.Label(caja1, text="Mostrar Datos",style='WhiteOnRed.TLabel', font=("Arial", 12, "bold"))
    info.grid(row=1, column=0, sticky="w")

    arbol = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    arbol.heading("Pieza", text="Pieza")
    arbol.heading("Cantidad", text="Cantidad", command=lambda: sort_column(arbol, "Cantidad", False),)
    arbol.column("#0", width=0, stretch=tk.NO)
    arbol.column("Pieza", anchor=tk.W, width=170)
    arbol.column("Cantidad", anchor=tk.W, width=90)
    arbol.config(height=25)
    arbol.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")

    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, padx=3, pady=3)

    caja3 = ttk.Frame(pestania, style='Color.TFrame')
    caja3.grid(row=2, column=1)

    torno = ttk.Frame(caja3, style='Color.TFrame')
    torno.grid(row=0, column=1, padx=15, pady=5, columnspan=2)

    ttk.Label(torno, text="Torno", style="WhiteOnRed.TLabel", font=("Verdana", 25, "bold")).grid(row=0, column=0, columnspan=2)

    ttk.Label(torno, text="Piezas A Tornear",style='WhiteOnRed.TLabel').grid(row=1, column=0)
    piezas_a_torner = ttk.Combobox(torno, values=piezas_a_torner_lista)
    piezas_a_torner.grid(row=2, column=0)

    ttk.Label(torno, text="Cantidad",style='WhiteOnRed.TLabel').grid(row=1, column=1)
    cantidad_torneada = ttk.Entry(torno, width=15, style='WhiteOnRed.TEntry')
    cantidad_torneada.grid(row=2, column=1)

    tk.Button(
        torno,
        text="Tornear",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza_torno(
            piezas_a_torner,
            cantidad_torneada,
            result,
            "piezas_finales_defenitivas",
            arbol,info
        ),
    ).grid(row=3, column=1, padx=5, pady=5)

    ttk.Separator(torno, orient="horizontal", style="Separador2.TSeparator").grid(
        row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    stock_torno = ttk.Frame(torno, style='Color.TFrame')
    stock_torno.grid(row=5, column=0, columnspan=2)
    ttk.Label(stock_torno, text="Stock del Torno", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_torno,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command=lambda: mostrar_datos_torno(arbol, "piezas_del_fundicion", info),
    ).grid(row=1, column=0, pady=5, padx=3)
    ttk.Button(
        stock_torno,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command=lambda: mostrar_piezas_torno_terminado(arbol, info),
    ).grid(row=1, column=1, pady=5, padx=3)

    ttk.Separator(torno, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    ttk.Label(torno, text="Torneado de cajas", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=7, column=0, columnspan=2)
    ttk.Label(torno, text="Cajas Terminadas", style="WhiteOnRed.TLabel").grid(row=8, column=0)
    caja_a_torner = ttk.Combobox(torno, values=cajas_torono)
    caja_a_torner.grid(row=9, column=0)

    ttk.Label(torno, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=8, column=1)
    cantidad_caja_torneada = ttk.Entry(torno ,width=15, style='WhiteOnRed.TEntry')
    cantidad_caja_torneada.grid(row=9, column=1)

    tk.Button(
        torno,
        text="Tornear",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: de_enbruto_a_torneado(
            caja_a_torner, cantidad_caja_torneada, result
        ),
    ).grid(row=10, column=1, padx=5, pady=5)
    
    stock_torneado = ttk.Frame(torno, style='Color.TFrame')
    stock_torneado.grid(row=11, column=0,columnspan=2)
    ttk.Button(
        stock_torneado, text="Stock Terminado",style="Estilo4.TButton", command=lambda: mostrar_datos_(arbol)
    ).grid(row=0, column=0, padx=5, pady=5)
    ttk.Button(
        stock_torneado, text="Stock Bruto",style="Estilo4.TButton", command=lambda: mostrar_cajas_bruto(arbol)
    ).grid(row=0, column=1, padx=5, pady=5)

    ttk.Separator(torno, orient="horizontal", style="Separador2.TSeparator").grid(
        row=12, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    ttk.Label(torno, text="Obsebaciones", style="WhiteOnRed.TLabel", font=("Arial", 12, "bold")).grid(row=13, column=0)
    info_torno = tk.Text(torno, height=6, width=25)
    info_torno.grid(row=14, column=0, columnspan=2)
    tk.Button(
        torno,
        text="Enviar", 
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: agregar_a_lista_tarea(info_torno, result)
    ).grid(row=15, column=0, sticky="e")

#--------------------------------
        
    mecanizado_de_piezas = ttk.Frame(pestania, style='Color.TFrame')
    mecanizado_de_piezas.grid(row=2, column=2, padx=7, pady=7)   
    
#____________________________________augeriado_______________________________________

    caja2 = ttk.Frame(mecanizado_de_piezas, style='Color.TFrame')
    caja2.grid(row=2, column=2, pady=20)
    
    ttk.Label(caja2, text="Aujugeriado de Piezas", style="WhiteOnRed.TLabel", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
    
    ttk.Label(caja2, text="Piezas Augeriadas", style="WhiteOnRed.TLabel").grid(row=1, column=0)
    piezas_a_augerias = ttk.Combobox(caja2, values=piezas_a_augeriar_lista)
    piezas_a_augerias.grid(row=2, column=0)

    ttk.Label(caja2, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=1)
    cantidad_augeriada = tk.Entry(caja2 ,width=15)
    cantidad_augeriada.grid(row=2, column=1)

    tk.Button(
        caja2,
        text="Enviar",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza_torno(
            piezas_a_augerias,
            cantidad_augeriada,
            result,
            "piezas_finales_defenitivas",
            arbol,info
        ),
    ).grid(row=3, column=1)
    
    stock_aujeriado = ttk.Frame(caja2, style='Color.TFrame')
    stock_aujeriado.grid(row=4, column=0, columnspan=2)
    ttk.Label(stock_aujeriado, text="Stock del Piezas", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_aujeriado,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, piezas_a_augeriar_lista, "Agujeriado", "piezas_del_fundicion")
    ).grid(row=1, column=0, pady=5, padx=3)
    ttk.Button(
        stock_aujeriado,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, piezas_a_augeriar_lista, "Agujeriado", "piezas_finales_defenitivas")
    ).grid(row=1, column=1, pady=5, padx=3)

    ttk.Separator(caja2, orient="horizontal", style="Separador1.TSeparator").grid(
        row=5, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    
    ttk.Separator(caja2, orient="vertical", style="SeparadorVertical.TSeparator").grid(
    row=0, column=2, rowspan=6, sticky="ns", padx=5)
#=-==========================Lijado=============================
    
    caja3 = ttk.Frame(mecanizado_de_piezas, style='Color.TFrame')
    caja3.grid(row=3, column=2, pady=20)
    
    ttk.Label(caja3, text="Lijado de Piezas", style="WhiteOnRed.TLabel", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
    
    ttk.Label(caja3, text="Piezas lijada", style="WhiteOnRed.TLabel").grid(row=1, column=0)
    piezas_a_lijada = ttk.Combobox(caja3, values=piezas_lijadas)
    piezas_a_lijada.grid(row=2, column=0)

    ttk.Label(caja3, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=1)
    cantidad_lijada = ttk.Entry(caja3 ,width=15)
    cantidad_lijada.grid(row=2, column=1)

    tk.Button(
        caja3,
        text="Enviar",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza_torno(
            piezas_a_lijada,
            cantidad_lijada,
            result,
            "piezas_finales_defenitivas",
            arbol,info
        ),
    ).grid(row=3, column=1)
    
    stock_lijado = ttk.Frame(caja3, style='Color.TFrame')
    stock_lijado.grid(row=4, column=0, columnspan=2)
    ttk.Label(stock_lijado, text="Stock del Lijado", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_lijado,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, piezas_lijadas, "Lijado","piezas_del_fundicion")
    ).grid(row=1, column=0, pady=5, padx=3)
    ttk.Button(
        stock_lijado,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, piezas_lijadas, "Lijado", "piezas_finales_defenitivas")
    ).grid(row=1, column=1, pady=5, padx=3)


    ttk.Separator(caja3, orient="horizontal", style="Separador1.TSeparator").grid(
        row=5, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    ttk.Separator(caja3, orient="vertical", style="SeparadorVertical.TSeparator").grid(
    row=0, column=2, rowspan=6, sticky="ns", padx=5)
#=--------------------------balancin---------------------------------
    
    caja4 = ttk.Frame(mecanizado_de_piezas, style='Color.TFrame')
    caja4.grid(row=4, column=2, pady=20)
    
    ttk.Label(caja4, text="Balancin", style="WhiteOnRed.TLabel", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
    
    ttk.Label(caja4, text="Piezas Balancin", style="WhiteOnRed.TLabel").grid(row=1, column=0)
    piezas_a_prenza = ttk.Combobox(caja4, values=piezas_prenza)
    piezas_a_prenza.grid(row=2, column=0)

    ttk.Label(caja4, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=1)
    cantidad_prenza = ttk.Entry(caja4 ,width=15)
    cantidad_prenza.grid(row=2, column=1)

    tk.Button(
        caja4,
        text="Enviar",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza_torno(
            piezas_a_prenza,
            cantidad_prenza,
            result,
            "piezas_finales_defenitivas",
            arbol,info
        ),
    ).grid(row=3, column=1)
    
    stock_balancin = ttk.Frame(caja4, style='Color.TFrame')
    stock_balancin.grid(row=4, column=0, columnspan=2)
    ttk.Label(stock_balancin, text="Stock del Piezas", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_balancin,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, piezas_prenza, "Balancin", "piezas_del_fundicion")
    ).grid(row=1, column=0, pady=5, padx=3)
    ttk.Button(
        stock_balancin,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, piezas_prenza, "Balancin", "piezas_finales_defenitivas")
    ).grid(row=1, column=1, pady=5, padx=3)

    ttk.Separator(caja4, orient="horizontal", style="Separador1.TSeparator").grid(
        row=5, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    ttk.Separator(caja4, orient="vertical", style="SeparadorVertical.TSeparator").grid(
    row=0, column=2, rowspan=5, sticky="ns", padx=5)
    
#------------------------pulido en fabrica---------------------------
    
    caja5 = ttk.Frame(mecanizado_de_piezas, style='Color.TFrame')
    caja5.grid(row=3, column=3, pady=20)
    
    ttk.Label(caja5, text="Pulido en fabrica", style="WhiteOnRed.TLabel", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
    
    ttk.Label(caja5, text="Piezas a Pulir", style="WhiteOnRed.TLabel").grid(row=1, column=0)
    piezas_a_pulir = ttk.Combobox(caja5, values=cabezal_inox)
    piezas_a_pulir.grid(row=2, column=0)

    ttk.Label(caja5, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=1)
    cantidad_pulido = ttk.Entry(caja5 ,width=15)
    cantidad_pulido.grid(row=2, column=1)

    tk.Button(
        caja5,
        text="Enviar",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza_torno(
            piezas_a_pulir,
            cantidad_pulido,
            result,
            "piezas_finales_defenitivas",
            arbol,info
        ),
    ).grid(row=3, column=1)

    stock_pulido = ttk.Frame(caja5, style='Color.TFrame')
    stock_pulido.grid(row=4, column=0, columnspan=2)
    ttk.Label(stock_pulido, text="Stock del Piezas", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_pulido,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, cabezal_inox, "Pulido", "piezas_del_fundicion")
    ).grid(row=1, column=0, pady=5, padx=3)
    ttk.Button(
        stock_pulido,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, cabezal_inox, "Pulido", "piezas_finales_defenitivas")
    ).grid(row=1, column=1, pady=5, padx=3)

    ttk.Separator(caja5, orient="horizontal", style="Separador1.TSeparator").grid(
        row=5, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )
    ttk.Separator(caja5, orient="vertical", style="SeparadorVertical.TSeparator").grid(
    row=0, column=2, rowspan=6, sticky="ns", padx=5
)
    
#-----------------------SOLDADO EN FABRICA-----------------------------------------

    caja6 = ttk.Frame(mecanizado_de_piezas, style='Color.TFrame')
    caja6.grid(row=2, column=3, padx=7, pady=20)
    
    ttk.Label(caja6, text="Soldado en fabrica", style="WhiteOnRed.TLabel", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
    
    ttk.Label(caja6, text="Piezas a soldar", style="WhiteOnRed.TLabel").grid(row=1, column=0)
    piezas_a_varilla = ttk.Combobox(caja6, values=varillas_soldar)
    piezas_a_varilla.grid(row=2, column=0)

    ttk.Label(caja6, text="Cantidad", style="WhiteOnRed.TLabel").grid(row=1, column=1)
    cantidad_varilla = tk.Entry(caja6 ,width=15)
    cantidad_varilla.grid(row=2, column=1)

    tk.Button(
        caja6,
        text="Enviar",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: varilla_para_soldar(cantidad_varilla, piezas_a_varilla.get(), result),
    ).grid(row=3, column=1)


    stock_soldado = ttk.Frame(caja6, style='Color.TFrame')
    stock_soldado.grid(row=4, column=0, columnspan=2)
    ttk.Label(stock_soldado, text="Stock del Piezas", style="WhiteOnRed.TLabel", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)
    ttk.Button(
        stock_soldado,
        text="Stock Bruto",
        style="Estilo4.TButton",
        command= lambda:mostrar_datos_mecanizado(arbol, info, varillas_soldar, "Solador", "chapa")
    ).grid(row=1, column=0, pady=5, padx=3)
    ttk.Button(
        stock_soldado,
        text="Stock Terminado",
        style="Estilo4.TButton",
        command= lambda:varilla_soldador(arbol, info, varillas_soldar, "Solador")
    ).grid(row=1, column=1, pady=5, padx=3)

    ttk.Separator(caja6, orient="horizontal", style="Separador1.TSeparator").grid(
        row=5, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    ) 
    ttk.Separator(caja6, orient="vertical", style="SeparadorVertical.TSeparator").grid(
    row=0, column=2, rowspan=8, sticky="ns", padx=5
)

#-------------------------------------------

    box7 = ttk.Frame(mecanizado_de_piezas, style='Color.TFrame')
    box7.grid(row=4, column=3, columnspan=2)
    
    ttk.Label(box7, text="Observaciones", style="WhiteOnRed.TLabel",font=("Arial", 15, "bold")).grid(row=0, column=1, sticky="w")
    caja_texto = tk.Text(box7, height=6, width=30,)
    caja_texto.grid(row=1, column=1, columnspan=1)
    ttk.Button(
        box7, text="Enviar", style="Estilo4.TButton", command=lambda: agregar_a_lista_tarea(caja_texto, result)
    ).grid(row=2, column=1, sticky="e", pady=5, padx=5)
