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
)

piezas_pedefinida_chapas = [
    "chapa_pincipal_330",
    "lateral_L_330",
    "lateral_R_330",
    "varilla_330",
    "planchuela_330",
    "portaeje",
    "arandela",
    "chapa_pincipal_300",
    "lateral_L_300",
    "lateral_R_300",
    "varilla_300",
    "planchuela_300",
    "chapa_U_cabezal",
    "tapa_cabezal",
    "bandeja_cabezal",
]

base_inox_330 = [
    "chapa_pincipal_330",
    "lateral_L_330",
    "lateral_R_330",
    "varilla_330",
    "planchuela_330",
    "portaeje",
    "arandela",
]
base_inox_300 = [
    "chapa_pincipal_300",
    "lateral_L_300",
    "lateral_R_300",
    "varilla_300",
    "planchuela_300",
    "portaeje",
    "arandela",
]

base_pintura_330 = [
    "chapa_pincipal_330",
    "lateral_L_330",
    "lateral_R_330",
    "varilla_330",
    "planchuela_330",
    "portaeje",
    "arandela",
]
base_pintura_300 = [
    "chapa_pincipal_300",
    "lateral_L_300",
    "lateral_R_300",
    "varilla_300",
    "planchuela_300",
    "portaeje",
    "arandela",
]

cabezal_final = ["chapa_U_cabezal", "tapa_cabezal", "bandeja_cabezal"]

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
    tabla_chapa.heading("Pieza", text="Pieza")
    tabla_chapa.heading("Cantidad", text="Cantidad")
    tabla_chapa.heading("Modelo", text="Modelo")
    tabla_chapa.heading("Tipo", text="Tipo")
    tabla_chapa.column("#0", width=0, stretch=tk.NO)
    tabla_chapa.column("Pieza", anchor=tk.W, width=150)
    tabla_chapa.column("Cantidad", anchor=tk.W, width=50)
    tabla_chapa.column("Modelo", anchor=tk.W, width=50)
    tabla_chapa.column("Tipo", anchor=tk.W, width=50)
    tabla_chapa.config(height=20)
    tabla_chapa.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")

    lista_acciones = tk.Listbox(box1, width=50)
    lista_acciones.grid(row=4, column=0)

    box2 = ttk.Frame(pestana_chapa)
    box2.grid(row=0, column=1, padx=5, pady=5, sticky="ne")

    titulo = ttk.Label(box2, text="Stock de Chapas", font=("Arial", 12, "bold")).grid(
        row=0, column=1, padx=5, pady=5
    )
    ttk.Label(box2, text="Total de Piezas").grid(row=1, column=0, padx=5, pady=5)
    btn_stock = ttk.Button(
        box2,
        text="Stock Total",
        command=lambda: mostrar_datos_chapa(tabla_chapa, "chapa"),
    ).grid(row=1, column=1, padx=5, pady=5)

    ttk.Separator(box2, orient="horizontal").grid(
        row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    ttk.Label(box2, text="Agregar Pieza").grid(row=3, column=0, padx=5, pady=5)
    lista_agregar = ttk.Combobox(box2, values=piezas_pedefinida_chapas, state="readonly")
    lista_agregar.grid(row=3, column=1, padx=2, pady=2, sticky="ne")
    ttk.Label(box2, text="Cantidad").grid(row=4, column=0, padx=5, pady=5)
    entrada_agregar = ttk.Entry(box2)
    entrada_agregar.grid(
        row=4, column=1, padx=5, pady=5
    )  # lista_predefinida, entrada_cantidad, res, table, funcion, tree
    agregar = ttk.Button(box2, text="Agregar").grid(row=5, column=1, padx=5, pady=5)

    ttk.Separator(box2, orient="horizontal").grid(
        row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    ttk.Label(box2, text="Eliminar Pieza").grid(row=7, column=0, padx=5, pady=5)
    lista_eliminar = ttk.Combobox(
        box2, values=piezas_pedefinida_chapas, state="readonly"
    )
    lista_eliminar.grid(row=7, column=1, padx=2, pady=2, sticky="ne")
    ttk.Label(box2, text="Cantidad").grid(row=8, column=0, padx=5, pady=5)
    entrada_eliminar = ttk.Entry(box2)
    entrada_eliminar.grid(row=8, column=1, padx=5, pady=5)
    eliminar = ttk.Button(box2, text="Borrar").grid(row=9, column=1, padx=5, pady=5)

    ttk.Separator(box2, orient="horizontal").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    ttk.Label(box2, text="Consultas", font=("Arial", 15, "bold")).grid(
        row=11, column=1, padx=5, pady=5
    )

    stock_pintada = ttk.Button(
        box2,
        text="Stock De Inox",
        command=lambda: stock_chapa(tabla_chapa, "acero", subtitulo),
    )
    stock_pintada.grid(row=12, column=0, padx=5, pady=5)

    stock_acero = ttk.Button(
        box2,
        text="Stock De Pintura",
        command=lambda: stock_chapa(tabla_chapa, "pintura", subtitulo),
    )
    stock_acero.grid(row=12, column=1, padx=5, pady=5)

    ttk.Separator(box2, orient="horizontal").grid(
        row=13, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    piezas_330_acero = ttk.Button(
        box2,
        text="Inox 330",
        command=lambda: consulta_de_piezas(tabla_chapa, "acero", "330", subtitulo),
    )
    piezas_330_acero.grid(row=14, column=0, padx=5, pady=5)

    piezas_300_acero = ttk.Button(
        box2,
        text="Pintura 330",
        command=lambda: consulta_de_piezas(tabla_chapa, "pintura", "330", subtitulo),
    )
    piezas_300_acero.grid(row=14, column=1, padx=5, pady=5)

    piezas_330_pintura = ttk.Button(
        box2,
        text="Inox 300",
        command=lambda: consulta_de_piezas(tabla_chapa, "acero", "300", subtitulo),
    )
    piezas_330_pintura.grid(row=15, column=0, padx=5, pady=5)

    piezas_300_pintura = ttk.Button(
        box2,
        text="Pintura 300",
        command=lambda: consulta_de_piezas(tabla_chapa, "pintura", "300", subtitulo),
    )
    piezas_300_pintura.grid(row=15, column=1, padx=5, pady=5)

    ttk.Separator(box2, orient="horizontal").grid(
        row=16, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    stock_cabezales_total = ttk.Button(
        box2,
        text="Cabezales_chapaNegra",
        command=lambda: consulta_cabezales(
            tabla_chapa, "pintura", "cabezal", subtitulo
        ),
    )
    stock_cabezales_total.grid(row=17, column=1, padx=5, pady=5, sticky="e")
    stock_cabezales_total = ttk.Button(
        box2,
        text="Cabezales_chapaInox",
        command=lambda: consulta_cabezales(tabla_chapa, "acero", "cabezal", subtitulo),
    )
    stock_cabezales_total.grid(row=17, column=0, padx=5, pady=5, sticky="e")

    ttk.Separator(box2, orient="horizontal").grid(
        row=18, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )
