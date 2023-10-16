import sqlite3


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
