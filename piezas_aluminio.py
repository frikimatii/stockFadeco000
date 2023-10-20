
import tkinter as tk
from tkinter import ttk
from funciones import mostrar_datos , enviar_piezas_a_pulido, mover_piezas_a_stock_pulidas

piezas_totales = ["brazo_250", "brazo_300","brazo_330","velero"]

def crear_pestana_aluminio(notebook):
    pestana_piezas = ttk.Frame(notebook)
    pestana_piezas.grid(row=0, column=0, padx=10, pady=10,)

    notebook.add(pestana_piezas, text="Piezas con Proveedor")

    # Crear tres Treeview uno al lado del otro
    treeview_frame1 = ttk.Frame(pestana_piezas)
    treeview_frame1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    ventana = ttk.Frame(treeview_frame1)
    ventana.grid(row=0,column=0, padx=5, pady=5, sticky="n")
    #botones 
    
    btn_piezas_brutos = ttk.Button(ventana, text="Stock en bruto", command=lambda: mostrar_datos(tabla, "pieza_en_bruto_aluminio")).grid(row=0,column=0, padx=3, pady=3)
    btn_piezas_pulidas = ttk.Button(ventana, text="Stock Pulido", command=lambda: mostrar_datos(tabla, "piezas_pulidas_terminada")).grid(row=1,column=0,padx=3, pady=3)
    
    
    tabla = ttk.Treeview(ventana, columns=("Piezas", "Cantidad"))
    tabla.heading("#1", text="Pieza")  # Cambia "Pieza" a "#1"
    tabla.heading("#2", text="Cantidad")  # Cambia "Cantidad" a "#2"
    tabla.column("#0", width=0, stretch=tk.NO)
    tabla.column("#1", anchor=tk.W, width=120)  # Cambia "Pieza" a "#1"
    tabla.column("#2", anchor=tk.W, width=50)  # Cambia "Cantidad" a "#2"
    tabla.config(height=20)
    tabla.grid(row=3, column=0, pady=5, padx=5, sticky="nsew") 
    
    
    
    
    ventana2 = ttk.Frame(treeview_frame1)
    ventana2.grid(row=0, column=1, padx=5, pady=5)
    
    #provedor = ttk.Label(ventana2, text="Provedores Pulidos", anchor="center", font=("Arial", 22, "bold"), foreground="orange").grid(row=0, column=1, padx=5, pady=5)

    
    # Crea campos de entrada para la cantidad de piezas a enviar
    envios = ttk.Label(ventana2, text="Envios",anchor="center", font=("Arial", 16, "bold"), foreground="green").grid(row=0, column=1, padx=3,pady=3)

    #_________________________________________Carmelo____________________________________________________
    ttk.Label(ventana2, text="Caramelo", font=("Arial", 14, "bold"), foreground="blue", anchor="center").grid(row=1, column=0, padx=3, pady=3)
    ttk.Label(ventana2, text="Pieza", font="bold").grid(row=2, column=0, padx=3, pady=3, sticky="nw")
    boxlist_caramelo = ttk.Combobox(ventana2, values=piezas_totales, state="readonly")
    boxlist_caramelo.grid(row=2, column=1, padx=3, pady=3, sticky="ne")
    ttk.Label(ventana2, text="Cantidad",font="bold").grid(row=3, column=0, padx=3, pady=3, sticky="nw")
    cantidad_caramelo = ttk.Entry(ventana2)
    cantidad_caramelo.grid(row=3, column=1, padx=3, pady=3, sticky="ne")

    # Agrega un botón para enviar piezas
    boton_enviar_piezas_caramelo = ttk.Button(ventana2, text="Enviar Piezas Caramelo", command=lambda: enviar_piezas_a_pulido(boxlist_caramelo, cantidad_caramelo, "carmelo_pulido", tabla2, tabla))
    boton_enviar_piezas_caramelo.grid(row=4, column=1, padx=3, pady=3, sticky="e")  
     
    separador = ttk.Separator(ventana2, orient="horizontal").grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
    #________________________________________________Maxi_________________________________
    ttk.Label(ventana2, text="Maxi", font=("Arial", 14, "bold"), foreground="blue").grid(row=6, column=0, padx=3, pady=3)
    ttk.Label(ventana2, text="Piezas",font="bold").grid(row=7, column=0, padx=3, pady=3, sticky="nw")
    boxlist_maxi = ttk.Combobox(ventana2, values=piezas_totales, state="readonly")
    boxlist_maxi.grid(row=7, column=1, padx=3, pady=3, sticky="ne")
    ttk.Label(ventana2, text="Cantidad",font="bold").grid(row=8, column=0, padx=3, pady=3, sticky="nw")
    cantidad_maxi = ttk.Entry(ventana2)
    cantidad_maxi.grid(row=8, column=1, padx=3, pady=3, sticky="ne")
    # Agrega un botón para enviar piezas
    boton_enviar_piezas_maxi = ttk.Button(ventana2, text="Enviar Piezas maxi", command=lambda: enviar_piezas_a_pulido(boxlist_maxi, cantidad_maxi, "maxi_pulido", tabla2, tabla))
    boton_enviar_piezas_maxi.grid(row=9, column=1, padx=3, pady=3, sticky="e")
    
    separador1 = ttk.Separator(ventana2, orient="horizontal").grid(row=10, column=0, padx=5, pady=5 , sticky="ew", columnspan=2)
    
    
    #CAMPOS DE ENTRADA DE PIEZAS ENTRANTES
    resibido = ttk.Label(ventana2, text="Resibidos",anchor="center", font=("Arial", 16, "bold"), foreground="green").grid(row=11, column=1, padx=3,pady=3)

    #---------------------------------------------------------------------------------------------

    ttk.Label(ventana2, text="Carmelo", font=("Arial", 14, "bold"), foreground="red").grid(row=12, column=0, padx=3,pady=3)
    ttk.Label(ventana2, text="Piezas",font="bold").grid(row=13, column=0, padx=3,pady=3, sticky="nw" )
    boxlist_carmelo_entrega = ttk.Combobox(ventana2, values=piezas_totales, state="readonly" )
    boxlist_carmelo_entrega.grid(row=13, column=1, padx=3, pady=3, sticky="ne")
    ttk.Label(ventana2, text="Cantidad",font="bold").grid(row=14, column=0, padx=3, pady=3, sticky="nw")
    cantidad_carmelo_resibida = ttk.Entry(ventana2)
    cantidad_carmelo_resibida.grid(row=14, column=1, padx=3, pady=3, sticky="ne")
    
    boton_enviar_piezas_resibidas_carmelo = ttk.Button(ventana2, text="Enviar Piezas", command=lambda: mover_piezas_a_stock_pulidas(boxlist_carmelo_entrega, cantidad_carmelo_resibida, "carmelo_pulido", "piezas_pulidas_terminada", tabla2, tabla ))
    boton_enviar_piezas_resibidas_carmelo.grid(row=15, column=1, padx=5, pady=3, sticky="e")
    
    separador = ttk.Separator(ventana2, orient="horizontal").grid(row=16, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

    ttk.Label(ventana2, text="Maxi", font=("Arial", 14, "bold"), foreground="red").grid(row=17, column=0, padx=3,pady=3)
    ttk.Label(ventana2, text="Piezas", font="bold").grid(row=18, column=0, padx=3,pady=3 ,sticky="nw")
    boxlist_maxi_enmtrega = ttk.Combobox(ventana2, values=piezas_totales, state="readonly" )
    boxlist_maxi_enmtrega.grid(row=18, column=1, padx=3, pady=3, sticky="ne")
    ttk.Label(ventana2, text="Cantidad",font="bold").grid(row=19, column=0, padx=3, pady=3, sticky="nw")
    cantidad_maxi_resibida = ttk.Entry(ventana2)
    cantidad_maxi_resibida.grid(row=19, column=1, padx=3, pady=3, sticky="ne")
    
    boton_enviar_piezas_resibidas_maxi = ttk.Button(ventana2, text="Enviar Piezas", command=lambda: mover_piezas_a_stock_pulidas(boxlist_maxi_enmtrega ,cantidad_maxi_resibida, "maxi_pulido", "piezas_pulidas_terminada", tabla2, tabla ))
    boton_enviar_piezas_resibidas_maxi.grid(row=20, column=1, padx=3, pady=3, sticky="e")
    
    separador = ttk.Separator(ventana2, orient="horizontal").grid(row=21, column=0, columnspan=2, sticky="ew", padx=5, pady=5)




    ventana3 = ttk.Label(treeview_frame1)
    ventana3.grid(row=0, column=2, padx=5, pady=5, sticky="n")
    
    btn_carmelo = ttk.Button(ventana3, text="Stock Carmelo",command=lambda: mostrar_datos(tabla2, "carmelo_pulido")).grid(row=0,column=0, padx=3, pady=3)
    btn_maxi = ttk.Button(ventana3, text="Stock Maxi", command=lambda:mostrar_datos(tabla2, "maxi_pulido")).grid(row=1,column=0, padx=3, pady=3)
    
    
    tabla2 = ttk.Treeview(ventana3, columns=("Piezas", "Cantidad"))
    tabla2.heading("#1", text="Pieza")
    tabla2.heading("#2", text="Cantidad")
    tabla2.column("#0", width=0, stretch=tk.NO)
    tabla2.column("#1", anchor=tk.W, width=130)  # Cambia "Pieza" a "#1"
    tabla2.column("#2", anchor=tk.W, width=50)  # Cambia "Cantidad" a "#2"
    tabla2.config(height=20)
    tabla2.grid(row=3, column=0, pady=5, padx=5) 
    
   