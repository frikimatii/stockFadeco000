import tkinter as tk
from tkinter import ttk
from funciones import mostrar_piezas_armados, mostrar_pieza, mostrar_piezas_modelo, ensamblar_motor_terminado,mostrar_datos, eliminar_pieza, stock_prearmado,  actualizar_inventario, mostrar_pieza_afilador, mostrar_afilador_final, motores_terminados,armado_final_afiladores_y_agregar_cantidad,  mostrar_por_pieza, bases_terminados, mostrar_piezas_finales, mostrar_piezas_i330, armado_de_maquinas, mostrar_maquinas_teminadas

tipo = ["330", "300", "250"]

piezas_delete_armadocaja = [
    "caja_torneado_330",
    "caja_torneado_300",
    "caja_torneado_250",
    "manchon",
    "manchon_250",
    "eje",
    "eje_250",
    "ruleman_1",
    "ruleman_2",
    "corona_330",
    "corona_250",
    "orni",
    "corona_300",
    "motores_220w",
    "seguer",
    "sinfin",
    "motores250_220w"
]
piezas_delete_prearmado = [
    "aro_numerador",
    "base_pintada_300",
    "base_pintada_330",
    "cable_220w",
    "cajamotor_final_250",
    "cajamotor_final_300",
    "cajamotor_final_330",
    "capacitores",
    "capacitores_250",
    "carros",
    "carros_250",
    "eje_rectificado",
    "espiral",
    "guia_U",
    "inox_250",
    "inox_300",
    "inox_330",
    "movimientos",
    "patas",
    "perilla_numerador",
    "resorte_carro",
    "resorte_movimiento",
    "rueditas",
    "tapita_perilla",
    "teclas",
    "tornillo_guia",
    "varilla_carro_250",
    "varilla_carro_300",
    "varilla_carro_330"
]

tipos_de_maquinas = ["inox_330", "inox_300", "inox_250", "pintada_330", "pintada_300"]

motores_330 = (
    "caja_torneado_330",
    "eje",
    "manchon",
    "ruleman_1",
    "ruleman_2",
    "corona_330",
    "seguer",
    "sinfin",
    "motores_220w",
)
motores_300 = (
    "caja_torneado_300",
    "eje",
    "manchon",
    "ruleman_1",
    "ruleman_2",
    "corona_300",
    "seguer",
    "sinfin",
    "motores_220w",
)
motores_250 = (
    "caja_torneado_250",
    "eje_250",
    "manchon_250",
    "ruleman_1",
    "ruleman_2",
    "corona_250",
    "seguer",
    "sinfin",
    "motores250_220w",
)

cantidad_piezas_afiladore = {
    "capuchon_afilador": 2,
    "carcaza_afilador": 1,
    "eje_corto": 1,
    "eje_largo": 1,
    "ruleman_afilador": 2,
    "palanca_afilador": 1
}

i330pieza = {
        "brazo_330",
        "cubrecuchilla_330",
        "velero",
        "perilla_brazo",
        "cabezal_inox",
        "teletubi_330",
        "cuchilla_330",
        "cuadrado_regulador",
        "vela_final_330",
        "cubre_motor_rectangulo",
        "cubre_motor_cuadrado",
        "planchada_final_330",
        "varilla_brazo_330",
        "resorte_brazo",
        "tapa_afilador",
        "pipas",
        "tubo_manija",
        "afilador_final",
        "perilla_cubrecuchilla",
        "perilla_afilador",
        "base_afilador_330",
        "base_pre_armada330inox",
        "piedra_afilador",
    }
i300pieza = {
    "brazo_300" ,
    "cubrecuchilla_300" ,
    "velero" ,
    "perilla_brazo" ,
    "cabezal_inox" ,
    "teletubi_300" ,
    "cuchilla_300" ,
    "cuadrado_regulador" ,
    "vela_final_300" ,
    "cubre_motor_rectangulo" ,
    "cubre_motor_cuadrado" ,
    "planchada_final_300" ,
    "varilla_brazo_300" ,
    "resorte_brazo" ,
    "tapa_afilador" ,
    "pipas" ,
    "tubo_manija" ,
    "afilador_final" ,
    "perilla_cubrecuchilla" ,
    "perilla_afilador" ,
    "base_afilador_300" ,
    "base_pre_armada300inox" ,
    "piedra_afilador" ,
}
i250pieza = {
    "brazo_250" ,
    "cubrecuchilla_250" ,
    "velero" ,
    "perilla_brazo" ,
    "cabezal_inox" ,
    "teletubi_250" ,
    "cuchilla_250" ,
    "cuadrado_regulador" ,
    "vela_final_250" ,
    "cubre_motor_rectangulo" ,
    "planchada_final_250" ,
    "varilla_brazo_250" ,
    "resorte_brazo" ,
    "tapa_afilador_250" ,
    "pipas" ,
    "tubo_manija_250" ,
    "afilador_final" ,
    "perilla_cubrecuchilla" ,
    "perilla_afilador" ,
    "base_afilador_250" ,
    "base_pre_armada250inox" ,
    "piedra_afilador" ,
}
p330pieza = {
    "brazo_330" ,
    "cubrecuchilla_330" ,
    "velero" ,
    "perilla_brazo" ,
    "cabezal_inox" ,
    "teletubi_330" ,
    "cuchilla_330" ,
    "cuadrado_regulador" ,
    "vela_final_330" ,
    "cubre_motor_rectangulo" ,
    "cubre_motor_cuadrado" ,
    "planchada_final_330" ,
    "varilla_brazo_330" ,
    "resorte_brazo" ,
    "tapa_afilador" ,
    "pipas" ,
    "tubo_manija" ,
    "afilador_final" ,
    "perilla_cubrecuchilla" ,
    "perilla_afilador" ,
    "base_afilador_330" ,
    "base_pre_armada330pint" ,
    "piedra_afilador" ,
}
p300pieza = {
    "brazo_300" ,
    "cubrecuchilla_300" ,
    "velero" ,
    "perilla_brazo" ,
    "cabezal_inox" ,
    "teletubi_300" ,
    "cuchilla_300" ,
    "cuadrado_regulador" ,
    "vela_final_300" ,
    "cubre_motor_rectangulo" ,
    "cubre_motor_cuadrado" ,
    "planchada_final_300" ,
    "varilla_brazo_300" ,
    "resorte_brazo" ,
    "tapa_afilador" ,
    "pipas" ,
    "tubo_manija" ,
    "afilador_final" ,
    "perilla_cubrecuchilla" ,
    "perilla_afilador",
    "base_afilador_300" ,
    "base_pre_armada300pint" ,
    "piedra_afilador" , 
}

piezas_armado_final_delete = [
    "afilador_final",
    "base_afilador_250",
    "base_afilador_300",
    "base_afilador_330",
    "base_pre_armada250inox",
    "base_pre_armada300inox",
    "base_pre_armada300pint",
    "base_pre_armada330inox",
    "base_pre_armada330pint",
    "brazo_250",
    "brazo_300",
    "brazo_330",
    "cabezal_inox",
    "cabezal_pintura",
    "cuadrado_regulador",
    "cubre_motor_cuadrado",
    "cubre_motor_rectangulo",
    "cubrecuchilla_250",
    "cubrecuchilla_300",
    "cubrecuchilla_330",
    "cuchilla_250",
    "cuchilla_300",
    "cuchilla_330",
    "perilla_afilador",
    "perilla_brazo",
    "perilla_cubrecuchilla",
    "piedra_afilador",
    "pipas",
    "planchada_final_250",
    "planchada_final_300",
    "planchada_final_330",
    "resorte_brazo",
    "tapa_afilador",
    "tapa_afilador_250",
    "teletubi_250",
    "teletubi_300",
    "teletubi_330",
    "tubo_manija",
    "tubo_manija_250",
    "varilla_brazo_250",
    "varilla_brazo_300",
    "varilla_brazo_330",
    "vela_final_250",
    "vela_final_300",
    "vela_final_330",
    "velero"
]


def seccion_armado(notebook):
    pestania = ttk.Frame(notebook)
    pestania.grid(
        row=0,
        column=0,
        padx=10,
        pady=10,
    )

    notebook.add(pestania, text="Zona De Armado")
    tk.Label(pestania, text="Zona De Armado").grid(
        row=1, column=0, columnspan=4)
    caja1 = ttk.Frame(pestania)
    caja1.grid(row=2, column=0)

    res = tk.Label(caja1, text="mostrar Datos")
    res.grid(row=1, column=0)

    arbol = ttk.Treeview(caja1, columns=("Pieza", "Cantidad"))
    arbol.heading("Pieza", text="Pieza")
    arbol.heading("Cantidad", text="Cantidad")
    arbol.column("#0", width=0, stretch=tk.NO)
    arbol.column("Pieza", anchor=tk.W, width=170)
    arbol.column("Cantidad", anchor=tk.W, width=90)
    arbol.config(height=20)
    arbol.grid(row=2, column=0, pady=5, padx=5, sticky="nsew")

    result = tk.Listbox(caja1, width=60)
    result.grid(row=3, column=0, padx=3, pady=3)

    caja2 = ttk.Frame(pestania)
    caja2.grid(row=2, column=1)

    tk.Label(caja2, text="Armado de Cajas").grid(row=0, column=0)

    tk.Label(caja2, text="Cantidad De Motores").grid(row=1, column=0)
    tk.Button(caja2, text="Motores", command=lambda:
              mostrar_pieza(arbol, "motores_220w", res)).grid(row=1, column=1)

    ttk.Separator(caja2, orient="horizontal").grid(
        row=2, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    tk.Label(caja2, text="Mostrar Piezas").grid(row=3, column=0)
    tk.Button(caja2, text="Ver", command=lambda:
              mostrar_piezas_armados(arbol, "armado_de_caja", res)).grid(row=3, column=1)

    ttk.Separator(caja2, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, pady=5, padx=5)
    

    botonera_cajas = tk.Frame(caja2)
    botonera_cajas.grid(row=5, column=0)

    tk.Label(botonera_cajas, text="Piezas por modelo").grid(
        row=0, column=0, columnspan=3)
    tk.Button(botonera_cajas, text="330", command=lambda: mostrar_piezas_modelo(arbol, motores_330, res, "330")).grid(row=1, column=0)
    tk.Button(botonera_cajas, text="300", command=lambda: mostrar_piezas_modelo(arbol, motores_300, res, "300")).grid(row=1, column=1)
    tk.Button(botonera_cajas, text="250", command=lambda: mostrar_piezas_modelo(arbol, motores_250, res, "250")).grid(row=1, column=2)

    ttk.Separator(botonera_cajas, orient="horizontal").grid(
        row=2, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja2, text="Motores Armados").grid(row=6, column=0)

    checkbox = ttk.Frame(caja2)
    checkbox.grid(row=7, column=0, columnspan=2)

    modelo = tk.IntVar()
    modelo.set(1)
    tk.Label(checkbox, text="Modelo").grid(row=0, column=0)
    tk.Radiobutton(checkbox, text="330", variable=modelo,
                   value=1).grid(row=1, column=0)
    tk.Radiobutton(checkbox, text="300", variable=modelo,
                   value=2).grid(row=1, column=1)
    tk.Radiobutton(checkbox, text="250", variable=modelo,
                   value=3).grid(row=1, column=2)

    tk.Label(caja2, text="Cantidad").grid(row=8, column=0)
    cantidad_motores = tk.Entry(caja2)
    cantidad_motores.grid(row=8, column=1)
    
    def enviar():
        # Obtener el valor actual del objeto IntVar (modelo)
        modelo_seleccionado = modelo.get()
        # Luego, usar el valor para acceder al diccionario y llamar a la función
        ensamblar_motor_terminado(modelo_seleccionado, cantidad_motores, result)

    # Crear el botón y asociarlo a la función 'enviar'
    tk.Button(caja2, text="Enviar", command=enviar).grid(row=9, column=1)

    ttk.Separator(caja2, orient="horizontal").grid(
        row=10, column=0, sticky="ew", columnspan=2, pady=5, padx=5)


    tk.Label(caja2, text="Consulta:").grid(row=11, column=0)
    tk.Label(caja2, text="Motores Terminados ").grid(row=12, column=0)
    tk.Button(caja2, text="Terminados", command=lambda: motores_terminados(arbol, res)).grid(row=13, column=1)
    
    ttk.Separator(caja2, orient="horizontal").grid(
        row=14, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja2, text="Piezas Rotas o Defectuosa").grid(row=15, column=0)

    tk.Label(caja2, text="Seleccionar Piezas").grid(row=16, column=0)
    pieza_del = ttk.Combobox(caja2, values=piezas_delete_armadocaja)
    pieza_del.grid(row=16, column=1)

    tk.Label(caja2, text="Cantidad").grid(row=17, column=0)
    cantidad_delete = ttk.Entry(caja2)
    cantidad_delete.grid(row=17, column=1)

    #eliminar_piez(combox, cantida list tabla , funcion , arbol)

    tk.Button(caja2, text="Ver", command=lambda: eliminar_pieza(pieza_del, cantidad_delete, result, "piezas_finales_defenitivas", mostrar_datos, arbol)).grid(row=18, column=1)


    ttk.Separator(caja2, orient="horizontal").grid(
        row=19, column=0, sticky="ew", columnspan=2, pady=5, padx=5)
    
    #------------------------Afilador ----------------------------
    caja3 = tk.Frame(pestania)
    caja3.grid(row=2, column=2)

    tk.Label(caja3, text="Armado De Afilador").grid(row=0, column=0)

    tk.Label(caja3, text="Mostrar Piezas").grid(row=1, column=0)
    tk.Button(caja3, text="Ver", command=lambda: mostrar_pieza_afilador(arbol, res)).grid(row=1, column=1)

    ttk.Separator(caja3, orient="horizontal").grid(
        row=2, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja3, text="Afiladores Terminadas").grid(row=3, column=0)
    tk.Button(caja3, text="Mostrar", command=lambda: mostrar_afilador_final(arbol, res)).grid(row=3, column=1)

    ttk.Separator(caja3, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja3, text="Cantidad Agregada").grid(row=5, column=0)
    cantidad_afilador = tk.Entry(caja3)
    cantidad_afilador.grid(row=6, column=0)
    tk.Button(caja3, text="Agregar", command=lambda:  armado_final_afiladores_y_agregar_cantidad(int(cantidad_afilador.get()), result)).grid(row=7, column=0)

    ttk.Separator(caja3, orient="horizontal").grid(
        row=8, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

     #=================================PRe Armado ==================+++++=====
    
    caja4 = tk.Frame(pestania)
    caja4.grid(row=2, column=3)

    tk.Label(caja4, text="Pre Armado").grid(row=0, column=0)

    tk.Label(caja4, text="Total De Piezas").grid(row=1, column=0)
    tk.Button(caja4, text="Mostrar", command=lambda: stock_prearmado(arbol, res)).grid(row=1, column=1)

    ttk.Separator(caja4, orient="horizontal").grid(
        row=2, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja4, text="Piezas De Modelos").grid(row=3, column=0)

    botonera_prearmado = tk.Frame(caja4)
    botonera_prearmado.grid(row=4, column=0)

 #ostrar_por_pieza(arbol, modelo, res)
    tk.Button(botonera_prearmado, text="330", command=lambda: mostrar_por_pieza(arbol,"330",res)).grid(row=0, column=0)
    tk.Button(botonera_prearmado, text="300", command=lambda: mostrar_por_pieza(arbol,"300", res)).grid(row=0, column=1)
    tk.Button(botonera_prearmado, text="250", command=lambda: mostrar_por_pieza(arbol,"250", res)).grid(row=0, column=3)

    ttk.Separator(caja4, orient="horizontal").grid(
        row=5, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja4, text="Maquinas pre-armadas").grid(row=6, column=0)

    tk.Label(caja4, text="Modelo de Maquina").grid(row=7, column=0)
    tipo_prearmada = ttk.Combobox(caja4, values=tipos_de_maquinas)
    tipo_prearmada.grid(row=7, column=1)

    tk.Label(caja4, text="Cantidad").grid(row=8, column=0)
    cantidad_prearmada = tk.Entry(caja4)
    cantidad_prearmada.grid(row=8, column=1)

    tk.Button(caja4, text="Enviar", command=lambda: actualizar_inventario(
            result, int(cantidad_prearmada.get()),tipo_prearmada.get()
        ),).grid(row=9, column=1)

    ttk.Separator(caja4, orient="horizontal").grid(
        row=10, column=0, sticky="ew", columnspan=2, pady=5, padx=5)



    tk.Label(caja4, text="Consulta:").grid(row=11, column=0)
    tk.Label(caja4, text="Motores Terminados ").grid(row=12, column=0)
    tk.Button(caja4, text="Terminados", command=lambda: bases_terminados(arbol, res)).grid(row=13, column=1)
    
    ttk.Separator(caja4, orient="horizontal").grid(
        row=14, column=0, sticky="ew", columnspan=2, pady=5, padx=5)



    tk.Label(caja4, text="Piezas Rotas o Defectuosa").grid(row=15, column=0)

    tk.Label(caja4, text="Seleccionar Piezas").grid(row=16, column=0)
    prearmadolo_delete = ttk.Combobox(caja4, values=piezas_delete_prearmado)
    prearmadolo_delete.grid(row=16, column=1)

    tk.Label(caja4, text="Cantidad").grid(row=17, column=0)
    cantidad_prearmado_delete = tk.Entry(caja4)
    cantidad_prearmado_delete.grid(row=17, column=1)

    tk.Button(caja4, text="Ver", command=lambda: eliminar_pieza(prearmadolo_delete, cantidad_prearmado_delete, result, "piezas_finales_defenitivas", mostrar_datos, arbol)).grid(row=18, column=1)

    ttk.Separator(caja4, orient="horizontal").grid(
        row=19, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

 #----------====armado======---------
    caja5 = tk.Frame(pestania)
    caja5.grid(row=2, column=4)

    tk.Label(caja5, text="Armado Final").grid(row=0, column=0)

    tk.Label(caja5, text="Piezas Totales").grid(row=1, column=0)
    tk.Button(caja5, text="Mostrar", command=lambda: mostrar_piezas_finales(arbol, res)).grid(row=1, column=1)

    ttk.Separator(caja5, orient="horizontal").grid(
        row=2, column=0, sticky="ew", columnspan=2, padx=5, pady=5
    )

    tk.Label(caja5, text="Mostrar Base Pre_armadas").grid(row=3, column=0)
    tk.Button(caja5, text="Ver", command=lambda: bases_terminados(arbol, res)).grid(row=3, column=1)

    ttk.Separator(caja5, orient="horizontal").grid(
        row=4, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    botonera_armadofinal = tk.Frame(caja5)
    botonera_armadofinal.grid(row=5, column=0)

    tk.Label(botonera_armadofinal, text="Piezas por modelo").grid(row=0, column=0, columnspan=3)
    
    tk.Button(botonera_armadofinal, text="Inox 330", command=lambda: mostrar_piezas_i330(arbol, res, i330pieza, "Inox 330")).grid(row=1, column=0)
    tk.Button(botonera_armadofinal, text="Inox 300", command=lambda: mostrar_piezas_i330(arbol, res, i300pieza, "Inox 300")).grid(row=1, column=1)
    tk.Button(botonera_armadofinal, text="Inox 250", command=lambda: mostrar_piezas_i330(arbol, res, i250pieza, "Inox 250")).grid(row=1, column=2)

    tk.Button(botonera_armadofinal, text="Pintada 330", command=lambda: mostrar_piezas_i330(arbol, res, p330pieza, "Pint 330")).grid(row=2, column=0)
    tk.Button(botonera_armadofinal, text="Pintada 300", command=lambda: mostrar_piezas_i330(arbol, res, p300pieza, "Pint 300")).grid(row=2, column=1)

    ttk.Separator(botonera_cajas, orient="horizontal").grid(
        row=3, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja5, text="Maquinas Teminadas").grid(row=6, column=0)

    tk.Label(caja5, text="Modelo").grid(row=7, column=0)
    modele_final = ttk.Combobox(caja5, values=tipos_de_maquinas)
    modele_final.grid(row=7, column=1)

    tk.Label(caja5, text="Cantidad").grid(row=8, column=0)
    cantidad_final = tk.Entry(caja5)
    cantidad_final.grid(row=8, column=1)

    tk.Button(caja5, text="Enviar", command=lambda: armado_de_maquinas(cantidad_final.get() ,modele_final.get(), result)).grid(row=9, column=1)

    ttk.Separator(caja5, orient="horizontal").grid(
        row=10, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja5, text="Piezas Rotas o Defectuosa").grid(row=11, column=0)

    tk.Label(caja5, text="Seleccionar Piezas").grid(row=12, column=0)
    armadolo_delete = ttk.Combobox(caja5, values=piezas_armado_final_delete)
    armadolo_delete.grid(row=12, column=1)

    tk.Label(caja5, text="Cantidad").grid(row=13, column=0)
    cantidad_delete_final = tk.Entry(caja5)
    cantidad_delete_final.grid(row=13, column=1)

    tk.Button(caja5, text="Ver", command=lambda: eliminar_pieza(armadolo_delete, cantidad_delete_final, result, "piezas_finales_defenitivas", mostrar_datos, arbol)).grid(row=14, column=1)

    ttk.Separator(caja5, orient="horizontal").grid(
        row=15, column=0, sticky="ew", columnspan=2, pady=5, padx=5)

    tk.Label(caja5, text="listado de maquinas terminadas").grid(
        row=16, column=0)
    tk.Button(caja5, text="Ver", command=lambda: mostrar_maquinas_teminadas(arbol, res)).grid(row=17, column=1)

    ttk.Separator(caja5, orient="horizontal").grid(
        row=18, column=0, sticky="ew", columnspan=2, pady=5, padx=5)
