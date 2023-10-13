import tkinter as tk
from tkinter import ttk
import sqlite3


def mostrar_datos_300():
    conn = sqlite3.connect("basedatospiezas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT piezas, cantidad FROM Piezas300")
    datos = cursor.fetchall()
    conn.close()
    
    for item in tree.get_children():
        thee.delete(item)
        
    for dato in datos:
        tree.insert("", "end", value=dato)
        
        
root = tk.Tk()
root.title("MOSTRAR DATOS")

tree = ttk.Treeview(root, columns=("Piezas", "Cantidad"))
tree.heading("#1", text="Pieza")
tree.heading("#2", text="Cantidad")
tree.pack()


btn_cargar = ttk.Button(root, text="Cargar Datos", comman=mostrar_datos_300)
btn_cargar.pack()


root.mainloop()