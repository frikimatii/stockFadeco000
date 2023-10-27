import tkinter as tk

def agregar_accion():
    accion = entrada_accion.get()
    if accion:
        lista_acciones.insert(tk.END, accion)
        entrada_accion.delete(0, tk.END)

def borrar_accion():
    seleccion = lista_acciones.curselection()
    if seleccion:
        lista_acciones.delete(seleccion)

root = tk.Tk()
root.title("Registro de Acciones")

entrada_accion = tk.Entry(root, width=40)
entrada_accion.pack(pady=10)

boton_agregar = tk.Button(root, text="Agregar Acción", command=agregar_accion)
boton_agregar.pack()

boton_borrar = tk.Button(root, text="Borrar Acción", command=borrar_accion)
boton_borrar.pack()

lista_acciones = tk.Listbox(root, width=50)
lista_acciones.pack()

root.mainloop()
