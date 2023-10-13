import sqlite3
from tkinter import ttk


def mostrar_datos_330(tree2):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM Piezas330")
    datos = cursor.fetchall()
    
    conn.close()
    
    for item in tree2.get_children():
        tree2.delete(item)
    
    for dato in datos:
        tree2.insert("", "end", values=dato)
    
    
def mostrar_datos_300(tree1):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM Piezas300")
    datos = cursor.fetchall()
    
    conn.close()
    
    for item in tree1.get_children():
        tree1.delete(item)
        
    for dato in datos:
        tree1.insert("", "end", values=dato)
        
            
    
def mostrar_datos_250(tree3):
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM Piezas250")
    datos = cursor.fetchall()
    
    conn.close()
    
    for item in tree3.get_children():
        tree3.delete(item)
        
    for dato in datos:
        tree3.insert("", "end", values=dato)
        
        

def actualizar_pieza(lista_predefinida330, entrada_cantidad330, res, tree2):
    actualizar_pieza = lista_predefinida330.get()
    entrada_actualizar = entrada_cantidad330.get()
    
    if entrada_actualizar.strip().isdigit():
        entrada_actualizar = int(entrada_actualizar)
        
        if entrada_actualizar < 0:
            res.config(text="La Cantidad NO puede ser Negativa")
        else:
            conn = sqlite3.connect("basedatospiezas.db")
            cursor = conn.cursor()
            cursor.execute("SELECT cantidad FROM Piezas330 WHERE piezas=?", (actualizar_pieza, ))
            cantidad_actual = cursor.fetchone()
            
            if cantidad_actual is not None:
                cantidad_actual = cantidad_actual[0]
                nueva_cantidad = cantidad_actual + entrada_actualizar
                cursor.execute("UPDATE Piezas330 SET cantidad=? WHERE piezas=?", (nueva_cantidad, actualizar_pieza))
                conn.commit()
                conn.close()
                mostrar_datos_330(tree2)  # Llama a la función para mostrar los datos actualizados
                res.config(text=f"Carga exitosa:Usted cargo {entrada_actualizar} {actualizar_pieza}:")
            else:
                res.config(text=f"La Pieza {actualizar_pieza} no se puede modificar")
    else:
        res.config(text="La cantidad ingresada no es un número válido")

    
def eliminar_pieza(lista_predefinida_eliminar330,entrada_cantidad_eliminar330, res,tree2 ):
    pieza_eliminar = lista_predefinida_eliminar330.get()
    cantidad_eliminar = entrada_cantidad_eliminar330.get()
    
    try:
       cantidad_eliminar = int(cantidad_eliminar)
       if cantidad_eliminar < 0:
           res.config(text="La cantidad no puede ser Negativa")
           return
    except ValueError:
        res.config(text="La cantidad de ser un numero entero positivo")
    
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT cantidad FROM Piezas330 WHERE piezas=?",(pieza_eliminar, ))
    cantidad_actual = cursor.fetchone()
    
    if cantidad_actual is not None:
        cantidad_actual = cantidad_actual[0]
        if cantidad_eliminar <= cantidad_actual:
            nueva_cantidad = cantidad_actual - cantidad_eliminar
            if nueva_cantidad >= 0:
                cursor.execute("UPDATE Piezas330 SET cantidad=? WHERE piezas=?", (nueva_cantidad,pieza_eliminar))
            
            else:
                res.config(text=f"No se Puede elimimar la pieza {pieza_eliminar}")
        else:
            res.config(text=f"No Hay suficiente {pieza_eliminar} en el stock")
    else:
        res.config(text=f"la Pieza {pieza_eliminar} No se puede eliminar")
    
    conn.commit()
    conn.close()
    mostrar_datos_330(tree2) 

