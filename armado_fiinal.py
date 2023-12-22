import tkinter as tk
from tkinter import ttk
import sqlite3

tipo = ["Inox 330", "Inox 300", "Inox 250", "Pintada 300", "Pintada 250"]

def mostrar_cantidad_de_piezas(stock, modelo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_final' AND piezas = ? ", (modelo,))
    filas = cursor.fetchall()

    for pieza, cantidad in filas:
        color_fondo = obtener_color_fondo(cantidad)
        stock.insert("", "end", values=(pieza, cantidad), tags=(color_fondo))

    conn.close()

def obtener_color_fondo(cantidad):
    if cantidad < 10:
        return "red"
    elif cantidad > 50:
        return "green"
    else:
        return ""

def carga_datos(stock):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_final'")
    filas = cursor.fetchall()

    for pieza, cantidad in filas:
        color_fondo = obtener_color_fondo(cantidad)
        stock.insert("", "end", values=(pieza, cantidad), tags=(color_fondo))
    conn.close()

def actualizar_tabla(stock):
    # Borra todas las entradas actuales en el Treeview antes de actualizar
    for i in stock.get_children():
        stock.delete(i)

    # Vuelve a cargar los datos desde la base de datos
    carga_datos(stock)

def armado_final1(notebook):
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

    tk.Label(caja1, text="Mostrar Datos").grid(row=1, column=0)

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

    tk.Button(botonesgrup, text="Insumos").grid(row=0, column=0)
    tk.Button(botonesgrup, text="Afiladores").grid(row=0, column=1)
    tk.Button(botonesgrup, text="Base Prearmadas").grid(row=0, column=2)
    tk.Button(botonesgrup, text="Piezas").grid(row=0, column=3)

    ttk.Separator(caja2, orient="horizontal").grid(row=2, column=0, sticky="ew", columnspan=2, padx=5, pady=5)

    tk.Label(caja2, text="Consulta de maquinas para armar").grid(row=3, column=0)

    btnposible = tk.Frame(caja2)
    btnposible.grid(row=4, column=0)

    for modelo in tipo:
        tk.Button(btnposible, text=modelo, command=lambda m=modelo: mostrar_cantidad_de_piezas(stock, m)).grid(row=0, column=tipo.index(modelo))

    caja3 = ttk.Frame(pestania)
    caja3.grid(row=2, column=2)

    tk.Label(caja3, text="Maquinas Armadas en el día ").grid(row=0, column=0)
    tk.Label(caja3, text="Tipo").grid(row=1, column=0)
    tipo_seleccionado = ttk.Combobox(caja3, values=tipo, state="readonly")
    tipo_seleccionado.grid(row=1, column=1)
    tk.Label(caja3, text="Cantidad").grid(row=2, column=0)
    cantidad = tk.Entry(caja3)
    cantidad.grid(row=2, column=1)
    ttk.Button(caja3, text="ENVIAR").grid(row=3, column=1)

    ttk.Separator(caja3, orient="horizontal").grid(row=4, column=0, sticky="ew", columnspan=2, padx=5, pady=5)

    tk.Label(caja3, text="Consultas maquinas del mes").grid(row=5, column=0)
    tk.Button(caja3, text="Consulta").grid(row=5, column=1)

    caja4 = ttk.Frame(pestania)
    caja4.grid(row=2, column=3)

    tk.Label(caja4, text="Piezas Principales").grid(row=0, column=0)

    stock = ttk.Treeview(caja4, columns=("Piezas", "Cantidad"), show="headings", selectmode="none")
    stock.grid(row=1, column=0)

    stock.heading("Piezas", text="Piezas")
    stock.heading("Cantidad", text="Cantidad")

    carga_datos(stock)

    stock.tag_configure("red", background="red")
    stock.tag_configure("green", background="green")

    tk.Button(caja4, text="Actualizar Tabla", command=lambda: actualizar_tabla(stock)).grid(row=2, column=0)

