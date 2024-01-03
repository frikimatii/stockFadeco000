import tkinter as tk
from tkinter import ttk

def on_button_click():
    print("Botón clickeado")

# Crear la ventana
root = tk.Tk()

# Estilo 1: Botón predeterminado
ttk.Button(root, text="Botón Predeterminado", command=on_button_click).pack(pady=5)

# Estilo 2: Botón con resalte (estilo 'TButton')
style2 = ttk.Style()
style2.configure("TButton", padding=10, relief="flat", background="#a6a6a6", font=("Arial", 10, "bold"))
ttk.Button(root, text="Botón con Resalte", style="TButton", command=on_button_click).pack(pady=5)

# Estilo 3: Botón redondeado con fondo y texto personalizados
style3 = ttk.Style()
style3.configure("Round.TButton", padding=10, relief="flat", background="#4caf50", font=("Arial", 12, "bold"))
ttk.Button(root, text="Botón Redondeado", style="Round.TButton", command=on_button_click).pack(pady=5)

# Estilo 4: Botón de radio
style4 = ttk.Style()
style4.configure("TRadiobutton", padding=10, relief="flat", background="#2196f3", font=("Arial", 12, "bold"))
ttk.Radiobutton(root, text="Opción 1", style="TRadiobutton").pack()
ttk.Radiobutton(root, text="Opción 2", style="TRadiobutton").pack()

# Estilo 5: Botón de chequeo
style5 = ttk.Style()
style5.configure("TCheckbutton", padding=10, relief="flat", background="#ff5722", font=("Arial", 12, "bold"))
ttk.Checkbutton(root, text="Aceptar Términos", style="TCheckbutton").pack()

style7 = ttk.Style()
style7.configure("ImageButton.TButton", padding=10, relief="flat", font=("Arial", 12, "bold"))
image = tk.PhotoImage(file="img/logofadeco.png")
ttk.Button(root, text="Botón con Imagen", style="ImageButton.TButton", image=image, compound="left", command=on_button_click).pack(pady=5)

# Estilo 8: Botón de gradiente
style8 = ttk.Style()
style8.configure("Gradient.TButton", padding=10, relief="flat", font=("Arial", 12, "bold"))
style8.map("Gradient.TButton", background=[("active", "#ff8f00"), ("!active", "#ffc107")])
ttk.Button(root, text="Botón con Gradiente", style="Gradient.TButton", command=on_button_click).pack(pady=5)

# Estilo 9: Botón grande con efecto de sombra
style9 = ttk.Style()
style9.configure("LargeShadow.TButton", padding=20, relief="flat", background="#2196f3", font=("Arial", 14, "bold"))
style9.map("LargeShadow.TButton", shadowcolor=[("active", "black")], bordercolor=[("active", "#2196f3")])
ttk.Button(root, text="Botón Grande con Sombra", style="LargeShadow.TButton", command=on_button_click).pack(pady=5)

# Estilo 10: Botón circular
style10 = ttk.Style()
style10.configure("Circular.TButton", padding=10, relief="flat", background="#4caf50", font=("Arial", 12, "bold"))
ttk.Button(root, text="Botón Circular", style="Circular.TButton", command=on_button_click).pack(pady=5)

# Estilo 11: Botón de borde doble
style11 = ttk.Style()
style11.configure("DoubleBorder.TButton", padding=10, relief="flat", background="#e91e63", font=("Arial", 12, "bold"))
style11.map("DoubleBorder.TButton", bordercolor=[("active", "#e91e63")])
ttk.Button(root, text="Botón con Borde Doble", style="DoubleBorder.TButton", command=on_button_click).pack(pady=5)

# Estilo 12: Botón 3D
style12 = ttk.Style()
style12.configure("3D.TButton", padding=10, relief="flat", background="#009688", font=("Arial", 12, "bold"))
style12.map("3D.TButton", relief=[("pressed", "sunken"), ("!pressed", "ridge")])
ttk.Button(root, text="Botón 3D", style="3D.TButton", command=on_button_click).pack(pady=5)

# Iniciar el bucle principal
root.mainloop()
