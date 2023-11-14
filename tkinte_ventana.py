
import tkinter as tk 
from tkinter import ttk ,messagebox
from funciones import mostrar_datos, actualizar_pieza, eliminar_pieza, mover_piezas_a_stock_pulidas
from piezas_aluminio import crear_pestana_aluminio
from stock_chapa import crear_pestana_chapa
from fundidor import ventana_fundidor

def crear_pestana(notebook, texto):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=texto)
    return frame


piezas_pedefinida = ["teletubi", "cuchilla", "motor", "vela", "planchada", "brazo", "afilador", "patas"]

root = tk.Tk()
root.title("Mostrar Datos de la Base De Datos")
root.iconbitmap("img/FLogo.ico")
notebook = ttk.Notebook(root)


ventana_fundidor(notebook)
crear_pestana_chapa(notebook)
crear_pestana_aluminio(notebook)  
pestania1 = crear_pestana(notebook, "Piezas 330")
pestania2 = crear_pestana(notebook, "Piezas 300")
pestania3 = crear_pestana(notebook, "Piezas 250")


# ______________________piezas 300______________________________________________________

frame300 = ttk.Frame(pestania2)
frame300.grid(row=0, column=0, padx=10, pady=10, sticky="w")
frame300.grid_rowconfigure(1, weight=1)
frame300.grid_columnconfigure(0, weight=1)
# TITULO
Titulo2 = ttk.Label(frame300, text="Piezas 300", font=("Arial", 10, "bold"))
Titulo2.grid(row=2, column=0, pady=2, padx=2)
# boton
btn_cargar_300 = ttk.Button(frame300, text="Cargar Datos", command=lambda: mostrar_datos(tree1, "Piezas300"))
btn_cargar_300.grid(row=2, column=0, padx=10, pady=10, sticky="se")
# datos
tree1 = ttk.Treeview(frame300, columns=("Pieza", "Cantidad"))
tree1.heading("Pieza", text="Pieza")
tree1.heading("Cantidad", text="Cantidad")
tree1.column("#0", width=0, stretch=tk.NO)
tree1.column("Pieza", anchor=tk.W, width=170)
tree1.column("Cantidad", anchor=tk.W, width=90)
tree1.config(height=20)
tree1.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")


# Mostrar Resultados
res2 = ttk.Label(frame300, text="Resultado")
res2.grid(row=4, column=0, padx=5, pady=5)

# Actualizar Cantidad
div = ttk.Frame(pestania2)
div.grid(row=0, column=1, padx=10, pady=10, sticky="n")

titulo_agregar = ttk.Label(div, text="Agregar Piezas", font=("Arial", 16, "bold"),)
titulo_agregar.grid(row=0, column=1, padx=5, pady=5)

label_agregar300 = ttk.Label(div, text="Agregar Pieza")
label_agregar300.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

lista_predefinida300 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida300.grid(row=1, column=1, padx=2, pady=2, sticky="ne")

agregar_cantidad300 = ttk.Label(div, text="Cantidad")
agregar_cantidad300.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad300 = ttk.Entry(div)
entrada_cantidad300.grid(row=2, column=1, padx=2, pady=2, sticky="ne")

boton_agregar300 = ttk.Button(div, text="Actualizar", command=lambda: actualizar_pieza(lista_predefinida300, entrada_cantidad300, res2, "Piezas300", mostrar_datos, tree1))
boton_agregar300.grid(row=3, column=1, padx=5, pady=5, sticky="se")

separador1 = ttk.Separator(div, orient="horizontal")
separador1.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

# eliminar Piezas

titulo_eliminar300 = ttk.Label(div, text="Eliminar Piezas", font=("Arial", 16, "bold"))
titulo_eliminar300.grid(row=5, column=1, padx=5, pady=5)

label_eliminar300 = ttk.Label(div, text="Eliminar Pieza")
label_eliminar300.grid(row=6, column=0, padx=5, pady=5)

lista_predefinida_eliminar300 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida_eliminar300.grid(row=6, column=1, padx=2, pady=2, sticky="ne")

eliminar_cantidad300 = ttk.Label(div, text="Cantidad")
eliminar_cantidad300.grid(row=7, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad_eliminar300 = ttk.Entry(div)
entrada_cantidad_eliminar300.grid(row=7, column=1, padx=2, pady=2, sticky="ne")

boton_eliminar300 = ttk.Button(div, text="Eliminar", command=lambda: eliminar_pieza(lista_predefinida_eliminar300, entrada_cantidad_eliminar300, res2, "Piezas300", mostrar_datos, tree1))
boton_eliminar300.grid(row=8, column=1, padx=5, pady=5, sticky="se")

separador2 = ttk.Separator(div, orient="horizontal")
separador2.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

# ______________________piezas 250______________________________________________________

frame250 = ttk.Frame(pestania3)
frame250.grid(row=0, column=0, padx=10, pady=10, sticky="w")
frame250.grid_rowconfigure(1, weight=1)
frame250.grid_columnconfigure(0, weight=1)
# TITULO
Titulo3 = ttk.Label(frame250, text="Piezas 250", font=("Arial", 10, "bold"))
Titulo3.grid(row=2, column=0, pady=2, padx=2)
# boton
btn_cargar_250 = ttk.Button(frame250, text="Cargar Datos", command=lambda: mostrar_datos(tree3, "Piezas250"))
btn_cargar_250.grid(row=2, column=0, padx=10, pady=10, sticky="se")
# datos
tree3 = ttk.Treeview(frame250, columns=("Pieza", "Cantidad"))
tree3.heading("Pieza", text="Pieza")
tree3.heading("Cantidad", text="Cantidad")
tree3.column("#0", width=0, stretch=tk.NO)
tree3.column("Pieza", anchor=tk.W, width=170)
tree3.column("Cantidad", anchor=tk.W, width=90)
tree3.config(height=20)
tree3.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
# Mostrar Resultados
res3 = ttk.Label(frame250, text="Resultado")
res3.grid(row=4, column=0, padx=5, pady=5)

# Actualizar Cantidad
div = ttk.Frame(pestania3)
div.grid(row=0, column=1, padx=10, pady=10, sticky="w")

titulo_agregar = ttk.Label(div, text="Agregar Piezas", font=("Arial", 16, "bold"),)
titulo_agregar.grid(row=0, column=1, padx=5, pady=5)

label_agregar250 = ttk.Label(div, text="Agregar Pieza")
label_agregar250.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

lista_predefinida250 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida250.grid(row=1, column=1, padx=2, pady=2, sticky="ne")

agregar_cantidad250 = ttk.Label(div, text="Cantidad")
agregar_cantidad250.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad250 = ttk.Entry(div)
entrada_cantidad250.grid(row=2, column=1, padx=2, pady=2, sticky="ne")

boton_agregar250 = ttk.Button(div, text="Actualizar", command=lambda: actualizar_pieza(lista_predefinida250, entrada_cantidad250, res3, "Piezas250", mostrar_datos ,tree3))
boton_agregar250.grid(row=3, column=1, padx=5, pady=5, sticky="se")

separador1 = ttk.Separator(div, orient="horizontal")
separador1.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

# eliminar Piezas

titulo_eliminar250 = ttk.Label(div, text="Eliminar Piezas", font=("Arial", 16, "bold"))
titulo_eliminar250.grid(row=5, column=1, padx=5, pady=5)

label_eliminar250 = ttk.Label(div, text="Eliminar Pieza")
label_eliminar250.grid(row=6, column=0, padx=5, pady=5)

lista_predefinida_eliminar250 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida_eliminar250.grid(row=6, column=1, padx=2, pady=2, sticky="ne")

eliminar_cantidad250 = ttk.Label(div, text="Cantidad")
eliminar_cantidad250.grid(row=7, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad_eliminar250 = ttk.Entry(div)
entrada_cantidad_eliminar250.grid(row=7, column=1, padx=2, pady=2, sticky="ne")

boton_eliminar250 = ttk.Button(div, text="Eliminar", command=lambda: eliminar_pieza(lista_predefinida_eliminar250, entrada_cantidad_eliminar250, res3, "Piezas250", mostrar_datos, tree3))                                                                   
boton_eliminar250.grid(row=8, column=1, padx=5, pady=5, sticky="se")

separador2 = ttk.Separator(div, orient="horizontal")
separador2.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

# ______________________piezas 330______________________________________________________

frame330 = ttk.Frame(pestania1)
frame330.grid(row=0, column=0, padx=10, pady=10, sticky="w")
frame330.grid_rowconfigure(1, weight=1)
frame330.grid_columnconfigure(0, weight=1)
# TITULO
Titulo1 = ttk.Label(frame330, text="Piezas 330", font=("Arial", 10, "bold"))
Titulo1.grid(row=2, column=0, pady=2, padx=2)
# boton
btn_cargar_330 = ttk.Button(frame330, text="Cargar Datos", command=lambda: mostrar_datos(tree2, "Piezas330"))
btn_cargar_330.grid(row=2, column=0, padx=10, pady=10, sticky="se")
# datos
tree2 = ttk.Treeview(frame330, columns=("Pieza", "Cantidad"))
tree2.heading("Pieza", text="Pieza")
tree2.heading("Cantidad", text="Cantidad")
tree2.column("#0", width=0, stretch=tk.NO)
tree2.column("Pieza", anchor=tk.W, width=170)
tree2.column("Cantidad", anchor=tk.W, width=90)
tree2.config(height=20)
tree2.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
# Mostrar Resultados

res1 = ttk.Label(frame330, text="Resultado")
res1.grid(row=8, column=0, padx=5, pady=5)

# Actualizar Cantidad
div = ttk.Frame(pestania1)
div.grid(row=0, column=1, padx=10, pady=10, sticky="w")

titulo_agregar = ttk.Label(div, text="Agregar Piezas", font=("Arial", 16, "bold"),)
titulo_agregar.grid(row=0, column=1, padx=5, pady=5)

label_agregar330 = ttk.Label(div, text="Agregar Pieza")
label_agregar330.grid(row=1, column=0, pady=5, padx=5, sticky="nw")

lista_predefinida330 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida330.grid(row=1, column=1, padx=2, pady=2, sticky="ne")

agregar_cantidad330 = ttk.Label(div, text="Cantidad")
agregar_cantidad330.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad330 = ttk.Entry(div)
entrada_cantidad330.grid(row=2, column=1, padx=2, pady=2, sticky="ne")

boton_agregar330 = ttk.Button(div, text="Actualizar", command=lambda: actualizar_pieza(lista_predefinida330, entrada_cantidad330, res1, "Piezas330", mostrar_datos, tree2))
boton_agregar330.grid(row=3, column=1, padx=5, pady=5, sticky="se")

separador1 = ttk.Separator(div, orient="horizontal")
separador1.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

# eliminar Piezas

titulo_eliminar330 = ttk.Label(div, text="Eliminar Piezas", font=("Arial", 16, "bold"))
titulo_eliminar330.grid(row=5, column=1, padx=5, pady=5)

label_eliminar330 = ttk.Label(div, text="Eliminar Pieza")
label_eliminar330.grid(row=6, column=0, padx=5, pady=5)

lista_predefinida_eliminar330 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida_eliminar330.grid(row=6, column=1, padx=2, pady=2, sticky="ne")

eliminar_cantidad330 = ttk.Label(div, text="Cantidad")
eliminar_cantidad330.grid(row=7, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad_eliminar330 = ttk.Entry(div)
entrada_cantidad_eliminar330.grid(row=7, column=1, padx=2, pady=2, sticky="ne")

boton_eliminar330 = ttk.Button(div, text="Eliminar", command=lambda: eliminar_pieza(lista_predefinida_eliminar330, entrada_cantidad_eliminar330, res1, "Piezas330", mostrar_datos, tree2))
boton_eliminar330.grid(row=8, column=1, padx=5, pady=5, sticky="se")


separador2 = ttk.Separator(div, orient="horizontal")
separador2.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)


notebook.pack()

root.mainloop()