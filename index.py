import tkinter as tk
from tkinter import ttk

def inicio(notebook):
    # Establecer el color de fondo del notebook 
    notebook.configure(style='Pestania.TNotebook')
    estilo_notebook = ttk.Style()
    estilo_notebook.configure('Pestania.TNotebook', background='#192965')

    # Establecer estilo para las pestañas
    estilo_pestanas = ttk.Style()
    estilo_pestanas.configure("TNotebook.Tab", font=('Helvetica', 12), padding=[10, 5])

    # Establecer estilo para la pestaña específica (cambiar el color de fondo)
    estilo_pestanas.configure("TNotebook.Tab", background="#192965", foreground="black", lightcolor="#192965", bordercolor="#192965")

    pestania = ttk.Frame(notebook)
    notebook.add(pestania, text="Inicio")

    # Crear un estilo y configurar el color de fondo
    estilo = ttk.Style()
    estilo.configure('Pestania.TFrame', background='#192965')

    index = ttk.Frame(pestania, style='Pestania.TFrame')
    index.grid(row=0, column=0, sticky="nsew")  # Empaqueta el frame index para expandirse en todas las direcciones

    # Configurar las columnas y filas para que se expandan
    pestania.grid_rowconfigure(0, weight=1)
    pestania.grid_columnconfigure(0, weight=1)


    box1 = tk.Frame(index, bg='#192965')  # Establecer el color de fondo de box1
    box1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



    # Insertar una imagen en lugar de texto
    image_path1 = "D:/base_datos_fadeco1_pyinstall/img/fadeco_logo.png"  # Reemplaza con la ruta real de tu imagen en formato PNG
    image1 = tk.PhotoImage(file=image_path1)
    label_image1 = tk.Label(box1, image=image1, bg='#192965')  # Cambiar el color de fondo de la imagen
    label_image1.image = image1  # Para evitar que la imagen sea eliminada por el recolector de basura
    label_image1.grid(row=1, column=0, padx=15, pady=15)
    
    tk.Label(box1, text="Modelo", font=('Tahoma', 50, 'bold underline'), bg='#192965', fg='white').grid(row=2, column=0, padx=2, pady=10)
    
    tk.Label(box1, text="Inoxidable 330", font=('Tahoma', 12), bg='#192965', fg='white').grid(row=3, column=0,padx=5, pady=5)
    tk.Label(box1, text="Inoxidable 300", font=('Tahoma', 12), bg='#192965', fg='white').grid(row=4, column=0, padx=5, pady=5)
    tk.Label(box1, text="Inoxidable 250", font=('Tahoma', 12), bg='#192965', fg='white').grid(row=5, column=0, padx=5, pady=5)
    tk.Label(box1, text="Pintada 330", font=('Tahoma', 12), bg='#192965', fg='white').grid(row=6, column=0, padx=5, pady=5)
    tk.Label(box1, text="Pintada 300", font=('Tahoma', 12), bg='#192965', fg='white').grid(row=7, column=0,padx=5, pady=5)


    box2 = tk.Frame(index, bg='#192965')  # Establecer el color de fondo de box2
    box2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    titulo = tk.Label(box2, text="Control De Stock", font=('Tahoma', 30), bg='#192965', fg='white')
    titulo.grid(row=0 ,column=0 , sticky="esw")
    

    image_path2 = "D:/base_datos_fadeco1_pyinstall/img/Cortadora.png"  # Reemplaza con la ruta real de tu imagen en formato PNG
    image2 = tk.PhotoImage(file=image_path2)
    label_image2 = tk.Label(box2, image=image2, bg='#192965')  # Cambiar el color de fondo de la imagen
    label_image2.image = image2  # Para evitar que la imagen sea eliminada por el recolector de basura
    label_image2.grid(row=1, column=0, padx=50, pady=50 )
 