import tkinter as tk

def agregar_pieza():
    pieza = entry_pieza.get()
    tipo = ""

    if tipo_var.get() == 1:
        tipo = "Acero"
    elif tipo_var.get() == 2:
        tipo = "Chapa"
    
    resultado_label.config(text=f"Se agregó la pieza: {pieza}, Tipo: {tipo}")

# Crear la ventana
window = tk.Tk()
window.title("Agregar Piezas")

# Crear una entrada de texto para la pieza
entry_pieza = tk.Entry(window, width=30)
entry_pieza.pack()

# Radio buttons para seleccionar el tipo de pieza
tipo_var = tk.IntVar()
tipo_var.set(1)  # Inicialmente selecciona Acero
acero_radio = tk.Radiobutton(window, text="Acero", variable=tipo_var, value=1)
acero_radio.pack()
chapa_radio = tk.Radiobutton(window, text="Chapa", variable=tipo_var, value=2)
chapa_radio.pack()

# Botón para agregar la pieza
agregar_button = tk.Button(window, text="Agregar Pieza", command=agregar_pieza)
agregar_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(window, text="")
resultado_label.pack()

# Ejecutar la aplicación
window.mainloop()

