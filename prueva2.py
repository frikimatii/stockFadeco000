import tkinter as tk

def enviar():
    # Función de ejemplo
    print("Botón presionado")

# Crear ventana
ventana = tk.Tk()
ventana.title("Botones con Distintos Estilos")

# Estilos para los primeros 15 botones
estilos = [
    {"text": "Botón 1", "background": "green", "foreground": "white", "font": ('Helvetica', 8, "bold")},
    {"text": "Botón 2", "background": "blue", "foreground": "white", "font": ('Arial', 10, "italic")},
    {"text": "Botón 3", "background": "red", "foreground": "white", "font": ('Courier', 12, "bold")},
    {"text": "Botón 4", "background": "purple", "foreground": "white", "font": ('Verdana', 10, "italic")},
    {"text": "Botón 5", "background": "orange", "foreground": "black", "font": ('Arial', 12, "bold")},
    {"text": "Botón 6", "background": "yellow", "foreground": "black", "font": ('Courier', 14, "italic")},
    {"text": "Botón 7", "background": "cyan", "foreground": "black", "font": ('Verdana', 12, "bold")},
    {"text": "Botón 8", "background": "pink", "foreground": "black", "font": ('Arial', 14, "italic")},
    {"text": "Botón 9", "background": "brown", "foreground": "white", "font": ('Courier', 10, "bold")},
    {"text": "Botón 10", "background": "gray", "foreground": "white", "font": ('Arial', 10, "italic")},
    {"text": "Botón 11", "background": "magenta", "foreground": "white", "font": ('Helvetica', 8, "bold")},
    {"text": "Botón 12", "background": "green", "foreground": "white", "font": ('Arial', 12, "bold")},
    {"text": "Botón 13", "background": "blue", "foreground": "white", "font": ('Courier', 10, "italic")},
    {"text": "Botón 14", "background": "red", "foreground": "white", "font": ('Verdana', 10, "bold")},
    {"text": "Botón 15", "background": "purple", "foreground": "white", "font": ('Helvetica', 12, "italic")}
]

# Crear y posicionar los primeros 15 botones con distintos estilos
for i, estilo in enumerate(estilos, start=1):
    tk.Button(
        ventana,
        text=estilo["text"],
        background=estilo["background"],
        foreground=estilo["foreground"],
        padx=10,
        pady=4,
        font=estilo["font"],
        command=enviar
    ).grid(row=i, column=0, columnspan=2, pady=5)



# Iniciar el bucle de la aplicación
ventana.mainloop()
