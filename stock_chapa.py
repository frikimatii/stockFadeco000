
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
    agregar_pieza_chapas,
    eliminar_pieza_chapas,
    sort_column,
    agregar_piezas_faltantes,
    eliminar_piezas_faltante,
    mostrar_stock_soldador,
    calcular_maquinas_posibles,
    eliminar_cantidad_de_piezas,
    bases_soldador_terminadas,
    mostrar_cabezales_en_bruto,
    mostrar_bases_en_bruto,
    agregar_a_lista_tarea,
    mostrar_datos_mecanizado,
    armar_cabezales_inox,
    armar_cabezales_250,
    armar_cabezales_pint
)

 
piezas_pedefinida_chapas_base = [
    "chapa_principal_330",
    "lateral_L_330",
    "lateral_R_330",
    "chapa_principal_300",
    "lateral_L_300",
    "lateral_R_300",
    "chapa_principal_250",
    "lateral_L_250",
    "lateral_R_250"
]

base_inox_330 = {"chapa_principal_330": 1, "lateral_L_330": 1, "lateral_R_330": 1}

base_inox_300 = {"chapa_principal_300": 1, "lateral_L_300": 1, "lateral_R_300": 1}

base_pintada_330 = {"chapa_principal_330": 1, "lateral_L_330": 1, "lateral_R_330": 1}

base_pintada_300 = {"chapa_principal_300": 1, "lateral_L_300": 1, "lateral_R_300": 1}

base_inox_250 = {"chapa_principal_250": 1, "lateral_L_250": 1, "lateral_R_250": 1}

piezas_faltante_330 = {"planchuela_330", "varilla_330", "portaeje", "arandela"}

piezas_faltante_250 = {"planchuela_250", "varilla_250", "portaeje", "arandela"}

piezas_faltante_300 = {"planchuela_300", "varilla_300", "portaeje", "arandela"}

tipos_de_bases = ["Inox 330", "Inox 300", "Inox_250", "Pintada 330", "Pintada 300"]

cabezal_final = ["chapa_U_cabezal", "tapa_cabezal", "bandeja_cabezal" ,"chapa_U_cabezal_250", "tapa_cabezal_250", "bandeja_cabezal_250"]

piezas_restante = [
    "planchuela_330",
    "varilla_330",
    "planchuela_300",
    "varilla_300",
    "varilla_250",
    "planchuela_250",
    "portaeje",
    "arandela",
]
# ------------------------------------------------------------------------
bases_dict = {
    "Inox 330": {
        "chapa_principal": "chapa_principal_330",
        "lateral_L": "lateral_L_330",
        "lateral_R": "lateral_R_330",
        "planchuela": "planchuela_330",
        "varilla": "varilla_330",
        "portaeje": "portaeje",
        "arandela": "arandela",
    },
    "Inox 300": {
        "chapa_principal": "chapa_principal_300",
        "lateral_L": "lateral_L_300",
        "lateral_R": "lateral_R_300",
        "planchuela": "planchuela_300",
        "varilla": "varilla_300",
        "portaeje": "portaeje",
        "arandela": "arandela",
    },
    "Pintada 330": {
        "chapa_principal": "chapa_principal_330",
        "lateral_L": "lateral_L_330",
        "lateral_R": "lateral_R_330",
        "planchuela": "planchuela_330",
        "varilla": "varilla_330",
        "portaeje": "portaeje",
        "arandela": "arandela",
    },
    "Pintada 300": {
        "chapa_principal": "chapa_principal_300",
        "lateral_L": "lateral_L_300",
        "lateral_R": "lateral_R_300",
        "planchuela": "planchuela_300",
        "varilla": "varilla_300",
        "portaeje": "portaeje",
        "arandela": "arandela",
    },
    "Inox 250": {
        "chapa_principal": "chapa_principal_250",
        "lateral_L": "lateral_L_250",
        "lateral_R": "lateral_R_250",
        "planchuela": "planchuela_250",
        "varilla": "varilla_250",
        "portaeje": "portaeje",
        "arandela": "arandela",
    }
}

cabezales_inox = {"chapa_U_cabezal", "tapa_cabezal", "bandeja_cabezal"}

cabezales_pintada = {"chapa_U_cabezal", "tapa_cabezal", "bandeja_cabezal"}

cabezal_250 = ["chapa_U_cabezal_250", "tapa_cabezal_250", "bandeja_cabezal_250"]

cabezal_250_ = {"chapa_U_cabezal_250", "tapa_cabezal_250", "bandeja_cabezal_250"}

color1 = "#1016cf"

def crear_pestana_chapa(notebook):
    pestana_chapa = ttk.Frame(notebook , style='Pestania.TFrame')
    pestana_chapa.grid(
        row=3,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestana_chapa, text="Session Chapas")
    
    notebook.style = ttk.Style()
    notebook.style.configure('Color.TFrame', background='#192965', radius=20, borderwidth=10)  # Puedes ajustar el color
    notebook.style.configure('WhiteOnRed.TLabel', background='#192965', foreground='white')  # Puedes ajustar el color
    notebook.style.configure('WhiteOnRed.TEntry', fieldbackground='black', foreground='black')  # Puedes ajustar el color
    notebook.style.configure('WhiteOnRed.TCombobox', fieldbackground='#192965', foreground='white')  # Puedes ajustar el color
    

    estilo = ttk.Style()
    estilo.configure('Pestania.TFrame', background='#192965')
    
    style = ttk.Style()
    style.configure("Custom.TLabel", foreground="white", background="#192965", font=("Arial", 10, "bold"))
    #estilo.configure('Color.TFrame', borderwidth=10 ,background='#434ed1', radius=20)

    notebook.configure(style='Pestania.TNotebook')

    box1 = ttk.Frame(pestana_chapa, style='Pestania.TFrame')
    box1.grid(row=0, column=0, pady=5, padx=5)

    titulo = ttk.Label(box1, text="Tabla de Chapas", background="#192965",foreground='white' ,font=("Arial", 10, "bold"))
    titulo.grid(row=0, column=0, padx=5, pady=5)
    
    subtitulo = ttk.Label(box1, text="", background="#192965", foreground="white", font=("Arial", 9, "bold"))
    subtitulo.grid(row=1, column=0, padx=5, pady=5)

    tabla_chapa = ttk.Treeview(box1, columns=("Pieza", "Cantidad", "Modelo", "Tipo"))
    tabla_chapa.heading("Pieza", text="Pieza",)
    tabla_chapa.heading("Cantidad", text="Cantidad",command=lambda: sort_column(tabla_chapa, "Cantidad", False))
    tabla_chapa.heading("Modelo", text="Modelo")
    tabla_chapa.heading("Tipo", text="Tipo")
    tabla_chapa.column("#0", width=0, stretch=tk.NO)
    tabla_chapa.column("Pieza", anchor=tk.W, width=150)
    tabla_chapa.column("Cantidad", anchor=tk.W, width=50)
    tabla_chapa.column("Modelo", anchor=tk.W, width=50)
    tabla_chapa.column("Tipo", anchor=tk.W, width=50)
    tabla_chapa.config(height=25)
    tabla_chapa.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
    
    tabla_chapa.tag_configure("red", background="red")
    tabla_chapa.tag_configure("green", background="green")
    

    lista_acciones = tk.Listbox(box1, width=60)
    lista_acciones.grid(
        row=4,
        column=0,
    )

    box2 = ttk.Frame(pestana_chapa, style='Pestania.TFrame')
    box2.grid(row=0, column=1, padx=5, pady=5, sticky="ne")

    etiqueta_stock_chapas = ttk.Label(
        box2,
        text="Stock de Chapas",
        font=("Arial", 22, "bold"),
        background="#192965",  # Fondo azul
        foreground="white",    # Texto blanco
)
    # Colocar la etiqueta en la ventana
    etiqueta_stock_chapas.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    etiqueta_total_piezas = ttk.Label(
        box2,
        text="Total de Piezas",
        font=("Arial", 12, "bold"),
        background="#192965",  # Fondo naranja (puedes ajustar el color)
        foreground="white",    # Texto negro (puedes ajustar el color)
)   
    # Colocar la etiqueta en la ventana
    etiqueta_total_piezas.grid(row=1, column=0, padx=5, sticky="e")

    boton_stock_total = tk.Button(
    box2,
    text="Consultar Stock Total",
    command=lambda: mostrar_datos_chapa(tabla_chapa, "chapa", subtitulo),
    bg="#434ed1",  # Color de fondo
    fg="white",    # Color del texto
    padx=10,
    pady=5,
    font=('Helvetica', 12, 'bold'),
    relief=tk.GROOVE,  # Tipo de relieve del botón
    )

    # Colocar el botón en la ventana
    boton_stock_total.grid(row=1, column=1, padx=5, sticky="w")


    ttk.Separator(box2, orient="horizontal").grid(
        row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )
    
    pieza_agregar_chapa = ttk.Frame(box2, style='Color.TFrame')
    pieza_agregar_chapa.grid(row=3, column=0, padx=7, pady=7)
    
    # Crear los elementos con el nuevo estilo
    ttk.Label(pieza_agregar_chapa, text="Agregar Piezas", font=("Arial", 10, "bold"), style='WhiteOnRed.TLabel').grid(row=0, column=1, pady=5, sticky="w")
    tipo_var = tk.IntVar()
    tipo_var.set(1)

    acero_radio_agregar = tk.Radiobutton(pieza_agregar_chapa, text="Acero", variable=tipo_var, value=1, background='#192965', foreground='#9fa0a5')
    acero_radio_agregar.grid(row=1, column=0)

    chapa_radio_agregar = tk.Radiobutton(pieza_agregar_chapa, text="Pintura", variable=tipo_var, value=2, background='#192965', foreground='#9fa0a5')
    chapa_radio_agregar.grid(row=1, column=1)

    ttk.Label(pieza_agregar_chapa, text="Agregar Pieza", style='WhiteOnRed.TLabel').grid(row=2, column=0, pady=5)
    lista_agregar_chapa = ttk.Combobox(pieza_agregar_chapa, values=piezas_pedefinida_chapas_base, state="readonly", style='WhiteOnRed.TCombobox')
    lista_agregar_chapa.grid(row=2, column=1, pady=5)
    
    ttk.Label(pieza_agregar_chapa, text="Cantidad", style='WhiteOnRed.TLabel').grid(row=3, column=0, sticky="nw", pady=5)
    cantidad_agregar = ttk.Entry(pieza_agregar_chapa, style='WhiteOnRed.TEntry')
    cantidad_agregar.grid(row=3, column=1, sticky="we", pady=5)
    
    btn_agregar = tk.Button(
        pieza_agregar_chapa,
        text="Agregar Pieza",
        bg="green",  # Color de fondo
        fg="white",    # Color del texto
        padx=10,
        pady=5,
        font=('Helvetica', 7, 'bold'),
        relief=tk.GROOVE,  # Tipo de relieve del botón
        command=lambda: agregar_pieza_chapas(
            tipo_var,
            lista_agregar_chapa,
            cantidad_agregar,
            tabla_chapa,
            "chapa",
            lista_acciones, subtitulo
        ),
    )
    btn_agregar.grid(row=4, column=1, sticky="ne", pady=5, padx=5)
    
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''   
    
    pieza_eliminar_chapa = ttk.Frame(box2, style='Color.TFrame')
    pieza_eliminar_chapa.grid(row=3, column=1, padx=7)

    ttk.Label(
        pieza_eliminar_chapa, text="Elimiar Pieza", font=("Arial", 10, "bold"), style="WhiteOnRed.TLabel"
    ).grid(row=0, column=1, sticky="w", pady=5)



    tipo_var_d = tk.IntVar()
    tipo_var_d.set(1)
    acero_radio_eliminar = tk.Radiobutton(
        pieza_eliminar_chapa, text="Acero", variable=tipo_var_d, value=1, background='#192965', foreground='#9fa0a5'
    )
    acero_radio_eliminar.grid(row=1, column=0)
    chapa_radio_eliminar = tk.Radiobutton(
        pieza_eliminar_chapa, text="Pintura", variable=tipo_var_d, value=2, background='#192965', foreground='#9fa0a5'
    )
    chapa_radio_eliminar.grid(row=1, column=1)

    ttk.Label(pieza_eliminar_chapa, text="Elimiar Pieza", style="WhiteOnRed.TLabel").grid(row=2, column=0, pady=5)
    lista_eliminar_chapa = ttk.Combobox(
        pieza_eliminar_chapa, values=piezas_pedefinida_chapas_base, state="readonly", style="WhiteOnRed.TCombobox"
    )
    lista_eliminar_chapa.grid(row=2, column=1, pady=5)

    ttk.Label(pieza_eliminar_chapa, text="Cantidad", style='WhiteOnRed.TLabel').grid(
        row=3, column=0, pady=5, sticky="nw"
    )
    cantidad_elimimar = ttk.Entry(pieza_eliminar_chapa, style='WhiteOnRed.TEntry')
    cantidad_elimimar.grid(row=3, column=1, sticky="we", pady=5)

    btn_eliminar = tk.Button(
        pieza_eliminar_chapa,
        text="Eliminar Pieza",
        bg="red",  # Color de fondo
        fg="white",    # Color del texto
        padx=10,
        pady=5,
        font=('Helvetica', 7, 'bold'),
        relief=tk.GROOVE,  # Tipo de relieve del botón
        command=lambda: eliminar_pieza_chapas(
            tipo_var_d,
            lista_eliminar_chapa,
            cantidad_elimimar,
            tabla_chapa,
            "chapa",
            lista_acciones, subtitulo
        ),
    )
    btn_eliminar.grid(row=4, column=1, sticky="ne", pady=5)
#_-----------------------------------------------------------------------------
    ttk.Separator(box2, orient="horizontal").grid(
        row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    ttk.Label(box2, text="Consultas", style="Custom.TLabel" ).grid(
        row=5, column=1, padx=5, sticky="e"
    )
    style8 = ttk.Style()
    style8.configure("Gradient.TButton", padding=9, relief="flat", font=("Arial", 10, "bold"))
    style8.map("Gradient.TButton", background=[("active", "#434ed1"), ("!active", "#434ed1")])
    
    ttk.Button(box2, text="Stock de Inox", style="Gradient.TButton",command=lambda: stock_chapa(tabla_chapa, "acero", subtitulo)).grid(row=6, column=0, padx=5, sticky="e")
    ttk.Button(box2,style="Gradient.TButton",  text="Stock De Pintura", command=lambda: stock_chapa(tabla_chapa, "pintura", subtitulo),).grid(row=6, column=1, padx=5, sticky="w")

    ttk.Separator(box2, orient="horizontal").grid(
        row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    ttk.Separator(box2, orient="horizontal").grid(
        row=19, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )
    # ____________________________________________________________________________________________

    ttk.Label(
        box2, text="Consulta Piezas de maquinas", style="Custom.TLabel"
    ).grid(row=8, column=1, pady=5, padx=5, sticky="e")
        
    style12 = ttk.Style()
    style12.configure("3D.TButton", padding=8, relief="flat", background="#009688", font=("Arial", 8, "bold"))
    style12.map("3D.TButton", relief=[("pressed", "sunken"), ("!pressed", "ridge")])
    
    botonera_consulta = ttk.Frame(box2, style='Color.TFrame')
    botonera_consulta.grid(row=9, column=0 , columnspan=3)    

    ttk.Button(botonera_consulta,text="Inox 330", style="3D.TButton",command=lambda: consulta_de_piezas(tabla_chapa, "acero", "330", subtitulo)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ttk.Button(botonera_consulta,text="Pintura 330", style="3D.TButton",command=lambda: consulta_de_piezas(tabla_chapa, "pintura", "330", subtitulo)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    ttk.Button(botonera_consulta, text="Inox 300", style="3D.TButton",command=lambda: consulta_de_piezas(tabla_chapa, "acero", "300", subtitulo)).grid(row=0, column=1, padx=5, pady=5, sticky="e")
    ttk.Button(botonera_consulta,text="Pintura 300", style="3D.TButton",command=lambda: consulta_de_piezas(tabla_chapa, "pintura", "300", subtitulo)).grid(row=1, column=2, padx=5, pady=5, sticky="w")

    ttk.Button(botonera_consulta, text="Inox 250", style="3D.TButton",command=lambda: consulta_de_piezas(tabla_chapa, "acero", "250", subtitulo)).grid(row=0, column=2, padx=5, pady=5, sticky="e")

    ttk.Separator(box2, orient="horizontal").grid(
        row=11, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    ttk.Label(box2, text="Stock de Cabezales", style="Custom.TLabel").grid(
        row=12, column=1, pady=5, padx=5, sticky="e"
    )

    consulta_cabezales_pieza = ttk.Frame(box2, style='Color.TFrame')
    consulta_cabezales_pieza.grid(row=13,column=0, columnspan=2)
    ttk.Button(consulta_cabezales_pieza,text="Cabezales Chapa negra", style="3D.TButton", command=lambda: consulta_cabezales(tabla_chapa, "pintura", "cabezal", subtitulo)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ttk.Button(consulta_cabezales_pieza,text="Cabezales Inox", style="3D.TButton",command=lambda: consulta_cabezales(tabla_chapa, "acero", "cabezal", subtitulo)).grid(row=0, column=1, padx=5, pady=5, sticky="e")
    ttk.Button(consulta_cabezales_pieza,text="Cabezales 250", style="3D.TButton",command=lambda: mostrar_datos_mecanizado(tabla_chapa, subtitulo, cabezal_250, "Cabezal 250", "chapa")).grid(row=0, column=2, padx=5, pady=5, sticky="e")

    pieza_agregar_cabezal = ttk.Frame(box2, style='Color.TFrame')
    pieza_agregar_cabezal.grid(row=18, column=0, padx=7)

    ttk.Label(
        pieza_agregar_cabezal, text="Agregar Piezas ", font=("Arial", 10, "bold"), style='WhiteOnRed.TLabel'
    ).grid(row=0, column=1, pady=5, sticky="w")

    tipo_var_c = tk.IntVar()
    tipo_var_c.set(1)

    acero_radio_agregar = tk.Radiobutton(
        pieza_agregar_cabezal, text="Acero", variable=tipo_var_c, value=1, background='#192965', foreground='#9fa0a5'
    )
    acero_radio_agregar.grid(row=1, column=0)
    chapa_radio_agregar = tk.Radiobutton(
        pieza_agregar_cabezal, text="Pintura", variable=tipo_var_c, value=2, background='#192965', foreground='#9fa0a5'
    )
    chapa_radio_agregar.grid(row=1, column=1)

    ttk.Label(pieza_agregar_cabezal, text="Agregar Pieza", style='WhiteOnRed.TLabel').grid(row=2, column=0, pady=5)
    lista_agregar_cabezal = ttk.Combobox(
        pieza_agregar_cabezal, values=cabezal_final, state="readonly" , style='WhiteOnRed.TCombobox'
    )
    lista_agregar_cabezal.grid(row=2, column=1, pady=5)

    ttk.Label(pieza_agregar_cabezal, text="Cantidad", style='WhiteOnRed.TLabel').grid(
        row=3, column=0, sticky="nw", pady=5
    )
    cantidad_agregar_cabezal = ttk.Entry(pieza_agregar_cabezal, style='WhiteOnRed.TEntry')
    cantidad_agregar_cabezal.grid(row=3, column=1, sticky="we", pady=5)

    btn_agregar_cabezal = tk.Button(
        pieza_agregar_cabezal,
        text="Agregar Pieza",
        bg="green",  # Color de fondo
        fg="white",    # Color del texto
        padx=10,
        pady=5,
        font=('Helvetica', 7, 'bold'),
        relief=tk.GROOVE,  # Tipo de relieve del botón
        command=lambda: agregar_pieza_chapas(
            tipo_var_c,
            lista_agregar_cabezal,
            cantidad_agregar_cabezal,
            tabla_chapa,
            "chapa",
            lista_acciones,subtitulo
        ),
    )
    btn_agregar_cabezal.grid(row=4, column=1, sticky="ne", pady=5)
    
#_________________________________________________________________________________

    pieza_eliminar_cabezal = ttk.Frame(box2, style='Color.TFrame')
    pieza_eliminar_cabezal.grid(row=18, column=1, padx=7)

    ttk.Label(
        pieza_eliminar_cabezal, text="Elimiar Pieza", font=("Arial", 10, "bold"), style="WhiteOnRed.TLabel"
    ).grid(row=0, column=1, sticky="w", pady=5)

    tipo_var_ce = tk.IntVar()
    tipo_var_ce.set(1)

    tipo_var_ce = tk.IntVar()
    tipo_var_ce.set(1)
    acero_radio_eliminar = tk.Radiobutton(
        pieza_eliminar_cabezal, text="Acero", variable=tipo_var_ce, value=1, background='#192965', foreground='#9fa0a5'
    )
    acero_radio_eliminar.grid(row=1, column=0)
    chapa_radio_eliminar = tk.Radiobutton(
        pieza_eliminar_cabezal, text="Pintura", variable=tipo_var_ce, value=2, background='#192965', foreground='#9fa0a5'
    )
    chapa_radio_eliminar.grid(row=1, column=1)

    ttk.Label(pieza_eliminar_cabezal, text="Elimiar Pieza", style="WhiteOnRed.TLabel").grid(
        row=2, column=0, pady=5
    )
    lista_eliminar_cabezal = ttk.Combobox(
        pieza_eliminar_cabezal, values=cabezal_final, state="readonly", style="WhiteOnRed.TCombobox"
    )
    lista_eliminar_cabezal.grid(row=2, column=1, pady=5)

    ttk.Label(pieza_eliminar_cabezal, text="Cantidad", style='WhiteOnRed.TLabel').grid(
        row=3, column=0, pady=5, sticky="nw"
    )
    cantidad_elimimar_cabezal = ttk.Entry(pieza_eliminar_cabezal, style='WhiteOnRed.TEntry')
    cantidad_elimimar_cabezal.grid(row=3, column=1, sticky="we", pady=5)

    btn_eliminar_cabezal = tk.Button(
        pieza_eliminar_cabezal,
        text="Eliminar Pieza",
        bg="red",  # Color de fondo
        fg="white",    # Color del texto
        padx=10,
        pady=5,
        font=('Helvetica', 7, 'bold'),
        relief=tk.GROOVE,  # Tipo de relieve del botón
        command=lambda: eliminar_pieza_chapas(
            tipo_var_ce,
            lista_eliminar_cabezal,
            cantidad_elimimar_cabezal,
            tabla_chapa,
            "chapa",
            lista_acciones,subtitulo
        ),
    )
    btn_eliminar_cabezal.grid(row=4, column=1, sticky="ne", pady=5)

    ttk.Separator(box2, orient="horizontal").grid(
        row=19, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )


# _________________________________________________________________________________________________

    box3 = ttk.Frame(pestana_chapa, style='Pestania.TFrame')
    box3.grid(row=0, column=3, pady=5, padx=5, sticky="nw")

    ttk.Label(box3, text="Agregado de Pieza Faltantes", font=("Arial", 9, "bold"), style="WhiteOnRed.TLabel").grid(
        row=0, column=1, pady=5
    )

    pieza_agregar_v_p = ttk.Frame(box3, style='Pestania.TFrame')
    pieza_agregar_v_p.grid(row=2, column=0, padx=7)

    ttk.Label(
        pieza_agregar_v_p, text="Agregar Piezas ", font=("Arial", 10, "bold"), style="WhiteOnRed.TLabel"
    ).grid(row=0, column=1, pady=5, sticky="w")

    ttk.Label(pieza_agregar_v_p, text="Agregar Pieza", style="WhiteOnRed.TLabel").grid(row=2, column=0, pady=5)
    lista_agregar_v_p = ttk.Combobox(
        pieza_agregar_v_p, values=piezas_restante, state="readonly"
    )
    lista_agregar_v_p.grid(row=2, column=1, pady=5)

    ttk.Label(pieza_agregar_v_p, text="Cantidad", style="WhiteOnRed.TLabel").grid(
        row=3, column=0, sticky="nw", pady=5
    )
    cantidad_agregar_v_p = ttk.Entry(pieza_agregar_v_p, style='WhiteOnRed.TEntry')
    cantidad_agregar_v_p.grid(row=3, column=1, sticky="we", pady=5)

    btn_agregar_v_p = tk.Button(
        pieza_agregar_v_p,
        text="Agregar Pieza",
        bg="green",  # Color de fondo
        fg="white",    # Color del texto
        padx=10,
        pady=5,
        font=('Helvetica', 7, 'bold'),
        relief=tk.GROOVE,  # Tipo de relieve del botón
        command=lambda: agregar_piezas_faltantes(
            lista_agregar_v_p,
            cantidad_agregar_v_p,
            tabla_chapa,
            lista_acciones,
            "chapa",
            subtitulo
        ),
    )
    btn_agregar_v_p.grid(row=4, column=1, sticky="ne", pady=5)

    # --------#

    pieza_eliminar_v_p = ttk.Frame(box3, style='Pestania.TFrame')
    pieza_eliminar_v_p.grid(row=2, column=1, padx=7)

    ttk.Label(
        pieza_eliminar_v_p, text="Elimiar Pieza", font=("Arial", 10, "bold"), style='WhiteOnRed.TLabel'
    ).grid(row=0, column=1, sticky="w", pady=5)

    ttk.Label(pieza_eliminar_v_p, text="Elimiar Pieza", style='WhiteOnRed.TLabel').grid(row=2, column=0, pady=5)
    lista_eliminar_v_p = ttk.Combobox(
        pieza_eliminar_v_p, values=piezas_restante, state="readonly", style='WhiteOnRed.TCombobox'
    )
    lista_eliminar_v_p.grid(row=2, column=1, pady=5)

    ttk.Label(pieza_eliminar_v_p, text="Cantidad", style='WhiteOnRed.TLabel').grid(
        row=3, column=0, pady=5, sticky="nw"
    )
    cantidad_elimimar_v_p = ttk.Entry(pieza_eliminar_v_p, style='WhiteOnRed.TEntry')
    cantidad_elimimar_v_p.grid(row=3, column=1, sticky="we", pady=5)

    btn_eliminar_v_p = tk.Button(
        pieza_eliminar_v_p,
        text="Eliminar Pieza",
        bg="red",  # Color de fondo
        fg="white",    # Color del texto
        padx=10,
        pady=5,
        font=('Helvetica', 7, 'bold'),
        relief=tk.GROOVE,  # Tipo de relieve del botón
        command=lambda: eliminar_piezas_faltante(
            lista_eliminar_v_p.get(),
            cantidad_elimimar_v_p.get(),
            tabla_chapa,
            lista_acciones,
            "chapa",
            subtitulo
        ),
    )
    btn_eliminar_v_p.grid(row=4, column=1, sticky="ne", pady=5)

    ttk.Separator(box3, orient="horizontal").grid(
        row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    # ----------- Soldador--------#


    style2 = ttk.Style()
    style2.configure("TButton", padding=7, relief="flat", background="#a6a6a6", font=("Arial", 8, "bold"))
    

    ttk.Label(box3, text="Soldador", font=("Arial", 17, "bold"), style='WhiteOnRed.TLabel').grid(
        row=5, column=1, padx=5, pady=5, sticky="e"
    )

    ttk.Label(box3, text="Stock Del Soldador", style='WhiteOnRed.TLabel').grid(row=6, column=0, padx=5, sticky="e")
    btn_stock_soldador = ttk.Button(
        box3, text="Stock", style="TButton",command=lambda: mostrar_stock_soldador(tabla_chapa)
    )
    btn_stock_soldador.grid(row=6, column=1, padx=5, sticky="w")

    ttk.Separator(box3, orient="horizontal").grid(
        row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    caja_botones = ttk.Frame(box3, style='Pestania.TFrame')
    caja_botones.grid(row=9, column=0, columnspan=2)
    ttk.Label(caja_botones, text="Cantidad de maquina posibles", style='WhiteOnRed.TLabel', font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=5)

    # Botones para calcular máquinas posibles
    btn_i_330 = ttk.Button(
        caja_botones,
        text="Inox 330",style="TButton",
        command=lambda: calcular_maquinas_posibles(
            base_inox_330, "acero", "330", lista_acciones
        ),
    )
    btn_i_330.grid(row=1, column=0, padx=5)

    btn_i_300 = ttk.Button(
        caja_botones,
        text="Inox 300",style="TButton",
        command=lambda: calcular_maquinas_posibles(
            base_inox_300, "acero", "300", lista_acciones
        ),
    )
    btn_i_300.grid(row=1, column=1, padx=5)

    btn_p_330 = ttk.Button(
        caja_botones,
        text="Pint 330",style="TButton",
        command=lambda: calcular_maquinas_posibles(
            base_pintada_330, "pintura", "330", lista_acciones
        ),
    )
    btn_p_330.grid(row=1, column=2, padx=5)

    btn_p_300 = ttk.Button(
        caja_botones,
        text="Pint 300",
        command=lambda: calcular_maquinas_posibles(
            base_pintada_300, "pintura", "300", lista_acciones
        ),
    )
    btn_p_300.grid(row=1, column=3, padx=5)
    
    btn_i_250 = ttk.Button(
        caja_botones,
        text="Inox 250",
        command=lambda: calcular_maquinas_posibles(
            base_inox_250, "acero", "250", lista_acciones
        ),
    )
    btn_i_250.grid(row=1, column=4, padx=5)


    ttk.Separator(box3, orient="horizontal").grid(
        row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    # ______________________soldador_________________________________________
    entrega_base = ttk.Frame(box3, style='Pestania.TFrame')
    entrega_base.grid(row=11, column=0)

    ttk.Label(entrega_base, text="Entregas al Soldador", style='WhiteOnRed.TLabel').grid(row=0, column=0)

    tipos_de_bases = list(bases_dict.keys())

    ttk.Label(entrega_base, text="Tipo De Base:", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    combocaja_soldador = ttk.Combobox(
        entrega_base, values=tipos_de_bases, state="readonly"
    )
    combocaja_soldador.grid(row=1, column=1, pady=4)

    ttk.Label(entrega_base, text="Cantidad:", style='WhiteOnRed.TLabel').grid(row=2, column=0)
    entrada_cantidad_soldador = ttk.Entry(entrega_base, style='WhiteOnRed.TEntry')
    entrada_cantidad_soldador.grid(row=2, column=1)

    btn_entrega_soldador = ttk.Button(
        entrega_base,
        text="Enviar Al Soldador",
        style="TButton",
        command=lambda: eliminar_cantidad_de_piezas(
            combocaja_soldador.get(),
            entrada_cantidad_soldador.get(),
            tabla_chapa,
            subtitulo,
            lista_acciones,
        ),
    )
    btn_entrega_soldador.grid(row=3, column=1, pady=2)

    resibidas_base = ttk.Frame(box3, style='Pestania.TFrame')
    resibidas_base.grid(row=11, column=1)

    ttk.Label(resibidas_base, text="Bases Terminadas", style='WhiteOnRed.TLabel').grid(row=0, column=0)

    ttk.Label(resibidas_base, text="Tipo De Base:", style='WhiteOnRed.TLabel').grid(row=1, column=0)
    combocaja_terminadas = ttk.Combobox(
        resibidas_base, values=tipos_de_bases, state="readonly"
    )
    combocaja_terminadas.grid(row=1, column=1, pady=4)

    ttk.Label(resibidas_base, text="Cantidad:", style='WhiteOnRed.TLabel').grid(row=2, column=0)
    entrada_cantidad_terminadas = ttk.Entry(resibidas_base, style='WhiteOnRed.TEntry')
    entrada_cantidad_terminadas.grid(row=2, column=1)

    btn_entrega_soldador = ttk.Button(
        resibidas_base,
        text="Bases Terminadas",
        style="TButton",
        command=lambda: bases_soldador_terminadas(
            combocaja_terminadas.get(),
            entrada_cantidad_terminadas.get(),
            lista_acciones,
            tabla_chapa,
        ),
    )
    btn_entrega_soldador.grid(row=3, column=1, pady=2)

    ttk.Separator(box3, orient="horizontal").grid(
        row=12, column=0, columnspan=2, sticky="ew", padx=10, pady=10
    )

    # _______________________datosFinales_________________________________

    datos_finales = ttk.Frame(box3, style='Pestania.TFrame')
    datos_finales.grid(row=14, column=0)

    boton_consulta_cabezales = ttk.Button(
        datos_finales,
        text="Consulta de Cabezales",style="TButton",
        command=lambda: mostrar_cabezales_en_bruto(tabla_chapa, subtitulo),
    )
    boton_consulta_cabezales.grid(row=0, column=1, pady=3)

    boton_consulta_bases_terminadas = ttk.Button(
        datos_finales,
        text="Consulta de Bases Termindas",style="TButton",
        command=lambda: mostrar_bases_en_bruto(tabla_chapa, subtitulo),
    )
    boton_consulta_bases_terminadas.grid(row=1, column=1, pady=3)

    # ___________________Cabezales_____________________________

    ttk.Label(box3, text="Cabezales Terminado", font=("Arial", 17, "bold"), style='WhiteOnRed.TLabel').grid(
        row=13, column=1, padx=5, pady=5, sticky="e"
    )

    cabezales_terminados = ttk.Frame(box3, style='Pestania.TFrame')
    cabezales_terminados.grid(row=14, column=1)


    ttk.Label(cabezales_terminados, style='WhiteOnRed.TLabel', text="acero").grid(row=1, column=0)

    entrada_cantida_inox = ttk.Entry(cabezales_terminados, width=10, style='WhiteOnRed.TEntry')
    entrada_cantida_inox.grid(row=2, column=0)

    btn_agregar_cabezal_inox = ttk.Button(
        cabezales_terminados,
        text="Agregar",
        style="TButton",
        command= lambda: armar_cabezales_inox(entrada_cantida_inox.get(), lista_acciones)
    )
    btn_agregar_cabezal_inox.grid(row=3, column=0, padx=3, pady=3)

    ttk.Label(cabezales_terminados, style='WhiteOnRed.TLabel', text="pintada").grid(row=1, column=1)

    entrada_cantidad_pintada = ttk.Entry(cabezales_terminados, width=10, style='WhiteOnRed.TEntry')
    entrada_cantidad_pintada.grid(row=2, column=1)

    btn_agregar_cabezal_pintada = ttk.Button(
        cabezales_terminados,
        text="Agregar",
        style="TButton",
        command=lambda: armar_cabezales_pint(entrada_cantidad_pintada.get(), lista_acciones)
    )
    btn_agregar_cabezal_pintada.grid(row=3, column=1, padx=3, pady=3)
    
    ttk.Label(cabezales_terminados, style='WhiteOnRed.TLabel', text="250").grid(row=1, column=2)

    entrada_cantidad_250 = ttk.Entry(cabezales_terminados, width=10, style='WhiteOnRed.TEntry')
    entrada_cantidad_250.grid(row=2, column=2)

    btn_agregar_cabezal_pintada = ttk.Button(
        cabezales_terminados,
        text="Agregar",
        style="TButton",
        command=lambda: armar_cabezales_250(entrada_cantidad_250.get(), lista_acciones)
        )

    btn_agregar_cabezal_pintada.grid(row=3, column=2, padx=3, pady=3)
#---------------------------------------------------------------\
    
    obseraciones = ttk.Frame(box3, style='Pestania.TFrame')
    obseraciones.grid(row=15, column=0 , columnspan=1, sticky="ne", pady=15)
    ttk.Label(obseraciones, text="Observaciones", style='WhiteOnRed.TLabel', font=("Arial", 13, "bold")).grid(row=16, column=0, sticky="w")
    caja_texto = tk.Text(obseraciones, height=5, width=30)
    caja_texto.grid(row=17, column=0, columnspan=2)

    boton_enviar = tk.Button(obseraciones, text="Enviar", command=lambda: agregar_a_lista_tarea(caja_texto, lista_acciones))
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