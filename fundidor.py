import tkinter as tk
from tkinter import ttk
from funciones import (
    mostrar_datos,
    actualizar_pieza,
    eliminar_pieza,
    mostrar_datos_materias,
)


piezas_fundidor_aluminio = [
   "caja_250", "caja_300", "caja_330", "brazo_330", "brazo_300", "brazo_250", "manchon", "manchon_250", "eje", "eje_250", "cubrecuchilla_330", "cubrecuchilla_300", "cubrecuchilla_250",
   "teletubi_250", "teletubi_300", "teletubi_330", "velero", "aro_numerador", "base_afilador_330", "base_afilador_300", "base_afilador_250", "tapa_afilador", "tapa_afilador_250", "carcaza_afilador"
]
piezas_fundidor_hierro = ["carros", "movimientos", "carros_250"]

piezas_plastico = [
    "perilla_numerador", "espiral", "perilla_brazo", "cubre_motor_rectangulo", "cubre_motor_cuadrado", "tapita_perilla","capuchon_afilador" 
]
shop = ["cable_220w", "ruleman_1", "ruleman_2", "orni", "capacitores", "capacitores_250", "cuchilla_330", "cuchilla_300", "cuchilla_250", "resorte_brazo", "perilla_cubrecuchilla", "perilla_afilador", "resorte_movimiento", "seguer", "sinfin", "resorte_carro", "piedra_afilador", "patas", "teclas", "corona_330", "corona_300", "corona_250", "pipas", "motores_220w", "motores250_220w", "ruleman_afilador"]

tornilleria = ["tornillo_guia","rueditas"]

piezas_chapa_final = [
    "vela_final_330",
    "vela_final_300",
    'vela_final_250',
    "planchada_final_330",
    "planchada_final_300",
    "planchada_final_250",
    
]
piezas_cortadas = ["guia_U", "eje_rectificado", "varilla_brazo_330","varilla_brazo_300", "varilla_brazo_250", "tubo_manija", "tubo_manija_250", "cuadrado_regulador", "palanca_afilador", "eje_corto", "eje_largo"]


def ventana_fundidor(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="session Stock")

    caja1 = ttk.Frame(pestania)
    caja1.grid(row=0, column=0, padx=5, pady=5)

    tablafundidor = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    tablafundidor.heading("Pieza", text="Pieza")
    tablafundidor.heading("Cantidad", text="Cantidad")
    tablafundidor.column("#0", width=0, stretch=tk.NO)
    tablafundidor.column("Pieza", anchor=tk.W, width=170)
    tablafundidor.column("Cantidad", anchor=tk.W, width=90)
    tablafundidor.config(height=20)
    tablafundidor.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    tk.Listbox
    ttk.Button(
        caja1,
        text="Mostras Datos bruto",
        command=lambda: mostrar_datos(tablafundidor, "piezas_del_fundicion"),
    ).grid(row=1, column=0, columnspan=2, padx=3, pady=3)
    ttk.Button(
        caja1,
        text="Mostras Datos terminado",
        command=lambda: mostrar_datos(tablafundidor, "piezas_finales_defenitivas"),
    ).grid(row=1, column=1, padx=3, pady=3)
    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, columnspan=2, padx=3, pady=3)


    # _______________________caja______________________________________________

    caja2 = ttk.Frame(pestania)
    caja2.grid(row=0, column=1, padx=3, pady=3, sticky="n")

    # _________________________________ALUMINIO_____________________________
    ttk.Label(caja2, text="Piezas Fundidor ALUMINIO", font=("Arial", 12, "bold")).grid(
        row=0, column=1, padx=3, pady=5
    )
    ttk.Label(caja2, text="Agregar Piezas").grid(
        row=1, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja2, text="Piezas").grid(row=2, column=0, padx=3, pady=3)
    predefinidas_aluminio = ttk.Combobox(
        caja2, values=piezas_fundidor_aluminio, state="readonly"
    )
    predefinidas_aluminio.grid(row=2, column=1, padx=3, pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=3, column=0, padx=3, pady=3)
    entrada_aluminio = ttk.Entry(caja2)
    entrada_aluminio.grid(row=3, column=1, padx=3, pady=3)

    ttk.Button(
        caja2,
        text="enviar",
        command=lambda: actualizar_pieza(
            predefinidas_aluminio,
            entrada_aluminio,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=4, column=1, padx=3, pady=5, sticky="ne")

    ttk.Separator(caja2, orient="horizontal").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja2, text="Eliminar Pieza").grid(
        row=6, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja2, text="Piezas: ").grid(row=7, column=0, padx=3, pady=3)
    predefinidas_aluminio_delete = ttk.Combobox(
        caja2, values=piezas_fundidor_aluminio, state="readonly"
    )
    predefinidas_aluminio_delete.grid(row=7, column=1, padx=3, pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=8, column=0, padx=3, pady=3)
    entrada_aluminio_delete = ttk.Entry(caja2)
    entrada_aluminio_delete.grid(row=8, column=1, padx=3, pady=3)

    ttk.Button(
        caja2,
        text="enviar",
        command=lambda: eliminar_pieza(
            predefinidas_aluminio_delete,
            entrada_aluminio_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=9, column=1, padx=5, pady=5, sticky="ne")

    ttk.Separator(caja2, orient="horizontal").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    # ____________________________Hierro_______________________________________
    ttk.Label(caja2, text="Piezas Fundidor HIERRO", font=("Arial", 12, "bold")).grid(
        row=11, column=1, padx=3, pady=3
    )
    ttk.Label(caja2, text="Agregar Piezas").grid(
        row=12, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja2, text="Piezas").grid(row=13, column=0, padx=3, pady=3)
    predefinidas_hierro = ttk.Combobox(
        caja2, values=piezas_fundidor_hierro, state="readonly"
    )
    predefinidas_hierro.grid(row=13, column=1, padx=3, pady=3)
    ttk.Label(caja2, text="Cantidad").grid(row=14, column=0, padx=3, pady=3)
    entrada_hierro = ttk.Entry(caja2)
    entrada_hierro.grid(row=14, column=1, padx=3, pady=3)

    ttk.Button(
        caja2,
        text="enviar",
        command=lambda: actualizar_pieza(
            predefinidas_hierro,
            entrada_hierro,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=15, column=1, padx=3, pady=5, sticky="ne")
    ttk.Separator(caja2, orient="horizontal").grid(
        row=16, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja2, text="Eliminar Pieza").grid(
        row=17, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja2, text="Piezas").grid(row=18, column=0, padx=3, pady=3)
    predefinidas_hierro_delete = ttk.Combobox(
        caja2, values=piezas_fundidor_hierro, state="readonly"
    )
    predefinidas_hierro_delete.grid(row=18, column=1, padx=3, pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=19, column=0, padx=3, pady=3)
    entrada_hierro_delete = ttk.Entry(caja2)
    entrada_hierro_delete.grid(row=19, column=1, padx=3, pady=3)

    ttk.Button(
        caja2,
        text="enviar",
        command=lambda: eliminar_pieza(
            predefinidas_hierro_delete,
            entrada_hierro_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=20, column=1, padx=5, pady=5, sticky="ne")
    ttk.Separator(caja2, orient="horizontal").grid(
        row=21, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    # -------------------------Plastico----------------------------------------------
    caja3 = ttk.Frame(pestania)
    caja3.grid(row=0, column=3, padx=3, pady=3, sticky="n")

    ttk.Label(caja3, text="Piezas De Plastico", font=("Arial", 12, "bold")).grid(
        row=0, column=1, padx=3, pady=5
    )
    ttk.Label(caja3, text="Agregar Piezas").grid(
        row=1, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja3, text="Piezas").grid(row=2, column=0, padx=3, pady=3)
    predefinidas_plastico = ttk.Combobox(
        caja3, values=piezas_plastico, state="readonly"
    )
    predefinidas_plastico.grid(row=2, column=1, padx=3, pady=3)
    ttk.Label(caja3, text="Cantidad:").grid(row=3, column=0, padx=3, pady=3)
    entrada_plastico = ttk.Entry(caja3)
    entrada_plastico.grid(row=3, column=1, padx=3, pady=3)

    ttk.Button(
        caja3,
        text="enviar",
        command=lambda: actualizar_pieza(
            predefinidas_plastico,
            entrada_plastico,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=4, column=1, padx=3, pady=5, sticky="ne")

    ttk.Separator(caja3, orient="horizontal").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja3, text="Eliminar Pieza").grid(
        row=6, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja3, text="Piezas: ").grid(row=7, column=0, padx=3, pady=3)
    predefinidas_plastico_delete = ttk.Combobox(
        caja3, values=piezas_plastico, state="readonly"
    )
    predefinidas_plastico_delete.grid(row=7, column=1, padx=3, pady=3)
    ttk.Label(caja3, text="Cantidad:").grid(row=8, column=0, padx=3, pady=3)
    entrada_plastico_delete = ttk.Entry(caja3)
    entrada_plastico_delete.grid(row=8, column=1, padx=3, pady=3)

    ttk.Button(
        caja3,
        text="enviar",
        command=lambda: eliminar_pieza(
            predefinidas_plastico_delete,
            entrada_plastico_delete,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=9, column=1, padx=5, pady=5, sticky="ne")

    ttk.Separator(caja3, orient="horizontal").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    # ____________________________shop _______________________________________
    ttk.Label(caja3, text="Shop", font=("Arial", 12, "bold")).grid(
        row=11, column=1, padx=3, pady=3
    )

    ttk.Label(caja3, text="Agregar Piezas").grid(
        row=12, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja3, text="Piezas").grid(row=13, column=0, padx=3, pady=3)
    predefinidas_shop = ttk.Combobox(caja3, values=shop, state="readonly")
    predefinidas_shop.grid(row=13, column=1, padx=3, pady=3)
    ttk.Label(caja3, text="Cantidad").grid(row=14, column=0, padx=3, pady=3)
    entrada_shop = ttk.Entry(caja3)
    entrada_shop.grid(row=14, column=1, padx=3, pady=3)

    ttk.Button(caja3, text="enviar", command=lambda: actualizar_pieza(
            predefinidas_shop,
            entrada_shop,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=15, column=1, padx=3, pady=5, sticky="ne")
    ttk.Separator(caja3, orient="horizontal").grid(
        row=16, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja3, text="Eliminar Pieza").grid(
        row=17, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja3, text="Piezas").grid(row=18, column=0, padx=3, pady=3)
    predefinidas_shop_delete = ttk.Combobox(
        caja3, values=shop, state="readonly"
    )
    predefinidas_shop_delete.grid(row=18, column=1, padx=3, pady=3)
    ttk.Label(caja3, text="Cantidad:").grid(row=19, column=0, padx=3, pady=3)
    entrada_shop_delete = ttk.Entry(caja3)
    entrada_shop_delete.grid(row=19, column=1, padx=3, pady=3)

    ttk.Button(caja3, text="enviar",command=lambda: eliminar_pieza(
            predefinidas_shop_delete,
            entrada_shop_delete,
            result,
            "piezas_finales_defenitivas",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=20, column=1, padx=5, pady=5, sticky="ne")
    ttk.Separator(caja3, orient="horizontal").grid(
        row=21, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    # ______________________________________________Pieza chapas terminadas__________________________________________________
    caja4 = ttk.Frame(pestania)
    caja4.grid(row=0, column=4, padx=3, pady=3, sticky="n")

    ttk.Label(caja4, text="Piezas Chapas Terminadas ", font=("Arial", 12, "bold")).grid(
        row=0, column=1, padx=3, pady=5
    )
    ttk.Label(caja4, text="Agregar Piezas").grid(
        row=1, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja4, text="Piezas").grid(row=2, column=0, padx=3, pady=3)
    predefinidas_chapa_final = ttk.Combobox(
        caja4, values=piezas_chapa_final, state="readonly"
    )
    predefinidas_chapa_final.grid(row=2, column=1, padx=3, pady=3)
    ttk.Label(caja4, text="Cantidad:").grid(row=3, column=0, padx=3, pady=3)
    entrada_chapa_final = ttk.Entry(caja4)
    entrada_chapa_final.grid(row=3, column=1, padx=3, pady=3)

    ttk.Button(
        caja4,
        text="enviar",
        command=lambda: actualizar_pieza(
            predefinidas_chapa_final,
            entrada_chapa_final,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=4, column=1, padx=3, pady=5, sticky="ne")

    ttk.Separator(caja4, orient="horizontal").grid(
        row=5, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja4, text="Eliminar Pieza").grid(
        row=6, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja4, text="Piezas: ").grid(row=7, column=0, padx=3, pady=3)
    predefinidas_chapa_final_delete = ttk.Combobox(
        caja4, values=piezas_chapa_final, state="readonly"
    )
    predefinidas_chapa_final_delete.grid(row=7, column=1, padx=3, pady=3)
    ttk.Label(caja4, text="Cantidad:").grid(row=8, column=0, padx=3, pady=3)
    entrada_chapa_final_delete = ttk.Entry(caja4)
    entrada_chapa_final_delete.grid(row=8, column=1, padx=3, pady=3)

    ttk.Button(
        caja4,
        text="enviar",
        command=lambda: eliminar_pieza(
            predefinidas_chapa_final_delete,
            entrada_chapa_final_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=9, column=1, padx=5, pady=5, sticky="ne")

    ttk.Separator(caja4, orient="horizontal").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )
#---------------------------------------pieza Cortadas ----------------------------

    ttk.Label(caja4, text="Piezas Cortadas", font=("Arial", 12, "bold")).grid(
        row=11, column=1, padx=3, pady=5
    )
    ttk.Label(caja4, text="Agregar Piezas").grid(
        row=12, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja4, text="Piezas").grid(row=13, column=0, padx=3, pady=3)
    predefinidas_pieza_final = ttk.Combobox(
        caja4, values=piezas_cortadas, state="readonly"
    )
    predefinidas_pieza_final.grid(row=13, column=1, padx=3, pady=3)
    ttk.Label(caja4, text="Cantidad:").grid(row=14, column=0, padx=3, pady=3)
    entrada_cortada_final = ttk.Entry(caja4)
    entrada_cortada_final.grid(row=14, column=1, padx=3, pady=3)

    ttk.Button(
        caja4,
        text="enviar",
        command=lambda: actualizar_pieza(
            predefinidas_pieza_final,
            entrada_cortada_final,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=15, column=1, padx=3, pady=5, sticky="ne")

    ttk.Separator(caja4, orient="horizontal").grid(
        row=16, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja4, text="Eliminar Pieza").grid(
        row=17, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja4, text="Piezas: ").grid(row=18, column=0, padx=3, pady=3)
    predefinidas_pieza_final_delete = ttk.Combobox(
        caja4, values=piezas_cortadas, state="readonly"
    )
    predefinidas_pieza_final_delete.grid(row=18, column=1, padx=3, pady=3)
    ttk.Label(caja4, text="Cantidad:").grid(row=19, column=0, padx=3, pady=3)
    entrada_pieza_final_delete = ttk.Entry(caja4)
    entrada_pieza_final_delete.grid(row=19, column=1, padx=3, pady=3)

    ttk.Button(
        caja4,
        text="enviar",
        command=lambda: eliminar_pieza(
            predefinidas_pieza_final_delete,
            entrada_pieza_final_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=20, column=1, padx=5, pady=5, sticky="ne")

    ttk.Separator(caja4, orient="horizontal").grid(
        row=21, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

#------------------------------------------------------------------2

    caja5 = tk.Frame(pestania)
    caja5.grid(row=0, column=5)

    ttk.Label(caja5, text="Consultas De Stock").grid(row=0, column=0)
    ttk.Label(caja5, text="Aluminio").grid(row=1, column=0)
    ttk.Button(
        caja5,
        text="Stock En Bruto",
        command=lambda: mostrar_datos_materias("aluminio", tablafundidor, result),
    ).grid(row=2, column=0)
    ttk.Label(caja5, text="Hierro").grid(row=3, column=0)
    ttk.Button(
        caja5,
        text="Stock Fundidor",
        command=lambda: mostrar_datos_materias("hierro", tablafundidor, result),
    ).grid(row=4, column=0)
    ttk.Label(caja5, text="Plastico").grid(row=5, column=0)
    ttk.Button(
        caja5,
        text="Stock De Plastico",
        command=lambda: mostrar_datos_materias("plastico", tablafundidor, result),
    ).grid(row=6, column=0)
    ttk.Label(caja5, text="Pieza Chapa final").grid(row=7, column=0)
    ttk.Button(
        caja5,
        text="Stock De Chapas",
        command=lambda: mostrar_datos_materias("chapa", tablafundidor, result),
    ).grid(row=8, column=0)
    ttk.Label(caja5, text="Tornilleria").grid(row=9, column=0)
    ttk.Button(caja5, text="Stock Total", command=lambda: mostrar_datos_materias("")).grid(row=10, column=0)
    ttk.Button(caja5, text="Stock Tornillo").grid(row=10, column=1)
    ttk.Button(caja5, text="Stock Arandela").grid(row=10, column=2)


#==========================tornillo===========================================
    
    ttk.Label(caja5, text="Tornillos", font=("Arial", 12, "bold")).grid(
        row=14, column=1, padx=3, pady=5
    )
    ttk.Label(caja5, text="Agregar Piezas").grid(
        row=15, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja5, text="Piezas").grid(row=16, column=0, padx=3, pady=3)
    predefinidas_tornillo_final = ttk.Combobox(
        caja5, values=tornilleria, state="readonly"
    )
    predefinidas_tornillo_final.grid(row=16, column=1, padx=3, pady=3)
    ttk.Label(caja5, text="Cantidad:").grid(row=17, column=0, padx=3, pady=3)
    entrada_tornillo = ttk.Entry(caja5)
    entrada_tornillo.grid(row=17, column=1, padx=3, pady=3)

    ttk.Button(
        caja5,
        text="enviar",
        command=lambda: actualizar_pieza(
            predefinidas_tornillo_final,
            entrada_tornillo,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=18, column=1, padx=3, pady=5, sticky="ne")

    ttk.Separator(caja5, orient="horizontal").grid(
        row=19, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )

    ttk.Label(caja5, text="Eliminar Pieza").grid(
        row=20, column=1, padx=3, pady=3, sticky="w"
    )
    ttk.Label(caja5, text="Piezas: ").grid(row=21, column=0, padx=3, pady=3)
    predefinidas_tornillo_final_delete = ttk.Combobox(
        caja5, values=tornilleria, state="readonly"
    )
    predefinidas_tornillo_final_delete.grid(row=21, column=1, padx=3, pady=3)
    ttk.Label(caja5, text="Cantidad:").grid(row=22, column=0, padx=3, pady=3)
    entrada_tornillo_delete = ttk.Entry(caja5)
    entrada_tornillo_delete.grid(row=22, column=1, padx=3, pady=3)

    ttk.Button(
        caja5,
        text="enviar",
        command=lambda: eliminar_pieza(
            predefinidas_tornillo_final_delete,
            entrada_tornillo_delete,
            result,
            "piezas_del_fundicion",
            mostrar_datos,
            tablafundidor,
        ),
    ).grid(row=23, column=1, padx=5, pady=5, sticky="ne")

    ttk.Separator(caja5, orient="horizontal").grid(
        row=24, column=0, columnspan=2, sticky="ew", padx=3, pady=3
    )