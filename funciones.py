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




