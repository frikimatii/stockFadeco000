import sqlite3
import tkinter as tk 
from tkinter import ttk ,messagebox

def mostrar_datos(tree1, table):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT piezas, cantidad FROM {table}")
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)
        
def sort_column(tree, col, reverse):
    items = [(tree.set(item, col), item) for item in tree.get_children('')]
    items.sort(reverse=reverse)

    # Reorganiza los elementos en la tabla
    for index, (val, item) in enumerate(items):
        tree.move(item, '', index)

    # Cambia la dirección de la ordenación
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))
        
def actualizar_pieza(lista_predefinida, entrada_cantidad, res, table, funcion, tree):
    actualizar_pieza = lista_predefinida.get()
    entrada_actualizar = entrada_cantidad.get()

    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)

        if entrada_actualizar < 0:
            res.config(text="La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT cantidad FROM {table} WHERE piezas=?", (actualizar_pieza,))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + entrada_actualizar
                cursor.execute(f"UPDATE {table} SET cantidad=? WHERE piezas=?", (nueva_cantidad, actualizar_pieza))
                conn.commit()
                conn.close()
                mostrar_datos(tree, table)  # Llama a la función para mostrar los datos actualizados
                res.config(text=f"Carga exitosa: Usted cargó {entrada_actualizar} {actualizar_pieza}:")
            else:
                res.config(text=f"La Pieza {actualizar_pieza} no se puede modificar")
    else:
        res.config(text="La cantidad ingresada no es un número válido")

def eliminar_pieza(lista_predefinida_eliminar, entrada_cantidad_eliminar, res, table, funcion, tree):
 
    pieza_eliminar = lista_predefinida_eliminar.get()
    cantidad_eliminar = entrada_cantidad_eliminar.get()

    try:
        cantidad_eliminar = int(cantidad_eliminar)
        if cantidad_eliminar < 0:
            res.config(text="La cantidad no puede ser Negativa")
            return
    except ValueError:
        res.config(text="La cantidad debe ser un número entero positivo")

    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT cantidad FROM {table} WHERE piezas=?", (pieza_eliminar,))
    cantidad_actual = cursor.fetchone()

    if cantidad_actual is not None:
        cantidad_actual = cantidad_actual[0]
        if cantidad_eliminar <= cantidad_actual:
            nueva_cantidad = cantidad_actual - cantidad_eliminar
            if nueva_cantidad >= 0:
                cursor.execute(f"UPDATE {table} SET cantidad=? WHERE piezas=?", (nueva_cantidad, pieza_eliminar))
                res.config(text=f" Descarga exitosa: se elimino {pieza_eliminar} {cantidad_eliminar}")

            else:
                res.config(text=f"No se puede eliminar la pieza {pieza_eliminar}")
        else:
            res.config(text=f"No hay suficiente {pieza_eliminar} en el stock")
    else:
        res.config(text=f"La pieza {pieza_eliminar} no se puede eliminar")

    conn.commit()
    conn.close()
    mostrar_datos(tree, table) 

def enviar_piezas_a_pulido(pieza, cantidad, tabla, tree, newtable):
    pieza_seleccionada = pieza.get()
    cantidad_ingresada = cantidad.get()
    
    if not cantidad_ingresada.isdigit() or int(cantidad_ingresada) < 0:
        messagebox.showerror("Error", "Ingrese una Cantidad Válida")
        return
    
    conn = None
    cursor = None

    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT cantidad FROM {tabla} WHERE piezas = ?", (pieza_seleccionada, ))
        resultado = cursor.fetchone()
        cantidad_existente = resultado[0] if resultado else 0

        nueva_cantidad = cantidad_existente + int(cantidad_ingresada)

        # Iniciar una transacción
        conn.execute("BEGIN")

        # Actualizar la tabla donde envías las piezas a pulido
        cursor.execute(f"UPDATE {tabla} SET cantidad = ? WHERE piezas = ?", (nueva_cantidad, pieza_seleccionada))

        # Reducir la cantidad en la tabla de stock en bruto
        cursor.execute(f"SELECT cantidad FROM pieza_en_bruto_aluminio WHERE piezas = ?", (pieza_seleccionada, ))
        resultado_stock_bruto = cursor.fetchone()
        cantidad_stock_bruto = resultado_stock_bruto[0] if resultado_stock_bruto else 0

        nueva_cantidad_stock_bruto = cantidad_stock_bruto - int(cantidad_ingresada)
        cursor.execute(f"UPDATE pieza_en_bruto_aluminio SET cantidad = ? WHERE piezas = ?", (nueva_cantidad_stock_bruto, pieza_seleccionada))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        # Revertir la transacción en caso de error
        if conn:
            conn.rollback()
        messagebox.showerror("Error", f"Error en la base de datos: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    mostrar_datos(tree, tabla)
    mostrar_datos(newtable, "pieza_en_bruto_aluminio")
    
    print(f"{cantidad_ingresada} pieza(s) de {pieza_seleccionada} han sido enviadas a pulido.")

def mover_piezas_a_stock_pulidas(pieza, cantidad, tabla_carmelo, tabla_stock_pulidas, tree_carmelo, tree_stock_pulidas):
    pieza_seleccionada = pieza.get()
    cantidad_ingresada = cantidad.get()
    
    if not cantidad_ingresada.isdigit() or int(cantidad_ingresada) < 0:
        messagebox.showerror("Error", "Ingrese una Cantidad Válida")
        return
    
    conn = None
    cursor = None

    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()

        cursor.execute(f"SELECT cantidad FROM {tabla_carmelo} WHERE piezas = ?", (pieza_seleccionada, ))
        resultado = cursor.fetchone()
        cantidad_existente = resultado[0] if resultado else 0

        if int(cantidad_ingresada) > cantidad_existente:
            messagebox.showerror("Error", "No hay suficientes piezas en la tabla de Carmelo.")
            return

        # Iniciar una transacción
        conn.execute("BEGIN")

        # Actualizar la tabla de Carmelo reduciendo la cantidad
        nueva_cantidad_carmelo = cantidad_existente - int(cantidad_ingresada)
        cursor.execute(f"UPDATE {tabla_carmelo} SET cantidad = ? WHERE piezas = ?", (nueva_cantidad_carmelo, pieza_seleccionada))

        # Actualizar la tabla de Stock Pulidas aumentando la cantidad
        cursor.execute(f"SELECT cantidad FROM {tabla_stock_pulidas} WHERE piezas = ?", (pieza_seleccionada, ))
        resultado_stock_pulidas = cursor.fetchone()
        cantidad_stock_pulidas = resultado_stock_pulidas[0] if resultado_stock_pulidas else 0

        nueva_cantidad_stock_pulidas = cantidad_stock_pulidas + int(cantidad_ingresada)
        cursor.execute(f"UPDATE {tabla_stock_pulidas} SET cantidad = ? WHERE piezas = ?", (nueva_cantidad_stock_pulidas, pieza_seleccionada))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        # Revertir la transacción en caso de error
        if conn:
            conn.rollback()
        messagebox.showerror("Error", f"Error en la base de datos: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    mostrar_datos(tree_carmelo, tabla_carmelo)
    mostrar_datos(tree_stock_pulidas, tabla_stock_pulidas)
    
    print(f"{cantidad_ingresada} pieza(s) de {pieza_seleccionada} han sido movidas a Stock Pulidas.")

#funciones de stock de chapas _________________________________________________
def mostrar_datos_chapa(tree1, table, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT piezas, cantidad, modelo, tipo_de_base FROM {table}")
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)
    
    subtitulo_text = "Stock Completo"
    subtitulo.config(text=subtitulo_text)
    
def consulta_de_piezas(tabla, tipo_de_base, modelo, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT piezas, cantidad FROM chapa WHERE tipo_de_base = ? AND modelo = ? ", (tipo_de_base, modelo))
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for dato in datos:
        tabla.insert("", "end", values=dato)
        
    subtitulo_text = f"Mostrando {tipo_de_base} {modelo}"
    subtitulo.config(text=subtitulo_text)

def consulta_cabezales(tabla, tipo_de_base, modelo, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM chapa WHERE tipo_de_base = ? AND modelo = ? AND piezas IN ('chapa_U_cabezal', 'tapa_cabezal', 'bandeja_cabezal')", (tipo_de_base, modelo))
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for dato in datos:
        tabla.insert("", "end", values=dato)
        
    subtitulo_text = f"Mostrando {tipo_de_base} {modelo}"
    subtitulo.config(text=subtitulo_text)
    
def stock_chapa(tabla, tipo_de_base, subtitulo):
    conn =sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad, modelo FROM chapa WHERE tipo_de_base = ?", (tipo_de_base, ))
    datos = cursor.fetchall()
    conn.close()
    
    for item in tabla.get_children():
        tabla.delete(item)
    for dato in datos:
        tabla.insert("", "end", values=dato)
        
    subtitulo_text = f"Mostrando {tipo_de_base}"
    subtitulo.config(text=subtitulo_text)
    
def agregar_pieza_chapas(tipo_var, lista_agregar_chapa, cantidad_agregar, arbol, tabla, lista_acciones):
    tipo = tipo_var.get()
    if tipo == 1:
        tipo = "acero"
    elif tipo == 2:
        tipo = "pintura"
    pieza = lista_agregar_chapa.get()
    cantidad = cantidad_agregar.get()

    if not cantidad.isdigit() or int(cantidad) < 1:
        lista_acciones.insert(0, "Ingrese una cantidad válida.")
    else:
        try:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM chapa WHERE tipo_de_base = ? AND piezas = ?", (tipo, pieza))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_existente = resultado[0]
                cantidad_nueva = cantidad_existente + int(cantidad)
                cursor.execute("UPDATE chapa SET cantidad = ? WHERE tipo_de_base = ? AND piezas = ?", (cantidad_nueva, tipo, pieza))
                conn.commit()
            else:
                cursor.execute("INSERT INTO chapa (tipo_de_base, piezas, cantidad) VALUES (?, ?, ?)", (tipo, pieza, cantidad))
            conn.commit()
        except sqlite3.Error as e:
            lista_acciones.insert(0, "ERROR EN LA BASE DE DATOS:", e)
        finally:
            if conn:
                conn.close()
            mostrar_datos(arbol, tabla)
            lista_acciones.insert(0, f"Carga exitosa: Agregó {cantidad} de {pieza}, de {tipo}")

def eliminar_pieza_chapas(tipo_var, lista_eliminar_chapa, cantidad_eliminar, arbol, tabla, lista_acciones ):
    tipo = tipo_var.get()
    if tipo == 1:
        tipo = "acero"
    elif tipo == 2:
        tipo = "pintura"
    pieza = lista_eliminar_chapa.get()
    cantidad = cantidad_eliminar.get()

    if not cantidad.isdigit() or int(cantidad) < 1:
        lista_acciones.insert(0, "Ingrese una cantidad válida.")
    else:
        try:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM chapa WHERE tipo_de_base = ? AND piezas = ?", (tipo, pieza))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_existente = resultado[0]
                if cantidad_existente >= int(cantidad):
                    cantidad_nueva = cantidad_existente - int(cantidad)
                    cursor.execute("UPDATE chapa SET cantidad = ? WHERE tipo_de_base = ? AND piezas = ?", (cantidad_nueva, tipo, pieza))
                    conn.commit()
                else:
                    lista_acciones.insert(0, "No hay suficiente cantidad para eliminar.")
            else:
                lista_acciones.insert(0, f"La pieza {pieza} no existe en la base de datos.")
        except sqlite3.Error as e:
            lista_acciones.insert(0, "ERROR EN LA BASE DE DATOS:", e)
        finally:
            if conn:
                conn.close()
            mostrar_datos(arbol, tabla)
            lista_acciones.insert(0, f"Eliminación exitosa: Eliminó {cantidad} de {pieza} de {tipo}")

def agregar_portaeje(entrada_agregar_porta_eje, tree, tabla, lista_acciones):
    entrada_actualizar = entrada_agregar_porta_eje.get()

    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)

        if entrada_actualizar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas = 'portaeje' ")
            cantidad_actual = cursor.fetchone()
            
            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + entrada_actualizar
                cursor.execute(f"UPDATE chapa SET cantidad=? WHERE piezas = 'portaeje' ", (nueva_cantidad, ))
                conn.commit()
                conn.close()
                mostrar_datos(tree , tabla)
                lista_acciones.insert(0, f"Carga de ejes: {entrada_actualizar}")
                
            else:
                lista_acciones.insert(0, "Cantidada ingresada invalida")
                
    else :
        lista_acciones.insert(0, "Ingrese un numero Valido")
        
def eliminar_portaeje(entrada_eliminar_porta_eje, tree, tabla, lista_acciones):
    entrada_eliminar = entrada_eliminar_porta_eje.get()

    if entrada_eliminar.strip().isdigit():
        entrada_eliminar = int(entrada_eliminar)

        if entrada_eliminar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas = 'portaeje' ")
            cantidad_actual = cursor.fetchone()
            
            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                if cantidad_actual >= entrada_eliminar:
                    nueva_cantidad = cantidad_actual - entrada_eliminar
                    cursor.execute(f"UPDATE chapa SET cantidad=? WHERE piezas = 'portaeje'", (nueva_cantidad, ))
                    conn.commit()
                    conn.close()
                    mostrar_datos(tree, tabla)
                    lista_acciones.insert(0, f"Eliminación de ejes: {entrada_eliminar}")
                else:
                    lista_acciones.insert(0, "No hay suficiente cantidad para eliminar.")
            else:
                lista_acciones.insert(0, "Cantidad ingresada inválida")
    else:
        lista_acciones.insert(0, "Ingrese un número válido")

def calcular_maquinas(maquina, lista_acciones):
    try:
        conn = sqlite3.connect("basedatospiezas.db")  # Reemplaza con el nombre de tu base de datos
        cursor = conn.cursor()

        # Consulta las cantidades de las piezas en la base de datos
        cantidades = {}
        for pieza, cantidad in maquina.items():
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas = ?", (pieza,))
            resultado = cursor.fetchone()
            if resultado is not None:
                cantidad_disponible = resultado[0]
                cantidades[pieza] = cantidad_disponible

        # Calcula la cantidad máxima de máquinas que se pueden armar
        cantidad_maquinas = min(cantidades.values()) // min(maquina.values())
        return lista_acciones.insert(0, f"Se pueden armar {cantidad_maquinas} máquinas de acero 330.")
    
    except sqlite3.Error as e:
        print("ERROR EN LA BASE DE DATOS:", e)
        return 0  # En caso de error, devuelve 0 máquinas

def agregar_piezas_faltantes(lista_agregar_v_p,cantidad_agregar_v_p, arbol, lista_acciones, tabla):
    pieza_seleccionada = lista_agregar_v_p.get()
    cantidad_ingregas = cantidad_agregar_v_p.get()
        
    if cantidad_ingregas.strip().isdigit():
        cantidad_ingregas = int(cantidad_ingregas)

        if cantidad_ingregas < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas=?", (pieza_seleccionada,))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + cantidad_ingregas
                cursor.execute(f"UPDATE chapa SET cantidad=? WHERE piezas=?", (nueva_cantidad, pieza_seleccionada))
                conn.commit()
                conn.close()
                mostrar_datos(arbol, tabla)
                lista_acciones.insert(0, f"Carga exitosa: Usted cargó {cantidad_ingregas} {pieza_seleccionada}:")
            else:
                lista_acciones.insert(0, f"La Pieza {pieza_seleccionada} no se puede modificar")
    else:
            lista_acciones.insert(0, "La cantidad ingresada no es un número válido")
    
def eliminar_piezas_faltante(pieza_seleccionada, cantidad_eliminar, arbol, lista_acciones, tabla):

    if cantidad_eliminar.strip().isdigit():
        cantidad_eliminar = int(cantidad_eliminar)

        if cantidad_eliminar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas=?", (pieza_seleccionada,))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]

                if cantidad_actual >= cantidad_eliminar:
                    nueva_cantidad = cantidad_actual - cantidad_eliminar
                    cursor.execute(f"UPDATE chapa SET cantidad=? WHERE piezas=?", (nueva_cantidad, pieza_seleccionada,))
                    conn.commit()
                    conn.close()
                    mostrar_datos(arbol, tabla)
                    lista_acciones.insert(0, f"Eliminación exitosa: Usted eliminó {cantidad_eliminar} de {pieza_seleccionada}")
                else:
                    lista_acciones.insert(0, "No hay suficiente cantidad para eliminar.")
            else:
                lista_acciones.insert(0, f"La Pieza {pieza_seleccionada} no se puede modificar")
    else:
        lista_acciones.insert(0, "La cantidad ingresada no es un número válido")

def mostrar_stock_soldador(tabla):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()

        cursor.execute("SELECT modelo, tipo, cantidad FROM soldador_stock WHERE cantidad > 0")
        stock_disponible = cursor.fetchall()

        # Limpiar la tabla antes de llenarla
        tabla.delete(*tabla.get_children())

        if stock_disponible:
            for modelo, tipo, cantidad in stock_disponible:
                tabla.insert("", "end", values=("Soldador", cantidad, modelo, tipo))
        else:
            print("No hay stock disponible para el soldador.")

        conn.close()

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")

def calcular_maquinas_posibles(base_modelo, tipo_base, modelo, lista_acciones):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        
        cantidades = {}

        for pieza, cantidad in base_modelo.items():
            cursor.execute("SELECT cantidad FROM chapa WHERE tipo_de_base = ? AND modelo = ? AND piezas = ?", (tipo_base, modelo, pieza))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_disponible = resultado[0]
                cantidades[pieza] = cantidad_disponible

        if len(cantidades) == len(base_modelo):
            cantidad_bases = min(cantidades.values()) // min(base_modelo.values())
            lista_acciones.insert(0, f"Se pueden armar {cantidad_bases} máquinas.")
        else:
            lista_acciones.insert(0, "No hay piezas suficientes para armar las máquinas.")
            
        conn.close()

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        lista_acciones.insert(0, "Error en la base de datos.")

def eliminar_base_ingreso_soldador(combocaja_soldador, entrada_cantidad_soldador):
    tipo_base = combocaja_soldador.get()
    cantidad = int(entrada_cantidad_soldador.get())
    
    bases_dict = {
    "Inox 330": {
        "chapa_principal": "chapa_principal_330",
        "lateral_L": "lateral_L_330",
        "lateral_R": "lateral_R_330",
        "planchuela": "planchuela_330",
        "varilla": "varilla_330",
        "portaeje": "portaeje",
        "arandela": "arandela"
    },
    "Inox 300": {
        "chapa_principal": "chapa_principal_300",
        "lateral_L": "lateral_L_300",
        "lateral_R": "lateral_R_300",
        "planchuela": "planchuela_300",
        "varilla": "varilla_300",
        "portaeje": "portaeje",
        "arandela": "arandela"
    },
    "Pintada 330": {
        "chapa_principal": "chapa_principal_330",
        "lateral_L": "lateral_L_330",
        "lateral_R": "lateral_R_330",
        "planchuela": "planchuela_330",
        "varilla": "varilla_330",
        "portaeje": "portaeje",
        "arandela": "arandela"
    },
    "Pintada 300": {
        "chapa_principal": "chapa_principal_300",
        "lateral_L": "lateral_L_300",
        "lateral_R": "lateral_R_300",
        "planchuela": "planchuela_300",
        "varilla": "varilla_300",
        "portaeje": "portaeje",
        "arandela": "arandela"
    }
}

    
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    
    modelo = tipo_base
    if tipo_base == "Inox 330":
        portaeje = bases_dict["Inox 330"]['portaeje']
        arandela = bases_dict["Inox 330"]['arandela']
        print("eliejiste inox330")
        cursor.execute(f"UPDATE chapa SET cantidad = cantidad - {cantidad} WHERE piezas = '{portaeje}'")
        cursor.execute(f"UPDATE chapa SET cantidad = cantidad - {cantidad} WHERE piezas = '{arandela}'")

    elif tipo_base == "Inox 300":
        print(bases_dict["Inox 300"])
        cursor.execute("update")
        
        
    elif tipo_base == "Pintada 330":
        print(bases_dict["Pintada 330"])

        print("elijiste pintada 330")
        
        
    else:
        print("elegitte pintada 300")
        print(bases_dict["Pintada 300"])

    conn.commit()
    conn.close()
    

    mensaje = f"Se ha Eliminado {cantidad} unidades de piezas de chapar en la tabla correspondiente a {tipo_base}, ({modelo})"    
    print(f"hola {tipo_base}, y {cantidad}")
    