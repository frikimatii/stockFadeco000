import sqlite3
import tkinter as tk 


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
                res.insert(0, f"Carga exitosa: Usted cargó {entrada_actualizar} {actualizar_pieza}:")
            else:
                res.insert(0, f"La Pieza {actualizar_pieza} no se puede modificar")
    else:
        res.insert(0, "La cantidad ingresada no es un número válido")

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
                res.insert(0, f" Descarga exitosa: se elimino {pieza_eliminar} {cantidad_eliminar}")

            else:
                res.insert(0, f"No se puede eliminar la pieza {pieza_eliminar}")
        else:
            res.insert(0, f"No hay suficiente {pieza_eliminar} en el stock")
    else:
        res.insert(0, f"La pieza {pieza_eliminar} no se puede eliminar")

    conn.commit()
    conn.close()
    mostrar_datos(tree, table) 

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
    cursor.execute(
    "SELECT piezas, cantidad FROM chapa WHERE tipo_de_base = 'acero_dulce' AND modelo IN (?, ?) UNION SELECT piezas, cantidad FROM chapa WHERE tipo_de_base = ? AND modelo = ?;",
    ('pieza', modelo, tipo_de_base, modelo)
    )
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

        cursor.execute("SELECT modelo, tipo , cantidad FROM soldador_stock ")
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

def is_positive_integer(value):
    try:
        num = int(value)
        return num >= 0
    except ValueError:
        return False

def eliminar_cantidad_de_piezas(combocaja_soldador, entrada_cantidad_soldador, tabla, subtitulo, lista_acciones):
    cantidad_str = entrada_cantidad_soldador
    tipo = combocaja_soldador

    # Verifica si la cantidad ingresada es un número
    if not cantidad_str.isdigit():
        mensaje_error = "Error: La cantidad debe ser un número entero."
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)
        return

    cantidad = int(cantidad_str)  # Convierte la cantidad a un entero

    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    # Obtiene información sobre la cantidad actual de las piezas
    cantidad_actual_por_pieza = {}

    if tipo == "Inox 330":
        lista_1 = ['chapa_principal_330', 'lateral_L_330', 'lateral_R_330']
        lista_2 = ['planchuela_330', 'varilla_330']
        lista_3 = ['arandela', 'portaeje']

        for pieza in lista_1:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero' AND modelo = 330 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(cantidad_actual_por_pieza[pieza] >= cantidad for pieza in lista_1 + lista_2 + lista_3)

        if not eliminacion_posible:
            mensaje_error = "Error: No es posible eliminar la cantidad deseada de piezas."
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero' AND modelo = 330 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """, (cantidad_restante, pieza))
            
        cursor.execute("UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '330' AND tipo = 'inox'", (cantidad,))
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador")
        conn.commit()
        consulta_de_piezas(tabla, "acero", "330", subtitulo)

    elif tipo == "Inox 300":
        lista_1 = ['chapa_principal_300', 'lateral_L_300', 'lateral_R_300']
        lista_2 = ['planchuela_300', 'varilla_300']
        lista_3 = ['arandela', 'portaeje']

        for pieza in lista_1:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero' AND modelo = 300 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(cantidad_actual_por_pieza[pieza] >= cantidad for pieza in lista_1 + lista_2 + lista_3)

        if not eliminacion_posible:
            mensaje_error = "Error: No es posible eliminar la cantidad deseada de piezas."
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero' AND modelo = 300 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """, (cantidad_restante, pieza))
            
        cursor.execute("UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '300' AND tipo = 'inox'", (cantidad,))
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador")
        conn.commit()
        consulta_de_piezas(tabla, "acero", "300", subtitulo)

    elif tipo == "Pintada 330":
        lista_1 = ['chapa_principal_330', 'lateral_L_330', 'lateral_R_330']
        lista_2 = ['planchuela_330', 'varilla_330']
        lista_3 = ['arandela', 'portaeje']

        for pieza in lista_1:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'pintura' AND modelo = 330 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(cantidad_actual_por_pieza[pieza] >= cantidad for pieza in lista_1 + lista_2 + lista_3)

        if not eliminacion_posible:
            mensaje_error = "Error: No es posible eliminar la cantidad deseada de piezas."
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'pintura' AND modelo = 330 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """, (cantidad_restante, pieza))
            
        cursor.execute("UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '330' AND tipo = 'pintada'", (cantidad,))
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador")
        conn.commit()
        consulta_de_piezas(tabla, "pintura", "330", subtitulo)

    elif tipo == "Pintada 300":
        lista_1 = ['chapa_principal_300', 'lateral_L_300', 'lateral_R_300']
        lista_2 = ['planchuela_300', 'varilla_300']
        lista_3 = ['arandela', 'portaeje']

        for pieza in lista_1:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'pintura' AND modelo = 300 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute("""
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """, (pieza,))
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(cantidad_actual_por_pieza[pieza] >= cantidad for pieza in lista_1 + lista_2 + lista_3)

        if not eliminacion_posible:
            mensaje_error = "Error: No es posible eliminar la cantidad deseada de piezas."
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'pintura' AND modelo = 300 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """, (cantidad_restante, pieza))

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute("""
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """, (cantidad_restante, pieza))
            
        cursor.execute("UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '300' AND tipo = 'pintada'", (cantidad,))
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador")
        conn.commit()
        consulta_de_piezas(tabla, "pintura", "300", subtitulo)

    conn.close()

def bases_soldador_terminadas(combocaja_terminadas, entrada_cantidad_terminadas, lista_acciones, tabla_chapa):
    tipo = combocaja_terminadas
    cantidad_str = entrada_cantidad_terminadas

    # Verifica si la cantidad ingresada es un número
    if not cantidad_str.isdigit():
        mensaje_error = "Error: La cantidad debe ser un número entero."
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)
        return

    cantidad = int(cantidad_str)  # Convierte la cantidad a un entero

    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    try:
        if tipo == "Inox 330":
            # Obtén la cantidad actual de la base de datos para Inox 330
            cursor.execute("SELECT cantidad FROM soldador_stock WHERE tipo = 'inox' AND modelo = '330'")
            cantidad_actual = cursor.fetchone()

            # Verifica si hay suficientes bases disponibles
            if cantidad_actual is None:
                mensaje_error = "No hay registros para Inox 330 en la base de datos."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            cantidad_actual = cantidad_actual[0]

            if cantidad_actual < cantidad:
                mensaje_error = f"No hay suficientes bases de Inox 330 disponibles. Cantidad actual: {cantidad_actual}."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            # Actualiza la cantidad en la base de datos soldador_stock
            nueva_cantidad_soldador = max(0, cantidad_actual - cantidad)
            cursor.execute("""
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'inox' AND modelo = '330'
            """, (nueva_cantidad_soldador,))

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute("""
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'inox_330'
            """, (cantidad,))

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Inox 330."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)

        if tipo == "Inox 300":
            # Obtén la cantidad actual de la base de datos para Inox 300
            cursor.execute("SELECT cantidad FROM soldador_stock WHERE tipo = 'inox' AND modelo = '300'")
            cantidad_actual = cursor.fetchone()

            # Verifica si hay suficientes bases disponibles
            if cantidad_actual is None:
                mensaje_error = "No hay registros para Inox 300 en la base de datos."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            cantidad_actual = cantidad_actual[0]

            if cantidad_actual < cantidad:
                mensaje_error = f"No hay suficientes bases de Inox 300 disponibles. Cantidad actual: {cantidad_actual}."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            # Actualiza la cantidad en la base de datos soldador_stock
            nueva_cantidad_soldador = max(0, cantidad_actual - cantidad)
            cursor.execute("""
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'inox' AND modelo = '300'
            """, (nueva_cantidad_soldador,))

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute("""
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'inox_300'
            """, (cantidad,))

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Inox 300."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)
        elif tipo == "Pintada 330":
               # Obtén la cantidad actual de la base de datos para Inox 330
            cursor.execute("SELECT cantidad FROM soldador_stock WHERE tipo = 'pintada' AND modelo = '330'")
            cantidad_actual = cursor.fetchone()

            # Verifica si hay suficientes bases disponibles
            if cantidad_actual is None:
                mensaje_error = "No hay registros para pintada 330 en la base de datos."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            cantidad_actual = cantidad_actual[0]

            if cantidad_actual < cantidad:
                mensaje_error = f"No hay suficientes bases de pintada 330 disponibles. Cantidad actual: {cantidad_actual}."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            # Actualiza la cantidad en la base de datos soldador_stock
            nueva_cantidad_soldador = max(0, cantidad_actual - cantidad)
            cursor.execute("""
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'pintada' AND modelo = '330'
            """, (nueva_cantidad_soldador,))

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute("""
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'Pintada_330'
            """, (cantidad,))

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Pintada 330."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)

        elif tipo == "Pintada 300":
               # Obtén la cantidad actual de la base de datos para Inox 300
            cursor.execute("SELECT cantidad FROM soldador_stock WHERE tipo = 'pintada' AND modelo = '300'")
            cantidad_actual = cursor.fetchone()

            # Verifica si hay suficientes bases disponibles
            if cantidad_actual is None:
                mensaje_error = "No hay registros para pintada 300 en la base de datos."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            cantidad_actual = cantidad_actual[0]

            if cantidad_actual < cantidad:
                mensaje_error = f"No hay suficientes bases de pintada 300 disponibles. Cantidad actual: {cantidad_actual}."
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)
                return

            # Actualiza la cantidad en la base de datos soldador_stock
            nueva_cantidad_soldador = max(0, cantidad_actual - cantidad)
            cursor.execute("""
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'pintada' AND modelo = '300'
            """, (nueva_cantidad_soldador,))

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute("""
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'Pintada_300'
            """, (cantidad,))

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Pintada 300."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)

        # Guarda los cambios en la base de datos
        conn.commit()

    except Exception as e:
        # Manejo de errores
        mensaje_error = f"Error: {e}"
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)

    finally:
        # Cierra la conexión a la base de datos
        conn.close()

def armado_de_cabezales(opcion_seleccionada, entrada_cantidad, lista_acciones,subtitulo, tabla_chapa):
    tipo_material = opcion_seleccionada.get()

    # Mapea el valor del tipo de material a una cadena
    if tipo_material == 1:
        tipo_material = "acero"
    elif tipo_material == 2:
        tipo_material = "pintura"
    else:
        # Maneja el caso en que el valor no sea 1 ni 2
        mensaje_error = "Error: Tipo de material no válido."
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)
        return

    # Lista de piezas necesarias para el armado de cabezales
    piezas = ['chapa_U_cabezal', 'tapa_cabezal', 'bandeja_cabezal']

    # Verifica si la cantidad ingresada es un número
    cantidad_str = entrada_cantidad.get()
    if not cantidad_str.isdigit():
        mensaje_error = "Error: La cantidad debe ser un número entero."
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)
        return

    cantidad_eliminar = int(cantidad_str)
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    try:
        # Itera sobre las piezas y muestra un mensaje por cada una
        for pieza in piezas:
            print(f"Se necesitan {cantidad_eliminar} unidades de {pieza} de tipo {tipo_material}.")
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas = ? AND tipo_de_base = ?", (pieza, tipo_material,))
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                if cantidad_eliminar <= cantidad_actual:
                    nueva_cantidad = cantidad_actual - cantidad_eliminar
                    cursor.execute("UPDATE chapa SET cantidad=? WHERE piezas=? AND tipo_de_base = ?", (nueva_cantidad, pieza, tipo_material,))

                else:
                    lista_acciones.insert(0, f"No hay suficientes unidades de {pieza} en el stock")

            else:
                lista_acciones.insert(0, f"No se puede eliminar {pieza}, no existe en el stock")
                
        consulta_cabezales(tabla_chapa, tipo_material, "cabezal", subtitulo)
        cursor.execute("UPDATE piezas_del_fundicion SET cantidad = cantidad + ? WHERE modelo = 'cabezal' AND material = ? ", (cantidad_str, tipo_material))
        lista_acciones.insert(0, f"se agregego {cantidad_str} cantidad a la cabezales terminados")
        # Muestra un mensaje de éxito y agrega la acción a la lista
        mensaje_exito = f"Se han eliminado {cantidad_eliminar} unidades de {tipo_material}."
        print(mensaje_exito)
        lista_acciones.insert(0, mensaje_exito)

    except Exception as e:
        # Manejo de errores
        mensaje_error = f"Error: {e}"
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)

    finally:
        # Cierra la conexión a la base de datos
        conn.commit()
        conn.close()
        
def mostrar_bases_en_bruto(tree1, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad, modelo FROM piezas_del_fundicion WHERE modelo = '330' OR modelo = '300' ")
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)
    
    subtitulo_text = "Bases En Bruto"
    subtitulo.config(text=subtitulo_text)

def mostrar_cabezales_en_bruto(tree1, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM piezas_del_fundicion WHERE modelo = 'cabezal' ")
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)
        
    subtitulo_text = "Cabezales en Bruto"
    subtitulo.config(text=subtitulo_text)
    
#--------------------------------funciiones de piezas fundidor ---------------------------------------------------------

def mostrar_datos_materias(material, tabla, res):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM piezas_del_fundicion WHERE material = ? ", (material, ))
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for dato in datos:
        tabla.insert("", "end", values=dato)
    res.insert(0, f"Stock de {material}")

def enviar_piezas_a_pulido(pieza, cantidad, tabla, tree, lista_acciones,):
    pieza_seleccionada = pieza.get()
    cantidad_ingresada = cantidad.get()
    
    if not cantidad_ingresada.isdigit() or int(cantidad_ingresada) < 0:
        lista_acciones.insert(0, "Ingrese una Cantidad Válida")
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
        cursor.execute(f"SELECT cantidad FROM piezas_del_fundicion WHERE piezas = ?", (pieza_seleccionada, ))
        resultado_stock_bruto = cursor.fetchone()
        cantidad_stock_bruto = resultado_stock_bruto[0] if resultado_stock_bruto else 0

        nueva_cantidad_stock_bruto = cantidad_stock_bruto - int(cantidad_ingresada)
        cursor.execute(f"UPDATE piezas_del_fundicion SET cantidad = ? WHERE piezas = ?", (nueva_cantidad_stock_bruto, pieza_seleccionada))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        # Revertir la transacción en caso de error
        if conn:
            conn.rollback()
        lista_acciones.insert(0, f"Error en la base de datos: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    mostrar_datos(tree, tabla)
    
    lista_acciones.insert(0, f"{cantidad_ingresada} piezas de {pieza_seleccionada} han sido enviadas a pulido.")

def mover_piezas_a_stock_pulidas(pieza, cantidad, tabla_carmelo, tabla_stock_pulidas, arbol, lista_acciones):
    pieza_seleccionada = pieza.get()
    cantidad_ingresada = cantidad.get()
    
    if not cantidad_ingresada.isdigit() or int(cantidad_ingresada) < 0:
        lista_acciones.insert(0,"Ingrese una Cantidad Válida")
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
            lista_acciones.insert(0,"No hay suficientes piezas en la tabla de Carmelo.")
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
        lista_acciones.insert(0, f"Error en la base de datos: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    mostrar_datos(arbol, tabla_carmelo)
    
    lista_acciones.insert(0,f"{cantidad_ingresada} pieza de {pieza_seleccionada} han sido movidas a Stock Pulidas.")
    
def mostrar_datos_especifico(tabla, modelo, arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT piezas, cantidad FROM {tabla} WHERE modelo =  ?", (modelo, ))
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)
    
def agregar_a_lista_tarea(caja_texto, lista_tarea):
    texto = caja_texto.get("1.0", "end-1c")  # Obtiene el texto desde la posición 1.0 hasta el final, excluyendo el último carácter (que es un salto de línea)
    
    if texto.strip():  # Verifica que el texto no esté vacío después de eliminar espacios en blanco
        lista_tarea.insert(0, texto)  # Agrega el texto a la lista
        caja_texto.delete("1.0", tk.END)  # Borra el contenido de la caja de texto

def mostrar(tree1,tabla, mecanizado):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.execute(f"SELECT piezas, cantidad FROM {tabla} WHERE mecanizado = ?", ( mecanizado, ))
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)
        
def envios_de_bruto_a_pulido(lista_piezas, cantidad_a_niquelar, lista_acciones, arbol, mecanizado):
    pieza = lista_piezas
    cantidad = cantidad_a_niquelar.get()
    
    if cantidad.strip().isdigit():
        cantidad = int(cantidad)
        
        if cantidad < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM piezas_del_fundicion WHERE mecanizado = ? AND piezas = ?", (mecanizado, pieza,))
            cantidad_actual = cursor.fetchone()
            
            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual - cantidad
                cursor.execute("UPDATE piezas_del_fundicion SET cantidad=? WHERE mecanizado = ? AND piezas = ?", (nueva_cantidad, mecanizado, pieza,))
                conn.commit()
                
                # Nueva consulta para actualizar otra tabla
                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE mecanizado = ? AND piezas = ?", (cantidad, mecanizado, pieza,))
                
                conn.commit()
                conn.close()
                lista_acciones.insert(0, f"Carga {pieza}: {cantidad} unidades")
            else:
                lista_acciones.insert(0, "Cantidad ingresada inválida")
    else:
        lista_acciones.insert(0, "Ingrese un número válido")

