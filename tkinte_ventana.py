
import tkinter as tk 
from tkinter import ttk
from funciones import mostrar_datos_300, mostrar_datos_330, mostrar_datos_250, actualizar_pieza, eliminar_pieza

def crear_pestana(notebook, texto):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=texto)
    return frame


piezas_pedefinida = ["teletubi","cuchilla","motor","vela","planchada","brazo","afilador","patas"]

root = tk.Tk()
root.title("Mostrar Datos de la Base De Datos")

notebook = ttk.Notebook(root)

pestania1 = crear_pestana(notebook, "Piezas 330")
pestania2 = crear_pestana(notebook, "Piezas 300")
pestania3 = crear_pestana(notebook, "Piezas 250")


#____________________piezas 330______________________________________________________   

frame330 = ttk.Frame(pestania1)
frame330.grid(row=0, column=0,padx=10,pady=10,sticky="w")
frame330.grid_rowconfigure(1, weight=1)
frame330.grid_columnconfigure(0, weight=1)
#TITULO
Titulo1 = ttk.Label(frame330, text="Piezas 330", anchor="center", font=("Arial", 16, "bold"))
Titulo1.grid(row=0,column=0,pady=2,padx=2)
#boton
btn_cargar_330 = ttk.Button(frame330, text="Cargar Datos", command=lambda: mostrar_datos_330(tree2))    
btn_cargar_330.grid(row=2, column=0, padx=10, pady=10, sticky="se")
#datos
tree2 = ttk.Treeview(frame330, columns=("Pieza", "Cantidad"))
tree2.heading("Pieza", text="Pieza")
tree2.heading("Cantidad", text="Cantidad")
tree2.column("#0", width=0, stretch=tk.NO)
tree2.column("Pieza", anchor=tk.W, width=170)
tree2.column("Cantidad", anchor=tk.W, width=90)
tree2.config(height=15)
tree2.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
#Mostrar Resultados
res = ttk.Label(frame330, text="Resultado")
res.grid(row=4, column=0, padx=5, pady=5)

#Actualizar Cantidad
div = ttk.Frame(pestania1)
div.grid(row=0, column=1,padx=10,pady=10,sticky="w")

titulo_agregar = ttk.Label(div, text="Agregar Piezas" ,font=("Arial", 16, "bold"),)
titulo_agregar.grid(row=0, column=1 , padx=5, pady=5)

label_agregar330 = ttk.Label(div, text="Agregar Pieza")
label_agregar330.grid(row=1, column=0, pady=5, padx=5 , sticky="nw")

lista_predefinida330 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida330.grid(row=1, column=1, padx=2, pady=2, sticky="ne") 

agregar_cantidad330 = ttk.Label(div, text="Cantidad")
agregar_cantidad330.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad330 = ttk.Entry(div)
entrada_cantidad330.grid(row=2, column=1, padx=2, pady=2, sticky="ne")

boton_agregar330 = ttk.Button(div, text="Actualizar", command=lambda: actualizar_pieza(lista_predefinida330, entrada_cantidad330, res, tree2))
boton_agregar330.grid(row=3, column=1, padx=5, pady=5, sticky="se")

separador1 = ttk.Separator(div, orient="horizontal")
separador1.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

#eliminar Piezas 

titulo_eliminar330 = ttk.Label(div, text="Eliminar Piezas" , font=("Arial", 16, "bold"))
titulo_eliminar330.grid(row=5, column=1 , padx=5, pady=5)

label_eliminar330 = ttk.Label(div, text="Eliminar Pieza")
label_eliminar330.grid(row=6, column=0, padx=5, pady=5)

lista_predefinida_eliminar330 = ttk.Combobox(div, values=piezas_pedefinida, state="readonly")
lista_predefinida_eliminar330.grid(row=6, column=1, padx=2, pady=2, sticky="ne") 

eliminar_cantidad330 = ttk.Label(div, text="Cantidad")
eliminar_cantidad330.grid(row=7, column=0, padx=5, pady=5, sticky="nw")

entrada_cantidad_eliminar330 = ttk.Entry(div)
entrada_cantidad_eliminar330.grid(row=7, column=1, padx=2, pady=2, sticky="ne")

boton_eliminar330 = ttk.Button(div, text="Eliminar",command=lambda: eliminar_pieza(lista_predefinida_eliminar330, entrada_cantidad_eliminar330, res, tree2))
boton_eliminar330.grid(row=8, column=1, padx=5, pady=5, sticky="se")

separador2 = ttk.Separator(div, orient="horizontal")
separador2.grid(row=9, column=0, columnspan=2, sticky="ew", padx=10, pady=10)


#________________________________________________________________________________________
etiqueta2 = ttk.Label(pestania2, text="Pieza 300")
etiqueta2.pack(padx=10, pady=10)

tree1 = ttk.Treeview(pestania2, columns=("Piezas", "Cantidad"))
tree1.heading("#1", text="Pieza")
tree1.heading("#2", text="Cantidad")
tree1.pack()

btn_cargar_300 = ttk.Button(pestania2, text="Cargar Datos", command= lambda: mostrar_datos_300(tree1))
btn_cargar_300.pack()

#______________________________________________________________________________________
etiqueta3 = ttk.Label(pestania3, text="Piezas 250")
etiqueta3.pack(padx=10, pady=10)
    
tree3 = ttk.Treeview(pestania3, columns=("Piezas", "Cantidad"))
tree3.heading("#1", text="Pieza")
tree3.heading("#2", text="Cantidad")
tree3.pack()

btn_cargar_250 = ttk.Button(pestania3, text="Cargar Datos", command= lambda: mostrar_datos_250(tree3))    
btn_cargar_250.pack()
    
#_______________________________________________________________________________________

notebook.pack(fill="both", expand=True)
    
root.mainloop()