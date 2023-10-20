import tkinter as tk
from tkinter import ttk
from funciones import mostrar_datos, actualizar_pieza, eliminar_pieza


piezas_fundidor_aluminio = ["brazo_330", "velero", "manchon", "cubrecuchilla_300", "ejes"] 
piezas_fundidor_hierro = ["carros", "movimientos"]


def ventana_fundidor(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(row=0, column=0, padx=10, pady=10,)

    notebook.add(pestania, text="Piezas Fundidor")
    
    caja1 = ttk.Frame(pestania)
    caja1.grid(row=0, column=0, padx=5, pady=5)
    
   
    
    tablafundidor = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    tablafundidor.heading("Pieza", text="Pieza")
    tablafundidor.heading("Cantidad", text="Cantidad")
    tablafundidor.column("#0", width=0, stretch=tk.NO)
    tablafundidor.column("Pieza", anchor= tk.W, width=170)
    tablafundidor.column("Cantidad", anchor=tk.W, width=90)
    tablafundidor.config(height=20)
    tablafundidor.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    boton_mostrar_datos_fundidor = ttk.Button(caja1,text="Mostras Datos", command= lambda: mostrar_datos(tablafundidor, "piezas_del_fundicion" )).grid(row=1, column=0, padx=3, pady=3)
    result = ttk.Label(caja1, text="")
    result.grid(row=3, column=0, padx=3,pady=3)
    #_______________________caja______________________________________________
    caja2 = ttk.Frame(pestania)
    caja2.grid(row=0, column=1, padx=3, pady=3, sticky="n")
    
    #_________________________________ALUMINIO_____________________________
    ttk.Label(caja2, text="Piezas Fundidor ALUMINIO", font=("Arial", 12, "bold")).grid(row=0, column=1,padx=3,pady=5)
    ttk.Label(caja2, text="Agregar Piezas").grid(row=1,column=1,padx=3,pady=3, sticky="w")
    ttk.Label(caja2, text="Piezas").grid(row=2, column=0,padx=3,pady=3)
    predefinidas_aluminio = ttk.Combobox(caja2, values=piezas_fundidor_aluminio,state="readonly")
    predefinidas_aluminio.grid(row=2, column=1, padx=3,pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=3, column=0, padx=3,pady=3)
    entrada_aluminio = ttk.Entry(caja2)
    entrada_aluminio.grid(row=3, column=1, padx=3,pady=3)
    # actualizar_pieza(lista_predefinida, entrada_cantidad, res, table, funcion, tree):
    #command=lambda: actualizar_pieza(lista_predefinida300, entrada_cantidad300, res2, "Piezas300", mostrar_datos, tree1))
    
    ttk.Button(caja2, text="enviar", command=lambda: actualizar_pieza(predefinidas_aluminio, entrada_aluminio, result, "piezas_del_fundicion", mostrar_datos, tablafundidor)).grid(row=4,column=1,padx=3,pady=5,sticky="ne")
    
    ttk.Separator(caja2, orient="horizontal").grid(row=5, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja2, text="Eliminar Pieza").grid(row=6, column=1, padx=3,pady=3,sticky="w")
    ttk.Label(caja2, text="Piezas: ").grid(row=7, column=0,padx=3,pady=3)
    predefinidas_aluminio_delete = ttk.Combobox(caja2, values=piezas_fundidor_aluminio,state="readonly")
    predefinidas_aluminio_delete.grid(row=7, column=1, padx=3,pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=8, column=0, padx=3,pady=3)
    entrada_aluminio_delete = ttk.Entry(caja2)
    entrada_aluminio_delete.grid(row=8, column=1, padx=3,pady=3)
    #boton_eliminar300 = ttk.Button(div, text="Eliminar", command=lambda: eliminar_pieza(lista_predefinida_eliminar300, entrada_cantidad_eliminar300, res2, "Piezas300", mostrar_datos, tree1))

    ttk.Button(caja2, text="enviar", command=lambda: eliminar_pieza(predefinidas_aluminio_delete,entrada_aluminio_delete, result, "piezas_del_fundicion", mostrar_datos, tablafundidor )).grid(row=9,column=1,padx=5,pady=5,sticky="ne")

    ttk.Separator(caja2, orient="horizontal").grid(row=10, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    
    #____________________________Hierro_______________________________________
    ttk.Label(caja2, text="Piezas Fundidor HIERRO", font=("Arial", 12, "bold")).grid(row=11,column=1, padx=3,pady=3)
    ttk.Label(caja2, text="Agregar Piezas").grid(row=12,column=1,padx=3,pady=3, sticky="w")
    ttk.Label(caja2, text="Piezas").grid(row=13, column=0,padx=3,pady=3)
    predefinidas_hierro = ttk.Combobox(caja2, values=piezas_fundidor_hierro,state="readonly")
    predefinidas_hierro.grid(row=13, column=1, padx=3,pady=3)
    ttk.Label(caja2, text="Cantidad").grid(row=14, column=0, padx=3,pady=3)
    entrada_hierro = ttk.Entry(caja2)
    entrada_hierro.grid(row=14, column=1, padx=3,pady=3)

    ttk.Button(caja2, text="enviar", command=lambda: actualizar_pieza(predefinidas_hierro, entrada_hierro, result, "piezas_del_fundicion", mostrar_datos, tablafundidor)).grid(row=15,column=1,padx=3,pady=5,sticky="ne")
    ttk.Separator(caja2, orient="horizontal").grid(row=16, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja2, text="Eliminar Pieza").grid(row=17, column=1, padx=3,pady=3,sticky="w")
    ttk.Label(caja2, text="Piezas").grid(row=18, column=0,padx=3,pady=3)
    predefinidas_hierro_delete = ttk.Combobox(caja2, values=piezas_fundidor_hierro,state="readonly")
    predefinidas_hierro_delete.grid(row=18, column=1, padx=3,pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=19, column=0, padx=3,pady=3)
    entrada_hierro_delete = ttk.Entry(caja2)
    entrada_hierro_delete.grid(row=19, column=1, padx=3,pady=3)
    
    ttk.Button(caja2, text="enviar", command=lambda: eliminar_pieza(predefinidas_hierro_delete,entrada_hierro_delete, result, "piezas_del_fundicion", mostrar_datos, tablafundidor )).grid(row=20,column=1,padx=5,pady=5,sticky="ne")
    ttk.Separator(caja2, orient="horizontal").grid(row=21, column=0,columnspan=2, sticky="ew", padx=3,pady=3)

    
