import tkinter as tk
from tkinter import ttk
from funciones import mostrar_datos, actualizar_pieza, eliminar_pieza, mostrar_datos_materias


piezas_fundidor_aluminio = ["velero", "aro", "base_afilador_330", "base_afilador_300", "base_afilador_250", "tapa_afilador", "tapa_afilador_250" ,"caja_250", "caja_300", "caja_330", "brazo_250", "brazo_300","brazo_330", "velero", "manchon", "cubrecuchilla_300", "eje"] 
piezas_fundidor_hierro = ["carros", "movimientos"]
piezas_plastico = ["cuadrado_motor", "cubre_motor", "rueditas", "pipas", "perillla_numerador", "manija_brazo", "espiral", "capuchon_afilador"]
tornilleria = ["Tornillo_1/4 ", "Arandela_1/2", "Cabeza_cuadrada", "Alem_3/4"]
piezas_chapa_final = ["vela_330", "vela_300", "planchada_330", "planchada_300", "guias_en_U"]

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
    tk.Listbox
    boton_mostrar_datos_fundidor = ttk.Button(caja1,text="Mostras Datos", command= lambda: mostrar_datos(tablafundidor, "piezas_del_fundicion" )).grid(row=1, column=0, padx=3, pady=3)
    result = tk.Listbox(caja1, width=60)
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

    ttk.Button(caja2, text="enviar", command=lambda: actualizar_pieza(predefinidas_aluminio, entrada_aluminio, result, "piezas_del_fundicion", mostrar_datos, tablafundidor)).grid(row=4,column=1,padx=3,pady=5,sticky="ne")
    
    ttk.Separator(caja2, orient="horizontal").grid(row=5, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja2, text="Eliminar Pieza").grid(row=6, column=1, padx=3,pady=3,sticky="w")
    ttk.Label(caja2, text="Piezas: ").grid(row=7, column=0,padx=3,pady=3)
    predefinidas_aluminio_delete = ttk.Combobox(caja2, values=piezas_fundidor_aluminio,state="readonly")
    predefinidas_aluminio_delete.grid(row=7, column=1, padx=3,pady=3)
    ttk.Label(caja2, text="Cantidad:").grid(row=8, column=0, padx=3,pady=3)
    entrada_aluminio_delete = ttk.Entry(caja2)
    entrada_aluminio_delete.grid(row=8, column=1, padx=3,pady=3)
   
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

    #-------------------------Plastico----------------------------------------------
    caja3 = ttk.Frame(pestania)
    caja3.grid(row=0, column=3, padx=3, pady=3, sticky="n")
    
    ttk.Label(caja3, text="Piezas De Plastico", font=("Arial", 12, "bold")).grid(row=0, column=1,padx=3,pady=5)
    ttk.Label(caja3, text="Agregar Piezas").grid(row=1,column=1,padx=3,pady=3, sticky="w")
    ttk.Label(caja3, text="Piezas").grid(row=2, column=0,padx=3,pady=3)
    predefinidas_plastico = ttk.Combobox(caja3, values=piezas_plastico, state="readonly")
    predefinidas_plastico.grid(row=2, column=1, padx=3,pady=3)
    ttk.Label(caja3, text="Cantidad:").grid(row=3, column=0, padx=3,pady=3)
    entrada_plastico = ttk.Entry(caja3)
    entrada_plastico.grid(row=3, column=1, padx=3,pady=3)

    ttk.Button(caja3, text="enviar" , command=lambda: actualizar_pieza(predefinidas_plastico, entrada_plastico, result, "piezas_del_fundicion", mostrar_datos, tablafundidor)).grid(row=4,column=1,padx=3,pady=5,sticky="ne")
    
    ttk.Separator(caja3, orient="horizontal").grid(row=5, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja3, text="Eliminar Pieza").grid(row=6, column=1, padx=3,pady=3,sticky="w")
    ttk.Label(caja3, text="Piezas: ").grid(row=7, column=0,padx=3,pady=3)
    predefinidas_plastico_delete = ttk.Combobox(caja3, values=piezas_plastico, state="readonly")
    predefinidas_plastico_delete.grid(row=7, column=1, padx=3,pady=3)
    ttk.Label(caja3, text="Cantidad:").grid(row=8, column=0, padx=3,pady=3)
    entrada_plastico_delete = ttk.Entry(caja3)
    entrada_plastico_delete.grid(row=8, column=1, padx=3,pady=3)
   
    ttk.Button(caja3, text="enviar", command=lambda: eliminar_pieza(predefinidas_plastico_delete,entrada_plastico_delete, result, "piezas_del_fundicion", mostrar_datos, tablafundidor )).grid(row=9,column=1,padx=5,pady=5,sticky="ne")

    ttk.Separator(caja3, orient="horizontal").grid(row=10, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    #____________________________Tornillos_______________________________________
    ttk.Label(caja3, text="Tornillos", font=("Arial", 12, "bold")).grid(row=11,column=1, padx=3,pady=3)
    
    ttk.Label(caja3, text="Agregar Piezas").grid(row=12,column=1,padx=3,pady=3, sticky="w")
    ttk.Label(caja3, text="Piezas").grid(row=13, column=0,padx=3,pady=3)
    predefinidas_tornillo = ttk.Combobox(caja3, values=tornilleria,state="readonly")
    predefinidas_tornillo.grid(row=13, column=1, padx=3,pady=3)
    ttk.Label(caja3, text="Cantidad").grid(row=14, column=0, padx=3,pady=3)
    entrada_tornillo = ttk.Entry(caja3)
    entrada_tornillo.grid(row=14, column=1, padx=3,pady=3)

    ttk.Button(caja3, text="enviar").grid(row=15,column=1,padx=3,pady=5,sticky="ne")
    ttk.Separator(caja3, orient="horizontal").grid(row=16, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja3, text="Eliminar Pieza").grid(row=17, column=1, padx=3,pady=3,sticky="w")
    ttk.Label(caja3, text="Piezas").grid(row=18, column=0,padx=3,pady=3)
    predefinidas_tornillo_delete = ttk.Combobox(caja3, values=tornilleria,state="readonly")
    predefinidas_tornillo_delete.grid(row=18, column=1, padx=3,pady=3)
    ttk.Label(caja3, text="Cantidad:").grid(row=19, column=0, padx=3,pady=3)
    entrada_tornillo_delete = ttk.Entry(caja3)
    entrada_tornillo_delete.grid(row=19, column=1, padx=3,pady=3)
    
    ttk.Button(caja3, text="enviar").grid(row=20,column=1,padx=5,pady=5,sticky="ne")
    ttk.Separator(caja3, orient="horizontal").grid(row=21, column=0,columnspan=2, sticky="ew", padx=3,pady=3)

 #______________________________________________Pieza chapas terminadas__________________________________________________
    caja4 = ttk.Frame(pestania)
    caja4.grid(row=0, column=4, padx=3, pady=3, sticky="n")
    
    ttk.Label(caja4, text="Piezas Chapas Terminadas ", font=("Arial", 12, "bold")).grid(row=0, column=1,padx=3,pady=5)
    ttk.Label(caja4, text="Agregar Piezas").grid(row=1,column=1,padx=3,pady=3, sticky="w")
    ttk.Label(caja4, text="Piezas").grid(row=2, column=0,padx=3,pady=3)
    predefinidas_chapa_final = ttk.Combobox(caja4, values=piezas_chapa_final, state="readonly")
    predefinidas_chapa_final.grid(row=2, column=1, padx=3,pady=3)
    ttk.Label(caja4, text="Cantidad:").grid(row=3, column=0, padx=3,pady=3)
    entrada_chapa_final = ttk.Entry(caja4)
    entrada_chapa_final.grid(row=3, column=1, padx=3,pady=3)

    ttk.Button(caja4, text="enviar" , command=lambda: actualizar_pieza(predefinidas_chapa_final, entrada_chapa_final, result, "piezas_del_fundicion", mostrar_datos, tablafundidor)).grid(row=4,column=1,padx=3,pady=5,sticky="ne")
    
    ttk.Separator(caja4, orient="horizontal").grid(row=5, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja4, text="Eliminar Pieza").grid(row=6, column=1, padx=3,pady=3,sticky="w")
    ttk.Label(caja4, text="Piezas: ").grid(row=7, column=0,padx=3,pady=3)
    predefinidas_chapa_final_delete = ttk.Combobox(caja4, values=piezas_chapa_final, state="readonly")
    predefinidas_chapa_final_delete.grid(row=7, column=1, padx=3,pady=3)
    ttk.Label(caja4, text="Cantidad:").grid(row=8, column=0, padx=3,pady=3)
    entrada_chapa_final_delete = ttk.Entry(caja4)
    entrada_chapa_final_delete.grid(row=8, column=1, padx=3,pady=3)
   
    ttk.Button(caja4, text="enviar", command=lambda: eliminar_pieza(predefinidas_chapa_final_delete,entrada_chapa_final_delete, result, "piezas_del_fundicion", mostrar_datos, tablafundidor )).grid(row=9,column=1,padx=5,pady=5,sticky="ne")

    ttk.Separator(caja4, orient="horizontal").grid(row=10, column=0,columnspan=2, sticky="ew", padx=3,pady=3)
    
    ttk.Label(caja4, text="Consultas De Stock").grid(row=11, column=0)
    ttk.Label(caja4, text="Aluminio").grid(row=12, column=0)
    ttk.Button(caja4, text="Stock En Bruto", command= lambda: mostrar_datos_materias("aluminio", tablafundidor, result)).grid(row=13, column=0)
    ttk.Label(caja4, text="Hierro").grid(row=14, column=0)
    ttk.Button(caja4, text="Stock Fundidor", command= lambda: mostrar_datos_materias("hierro", tablafundidor, result)).grid(row=15, column=0)
    ttk.Label(caja4, text="Plastico").grid(row=16, column=0)
    ttk.Button(caja4, text="Stock De Plastico", command= lambda: mostrar_datos_materias("plastico", tablafundidor, result)).grid(row=17, column=0)
    ttk.Label(caja4, text="Pieza Chapa final").grid(row=18, column=0)
    ttk.Button(caja4, text="Stock De Chapas", command= lambda: mostrar_datos_materias("chapa", tablafundidor, result)).grid(row=19, column=0)
    ttk.Label(caja4, text="Tornilleria").grid(row=20, column=0)
    ttk.Button(caja4, text="Stock Total").grid(row=21, column=0)
    ttk.Button(caja4, text="Stock Tornillo").grid(row=21, column=1)
    ttk.Button(caja4, text="Stock Arandela").grid(row=21, column=2)
    