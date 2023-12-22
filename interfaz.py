import tkinter as tk
from tkinter import ttk

class AplicacionLista:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Treeview con Colores Condicionales")

        # Crear un Treeview
        self.treeview = ttk.Treeview(root, columns=("Elemento", "Cantidad"))
        self.treeview.pack(padx=10, pady=10)

        # Configurar encabezados
        self.treeview.heading("#0", text="Elemento")
        self.treeview.heading("Cantidad", text="Cantidad")

        # Agregar elementos a la lista con cantidades
        elementos = [("Elemento 1", 5), ("Elemento 2", 20), ("Elemento 3", 40), ("Elemento 4", 12), ("Elemento 5", 60)]
        for elemento, cantidad in elementos:
            color_fondo = self.obtener_color_fondo(cantidad)
            self.treeview.insert("", tk.END, values=(elemento, cantidad), tags=(color_fondo,))

        # Establecer reglas de estilo para colores
        self.treeview.tag_configure("red", background="red")
        self.treeview.tag_configure("green", background="green")

    def obtener_color_fondo(self, cantidad):
        if cantidad < 10:
            return "red"
        elif cantidad > 50:
            return "green"
        else:
            return ""

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionLista(root)
    root.mainloop()
