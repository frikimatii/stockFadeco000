import sqlite3
import tkinter as tk

def obtener_color_fondo(cantidad):
    if cantidad < 5:
        return "red"
    elif cantidad > 50:
        return "green"
    else:
        return ""
    

def mostrar_datos(treeview, table):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT piezas, cantidad FROM {table}")
    datos = cursor.fetchall()
    conn.close()

    # Limpiar la tabla antes de agregar nuevos datos
    for item in treeview.get_children():
        treeview.delete(item)

    # Agregar elementos a la lista con cantidades y aplicar colores
    for pieza, cantidad in datos:
        color_fondo = obtener_color_fondo(cantidad)
        treeview.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))


def sort_column(tree, col, reverse):
    items = [(float(tree.set(item, col)), item) for item in tree.get_children("")]
    items.sort(reverse=reverse)

    # Reorganiza los elementos en la tabla
    for index, (val, item) in enumerate(items):
        tree.move(item, "", index)

    # Cambia la dirección de la ordenación
    tree.heading(col, command=lambda: sort_column(tree, col, not reverse))


def sort_column_numeric(tree, col, reverse):
    items = [(float(tree.set(item, col)), item)
             for item in tree.get_children("")]
    items.sort(reverse=reverse)

    # Reorganiza los elementos en la tabla
    for index, (val, item) in enumerate(items):
        tree.move(item, "", index)

    # Cambia la dirección de la ordenación para el próximo clic
    tree.heading(col, command=lambda: sort_column_numeric(
        tree, col, not reverse))


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
            cursor.execute(
                f"SELECT cantidad FROM {table} WHERE piezas=?", (
                    actualizar_pieza,)
            )
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + entrada_actualizar
                cursor.execute(
                    f"UPDATE {table} SET cantidad=? WHERE piezas=?",
                    (nueva_cantidad, actualizar_pieza),
                )
                conn.commit()
                conn.close()
                mostrar_datos(
                    tree, table
                )  # Llama a la función para mostrar los datos actualizados
                res.insert(
                    0,
                    f"Carga exitosa: Usted cargó {entrada_actualizar} {actualizar_pieza}:",
                )
            else:
                res.insert(
                    0, f"La Pieza {actualizar_pieza} no se puede modificar")
    else:
        res.insert(0, "La cantidad ingresada no es un número válido")


#eliminar_piez(combox, cantida list tabla , funcion , arbol)
    
def eliminar_pieza(
    lista_predefinida_eliminar, entrada_cantidad_eliminar, res, table, funcion, tree
):
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
    cursor.execute(
        f"SELECT cantidad FROM {table} WHERE piezas=?", (pieza_eliminar,))
    cantidad_actual = cursor.fetchone()

    if cantidad_actual is not None:
        cantidad_actual = cantidad_actual[0]
        if cantidad_eliminar <= cantidad_actual:
            nueva_cantidad = cantidad_actual - cantidad_eliminar
            if nueva_cantidad >= 0:
                cursor.execute(
                    f"UPDATE {table} SET cantidad=? WHERE piezas=?",
                    (nueva_cantidad, pieza_eliminar),
                )
                res.insert(
                    0,
                    f" Descarga exitosa: se elimino {pieza_eliminar}, Cant: {cantidad_eliminar}",
                )

            else:
                res.insert(
                    0, f"No se puede eliminar la pieza {pieza_eliminar}")
        else:
            res.insert(0, f"No hay suficiente {pieza_eliminar} en el stock")
    else:
        res.insert(0, f"La pieza {pieza_eliminar} no se puede eliminar")

    conn.commit()
    conn.close()
    mostrar_datos(tree, table)

    
# ---------------funciones de stock de chapas _________________________________________________
    
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
        ("pieza", modelo, tipo_de_base, modelo),
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
    cursor.execute(
        "SELECT piezas, cantidad FROM chapa WHERE tipo_de_base = ? AND modelo = ? AND piezas IN ('chapa_U_cabezal', 'tapa_cabezal', 'bandeja_cabezal')",
        (tipo_de_base, modelo),
    )
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for dato in datos:
        tabla.insert("", "end", values=dato)

    subtitulo_text = f"Mostrando {tipo_de_base} {modelo}"
    subtitulo.config(text=subtitulo_text)


def stock_chapa(tabla, tipo_de_base, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad, modelo FROM chapa WHERE tipo_de_base = ?",
        (tipo_de_base,),
    )
    datos = cursor.fetchall()
    conn.close()

    for item in tabla.get_children():
        tabla.delete(item)
    for dato in datos:
        tabla.insert("", "end", values=dato)

    subtitulo_text = f"Mostrando {tipo_de_base}"
    subtitulo.config(text=subtitulo_text)


def agregar_pieza_chapas(
    tipo_var, lista_agregar_chapa, cantidad_agregar, arbol, tabla, lista_acciones
):
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
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE tipo_de_base = ? AND piezas = ?",
                (tipo, pieza),
            )
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_existente = resultado[0]
                cantidad_nueva = cantidad_existente + int(cantidad)
                cursor.execute(
                    "UPDATE chapa SET cantidad = ? WHERE tipo_de_base = ? AND piezas = ?",
                    (cantidad_nueva, tipo, pieza),
                )
                conn.commit()
            else:
                cursor.execute(
                    "INSERT INTO chapa (tipo_de_base, piezas, cantidad) VALUES (?, ?, ?)",
                    (tipo, pieza, cantidad),
                )
            conn.commit()
        except sqlite3.Error as e:
            lista_acciones.insert(0, "ERROR EN LA BASE DE DATOS:", e)
        finally:
            if conn:
                conn.close()
            mostrar_datos(arbol, tabla)
            lista_acciones.insert(
                0, f"Carga exitosa: Agregó {cantidad} de {pieza}, de {tipo}"
            )


def eliminar_pieza_chapas(
    tipo_var, lista_eliminar_chapa, cantidad_eliminar, arbol, tabla, lista_acciones
):
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
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE tipo_de_base = ? AND piezas = ?",
                (tipo, pieza),
            )
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_existente = resultado[0]
                if cantidad_existente >= int(cantidad):
                    cantidad_nueva = cantidad_existente - int(cantidad)
                    cursor.execute(
                        "UPDATE chapa SET cantidad = ? WHERE tipo_de_base = ? AND piezas = ?",
                        (cantidad_nueva, tipo, pieza),
                    )
                    conn.commit()
                else:
                    lista_acciones.insert(
                        0, "No hay suficiente cantidad para eliminar."
                    )
            else:
                lista_acciones.insert(
                    0, f"La pieza {pieza} no existe en la base de datos."
                )
        except sqlite3.Error as e:
            lista_acciones.insert(0, "ERROR EN LA BASE DE DATOS:", e)
        finally:
            if conn:
                conn.close()
            mostrar_datos(arbol, tabla)
            lista_acciones.insert(
                0, f"Eliminación exitosa: Eliminó {cantidad} de {pieza} de {tipo}"
            )


def agregar_portaeje(entrada_agregar_porta_eje, tree, tabla, lista_acciones):
    entrada_actualizar = entrada_agregar_porta_eje.get()

    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)

        if entrada_actualizar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE piezas = 'portaeje' ")
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + entrada_actualizar
                cursor.execute(
                    f"UPDATE chapa SET cantidad=? WHERE piezas = 'portaeje' ",
                    (nueva_cantidad,),
                )
                conn.commit()
                conn.close()
                mostrar_datos(tree, tabla)
                lista_acciones.insert(
                    0, f"Carga de ejes: {entrada_actualizar}")

            else:
                lista_acciones.insert(0, "Cantidada ingresada invalida")

    else:
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
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE piezas = 'portaeje' ")
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                if cantidad_actual >= entrada_eliminar:
                    nueva_cantidad = cantidad_actual - entrada_eliminar
                    cursor.execute(
                        f"UPDATE chapa SET cantidad=? WHERE piezas = 'portaeje'",
                        (nueva_cantidad,),
                    )
                    conn.commit()
                    conn.close()
                    mostrar_datos(tree, tabla)
                    lista_acciones.insert(
                        0, f"Eliminación de ejes: {entrada_eliminar}")
                else:
                    lista_acciones.insert(
                        0, "No hay suficiente cantidad para eliminar."
                    )
            else:
                lista_acciones.insert(0, "Cantidad ingresada inválida")
    else:
        lista_acciones.insert(0, "Ingrese un número válido")


def calcular_maquinas(maquina, lista_acciones):
    try:
        conn = sqlite3.connect(
            "basedatospiezas.db"
        )  # Reemplaza con el nombre de tu base de datos
        cursor = conn.cursor()

        # Consulta las cantidades de las piezas en la base de datos
        cantidades = {}
        for pieza, cantidad in maquina.items():
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE piezas = ?", (pieza,))
            resultado = cursor.fetchone()
            if resultado is not None:
                cantidad_disponible = resultado[0]
                cantidades[pieza] = cantidad_disponible

        # Calcula la cantidad máxima de máquinas que se pueden armar
        cantidad_maquinas = min(cantidades.values()) // min(maquina.values())
        return lista_acciones.insert(
            0, f"Se pueden armar {cantidad_maquinas} máquinas de acero 330."
        )

    except sqlite3.Error as e:
        print("ERROR EN LA BASE DE DATOS:", e)
        return 0  # En caso de error, devuelve 0 máquinas


def agregar_piezas_faltantes(
    lista_agregar_v_p, cantidad_agregar_v_p, arbol, lista_acciones, tabla
):
    pieza_seleccionada = lista_agregar_v_p.get()
    cantidad_ingregas = cantidad_agregar_v_p.get()

    if cantidad_ingregas.strip().isdigit():
        cantidad_ingregas = int(cantidad_ingregas)

        if cantidad_ingregas < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE piezas=?", (
                    pieza_seleccionada,)
            )
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + cantidad_ingregas
                cursor.execute(
                    f"UPDATE chapa SET cantidad=? WHERE piezas=?",
                    (nueva_cantidad, pieza_seleccionada),
                )
                conn.commit()
                conn.close()
                mostrar_datos(arbol, tabla)
                lista_acciones.insert(
                    0,
                    f"Carga exitosa: Usted cargó {cantidad_ingregas} {pieza_seleccionada}:",
                )
            else:
                lista_acciones.insert(
                    0, f"La Pieza {pieza_seleccionada} no se puede modificar"
                )
    else:
        lista_acciones.insert(
            0, "La cantidad ingresada no es un número válido")


def eliminar_piezas_faltante(
    pieza_seleccionada, cantidad_eliminar, arbol, lista_acciones, tabla
):
    if cantidad_eliminar.strip().isdigit():
        cantidad_eliminar = int(cantidad_eliminar)

        if cantidad_eliminar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE piezas=?", (
                    pieza_seleccionada,)
            )
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]

                if cantidad_actual >= cantidad_eliminar:
                    nueva_cantidad = cantidad_actual - cantidad_eliminar
                    cursor.execute(
                        f"UPDATE chapa SET cantidad=? WHERE piezas=?",
                        (
                            nueva_cantidad,
                            pieza_seleccionada,
                        ),
                    )
                    conn.commit()
                    conn.close()
                    mostrar_datos(arbol, tabla)
                    lista_acciones.insert(
                        0,
                        f"Eliminación exitosa: Usted eliminó {cantidad_eliminar} de {pieza_seleccionada}",
                    )
                else:
                    lista_acciones.insert(
                        0, "No hay suficiente cantidad para eliminar."
                    )
            else:
                lista_acciones.insert(
                    0, f"La Pieza {pieza_seleccionada} no se puede modificar"
                )
    else:
        lista_acciones.insert(
            0, "La cantidad ingresada no es un número válido")


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
                tabla.insert("", "end", values=(
                    "Soldador", cantidad, modelo, tipo))
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
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE tipo_de_base = ? AND modelo = ? AND piezas = ?",
                (tipo_base, modelo, pieza),
            )
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_disponible = resultado[0]
                cantidades[pieza] = cantidad_disponible

        if len(cantidades) == len(base_modelo):
            cantidad_bases = min(cantidades.values()
                                 ) // min(base_modelo.values())
            lista_acciones.insert(
                0, f"Se pueden armar {cantidad_bases} máquinas {tipo_base} {modelo}.")
        else:
            lista_acciones.insert(
                0, "No hay piezas suficientes para armar las máquinas."
            )

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


def eliminar_cantidad_de_piezas(
    combocaja_soldador, entrada_cantidad_soldador, tabla, subtitulo, lista_acciones
):
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
        lista_1 = ["chapa_principal_330", "lateral_L_330", "lateral_R_330"]
        lista_2 = ["planchuela_330", "varilla_330"]
        lista_3 = ["arandela", "portaeje"]

        for pieza in lista_1:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero' AND modelo = 330 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(
            cantidad_actual_por_pieza[pieza] >= cantidad
            for pieza in lista_1 + lista_2 + lista_3
        )

        if not eliminacion_posible:
            mensaje_error = (
                "Error: No es posible eliminar la cantidad deseada de piezas."
            )
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero' AND modelo = 330 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        cursor.execute(
            "UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '330' AND tipo = 'inox'",
            (cantidad,),
        )
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador acero 330")
        conn.commit()
        consulta_de_piezas(tabla, "acero", "330", subtitulo)

    elif tipo == "Inox 300":
        lista_1 = ["chapa_principal_300", "lateral_L_300", "lateral_R_300"]
        lista_2 = ["planchuela_300", "varilla_300"]
        lista_3 = ["arandela", "portaeje"]

        for pieza in lista_1:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero' AND modelo = 300 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(
            cantidad_actual_por_pieza[pieza] >= cantidad
            for pieza in lista_1 + lista_2 + lista_3
        )

        if not eliminacion_posible:
            mensaje_error = (
                "Error: No es posible eliminar la cantidad deseada de piezas."
            )
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero' AND modelo = 300 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        cursor.execute(
            "UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '300' AND tipo = 'inox'",
            (cantidad,),
        )
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador acero 300")
        conn.commit()
        consulta_de_piezas(tabla, "acero", "300", subtitulo)

    elif tipo == "Pintada 330":
        lista_1 = ["chapa_principal_330", "lateral_L_330", "lateral_R_330"]
        lista_2 = ["planchuela_330", "varilla_330"]
        lista_3 = ["arandela", "portaeje"]

        for pieza in lista_1:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'pintura' AND modelo = 330 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(
            cantidad_actual_por_pieza[pieza] >= cantidad
            for pieza in lista_1 + lista_2 + lista_3
        )

        if not eliminacion_posible:
            mensaje_error = (
                "Error: No es posible eliminar la cantidad deseada de piezas."
            )
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'pintura' AND modelo = 330 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 330 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        cursor.execute(
            "UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '330' AND tipo = 'pintada'",
            (cantidad,),
        )
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador pintura 330")
        conn.commit()
        consulta_de_piezas(tabla, "pintura", "330", subtitulo)

    elif tipo == "Pintada 300":
        lista_1 = ["chapa_principal_300", "lateral_L_300", "lateral_R_300"]
        lista_2 = ["planchuela_300", "varilla_300"]
        lista_3 = ["arandela", "portaeje"]

        for pieza in lista_1:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'pintura' AND modelo = 300 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_2:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        for pieza in lista_3:
            cursor.execute(
                """
            SELECT cantidad FROM chapa
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (pieza,),
            )
            cantidad_actual = cursor.fetchone()
            if cantidad_actual:
                cantidad_actual_por_pieza[pieza] = cantidad_actual[0]

        # Verifica si es posible eliminar la cantidad deseada de todas las piezas
        eliminacion_posible = all(
            cantidad_actual_por_pieza[pieza] >= cantidad
            for pieza in lista_1 + lista_2 + lista_3
        )

        if not eliminacion_posible:
            mensaje_error = (
                "Error: No es posible eliminar la cantidad deseada de piezas."
            )
            print(mensaje_error)
            lista_acciones.insert(0, mensaje_error)
            return

        # Si la eliminación es posible, procede con la actualización
        for pieza in lista_1:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'pintura' AND modelo = 300 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_2:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE tipo_de_base = 'acero_dulce' AND modelo = 300 AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        for pieza in lista_3:
            cantidad_restante = cantidad_actual_por_pieza[pieza] - cantidad
            cursor.execute(
                """
            UPDATE chapa
            SET cantidad = ?
            WHERE modelo = 'pieza' AND piezas = ?
            """,
                (cantidad_restante, pieza),
            )

        cursor.execute(
            "UPDATE soldador_stock SET cantidad = cantidad + ? WHERE modelo = '300' AND tipo = 'pintada'",
            (cantidad,),
        )
        lista_acciones.insert(0, f"Se envio {cantidad} bases al soldador de pintada 300")
        conn.commit()
        consulta_de_piezas(tabla, "pintura", "300", subtitulo)

    conn.close()


def bases_soldador_terminadas(
    combocaja_terminadas, entrada_cantidad_terminadas, lista_acciones, tabla_chapa
):
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
            cursor.execute(
                "SELECT cantidad FROM soldador_stock WHERE tipo = 'inox' AND modelo = '330'"
            )
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
            cursor.execute(
                """
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'inox' AND modelo = '330'
            """,
                (nueva_cantidad_soldador,),
            )

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute(
                """
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'inox_330'
            """,
                (cantidad,),
            )

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Inox 330."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)

        if tipo == "Inox 300":
            # Obtén la cantidad actual de la base de datos para Inox 300
            cursor.execute(
                "SELECT cantidad FROM soldador_stock WHERE tipo = 'inox' AND modelo = '300'"
            )
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
            cursor.execute(
                """
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'inox' AND modelo = '300'
            """,
                (nueva_cantidad_soldador,),
            )

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute(
                """
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'inox_300'
            """,
                (cantidad,),
            )

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Inox 300."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)
        elif tipo == "Pintada 330":
            # Obtén la cantidad actual de la base de datos para Inox 330
            cursor.execute(
                "SELECT cantidad FROM soldador_stock WHERE tipo = 'pintada' AND modelo = '330'"
            )
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
            cursor.execute(
                """
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'pintada' AND modelo = '330'
            """,
                (nueva_cantidad_soldador,),
            )

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute(
                """
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'base_pintada_330'
            """,
                (cantidad,),
            )

            # Muestra un mensaje de éxito y agrega la acción a la lista
            mensaje_exito = f"Se han terminado {cantidad} bases de Pintada 330."
            print(mensaje_exito)
            lista_acciones.insert(0, mensaje_exito)
            mostrar_stock_soldador(tabla_chapa)

        elif tipo == "Pintada 300":
            # Obtén la cantidad actual de la base de datos para Inox 300
            cursor.execute(
                "SELECT cantidad FROM soldador_stock WHERE tipo = 'pintada' AND modelo = '300'"
            )
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
            cursor.execute(
                """
                UPDATE soldador_stock
                SET cantidad = ?
                WHERE tipo = 'pintada' AND modelo = '300'
            """,
                (nueva_cantidad_soldador,),
            )

            # Actualiza la cantidad en la tabla piezas_del_fundicion
            cursor.execute(
                """
                UPDATE piezas_del_fundicion
                SET cantidad = cantidad + ?
                WHERE piezas = 'base_pintada_300'
            """,
                (cantidad,),
            )

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


def armado_de_cabezales(
    opcion_seleccionada, entrada_cantidad, lista_acciones, subtitulo, tabla_chapa
):
    def verificar_suficientes_piezas(cursor, pieza, tipo_material, cantidad_eliminar):
        cursor.execute(
            "SELECT cantidad FROM chapa WHERE piezas = ? AND tipo_de_base = ?",
            (
                pieza,
                tipo_material,
            ),
        )
        cantidad_actual = cursor.fetchone()

        if cantidad_actual is not None:
            cantidad_actual = cantidad_actual[0]
            return cantidad_eliminar <= cantidad_actual
        else:
            return False

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
    piezas = ["chapa_U_cabezal", "tapa_cabezal", "bandeja_cabezal"]

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
        # Verifica si hay suficientes piezas en el stock
        suficientes_piezas = all(
            verificar_suficientes_piezas(
                cursor, pieza, tipo_material, cantidad_eliminar
            )
            for pieza in piezas
        )

        if not suficientes_piezas:
            lista_acciones.insert(
                0, "No hay suficientes piezas en el stock para armar el cabezal."
            )
            return

        # Itera sobre las piezas y muestra un mensaje por cada una
        for pieza in piezas:
            cursor.execute(
                "SELECT cantidad FROM chapa WHERE piezas = ? AND tipo_de_base = ?",
                (
                    pieza,
                    tipo_material,
                ),
            )
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual - cantidad_eliminar
                cursor.execute(
                    "UPDATE chapa SET cantidad=? WHERE piezas=? AND tipo_de_base = ?",
                    (
                        nueva_cantidad,
                        pieza,
                        tipo_material,
                    ),
                )
                conn.commit()
            else:
                lista_acciones.insert(
                    0, f"No se puede eliminar {pieza}, no existe en el stock"
                )

        cursor.execute(
            "UPDATE piezas_del_fundicion SET cantidad = cantidad + ? WHERE modelo = 'cabezal' AND material = ? ",
            (cantidad_str, tipo_material),
        )
        conn.commit()

        consulta_cabezales(tabla_chapa, tipo_material, "cabezal", subtitulo)

        # Muestra un mensaje de éxito y agrega la acción a la lista
        mensaje_exito = (
            f"Se han eliminado {cantidad_eliminar} unidades de {tipo_material}."
        )
        lista_acciones.insert(0, mensaje_exito)

    except Exception as e:
        # Manejo de errores
        mensaje_error = f"Error: {e}"
        print(mensaje_error)
        lista_acciones.insert(0, mensaje_error)

    finally:
        # Cierra la conexión a la base de datos
        conn.close()


def mostrar_bases_en_bruto(tree1, subtitulo):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad, modelo FROM piezas_del_fundicion WHERE modelo = '330' OR modelo = '300' "
    )
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
    cursor.execute(
        "SELECT piezas, cantidad FROM piezas_del_fundicion WHERE modelo = 'cabezal' "
    )
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)

    subtitulo_text = "Cabezales en Bruto"
    subtitulo.config(text=subtitulo_text)


# --------------------------------funciiones de piezas fundidor --------------------------------------------------------


def mostrar_datos_materias(material, tabla, res, sub):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad FROM piezas_del_fundicion WHERE material = ? ",
        (material,),
    )
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for pieza, cantidad in datos:
        color_fondo = obtener_color_fondo(cantidad)
        tabla.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))
    res.insert(0, f"Stock de {material}")
    sub_text = f"Mostrando {material}"
    sub.config(text=sub_text)

def mostrar_plastico(material, tabla, res, sub):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE tipo = ? ",
        (material,),
    )
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for pieza, cantidad in datos:
        color_fondo = obtener_color_fondo(cantidad)
        tabla.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))
    res.insert(0, f"Stock de {material}")
    
    sub_text = f"Mostrando {material}"
    sub.config(text=sub_text)

def mostrar_shop(material, tabla, res, sub):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE mecanizado = ? ",
        (material,),
    )
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for pieza, cantidad in datos:
        color_fondo = obtener_color_fondo(cantidad)
        tabla.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))
    res.insert(0, f"Stock de {material}")
    sub_text = f"Mostrando {material}"
    sub.config(text=sub_text)

def mostrar_chapa_cortada(tabla, res, sub):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT cantidad, piezas FROM piezas_del_fundicion WHERE material= 'chapa' AND mecanizado = 'pulido'")
    datos = cursor.fetchall()
    conn.close()
    for item in tabla.get_children():
        tabla.delete(item)
    for cantidad , pieza in datos:
        color_fondo = obtener_color_fondo(cantidad)
        tabla.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))
    res.insert(0, f"Stock de Chapa Cortada")
    sub_text = f"Mostrando Chapa Cortada"
    sub.config(text=sub_text)
    
def mostrar_piezas_cortadas(tabla, res, sub):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    
    # Corrige la consulta SQL
    cursor.execute("""
        SELECT piezas, SUM(cantidad) AS cantidad_cortada
        FROM piezas_del_fundicion
        WHERE piezas IN ('guia_U', 'eje_rectificado', 'varilla_brazo_330', 'varilla_brazo_300', 'varilla_brazo_250', 'tubo_manija', 'tubo_manija_250', 'cuadrado_regulador', 'palanca_afilador', 'eje_corto', 'eje_largo')
        GROUP BY piezas
    """)
    
    datos = cursor.fetchall()
    conn.close()
    
    # Limpia la tabla antes de agregar nuevos datos
    for item in tabla.get_children():
        tabla.delete(item)
    
    # Agrega los datos a la tabla
    for pieza, cantidad in datos:
        color_fondo = obtener_color_fondo(cantidad)
        tabla.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))
    
    res.insert(0, f"Stock de Piezas Cortada")
    
    sub_text = f"Mostrando Piezas Cortadas"
    sub.config(text=sub_text)
    
def mostrar_tornillo_guia_rueditas(tabla, res, sub):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    
    # Corrige la consulta SQL
    cursor.execute("""
        SELECT piezas, SUM(cantidad) AS cantidad_cortada
        FROM piezas_del_fundicion
        WHERE piezas IN ('tornillo_guia', 'rueditas')
        GROUP BY piezas
    """)
    
    datos = cursor.fetchall()
    conn.close()
    
    # Limpia la tabla antes de agregar nuevos datos
    for item in tabla.get_children():
        tabla.delete(item)
    
    # Agrega los datos a la tabla
    for pieza, cantidad in datos:
        color_fondo = obtener_color_fondo(cantidad)
        tabla.insert("", tk.END, values=(pieza, cantidad), tags=(color_fondo,))
    
    res.insert(0, f"Stock de Tornillo Guia / Tornillo")
    
    sub_text = f"Mostrando Varios"
    sub.config(text=sub_text)
    

def enviar_piezas_a_pulido(
    pieza,
    cantidad,
    tabla,
    tree,
    lista_acciones,
):
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

        cursor.execute(
            f"SELECT cantidad FROM {tabla} WHERE piezas = ?", (
                pieza_seleccionada,)
        )
        resultado = cursor.fetchone()
        cantidad_existente = resultado[0] if resultado else 0

        nueva_cantidad = cantidad_existente + int(cantidad_ingresada)

        # Iniciar una transacción
        conn.execute("BEGIN")

        # Actualizar la tabla donde envías las piezas a pulido
        cursor.execute(
            f"UPDATE {tabla} SET cantidad = ? WHERE piezas = ?",
            (nueva_cantidad, pieza_seleccionada),
        )

        # Reducir la cantidad en la tabla de stock en bruto
        cursor.execute(
            f"SELECT cantidad FROM piezas_del_fundicion WHERE piezas = ?",
            (pieza_seleccionada,),
        )
        resultado_stock_bruto = cursor.fetchone()
        cantidad_stock_bruto = resultado_stock_bruto[0] if resultado_stock_bruto else 0

        nueva_cantidad_stock_bruto = cantidad_stock_bruto - \
            int(cantidad_ingresada)
        cursor.execute(
            f"UPDATE piezas_del_fundicion SET cantidad = cantidad = ? WHERE piezas = ?",
            (nueva_cantidad_stock_bruto, pieza_seleccionada),
        )

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

    lista_acciones.insert(
        0,
        f"{cantidad_ingresada} piezas de {pieza_seleccionada} han sido enviadas a pulido.",
    )


def mover_piezas_a_stock_pulidas(
    pieza, cantidad, tabla_carmelo, tabla_stock_pulidas, arbol, lista_acciones
):
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

        cursor.execute(
            f"SELECT cantidad FROM {tabla_carmelo} WHERE piezas = ?",
            (pieza_seleccionada,),
        )
        resultado = cursor.fetchone()
        cantidad_existente = resultado[0] if resultado else 0

        if int(cantidad_ingresada) > cantidad_existente:
            lista_acciones.insert(
                0, "No hay suficientes piezas en la tabla de Carmelo."
            )
            return

        # Iniciar una transacción
        conn.execute("BEGIN")

        # Actualizar la tabla de Carmelo reduciendo la cantidad
        nueva_cantidad_carmelo = cantidad_existente - int(cantidad_ingresada)
        cursor.execute(
            f"UPDATE {tabla_carmelo} SET cantidad = ? WHERE piezas = ?",
            (nueva_cantidad_carmelo, pieza_seleccionada),
        )

        # Actualizar la tabla de Stock Pulidas aumentando la cantidad
        cursor.execute(
            f"SELECT cantidad FROM {tabla_stock_pulidas} WHERE piezas = ?",
            (pieza_seleccionada,),
        )
        resultado_stock_pulidas = cursor.fetchone()
        cantidad_stock_pulidas = (
            resultado_stock_pulidas[0] if resultado_stock_pulidas else 0
        )

        nueva_cantidad_stock_pulidas = cantidad_stock_pulidas + \
            int(cantidad_ingresada)
        cursor.execute(
            f"UPDATE {tabla_stock_pulidas} SET cantidad = ? WHERE piezas = ?",
            (nueva_cantidad_stock_pulidas, pieza_seleccionada),
        )

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

    lista_acciones.insert(
        0,
        f"{cantidad_ingresada} pieza de {pieza_seleccionada} han sido movidas a Stock Pulidas.",
    )


def mostrar_datos_especifico(tabla, modelo, arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas, cantidad FROM {tabla} WHERE modelo =  ?", (modelo,))
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def agregar_a_lista_tarea(caja_texto, lista_tarea):
    texto = caja_texto.get(
        "1.0", "end-1c"
    )  # Obtiene el texto desde la posición 1.0 hasta el final, excluyendo el último carácter (que es un salto de línea)

    if (
        texto.strip()
    ):  # Verifica que el texto no esté vacío después de eliminar espacios en blanco
        lista_tarea.insert(0, texto)  # Agrega el texto a la lista
        # Borra el contenido de la caja de texto
        caja_texto.delete("1.0", tk.END)


def mostrar(tree1, tabla, mecanizado):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.execute(
        f"SELECT piezas, cantidad FROM {tabla} WHERE mecanizado = ?", (
            mecanizado,)
    )
    datos = cursor.fetchall()
    conn.close()
    for item in tree1.get_children():
        tree1.delete(item)
    for dato in datos:
        tree1.insert("", "end", values=dato)


def envios_de_bruto_a_pulido(
    lista_piezas, cantidad_a_niquelar, lista_acciones, arbol, mecanizado
):
    pieza = lista_piezas
    cantidad = cantidad_a_niquelar.get()

    if cantidad.strip().isdigit():
        cantidad = int(cantidad)

        if cantidad < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT cantidad FROM piezas_del_fundicion WHERE mecanizado = ? AND piezas = ?",
                (
                    mecanizado,
                    pieza,
                ),
            )
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual - cantidad
                cursor.execute(
                    "UPDATE piezas_del_fundicion SET cantidad=? WHERE mecanizado = ? AND piezas = ?",
                    (
                        nueva_cantidad,
                        mecanizado,
                        pieza,
                    ),
                )
                conn.commit()

                # Nueva consulta para actualizar otra tabla
                cursor.execute(
                    "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE mecanizado = ? AND piezas = ?",
                    (
                        cantidad,
                        mecanizado,
                        pieza,
                    ),
                )

                conn.commit()
                conn.close()
                lista_acciones.insert(0, f"Carga {pieza}: {cantidad} unidades")
            else:
                lista_acciones.insert(0, "Cantidad ingresada inválida")
    else:
        lista_acciones.insert(0, "Ingrese un número válido")


# -------------------------------------Funciones Mecanizado------------------------------------------------------------


def mostrar_datos_torno(arbol, tabla):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas, cantidad FROM {tabla} WHERE mecanizado = 'torno' AND piezas NOT IN ('caja_torneado_330', 'caja_torneado_300', 'caja_torneado_250')"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def mostrar_datos_(arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas, cantidad FROM piezas_del_fundicion WHERE piezas IN ('caja_torneado_330', 'caja_torneado_300', 'caja_torneado_250')"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def actualizar_pieza_torno(lista_predefinida, entrada_cantidad, res, table, tree):
    actualizar_pieza = lista_predefinida.get()
    entrada_actualizar = entrada_cantidad.get()

    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)

        if entrada_actualizar < 0:
            res.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT cantidad FROM piezas_del_fundicion WHERE piezas=?",
                (actualizar_pieza,),
            )
            cantidad_actual = cursor.fetchone()

            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]

                # Verifica si hay suficientes piezas disponibles
                if cantidad_actual >= entrada_actualizar:
                    nueva_cantidad = max(
                        0, cantidad_actual - entrada_actualizar)
                    cursor.execute(
                        f"UPDATE piezas_del_fundicion SET cantidad=? WHERE piezas=?",
                        (nueva_cantidad, actualizar_pieza),
                    )
                    conn.commit()

                    # Extrae el valor del Entry antes de pasarlo a la consulta SQL
                    cantidad_a_actualizar = entrada_cantidad.get()
                    cursor.execute(
                        "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = ?",
                        (cantidad_a_actualizar, actualizar_pieza),
                    )
                    conn.commit()
                    conn.close()
                    mostrar_datos(
                        tree, table
                    )  # Llama a la función para mostrar los datos actualizados
                    res.insert(
                        0,
                        f"Carga exitosa: Usted cargó {entrada_actualizar} {actualizar_pieza}:",
                    )
                else:
                    conn.close()
                    res.insert(
                        0,
                        f"No hay suficientes piezas de {actualizar_pieza} disponibles.",
                    )
            else:
                conn.close()
                res.insert(
                    0, f"La Pieza {actualizar_pieza} no se puede modificar")
    else:
        res.insert(0, "La cantidad ingresada no es un número válido")


def actualizar_caja_torno(lista_predefinida, entrada_cantidad, res, tree):
    actualizar_pieza = lista_predefinida.get()
    entrada_actualizar = entrada_cantidad.get()

    try:
        if entrada_actualizar.strip().isdigit():
            entrada_actualizar = int(entrada_actualizar)

            if entrada_actualizar < 0:
                res.insert(0, "La Cantidad NO puede ser Negativa")
            else:
                conn = sqlite3.connect("basedatospiezas.db")
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT cantidad FROM piezas_del_fundicion WHERE piezas=?",
                    (actualizar_pieza,),
                )
                cantidad_actual = cursor.fetchone()

                if cantidad_actual is not None:
                    cantidad_actual = cantidad_actual[0]

                    if cantidad_actual >= entrada_actualizar:
                        nueva_cantidad = max(
                            0, cantidad_actual - entrada_actualizar)

                        cursor.execute(
                            "UPDATE piezas_del_fundicion SET cantidad=? WHERE piezas=?",
                            (nueva_cantidad, actualizar_pieza),
                        )
                        conn.commit()
                        cantidad_a_actualizar = entrada_cantidad.get()
                        cursor.execute(
                            "UPDATE torno SET cantidad = cantidad + ? WHERE piezas = ?",
                            (cantidad_a_actualizar, actualizar_pieza),
                        )
                        conn.commit()
                        cursor.execute(
                            "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = ?",
                            (cantidad_a_actualizar, actualizar_pieza),
                        )
                        conn.commit()
                        conn.close()
                        mostrar_datos(tree, "torno")
                        res.insert(
                            0,
                            f"Carga exitosa: Usted cargó {entrada_actualizar} {actualizar_pieza}:",
                        )
                    else:
                        res.insert(
                            0,
                            f"No hay suficientes piezas de {actualizar_pieza} disponibles.",
                        )
                else:
                    res.insert(
                        0, f"La Pieza {actualizar_pieza} no se puede modificar")
        else:
            res.insert(0, "La cantidad ingresada no es un número válido")
    except Exception as e:
        res.insert(0, f"Error: {e}")


def mostrar_piezas_torno_terminado(arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE piezas IN ( 'manchon', 'manchon_250', 'eje_250', 'eje', 'rueditas', 'tornillo_guia', 'carros', 'movientos', 'carros_250');"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def pulido_cabezal(entrada_agregar_porta_eje, lista_acciones):
    entrada_actualizar = entrada_agregar_porta_eje.get()

    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)

        if entrada_actualizar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()

            try:
                cursor.execute(
                    "SELECT cantidad FROM piezas_del_fundicion WHERE piezas = 'cabezal_inox'"
                )
                cantidad_actual = cursor.fetchone()

                if cantidad_actual is not None:
                    cantidad_actual = cantidad_actual[0]
                    nueva_cantidad = cantidad_actual - entrada_actualizar

                    cursor.execute(
                        "UPDATE piezas_del_fundicion SET cantidad= cantidad  - ? WHERE piezas = 'cabezal_inox'",
                        (entrada_actualizar,),
                    )
                    conn.commit()
                    cursor.execute(
                        "UPDATE piezas_finales_defenitivas SET cantidad= cantidad + ? WHERE piezas = 'cabezal_inox'",
                        (entrada_actualizar,),
                    )

                    conn.commit()
                    lista_acciones.insert(
                        0, f"Cabezales Pulidos: {entrada_actualizar}")
                else:
                    lista_acciones.insert(0, "Cantidad ingresada inválida")

            except Exception as e:
                # Manejo de errores
                mensaje_error = f"Error: {e}"
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)

            finally:
                conn.close()

    else:
        lista_acciones.insert(0, "Ingrese un número válido")


def de_enbruto_a_torneado(piezas, cantidad, lista_acciones):
    pieza = piezas.get()
    cantidad = cantidad.get()

    if cantidad.strip().isdigit():
        cantidad = int(cantidad)

        if cantidad < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()

            try:
                if pieza == "caja_torneado_330":
                    cursor.execute(
                        "SELECT cantidad FROM piezas_del_fundicion WHERE piezas = 'caja_330'"
                    )
                    cantidad_actual = cursor.fetchone()

                    if cantidad_actual is not None:
                        cantidad_actual = cantidad_actual[0]

                        # Verifica si hay suficientes piezas disponibles
                        if cantidad_actual >= cantidad:
                            nueva_cantidad_enbruto = max(
                                0, cantidad_actual - cantidad)

                            # Actualiza la cantidad de cajas en bruto
                            cursor.execute(
                                f"UPDATE piezas_del_fundicion SET cantidad = ? WHERE piezas = 'caja_330'",
                                (nueva_cantidad_enbruto,),
                            )

                            # Actualiza la cantidad de cajas tornadas
                            cursor.execute(
                                f"UPDATE piezas_del_fundicion SET cantidad = cantidad + ? WHERE piezas = 'caja_torneado_330'",
                                (cantidad,),
                            )
                        else:
                            lista_acciones.insert(
                                0,
                                f"No hay suficientes piezas de {pieza} en bruto disponibles.",
                            )
                    else:
                        lista_acciones.insert(
                            0, f"No se encontró la pieza {pieza}.")

                    lista_acciones.insert(
                        0, f"Se han Torneado {cantidad} caja_330.")
                    lista_acciones.insert(0, f"se agrego {cantidad} {pieza}")

                elif pieza == "caja_torneado_300":
                    cursor.execute(
                        "SELECT cantidad FROM piezas_del_fundicion WHERE piezas = 'caja_300'"
                    )
                    cantidad_actual = cursor.fetchone()

                    if cantidad_actual is not None:
                        cantidad_actual = cantidad_actual[0]

                        # Verifica si hay suficientes piezas disponibles
                        if cantidad_actual >= cantidad:
                            nueva_cantidad_enbruto = max(
                                0, cantidad_actual - cantidad)

                            # Actualiza la cantidad de cajas en bruto
                            cursor.execute(
                                f"UPDATE piezas_del_fundicion SET cantidad = ? WHERE piezas = 'caja_300'",
                                (nueva_cantidad_enbruto,),
                            )

                            # Actualiza la cantidad de cajas tornadas
                            cursor.execute(
                                f"UPDATE piezas_del_fundicion SET cantidad = cantidad + ? WHERE piezas = 'caja_torneado_300'",
                                (cantidad,),
                            )
                        else:
                            lista_acciones.insert(
                                0,
                                f"No hay suficientes piezas de {pieza} en bruto disponibles.",
                            )
                    else:
                        lista_acciones.insert(
                            0, f"No se encontró la pieza {pieza}.")

                    lista_acciones.insert(
                        0, f"Se han Torneado {cantidad} caja_300.")
                    lista_acciones.insert(0, f"se agrego {cantidad} {pieza}")

                elif pieza == "caja_torneado_250":
                    cursor.execute(
                        "SELECT cantidad FROM piezas_del_fundicion WHERE piezas = 'caja_250'"
                    )
                    cantidad_actual = cursor.fetchone()

                    if cantidad_actual is not None:
                        cantidad_actual = cantidad_actual[0]

                        # Verifica si hay suficientes piezas disponibles
                        if cantidad_actual >= cantidad:
                            nueva_cantidad_enbruto = max(
                                0, cantidad_actual - cantidad)

                            # Actualiza la cantidad de cajas en bruto
                            cursor.execute(
                                f"UPDATE piezas_del_fundicion SET cantidad = ? WHERE piezas = 'caja_250'",
                                (nueva_cantidad_enbruto,),
                            )

                            # Actualiza la cantidad de cajas tornadas
                            cursor.execute(
                                f"UPDATE piezas_del_fundicion SET cantidad = cantidad + ? WHERE piezas = 'caja_torneado_250'",
                                (cantidad,),
                            )
                        else:
                            lista_acciones.insert(
                                0,
                                f"No hay suficientes piezas de {pieza} en bruto disponibles.",
                            )
                    else:
                        lista_acciones.insert(
                            0, f"No se encontró la pieza {pieza}.")

                    lista_acciones.insert(
                        0, f"Se han Torneado {cantidad} caja_250.")
                    lista_acciones.insert(0, f"se agrego {cantidad} {pieza}")

                conn.commit()

            except Exception as e:
                # Manejo de errores
                mensaje_error = f"Error: {e}"
                lista_acciones.insert(0, mensaje_error)

            finally:
                conn.close()


def mostrar_cajas_bruto(arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas, cantidad FROM piezas_del_fundicion WHERE piezas IN ('caja_330', 'caja_300', 'caja_250')"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def varilla_para_soldar(entrada_cantidad, varilla_tipo , lista_acciones):
    if varilla_tipo == "varilla_330":
        tipo = "330"
    elif varilla_tipo == "varilla_300":
        tipo = "300"
    elif varilla_tipo == "varilla_250":
        tipo = "250"
        
    entrada_actualizar = entrada_cantidad.get()

    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)

        if entrada_actualizar < 0:
            lista_acciones.insert(0, "La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()

            try:
                cursor.execute(
                    f"SELECT cantidad FROM chapa WHERE piezas = 'varilla_{tipo}'"
                )
                cantidad_actual = cursor.fetchone()

                if cantidad_actual is not None:
                    cantidad_actual = cantidad_actual[0]
                    nueva_cantidad = cantidad_actual - entrada_actualizar

                    cursor.execute(
                        f"UPDATE chapa SET cantidad= cantidad  - ? WHERE piezas = 'varilla_{tipo}'",
                        (entrada_actualizar,),
                    )
                    conn.commit()
                    cursor.execute(
                        f"UPDATE piezas_finales_defenitivas SET cantidad= cantidad + ? WHERE piezas = 'varilla_carro_{tipo}'",
                        (entrada_actualizar,),
                    )

                    conn.commit()
                    lista_acciones.insert(
                        0, f"Varillas Soldadas: {entrada_actualizar}")
                else:
                    lista_acciones.insert(0, "Cantidad ingresada inválida")

            except Exception as e:
                # Manejo de errores
                mensaje_error = f"Error: {e}"
                print(mensaje_error)
                lista_acciones.insert(0, mensaje_error)

            finally:
                conn.close()

    else:
        lista_acciones.insert(0, "Ingrese un número válido")
    pass 



# --------------------------------------Armado de motores-----------------------------------------------------------

"""

def mostrar_motores(arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE piezas = 'motores_220w'"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def mostrar_pieza_motores(arbol):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_de_caja'"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)


def armado_de_motor(modelo, cantidad, lista_acciones):
    tipo = modelo.get()
    cantidad_ = int(cantidad.get())  # Asegurarse de convertir la cantidad a un entero

    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    if tipo == 1:
        motores_finales = [
            "caja_torneado_330",
            "eje",
            "manchon",
            "ruleman_1",
            "ruleman_2",
            "corona_330",
            "seguer",
            "sinfin",
            "motor",
        ]
    elif tipo == 2:
        motores_finales = [
            "caja_torneado_300",
            "eje",
            "manchon",
            "ruleman_1",
            "ruleman_2",
            "corona_300",
            "seguer",
            "sinfin",
            "motor",
        ]
    else:
        lista_acciones.insert(0, "modelo NO valido")

    # Verificar si hay suficientes piezas en la base de datos
    for pieza in motores_finales:
        cursor.execute(
            "SELECT cantidad FROM piezas_del_fundicion WHERE piezas = ?", (pieza,)
        )
        cantidad_disponible = cursor.fetchone()[0]

        if cantidad_disponible < cantidad_:
            lista_acciones.insert(0, f"NO hay suficiente {pieza} para ensamblar")
            conn.close()

    # Si hay suficientes piezas, calcular la cantidad máxima de armado de motor
    for pieza in motores_finales:
        cursor.execute(
            "UPDATE piezas_del_fundicion SET cantidad = cantidad - ? WHERE piezas = ?",
            (cantidad_, pieza),
        )

    conn.commit()
    conn.close()

    lista_acciones.insert(
        f"Se ensamblaron {cantidad_} unidades del motor {tipo} correctamente."
    )


def cantida_posible_motores(piezas, lista_acciones, base_modelo=None):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    cantidades = {}

    try:
        for pieza in piezas:
            cursor.execute(
                "SELECT cantidad FROM piezas_finales_defenitivas WHERE piezas = ?",
                (pieza,),
            )
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_disponible = resultado[0]
                cantidades[pieza] = cantidad_disponible

        if base_modelo is not None and len(cantidades) == len(base_modelo):
            cantidad_bases = min(cantidades.values()) // min(base_modelo.values())
            lista_acciones.insert(0, f"Se pueden armar {cantidad_bases} máquinas.")
        else:
            lista_acciones.insert(
                0, "No hay piezas suficientes para armar las máquinas."
            )
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def armado_de_motor(modelo, cantidad, lista_acciones):
    tipo = modelo.get()
    cantidad_ = int(cantidad.get())  # Asegurarse de convertir la cantidad a un entero

    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    if tipo == 1:
        motores_finales = [
            "caja_torneado_330",
            "eje",
            "manchon",
            "ruleman_1",
            "ruleman_2",
            "corona_330",
            "seguer",
            "sinfin",
            "motor",
        ]
    elif tipo == 2:
        motores_finales = [
            "caja_torneado_300",
            "eje",
            "manchon",
            "ruleman_1",
            "ruleman_2",
            "corona_300",
            "seguer",
            "sinfin",
            "motor",
        ]
    else:
        lista_acciones.insert(0, "modelo NO valido")

    # Verificar si hay suficientes piezas en la base de datos
    for pieza in motores_finales:
        cursor.execute(
            "SELECT cantidad FROM piezas_del_fundicion WHERE piezas = ?", (pieza,)
        )
        cantidad_disponible = cursor.fetchone()[0]

        if cantidad_disponible < cantidad_:
            lista_acciones.insert(0, f"NO hay suficiente {pieza} para ensamblar")
            conn.close()

    # Si hay suficientes piezas, calcular la cantidad máxima de armado de motor
    for pieza in motores_finales:
        cursor.execute(
            "UPDATE piezas_del_fundicion SET cantidad = cantidad - ? WHERE piezas = ?",
            (cantidad_, pieza),
        )

    conn.commit()
    conn.close()

    lista_acciones.insert(
        f"Se ensamblaron {cantidad_} unidades del motor {tipo} correctamente."
    )


def cajas_terminadas(entry_cantidad, modelo, lista_acciones):
    try:
        cantidad = int(entry_cantidad.get())
    except ValueError:
        lista_acciones.insert(0, "Error: Ingrese un número válido.")
        return

    modelo_opcion = modelo.get()

    modelos_disponibles = {
        1: { 
            "caja_torneado_330": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_1": 1,
            "ruleman_2": 2,
            "corona_330": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores_220w": 1,
        },
        2: {
            "caja_torneado_300": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_1": 1,
            "ruleman_2": 2,
            "corona_300": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores_220w": 1,
        },
        3: {
            "caja_torneado_250": 1,
            "eje_250": 1,
            "manchon_250": 1,
            "ruleman_1": 1,
            "ruleman_2": 2,
            "corona_250": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores250_220w": 1,
        },
    }

    if modelo_opcion not in modelos_disponibles:
        lista_acciones.insert(0, "Error: Opción de modelo no válida.")
        return

    modelo_dict = modelos_disponibles[modelo_opcion]
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    try:
        piezas_faltantes = []

        for pieza, cantidad_modelo in modelo_dict.items():
            cursor.execute(
                "SELECT cantidad FROM piezas_finales_defenitivas WHERE piezas = ? AND modelo = ?",
                (pieza, modelo_opcion),
            )
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_actual = resultado[0]
                nueva_cantidad = cantidad_actual - (cantidad_modelo * cantidad)

                if nueva_cantidad < 0:
                    piezas_faltantes.append((pieza, abs(nueva_cantidad)))
                else:
                    # Actualizar la cantidad en la base de datos
                    cursor.execute(
                        "UPDATE piezas_finales_defenitivas SET cantidad = ? WHERE piezas = ? AND modelo = ?",
                        (nueva_cantidad, pieza, modelo_opcion),
                    )

        if piezas_faltantes:
            mensaje = f"Operación Cancelada. Piezas faltantes: {', '.join([f'{pieza} ({cantidad})' for pieza, cantidad in piezas_faltantes])}"
            lista_acciones.insert(0, mensaje)
        else:
            # Realizar las actualizaciones necesarias según el modelo
            if modelo_opcion == 1:
                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'cajamotor_final_330' AND modelo = ?", (cantidad, modelo_opcion))
                print("330")
            elif modelo_opcion == 2:
                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'cajamotor_final_300' AND modelo = ?", (cantidad, modelo_opcion))
                print("300")
            elif modelo_opcion == 3:
                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'cajamotor_final_250' AND modelo = ?", (cantidad, modelo_opcion))
                print("250")
            else:
                lista_acciones.insert(0, "Error: Opción de modelo no válida.")

            lista_acciones.insert(
                0,
                "Operación Completada con Éxito. Todas las piezas se han actualizado.",
            )

        conn.commit()

    except sqlite3.Error as e:
        lista_acciones.insert(0, f"Error al actualizar la base de datos: {e}")

    finally:
        conn.close()
 
"""


def mostrar_pieza(arbol, piezas, res):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE piezas = '{piezas}'"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

    text = "Mostrar Cantidad De Motore"
    res.config(text=text)

def mostrar_piezas_armados(arbol, sector, res):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = '{sector}'"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

    text = "Mostrar Cantidad De Piezas Para Motores"
    res.config(text=text)

def mostrar_piezas_por_modelo(arbol, pieza):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_de_caja' AND  pieza = ? ", (
            pieza)
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

def mostrar_piezas_modelo(arbol, modelos, res, tipo):
    # Conectar a la base de datos
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    # Limpiar los datos existentes en el treeview
    for item in arbol.get_children():
        arbol.delete(item)

    # Iterar sobre los modelos y ejecutar la consulta para cada uno
    for tipo_motor in modelos:
        cursor.execute(
            "SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE piezas = ?",
            (tipo_motor,)
        )
        datos = cursor.fetchall()

        # Insertar los nuevos datos en el treeview
        for dato in datos:
            arbol.insert("", "end", values=dato)

    # Cerrar la conexión a la base de datos
    conn.close()

    text = f"Cantidad de piezas {tipo}"
    res.config(text=text)

def ensamblar_motor_terminado(modelo_seleccionado, cantidad_motores, res):

    motores_terminado = {
        1: {
            "caja_torneado_330": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_1": 1,
            "ruleman_2": 2,
            "corona_330": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores_220w": 1,
        },
        2: {
            "caja_torneado_300": 1,
            "eje": 1,
            "manchon": 1,
            "ruleman_1": 1,
            "ruleman_2": 2,
            "corona_300": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores_220w": 1,
        },
        3: {
            "caja_torneado_250": 1,
            "eje_250": 1,
            "manchon_250": 1,
            "ruleman_1": 1,
            "ruleman_2": 2,
            "corona_250": 1,
            "seguer": 1,
            "sinfin": 1,
            "motores250_220w": 1,
        }
    }

    # Conectar a la base de datos usando 'with' statement
    with sqlite3.connect("basedatospiezas.db") as conn:
        cursor = conn.cursor()

        try:
            # Obtener las piezas necesarias para el modelo seleccionado
            piezas_necesarias = motores_terminado.get(modelo_seleccionado, {})

            if not piezas_necesarias:
                raise ValueError(
                    res.insert(0, f"No se encontró información para el modelo {modelo_seleccionado}."))

            # Verificar si hay suficientes piezas en el inventario
            cantidad = int(cantidad_motores.get())

            for pieza, cantidad_necesaria in piezas_necesarias.items():
                cursor.execute(
                    "SELECT cantidad FROM piezas_finales_defenitivas WHERE piezas = ?",
                    (pieza,)
                )
                cantidad_actual = cursor.fetchone()

                if cantidad_actual is None or cantidad_actual[0] < cantidad_necesaria * cantidad:
                    raise ValueError(
                         res.insert(0, f"No hay suficientes {pieza} en el inventario."))

            # Restar la cantidad necesaria de cada pieza en el inventario
            for pieza, cantidad_necesaria in piezas_necesarias.items():
                cursor.execute(
                    "UPDATE piezas_finales_defenitivas SET cantidad = cantidad - ? WHERE piezas = ?",
                    (cantidad_necesaria * cantidad, pieza)
                )
                #cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE mecanizado = 'armado_caja' AND modelo = ?", (cantidad_motores, modelo))
            

            # Commit para aplicar los cambios
            conn.commit()
            res.insert(0, f"Se ensamblaron {cantidad} motores {modelo_seleccionado}.")

            if modelo_seleccionado in [1, 2, 3]:
                if modelo_seleccionado == 1:
                    nombre_pieza = "cajamotor_final_330"
                elif modelo_seleccionado == 2:
                    nombre_pieza = "cajamotor_final_300"
                elif modelo_seleccionado == 3:
                    nombre_pieza = "cajamotor_final_250"

                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = ?", (cantidad, nombre_pieza))

                if cantidad == 1:
                    res.insert(0, f"Se agregó {cantidad} motor terminado")
                else:
                    res.insert(0, f"Se agregaron {cantidad} motores terminados")
            else:
                res.insert(0, "Modelo no reconocido")

            conn.commit()
            
        except sqlite3.Error as e:
            # Imprimir el error y hacer rollback en caso de error
            res.insert(0, f"Error en la base de datos: {e}")
            conn.rollback()

        except ValueError as ve:
            print(ve)


def motores_terminados(arbol, res):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE mecanizado = 'armado_caja'"
    )
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

    text = "Mostrar: Motores terminados "
    res.config(text=text)
    
    
    
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# -----------------------------------Pre Armado---------------------------


def stock_prearmado(arbol, res):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = 'pre_armado'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
        
    text = "Mostrar: Piezas PreArmado"
    res.config(text=text)


base_pre_inox_armada330 = {
    "inox_330": 1,
    "aro_numerador": 1,
    "espiral": 1,
    "perilla_numerador": 1,
    "tapita_perilla": 1,
    "patas": 4,
    "movimientos": 1,
    "eje_rectificado": 1,
    "resorte_movimiento": 1,
    "tornillo_guia": 1,
    "guia_U": 1,
    "teclas": 1,
    "cable_220w": 1,
    "varilla_carro_330": 1,
    "carros": 1,
    "rueditas": 4,
    "resorte_carro": 2,
    "cajamotor_final_330": 1,
    "capacitores": 1,
}

base_pre_inox_armada300 = {
    "inox_300": 1,
    "aro_numerador": 1,
    "espiral": 1,
    "perilla_numerador": 1,
    "tapita_perilla": 1,
    "patas": 4,
    "movimientos": 1,
    "eje_rectificado": 1,
    "resorte_movimiento": 1,
    "tornillo_guia": 1,
    "guia_U": 1,
    "teclas": 1,
    "cable_220w": 1,
    "varilla_carro_300": 1,
    "carros": 1,
    "rueditas": 4,
    "resorte_carro": 2,
    "cajamotor_final_300": 1,
    "capacitores": 1,
}

base_pre_inox_armada250 = {
    "inox_250": 1,
    "aro_numerador": 1,
    "espiral": 1,
    "perilla_numerador": 1,
    "tapita_perilla": 1,
    "patas": 4,
    "movimientos": 1,
    "eje_rectificado": 1,
    "resorte_movimiento": 1,
    "tornillo_guia": 1,
    "guia_U": 1,
    "teclas": 1,
    "cable_220w": 1,
    "varilla_carro_250": 1,
    "carros_250": 1,
    "rueditas": 4,
    "cajamotor_final_250": 1,
    "capacitores_250": 1,
}

base_pre_pintada_armada330 = {
    "base_pintada_330": 1,
    "aro_numerador": 1,
    "espiral": 1,
    "perilla_numerador": 1,
    "tapita_perilla": 1,
    "patas": 4,
    "movimientos": 1,
    "eje_rectificado": 1,
    "resorte_movimiento": 1,
    "tornillo_guia": 1,
    "guia_U": 1,
    "teclas": 1,
    "cable_220w": 1,
    "varilla_carro_330": 1,
    "carros": 1,
    "rueditas": 4,
    "resorte_carro": 2,
    "cajamotor_final_330": 1,
    "capacitores": 1,
}

base_pre_pintada_armada300 = {
    "base_pintada_300": 1,
    "aro_numerador": 1,
    "espiral": 1,
    "perilla_numerador": 1,
    "tapita_perilla": 1,
    "patas": 4,
    "movimientos": 1,
    "eje_rectificado": 1,
    "resorte_movimiento": 1,
    "tornillo_guia": 1,
    "guia_U": 1,
    "teclas": 1,
    "cable_220w": 1,
    "varilla_carro_300": 1,
    "carros": 1,
    "rueditas": 4,
    "resorte_carro": 2,
    "cajamotor_final_300": 1,
    "capacitores": 1,
}


def mostrar_por_pieza(arbol, modelo, res):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = 'pre_armado' AND modelo = '{modelo}'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
        
    text = f"Mostrar: Piezas {modelo}"
    res.config(text=text)


def maquinas_pre_armadas_disponibles(
    cantidad_maquinas, base_pre_armada, inventario_piezas
):
    # Inicializar la lista de piezas faltantes
    piezas_faltantes = []

    for pieza, cantidad_necesaria in base_pre_armada.items():
        if pieza not in inventario_piezas:
            # Si falta una pieza en el inventario, agregar a la lista de piezas faltantes
            piezas_faltantes.append(
                (pieza, cantidad_necesaria * cantidad_maquinas))
        else:
            cantidad_inventario = inventario_piezas[pieza]
            maquinas_posibles_con_pieza = cantidad_inventario // cantidad_necesaria

            # Verificar si la cantidad de piezas en inventario es suficiente
            if maquinas_posibles_con_pieza < cantidad_maquinas:
                piezas_faltantes.append(
                    (
                        pieza,
                        cantidad_necesaria
                        * (cantidad_maquinas - maquinas_posibles_con_pieza),
                    )
                )

    return piezas_faltantes


def conectar_base_datos_y_calcular_maquinas(cantidad_maquinas, base_pre_armada, res):
    # Conectar a la base de datos
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    try:
        # Ejecutar una consulta para obtener la cantidad de cada pieza en el inventario
        cursor.execute(
            "SELECT piezas, cantidad FROM piezas_finales_defenitivas")
        resultados = cursor.fetchall()

        # Crear un diccionario con la información del inventario
        inventario_piezas = dict(resultados)

        # Calcular las piezas faltantes para la cantidad de máquinas especificada
        piezas_faltantes = maquinas_pre_armadas_disponibles(
            cantidad_maquinas, base_pre_armada, inventario_piezas
        )

        if not piezas_faltantes:
            res.insert(0, f"Se pueden armar {cantidad_maquinas} máquinas pre-armadas.")
        else:
            res.insert(0, 
                f"No hay suficientes piezas para armar {cantidad_maquinas} máquinas pre-armadas. Piezas faltantes:"
            )
            for pieza, cantidad_faltante in piezas_faltantes:
                res.insert(0, f"{pieza}: {cantidad_faltante}")

    except sqlite3.Error as e:
        res.insert(0, f"Error al obtener datos de la base de datos: {e}")

    finally:
        # Cerrar la conexión a la base de datos
        conn.close()

#conectar_base_datos_y_calcular_maquinas(5, base_pre_inox_armada330)

def actualizar_inventario(res ,cantidad_maquinas, tipo_maquina, ensamblar=True):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    
    try:
        #H
        cursor.execute("SELECT piezas, cantidad FROM piezas_finales_defenitivas")
        resultados = cursor.fetchall()
        inventario_piezas = dict(resultados)

        # Definir la base pre-armada según el tipo de máquina
        if tipo_maquina == "inox_330":
            base_pre_armada = base_pre_inox_armada330
        elif tipo_maquina == "inox_300":
            base_pre_armada = base_pre_inox_armada300
        elif tipo_maquina == "inox_250":
            base_pre_armada = base_pre_inox_armada250
        elif tipo_maquina == "pintada_330":
            base_pre_armada = base_pre_pintada_armada330
        elif tipo_maquina == "pintada_300":
            base_pre_armada = base_pre_pintada_armada300
        else:
            res.insert(0, f"Tipo de máquina no reconocido: {tipo_maquina}")
            return inventario_piezas, []

        # Verificar si hay suficientes piezas disponibles antes de realizar el descuento
        piezas_faltantes = []
        for pieza, cantidad_necesaria in base_pre_armada.items():
            if inventario_piezas[pieza] < cantidad_necesaria * cantidad_maquinas:
                piezas_faltantes.append(
                    (
                        pieza,
                        cantidad_necesaria * cantidad_maquinas - inventario_piezas[pieza],
                    )
                )

        if piezas_faltantes:
            res.insert(0, "No hay suficientes piezas para ensamblar la cantidad deseada de máquinas.")
            # Imprimir las piezas que faltan en la consola
            res.insert(0, f"Piezas faltantes para ensamblar {cantidad_maquinas} máquinas {tipo_maquina}:")
            for pieza, cantidad_faltante in piezas_faltantes:
                res.insert(0, f"_____________________________")
                res.insert(0, f"Faltan {pieza}: {cantidad_faltante}")

            return inventario_piezas, piezas_faltantes



        # Actualizar el inventario según sea necesario
        for pieza, cantidad_necesaria in base_pre_armada.items():
            if ensamblar:
                inventario_piezas[pieza] -= cantidad_necesaria * cantidad_maquinas
                if inventario_piezas[pieza] < 0:
                    inventario_piezas[pieza] = 0
            else:
                inventario_piezas[pieza] += cantidad_necesaria * cantidad_maquinas

        # Actualizar la base de datos con el nuevo inventario
        for pieza, cantidad_actualizada in inventario_piezas.items():
            cursor.execute(
                "UPDATE piezas_finales_defenitivas SET cantidad = ? WHERE piezas = ?",
                (cantidad_actualizada, pieza),
            )

        # Incrementar la cantidad de la base pre-armada según el tipo de máquina
        if tipo_maquina == "inox_330":
            cursor.execute(
                "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'base_pre_armada330inox'",
                (cantidad_maquinas,),
            )
        elif tipo_maquina == "inox_300":
            cursor.execute(
                "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'base_pre_armada300inox'",
                (cantidad_maquinas,),
            )
        elif tipo_maquina == "inox_250":
            cursor.execute(
                "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'base_pre_armada250inox'",
                (cantidad_maquinas,),
            )
        elif tipo_maquina == "pintada_330":
            cursor.execute(
                "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'base_pre_armada330pint'",
                (cantidad_maquinas,),
            )
        elif tipo_maquina == "pintada_300":
            cursor.execute(
                "UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'base_pre_armada300pint'",
                (cantidad_maquinas,),
            )
        else:
            res.insert(0,"Error al actualizar.")

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Imprimir un mensaje indicando si se ensamblaron o eliminaron las máquinas
        accion = "ensamblaron" if ensamblar else "eliminaron"
        res.insert(0,f"{cantidad_maquinas} máquinas {tipo_maquina} se {accion}. Inventario actualizado en la base de datos.")

    except sqlite3.Error as e:
        res.insert(0,f"Error al actualizar el inventario en la base de datos: {e}")
        piezas_faltantes = []

    finally:
        conn.close()


def stock_prebases(arbol):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE mecanizado = 'prearmado'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)


def ensamblar_maquinas(cantidad_ensamblar_entry, lista_acciones):

    maquinas_mes = 0

    cantidad_ensamblada = cantidad_ensamblar_entry.get()

    # Validamos que la cantidad ingresada sea un número válido
    try:
        cantidad_ensamblada = int(cantidad_ensamblada)
    except ValueError:
        lista_acciones.insert(0, "Ingrese una Cantidad Válida")
        return

    conn = sqlite3.connect("Stock_Fadeco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT Pieza, Cantidad FROM piezas_de_330")
    stock = cursor.fetchall()

    cantidades_requeridas = {
        "Base": 1,
        "Motor": 1,
        "Teletubi": 1,
        "Cuchilla": 1,
        "Vela": 1,
        "CubreCuchilla": 1,
        "Cabezal": 1,
        "Planchada": 1,
        "Brazo": 1,
        "Tapa_afilador": 1,
        "Afilador": 1,
        "Patas": 4
    }

    for pieza, cantidad in stock:
        if pieza in cantidades_requeridas:
            cantidades_requerida = cantidades_requeridas[pieza] * \
                cantidad_ensamblada
            if cantidad < cantidades_requerida:
                lista_acciones.insert(
                    0, "No hay suficientes {pieza} en el stock para ensamblar {cantidad_ensamblada} máquinas.")
                conn.close()
                return

    # Si hay suficientes piezas, ensamblar las máquinas y actualizar las cantidades en la base de datos
    for pieza, cantidad in stock:
        if pieza in cantidades_requeridas:
            cantidad_requerida = cantidades_requeridas[pieza] * \
                cantidad_ensamblada
            nueva_cantidad = cantidad - cantidad_requerida
            cursor.execute(
                "UPDATE piezas_de_330 SET Cantidad=? WHERE Pieza=?", (nueva_cantidad, pieza))

    # Actualizar el contador de máquinas ensambladas

    maquinas_mes += cantidad_ensamblada

    # Crear una etiqueta para mostrar la cantidad total de máquinas ensambladas en el mes
    lista_acciones.insert(0, "Maquinas Terminadas en el mes: {maquinas_mes}")

    # Mostrar la cantidad total de máquinas ensambladas
    lista_acciones.insert(
        0, "Se Armaron {cantidad_ensamblada} máquinas \h Total del mes: {maquinas_mes}")

    conn.commit()
    conn.close()
    mostrar_datos()

def bases_terminados(arbol, res):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE mecanizado = 'prearmado'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
        
    text = "Mostrar: Piezas PreArmado"
    res.config(text=text)


#-----------------------armado-afilador----------------------------------------------

def mostrar_pieza_afilador(arbol, res ):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = 'afilador'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        res.insert(0, f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
        
        text = "Mostrar Pieza de Afiladores"
        res.config(text=text)

def mostrar_afilador_final(arbol, res):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE piezas = 'afilador_final'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        res.insert(0, f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
    
    text = "Mostrar Afiladores Terminados"
    res.config(text=text)

def armado_final_afiladores_y_agregar_cantidad(cantidad_ingresada, res):
    cantidad_piezas = {
        "capuchon_afilador": 2,
        "carcaza_afilador": 1,
        "eje_corto": 1,
        "eje_largo": 1,
        "ruleman_afilador": 2,
        "palanca_afilador": 1
    }

    with sqlite3.connect("basedatospiezas.db") as conn:
        cursor = conn.cursor()

        try:
            piezas_suficientes = True  # Flag para verificar si hay suficientes piezas para actualizar afilador_final

            for pieza, cantidad_pieza in cantidad_piezas.items():
                cursor.execute("SELECT cantidad FROM piezas_finales_defenitivas WHERE piezas = ?", (pieza,))
                cantidad_actual = cursor.fetchone()

                if cantidad_actual is None or cantidad_actual[0] < cantidad_ingresada * cantidad_pieza:
                    res.insert(0, f"No hay suficiente cantidad de {pieza} en la base de datos.")
                    piezas_suficientes = False
                else:
                    cantidad_restante = cantidad_actual[0] - cantidad_ingresada * cantidad_pieza
                    if cantidad_restante >= 0:
                        cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = ? WHERE piezas = ?", (cantidad_restante, pieza))
                    else:
                        res.insert(0, f"No hay suficiente cantidad de {pieza} en la base de datos.")
                        piezas_suficientes = False

            # Actualizar la cantidad de afilador_final solo si hay suficientes piezas
            if piezas_suficientes:
                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad + ? WHERE piezas = 'afilador_final'", (cantidad_ingresada,))
                conn.commit()
                res.insert(0, f"Se restaron {cantidad_ingresada} unidades de las piezas en la base de datos y se actualizó afilador_final.")

        except sqlite3.Error as e:
            res.insert(0, f"Error en la base de datos: {e}")
            conn.rollback()

        except ValueError as ve:
            res.insert(0, ve)


# '''''''''''''''''''''''''''''''''''''''''''''''ARmado Final''''''''''''''''''''''

def mostrar_piezas_finales(arbol, res):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas ,cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_final'"
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
        
    text = "Mostrar: Piezas Finales"
    res.config(text=text)

def mostrar_piezas_i330(arbol, res, modelo, tipo):
    
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE piezas IN ({seq}) AND sector = 'armado_final'"
            .format(seq=','.join(['?']*len(modelo))),
            tuple(modelo)
        )
        datos = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener datos de la base de datos: {e}")
    finally:
        conn.close()

    for item in arbol.get_children():
        arbol.delete(item)

    for dato in datos:
        arbol.insert("", "end", values=dato)
        

    text = f"Mostrar: Piezas Seleccionadas {tipo}"
    res.config(text=text)





#'''''''''''''''''''armado'''''''''''''''''''''''''''''''''''''''''''''''''''''''''



def consulta_bases_terminadas(arbol, mostrar):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad , modelo FROM piezas_finales_defenitivas WHERE mecanizado = 'prearmado'")
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

    subtitulo_text = "Mostrar Datos: Bases Terminadas"
    mostrar.config(text=subtitulo_text)


def consulta_insumos(arbol, mostrar):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad, modelo FROM piezas_finales_defenitivas WHERE sector = 'armado_final' AND mecanizado = 'shop'")
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

    subtitulo_text = "Mostrar Datos: Insumos"
    mostrar.config(text=subtitulo_text)


def consulta_piezas(arbol, mostrar):
    try:
        with sqlite3.connect("basedatospiezas.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT piezas, cantidad, modelo FROM piezas_finales_defenitivas WHERE sector = 'armado_final' AND mecanizado IN ('pulido', 'niquelado')")
            datos = cursor.fetchall()

        # Borrar todos los elementos existentes en el Treeview
        for item in arbol.get_children():
            arbol.delete(item)

        # Insertar los nuevos datos en el Treeview
        for dato in datos:
            arbol.insert("", "end", values=dato)

        subtitulo_text = "Mostrar Datos: Piezas"
        mostrar.config(text=subtitulo_text)
    except sqlite3.Error as e:
        # Manejo de errores: Imprimir el error o realizar alguna acción adecuada.
        print(f"Error SQLite: {e}")


def consulta_afiladores(arbol, mostrar):
    try:
        with sqlite3.connect("basedatospiezas.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT piezas, cantidad, modelo FROM piezas_finales_defenitivas WHERE piezas = 'afilador_final'")
            datos = cursor.fetchall()

        # Borrar todos los elementos existentes en el Treeview
        for item in arbol.get_children():
            arbol.delete(item)

        # Insertar los nuevos datos en el Treeview
        for dato in datos:
            arbol.insert("", "end", values=dato)

        subtitulo_text = "Mostrar Datos: Piezas"
        mostrar.config(text=subtitulo_text)
    except sqlite3.Error as e:
        # Manejo de errores: Imprimir el error o realizar alguna acción adecuada.
        print(f"Error SQLite: {e}")

i330 = {
    "brazo_330": 1,
    "cubrecuchilla_330": 1,
    "velero": 1,
    "perilla_brazo": 1,
    "cabezal_inox": 1,
    "teletubi_330": 1,
    "cuchilla_330": 1,
    "cuadrado_regulador": 1,
    "vela_final_330": 1,
    "cubre_motor_rectangulo": 1,
    "cubre_motor_cuadrado": 1,
    "planchada_final_330": 1,
    "varilla_brazo_330": 1,
    "resorte_brazo": 1,
    "tapa_afilador": 1,
    "pipas": 2,
    "tubo_manija": 1,
    "afilador_final": 1,
    "perilla_cubrecuchilla": 2,
    "perilla_afilador": 1,
    "base_afilador_330": 1,
    "base_pre_armada330inox": 1,
    "piedra_afilador": 1,
}

i300 = {
    "brazo_300": 1,
    "cubrecuchilla_300": 1,
    "velero": 1,
    "perilla_brazo": 1,
    "cabezal_inox": 1,
    "teletubi_300": 1,
    "cuchilla_300": 1,
    "cuadrado_regulador": 1,
    "vela_final_300": 1,
    "cubre_motor_rectangulo": 1,
    "cubre_motor_cuadrado": 1,
    "planchada_final_300": 1,
    "varilla_brazo_300": 1,
    "resorte_brazo": 1,
    "tapa_afilador": 1,
    "pipas": 2,
    "tubo_manija": 1,
    "afilador_final": 1,
    "perilla_cubrecuchilla": 2,
    "perilla_afilador": 1,
    "base_afilador_300": 1,
    "base_pre_armada300inox": 1,
    "piedra_afilador": 1,
}

i250 = {
    "brazo_250": 1,
    "cubrecuchilla_250": 1,
    "velero": 1,
    "perilla_brazo": 1,
    "cabezal_inox": 1,
    "teletubi_250": 1,
    "cuchilla_250": 1,
    "cuadrado_regulador": 1,
    "vela_final_250": 1,
    "cubre_motor_rectangulo": 1,
    "planchada_final_250": 1,
    "varilla_brazo_250": 1,
    "resorte_brazo": 1,
    "tapa_afilador_250": 1,
    "pipas": 2,
    "tubo_manija_250": 1,
    "afilador_final": 1,
    "perilla_cubrecuchilla": 2,
    "perilla_afilador": 1,
    "base_afilador_250": 1,
    "base_pre_armada250inox": 1,
    "piedra_afilador": 1,
}

p330 = {
    "brazo_330": 1,
    "cubrecuchilla_330": 1,
    "velero": 1,
    "perilla_brazo": 1,
    "cabezal_inox": 1,
    "teletubi_330": 1,
    "cuchilla_330": 1,
    "cuadrado_regulador": 1,
    "vela_final_330": 1,
    "cubre_motor_rectangulo": 1,
    "cubre_motor_cuadrado": 1,
    "planchada_final_330": 1,
    "varilla_brazo_330": 1,
    "resorte_brazo": 1,
    "tapa_afilador": 1,
    "pipas": 2,
    "tubo_manija": 1,
    "afilador_final": 1,
    "perilla_cubrecuchilla": 2,
    "perilla_afilador": 1,
    "base_afilador_330": 1,
    "base_pre_armada330pint": 1,
    "piedra_afilador": 1,
}

p300 = {
    "brazo_300": 1,
    "cubrecuchilla_300": 1,
    "velero": 1,
    "perilla_brazo": 1,
    "cabezal_inox": 1,
    "teletubi_300": 1,
    "cuchilla_300": 1,
    "cuadrado_regulador": 1,
    "vela_final_300": 1,
    "cubre_motor_rectangulo": 1,
    "cubre_motor_cuadrado": 1,
    "planchada_final_300": 1,
    "varilla_brazo_300": 1,
    "resorte_brazo": 1,
    "tapa_afilador": 1,
    "pipas": 2,
    "tubo_manija": 1,
    "afilador_final": 1,
    "perilla_cubrecuchilla": 2,
    "perilla_afilador": 1,
    "base_afilador_300": 1,
    "base_pre_armada300pint": 1,
    "piedra_afilador": 1,
}


def armado_de_maquinas(cantidad_maquinas, tipo_seleccionado, result):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()

    cursor.execute("SELECT piezas, cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_final'")
    filas = cursor.fetchall()
    base_de_datos = {pieza: cantidad for pieza, cantidad in filas}

    piezas_faltantes = {}

    # Utiliza diccionarios específicos para cada tipo
    tipos_piezas = {
        'inox_330': i330,
        'inox_300': i300,
        'inox_250': i250,
        'pintada_330': p330,
        'pintada_300': p300,
        # ... (add more types as needed)
    }

    # Obtén el diccionario específico para el tipo seleccionado
    tipo_a_ensamblar = tipos_piezas.get(tipo_seleccionado)

    if tipo_a_ensamblar is None:
        text2 = (f"Tipo {tipo_seleccionado} no reconocido.")
        result.insert(0, text2)
        conn.close()
        return

    # Actualiza el diccionario para reflejar la cantidad de máquinas
    tipo_a_ensamblar = {pieza: cantidad * int(cantidad_maquinas)
                        for pieza, cantidad in tipo_a_ensamblar.items()}

    for pieza, cantidad_necesaria in tipo_a_ensamblar.items():
        cursor.execute(
            "SELECT cantidad FROM piezas_finales_defenitivas WHERE sector = 'armado_final' AND piezas = ?", (pieza,))
        cantidad_disponible = cursor.fetchone()

        if cantidad_disponible:
            cantidad_disponible = int(cantidad_disponible[0])
            cantidad_faltante = max(
                0, cantidad_necesaria - cantidad_disponible)

            if cantidad_faltante > 0:
                piezas_faltantes[pieza] = cantidad_faltante
            else:
                # Resta la cantidad utilizada de la base de datos
                cursor.execute("UPDATE piezas_finales_defenitivas SET cantidad = cantidad - ? WHERE sector = 'armado_final' AND piezas = ?",
                               (cantidad_necesaria, pieza))
                conn.commit()
        else:
            text1 = f"No se encontró cantidad para la pieza {pieza} en la base de datos."
            result.insert(0, text1)

    if not piezas_faltantes:
        cursor.execute(f"UPDATE producto_final SET cantidad = cantidad + ? WHERE piezas = ?",
                       (int(cantidad_maquinas), tipo_seleccionado))
        conn.commit()
        text3 = f"Se Agregaron {cantidad_maquinas} máquinas {tipo_seleccionado}."
        result.insert(0, text3)
    else:
        text4 = "No hay suficientes piezas para ensamblar las máquinas. Faltan las siguientes piezas:"
        result.insert(0, text4)
        for pieza, cantidad_faltante in piezas_faltantes.items():
            result.insert(0, f"{pieza}: {cantidad_faltante} unidades.")

    conn.close()


def mostrar_maquinas_teminadas(arbol,res):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT piezas, cantidad, modelo  FROM producto_final ")
    datos = cursor.fetchall()
    conn.close()
    for item in arbol.get_children():
        arbol.delete(item)
    for dato in datos:
        arbol.insert("", "end", values=dato)

    subtitulo_text = "Mostrar Datos: Maquinas Terminadas"
    res.config(text=subtitulo_text)

#9999999999999999999999999999999999999999
