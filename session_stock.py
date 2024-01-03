import tkinter as tk
from tkinter import ttk
from funciones import (
    mostrar_datos,
    actualizar_pieza,
    eliminar_pieza,
    mostrar_datos_materias,
    sort_column,
    agregar_a_lista_tarea,
    mostrar_plastico,
    mostrar_shop,
    mostrar_chapa_cortada,
    mostrar_piezas_cortadas,
    mostrar_tornillo_guia_rueditas
)


piezas_fundidor_aluminio = [
   "caja_250", "caja_300", "caja_330", "brazo_330", "brazo_300", "brazo_250", "manchon", "manchon_250", "eje", "eje_250", "cubrecuchilla_330", "cubrecuchilla_300", "cubrecuchilla_250",
   "teletubi_250", "teletubi_300", "teletubi_330", "velero", "aro_numerador", "base_afilador_330", "base_afilador_300", "base_afilador_250", "tapa_afilador", "tapa_afilador_250", "carcaza_afilador"
]
piezas_fundidor_hierro = ["carros", "movimientos", "carros_250"]
piezas_plastico = [
    "perilla_numerador", "espiral", "perilla_brazo", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "tapita_perilla","capuchon_afilador" 
]
shop = [
    "cable_220w", "ruleman_1", "ruleman_2", "orni", "capacitores", "capacitores_250", "cuchilla_330", "cuchilla_300", "cuchilla_250", "resorte_brazo", "perilla_cubrecuchilla", "perilla_afilador", "resorte_movimiento", "seguer", "sinfin", "resorte_carro", "piedra_afilador", "patas", "teclas", "corona_330", "corona_300", "corona_250", "pipas", "motores_220w", "motores250_220w", "ruleman_afilador"]
tornilleria = ["tornillo_guia","rueditas"]
piezas_chapa_final = [
    "vela_final_330",
    "vela_final_300",
    'vela_final_250',
    "planchada_final_330",
    "planchada_final_300",
    "planchada_final_250",
    
]
piezas_cortadas = [
    "guia_U", "eje_rectificado", "varilla_brazo_330","varilla_brazo_300", "varilla_brazo_250", "tubo_manija", "tubo_manija_250", "cuadrado_regulador", "palanca_afilador", "eje_corto", "eje_largo"]


def stock(notebook):
    pestania = ttk.Frame(notebook, style='Color.TFrame')
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="session Stock")
    
    #------------------------------sTYLO------------------------------------------
    
    style = ttk.Style()
    style.configure("Color.TFrame", background ="#192965")
    style.configure("Color.TLabel", background ="#192965", foreground="white")
    style.configure('WhiteOnRed.TEntry', fieldbackground='black', foreground='black')  # Puedes ajustar el color
    style.configure("Separador1.TSeparator", background="yellow")
    style.configure("Separador2.TSeparator", background="black")
    style.configure("Colortitulo.TLabel", background ="#192965", foreground="yellow")



    
   # ______________________Titulo _____________________________________________

    caja = ttk.Frame(pestania, style='Color.TFrame')
    caja.grid(row=0, column=0, padx=5, pady=5)

    titulo = ttk.Label(caja, text="Session Stock de Piezas",style="Color.TLabel" ,font=("Verdana", 22, "bold"))
    titulo.grid(row=0, column=0, columnspan=4)

    # ______________________Tabla MOSTRAR datos _____________________________________________

    caja1 = ttk.Frame(pestania, style="Color.TFrame")
    caja1.grid(row=1, column=0)

    tablafundidor = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    tablafundidor.heading("Pieza", text="Pieza")
    tablafundidor.heading("Cantidad", text="Cantidad", command=lambda: sort_column(tablafundidor, "Cantidad", False))
    tablafundidor.column("#0", width=0, stretch=tk.NO)
    tablafundidor.column("Pieza", anchor=tk.W, width=170)
    tablafundidor.column("Cantidad", anchor=tk.W, width=90)
    tablafundidor.config(height=20)
    tablafundidor.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    
    tablafundidor.tag_configure("red", background="red")
    tablafundidor.tag_configure("green", background="green")
    
    consulta1 = ttk.Frame(caja1, style='Color.TFrame')
    consulta1.grid(row=0, column=0)

    ttk.Button(consulta1, text="Mostras Datos bruto",command=lambda: mostrar_datos(tablafundidor, "piezas_del_fundicion"),).grid(row=0, column=0,padx=3, pady=3)
    ttk.Button(consulta1, text="Mostras Datos terminado",command=lambda: mostrar_datos(tablafundidor, "piezas_finales_defenitivas"),).grid(row=0, column=1, padx=3, pady=3)
    
    box = ttk.Label(consulta1, text="",style="Color.TLabel")
    box.grid(row=1, column=0, columnspan=2)
    
    result = tk.Listbox(caja1, width=60)
    result.grid(row=2, column=0, padx=3, pady=3)

# ______________________Caja 2____________________________________________

    caja2 = ttk.Frame(pestania, style='Color.TFrame')
    caja2.grid(row=1, column=1, padx=3, pady=3, sticky="n")

#_________________________________ALUMINIO_____________________________

    ttk.Label(caja2, text="Piezas Fundidor ALUMINIO" ,style="Colortitulo.TLabel", font=("Verdana", 11, "bold")).grid(
        row=0, column=0, padx=3, pady=2, sticky="en", columnspan=2
    )
    ttk.Label(caja2, text="Agregar Piezas" ,style="Color.TLabel" ,font=( "Arial", 9, "bold")).grid(
        row=1, column=0, padx=3, pady=3, sticky="we", columnspan=2
    )
    ttk.Label(caja2, text="Piezas",style="Color.TLabel").grid(row=2, column=0, padx=1, pady=1, sticky="e")
    
    predefinidas_aluminio = ttk.Combobox(
        caja2, values=piezas_fundidor_aluminio, state="readonly"
    )
    predefinidas_aluminio.grid(row=2, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja2, text="Cantidad",style="Color.TLabel").grid(row=3, column=0, padx=1, pady=1, sticky="e")
    entrada_aluminio = ttk.Entry(caja2, style='WhiteOnRed.TEntry')
    entrada_aluminio.grid(row=3, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja2,
        text="Agregar Pieza",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_aluminio,
            entrada_aluminio,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        )
    ).grid(row=4, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja2, orient="horizontal", style="Separador2.TSeparator").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja2, text="Eliminar Pieza(rotas)",style="Color.TLabel" ,font=( "Arial", 9, "bold")).grid(
        row=6, column=0, padx=3, pady=3, sticky="we", columnspan=2)
    
    ttk.Label(caja2, text="Piezas",style="Color.TLabel").grid(row=7, column=0, padx=1, pady=1, sticky="e")
    predefinidas_aluminio_delete = ttk.Combobox(
        caja2, values=piezas_fundidor_aluminio, state="readonly"
    )
    predefinidas_aluminio_delete.grid(row=7, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja2, text="Cantidad",style="Color.TLabel").grid(row=8, column=0, padx=1, pady=1, sticky="e")
    entrada_aluminio_delete = ttk.Entry(caja2, style='WhiteOnRed.TEntry')
    entrada_aluminio_delete.grid(row=8, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja2,
        text="Elimimar Pieza",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_aluminio_delete,
            entrada_aluminio_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=9, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja2, orient="horizontal", style="Separador2.TSeparator").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja2, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="we", columnspan=2)
    ttk.Label(caja2, text="Aluminio",style="Color.TLabel", font=("Arial", 12)).grid(row=12, column=0, columnspan=2, sticky="ew")
    btn_stock_en_bruto = tk.Button(
        caja2,
        text="Stock En Bruto",
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        command=lambda: mostrar_datos_materias("aluminio", tablafundidor, result, box ),
    )
    btn_stock_en_bruto.grid(row=13, column=0)

    separador = ttk.Separator(caja2, orient="horizontal", style="Separador1.TSeparator")
    separador.grid(row=14, column=0, columnspan=2, sticky="ew", padx=7, pady=7)
    
    
    # ____________________________Hierro_______________________________________
    ttk.Label(caja2, text="Piezas Fundidor HIERRO",style="Colortitulo.TLabel", font=("Verdana", 11, "bold")).grid(
        row=15, column=0, padx=3, pady=2, sticky="en", columnspan=2
    )
    ttk.Label(caja2, text="Agregar Piezas",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=16, column=0, padx=3, pady=3, sticky="we", columnspan=2
    )
    ttk.Label(caja2, text="Piezas",style="Color.TLabel").grid(row=17, column=0, padx=1, pady=1, sticky="e")
    
    predefinidas_hierro = ttk.Combobox(
        caja2, values=piezas_fundidor_hierro, state="readonly"
    )
    predefinidas_hierro.grid(row=17, column=1, padx=3, pady=3, sticky="w")
    
    ttk.Label(caja2, text="Cantidad",style="Color.TLabel").grid(row=18, column=0, padx=3, pady=3, sticky="e")
    entrada_hierro = ttk.Entry(caja2)
    entrada_hierro.grid(row=18, column=1, padx=3, pady=3, sticky="w")

    tk.Button(
        caja2,
        text="Agregar Piezas",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_hierro,
            entrada_hierro,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=19, column=1, padx=2, pady=2, sticky="ew")
    
    ttk.Separator(caja2, orient="horizontal", style="Separador2.TSeparator").grid(
        row=20, column=0, columnspan=2, sticky="ew", padx=4, pady=4)

    ttk.Label(caja2, text="Eliminar Pieza(rotas)",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=21, column=0, padx=3, pady=3, sticky="w", columnspan=2)
    
    ttk.Label(caja2, text="Piezas",style="Color.TLabel").grid(row=22, column=0, padx=3, pady=3, sticky="e")
    
    predefinidas_hierro_delete = ttk.Combobox(
        caja2, values=piezas_fundidor_hierro, state="readonly")
    predefinidas_hierro_delete.grid(row=22, column=1, padx=1, pady=1, sticky="w")
    
    ttk.Label(caja2, text="Cantidad",style="Color.TLabel").grid(row=23, column=0, padx=1, pady=1, sticky="e")
    
    entrada_hierro_delete = ttk.Entry(caja2)
    entrada_hierro_delete.grid(row=23, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja2,
        text="Eliminar Piezas",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_hierro_delete,
            entrada_hierro_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=24, column=1, padx=2, pady=2, sticky="ew")
    
    ttk.Separator(caja2, orient="horizontal", style="Separador2.TSeparator").grid(
        row=25, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )
    
    ttk.Label(caja2, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=26, column=0, sticky="we", columnspan=2)
    ttk.Label(caja2, text="Hierro",style="Color.TLabel", font=("Arial", 12)).grid(row=27, column=0, columnspan=2, sticky="ew")
    tk.Button(
        caja2,
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        text="Stock Fundidor",
        command=lambda: mostrar_datos_materias("hierro", tablafundidor, result, box),
    ).grid(row=28, column=0)
    
    
# -------------------------Plastico----------------------------------------------

    caja3 = ttk.Frame(pestania, style='Color.TFrame' )
    caja3.grid(row=1, column=2, padx=3, pady=3, sticky="n")

    ttk.Label(caja3, text="Piezas De Plastico",style='Colortitulo.TLabel', font=("Verdana", 11, "bold")).grid(
        row=0, column=0, padx=3, pady=2, sticky="en", columnspan=2)
    
    ttk.Label(caja3, text="Agregar Piezas",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=1, column=0, padx=3, pady=3, sticky="we", columnspan=2
    )
    ttk.Label(caja3, text="Piezas",style="Color.TLabel").grid(row=2, column=0, padx=1, pady=1, sticky="e")
    
    predefinidas_plastico = ttk.Combobox(
        caja3, values=piezas_plastico, state="readonly"
    )
    predefinidas_plastico.grid(row=2, column=1, padx=1, pady=1, sticky="w")
    
    ttk.Label(caja3, text="Cantidad",style="Color.TLabel").grid(row=3, column=0, padx=1, pady=1, sticky="e")
    
    entrada_plastico = ttk.Entry(caja3)
    entrada_plastico.grid(row=3, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja3,
        text="Agregar Pieza",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_plastico,
            entrada_plastico,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=4, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja3, orient="horizontal", style="Separador2.TSeparator").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja3, text="Eliminar Pieza (rotas)",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=6, column=0, padx=3, pady=3, sticky="we", columnspan=2
    )
    ttk.Label(caja3, text="Piezas",style="Color.TLabel").grid(row=7, column=0, padx=3, pady=3, sticky="e")
    predefinidas_plastico_delete = ttk.Combobox(
        caja3, values=piezas_plastico, state="readonly"
    )
    predefinidas_plastico_delete.grid(row=7, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja3, text="Cantidad",style="Color.TLabel").grid(row=8, column=0, padx=1, pady=1, sticky="e")
    entrada_plastico_delete = ttk.Entry(caja3)
    entrada_plastico_delete.grid(row=8, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja3,
        text="Elimimar Pieza",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_plastico_delete,
            entrada_plastico_delete,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=9, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja3, orient="horizontal", style="Separador2.TSeparator").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja3, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=11, column=0, columnspan=2, sticky="we")

    ttk.Label(caja3, text="Plastico",style="Color.TLabel", font=("Arial", 12)).grid(row=12, column=0, columnspan=2, sticky="ew")
    tk.Button(
        caja3,
        text="Stock En Plastico",
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        command=lambda: mostrar_plastico("plastico", tablafundidor, result, box),
    ).grid(row=13, column=0)
    
    ttk.Separator(caja3, orient="horizontal", style="Separador1.TSeparator").grid(row=14, column=0, columnspan=2, sticky="ew", padx=3, pady=3)



# ____________________________shop _______________________________________

    ttk.Label(caja3, text="Piezas Shop(comprar)",style="Colortitulo.TLabel", font=("Verdana", 11, "bold")).grid(
        row=15, column=0, padx=3, pady=2, sticky="en", columnspan=2
    )

    ttk.Label(caja3, text="Agregar Piezas",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=16, column=0, padx=3, pady=3, sticky="we", columnspan=2
    )
    ttk.Label(caja3, text="Piezas",style="Color.TLabel").grid(row=17, column=0, padx=1, pady=1, sticky="e")
    
    predefinidas_shop = ttk.Combobox(caja3, values=shop, state="readonly")
    predefinidas_shop.grid(row=17, column=1, padx=1, pady=1, sticky="w")
    
    ttk.Label(caja3, text="Cantidad",style="Color.TLabel").grid(row=18, column=0, padx=1, pady=1, sticky="e")
    
    entrada_shop = ttk.Entry(caja3)
    entrada_shop.grid(row=18, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja3,
        text="Agregar Pieza",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_shop,
            entrada_shop,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=19, column=1, padx=2, pady=2, sticky="ew")
    
    ttk.Separator(caja3, orient="horizontal", style="Separador2.TSeparator").grid(
        row=20, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja3, text="Eliminar Pieza",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=21, column=0, padx=3, pady=3, sticky="w", columnspan=2
    )
    ttk.Label(caja3, text="Piezas",style="Color.TLabel").grid(row=22, column=0, padx=3, pady=3, sticky="e")
    predefinidas_shop_delete = ttk.Combobox(
        caja3, values=shop, state="readonly"
    )
    predefinidas_shop_delete.grid(row=22, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja3, text="Cantidad",style="Color.TLabel").grid(row=23, column=0, padx=1, pady=1, sticky="e")
    entrada_shop_delete = ttk.Entry(caja3)
    entrada_shop_delete.grid(row=23, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja3,
        text="Elimimar Pieza",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_shop_delete,
            entrada_shop_delete,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=24, column=1, padx=2, pady=2, sticky="ew")
    
    ttk.Separator(caja3, orient="horizontal", style="Separador2.TSeparator").grid(
        row=25, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja3, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=26, column=0, columnspan=2, sticky="we")
    ttk.Label(caja3, text="Shop/ Compras",style="Color.TLabel", font=("Arial", 12)).grid(row=27, column=0, sticky="ew", columnspan=2)
    tk.Button(
        caja3,
        text="Stock Shop",
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        command=lambda: mostrar_shop("shop", tablafundidor, result, box),
    ).grid(row=28, column=0)


#______________________________________________Pieza chapas terminadas__________________________________________________

    caja4 = ttk.Frame(pestania, style='Color.TFrame')
    caja4.grid(row=1, column=4, padx=3, pady=3, sticky="n")

    ttk.Label(caja4, text="Piezas Chapas Terminadas ", style='Colortitulo.TLabel', font=("Verdana", 11, "bold")).grid(
        row=0, column=0, padx=3, pady=2, sticky="en", columnspan=2
    )
    ttk.Label(caja4, text="Agregar Piezas",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=1, column=0, padx=3, pady=3, sticky="w", columnspan=2
    )
    ttk.Label(caja4, text="Piezas",style="Color.TLabel").grid(row=2, column=0, padx=1, pady=1, sticky="e")
    
    predefinidas_chapa_final = ttk.Combobox(
        caja4, values=piezas_chapa_final, state="readonly"
    )
    predefinidas_chapa_final.grid(row=2, column=1, padx=1, pady=1 , sticky="w")
    ttk.Label(caja4, text="Cantidad",style="Color.TLabel").grid(row=3, column=0, padx=1, pady=1, sticky="e")
    entrada_chapa_final = ttk.Entry(caja4)
    entrada_chapa_final.grid(row=3, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja4,
        text="Agregar Pieza",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_chapa_final,
            entrada_chapa_final,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=4, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja4, orient="horizontal", style="Separador2.TSeparator").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja4, text="Eliminar Pieza",style="Color.TLabel", font=("Arial",9, "bold")).grid(
        row=6, column=1, padx=3, pady=3, sticky="we", columnspan=2)
    
    ttk.Label(caja4, text="Piezas",style="Color.TLabel").grid(row=7, column=0, padx=1, pady=1, sticky="e")
    
    predefinidas_chapa_final_delete = ttk.Combobox(
        caja4, values=piezas_chapa_final, state="readonly"
    )
    predefinidas_chapa_final_delete.grid(row=7, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja4, text="Cantidad",style="Color.TLabel").grid(row=8, column=0, padx=1, pady=1, sticky="e")
    entrada_chapa_final_delete = ttk.Entry(caja4)
    entrada_chapa_final_delete.grid(row=8, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja4,
        text="Elimimar Pieza",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_chapa_final_delete,
            entrada_chapa_final_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=9, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja4, orient="horizontal", style="Separador2.TSeparator").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )
    
    ttk.Label(caja4, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=11, column=0, sticky="we", columnspan=2)
    ttk.Label(caja4, text="Chapa Cortada",style="Color.TLabel", font=("Arial", 12)).grid(row=12, column=0, columnspan=2, sticky="ew")
    tk.Button(
        caja4,
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        text="Stock Chapa Cortada",
        command=lambda: mostrar_chapa_cortada(tablafundidor, result, box),
    ).grid(row=13, column=0)
    
    ttk.Separator(caja4, orient="horizontal", style="Separador1.TSeparator").grid(row=14, column=0, columnspan=2, sticky="ew", padx=3, pady=3)
    
    
#---------------------------------------pieza Cortadas ----------------------------


    ttk.Label(caja4, text="Piezas Cortadas",style="Colortitulo.TLabel", font=("Arial", 11, "bold")).grid(
        row=15, column=0, padx=3, pady=5, sticky="en", columnspan=2
    )
    ttk.Label(caja4, text="Agregar Piezas",style="Color.TLabel", font=("Arial", 9,"bold")).grid(
        row=16, column=0, padx=3, pady=3, sticky="we", columnspan=2
    )
    ttk.Label(caja4, text="Piezas",style="Color.TLabel").grid(row=17, column=0, padx=1, pady=1, sticky="e")
    predefinidas_pieza_final = ttk.Combobox(
        caja4, values=piezas_cortadas, state="readonly"
    )
    predefinidas_pieza_final.grid(row=17, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja4, text="Cantidad",style="Color.TLabel").grid(row=18, column=0, padx=1, pady=1, sticky="e")
    entrada_cortada_final = ttk.Entry(caja4)
    entrada_cortada_final.grid(row=18, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja4,
        text="Agregar Piezas",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_pieza_final,
            entrada_cortada_final,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=19, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja4, orient="horizontal", style="Separador2.TSeparator").grid(
        row=20, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja4, text="Eliminar Pieza",style="Color.TLabel", font=("Arial", 9, "bold")).grid(
        row=21, column=1, padx=3, pady=3, sticky="w", columnspan=2
    )
    ttk.Label(caja4, text="Piezas",style="Color.TLabel").grid(row=22, column=0, padx=1, pady=1, sticky="e")
    predefinidas_pieza_final_delete = ttk.Combobox(
        caja4, values=piezas_cortadas, state="readonly"
    )
    predefinidas_pieza_final_delete.grid(row=22, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja4, text="Cantidad",style="Color.TLabel").grid(row=23, column=0, padx=1, pady=1, sticky="e")
    entrada_pieza_final_delete = ttk.Entry(caja4)
    entrada_pieza_final_delete.grid(row=23, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja4,
        text="Eliminar Piezas",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_pieza_final_delete,
            entrada_pieza_final_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=24, column=1, padx=5, pady=5, sticky="ne")

    ttk.Separator(caja4, orient="horizontal", style="Separador2.TSeparator").grid(
        row=25, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja4, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=26, column=0, sticky="we", columnspan=2)
    ttk.Label(caja4, text="Pieza Cortadas",style="Color.TLabel", font=("Arial", 12)).grid(row=27, column=0, columnspan=2, sticky="ew")
    tk.Button(
        caja4,
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        text="Piezas Cortadas",
        command=lambda: mostrar_piezas_cortadas(tablafundidor, result, box),

    ).grid(row=28, column=0)
    
    
    ttk.Separator(caja4, orient="vertical", style="Separador1.TSeparator").grid(row=1, column=3, columnspan=3, sticky="ew")
    
    
    

    caja5 = ttk.Frame(pestania, style='Color.TFrame')
    caja5.grid(row=1, column=5, padx=3, pady=3, sticky="n")

#==========================tornillo===========================================
    
    ttk.Label(caja5, text="Tornillos, Ruediatas",style="Colortitulo.TLabel", font=("Verdana", 11, "bold")).grid(
        row=1, column=0, padx=3, pady=5, sticky="en", columnspan=2
    )
    ttk.Label(caja5, text="Agregar Piezas",style="Color.TLabel",font=( "Arial", 9, "bold")).grid(
        row=2, column=0, padx=3, pady=3,sticky="we", columnspan=2
    )
    ttk.Label(caja5, text="Piezas",style="Color.TLabel").grid(row=3, column=0, padx=1, pady=1, sticky="e")
    predefinidas_tornillo_final = ttk.Combobox(
        caja5, values=tornilleria, state="readonly"
    )
    predefinidas_tornillo_final.grid(row=3, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja5, text="Cantidad",style="Color.TLabel").grid(row=4, column=0, padx=1, pady=1, sticky="e")
    entrada_tornillo = ttk.Entry(caja5)
    entrada_tornillo.grid(row=4, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja5,
        text="Agregar Pieza",
        background="green",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: actualizar_pieza(
            predefinidas_tornillo_final,
            entrada_tornillo,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=5, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja5, orient="horizontal", style="Separador2.TSeparator").grid(
        row=6, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja5, text="Eliminar Pieza",style="Color.TLabel" ,font=( "Arial", 9, "bold")).grid(
        row=7, column=0, padx=3, pady=3, sticky="ew", columnspan=2
    )
    ttk.Label(caja5, text="Piezas",style="Color.TLabel").grid(row=8, column=0, padx=1, pady=1, sticky="e")
    predefinidas_tornillo_final_delete = ttk.Combobox(
        caja5, values=tornilleria, state="readonly"
    )
    predefinidas_tornillo_final_delete.grid(row=8, column=1, padx=1, pady=1, sticky="w")
    ttk.Label(caja5, text="Cantidad",style="Color.TLabel").grid(row=9, column=0, padx=1, pady=1, sticky="e")
    entrada_tornillo_delete = ttk.Entry(caja5)
    entrada_tornillo_delete.grid(row=9, column=1, padx=1, pady=1, sticky="w")

    tk.Button(
        caja5,
        text="Elimimar Pieza",
        background="red",
        foreground="white",
        padx=10,
        pady=4,
        font=('Helvetica', 8, "bold"),
        command=lambda: eliminar_pieza(
            predefinidas_tornillo_final_delete,
            entrada_tornillo_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=10, column=1, padx=2, pady=2, sticky="ew")

    ttk.Separator(caja5, orient="horizontal", style="Separador2.TSeparator").grid(
        row=11, column=0, columnspan=2, sticky="ew", padx=4, pady=4
    )

    ttk.Label(caja5, text="Consultas De Stock",style="Color.TLabel", font=("Arial", 12, "bold")).grid(row=12, column=0, sticky="we", columnspan=2)
    ttk.Label(caja5, text="Varios",style="Color.TLabel", font=("Arial", 12)).grid(row=13, column=0, columnspan=2, sticky="ew")
    btn_stock_en_bruto = tk.Button(
        caja5,
        text="Stock En Bruto",
        background="blue",  # Puedes ajustar el color de fondo según tus preferencias
        foreground="white",
        padx=5,
        pady=3,
        font=('Helvetica', 10),
        command=lambda: mostrar_tornillo_guia_rueditas( tablafundidor, result, box),
    )
    btn_stock_en_bruto.grid(row=14, column=0)

    ttk.Separator(caja5, orient="horizontal", style="Separador1.TSeparator").grid(
        row=15, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )
    
    
#_----------------------------------obserbaciones------------------------------------------------
    ttk.Label(caja5, text="Observaciones",style="Colortitulo.TLabel", font=("Arial", 13, "bold")).grid(row=16, column=0, sticky="w")
    caja_texto = tk.Text(caja5, height=10, width=30)
    caja_texto.grid(row=17, column=0, columnspan=2)

    boton_enviar = tk.Button(caja5, text="Enviar", command=lambda: agregar_a_lista_tarea(caja_texto, result))
    boton_enviar.grid(row=18, column=1, sticky="e", padx=4, pady=4)

# Configuración de estilo del botón
    boton_enviar.config(
        background="#584df9",  # Color de fondo
        foreground="white",   # Color del texto
        padx=10,              # Espaciado horizontal interno
        pady=4,               # Espaciado vertical interno
        font=('Helvetica', 8, "bold"),# Configuración de la fuente
        borderwidth=6,  # Ajusta el ancho del borde según tus preferencias
        relief="flat"  # Puedes cambiar el tipo de relieve (flat, groove, raised, ridge, solid, etc.)

)