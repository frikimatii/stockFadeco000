import tkinter as tk
from tkinter import ttk

class ControlDeStockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Stock")

        # Crear pestañas
        self.tabControl = ttk.Notebook(root)
        self.tab_inventario = ttk.Frame(self.tabControl)
        self.tab_proveedores = ttk.Frame(self.tabControl)
        self.tab_ordenes = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab_inventario, text="Inventario")
        self.tabControl.add(self.tab_proveedores, text="Proveedores")
        self.tabControl.add(self.tab_ordenes, text="Órdenes de Compra")

        self.tabControl.pack(expand=1, fill="both")

        # Botones de navegación
        self.btn_anterior = ttk.Button(root, text="Anterior", command=self.ir_a_pestaña_anterior)
        self.btn_anterior.pack(side=tk.LEFT, padx=5)

        self.btn_siguiente = ttk.Button(root, text="Siguiente", command=self.ir_a_siguiente_pestaña)
        self.btn_siguiente.pack(side=tk.LEFT, padx=5)

        # Contenido de las pestañas...

    def ir_a_pestaña_anterior(self):
        current_index = self.tabControl.index(self.tabControl.select())
        if current_index > 0:
            self.tabControl.select(current_index - 1)

    def ir_a_siguiente_pestaña(self):
        current_index = self.tabControl.index(self.tabControl.select())
        if current_index < self.tabControl.index("end") - 1:
            self.tabControl.select(current_index + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControlDeStockApp(root)
    root.mainloop()
