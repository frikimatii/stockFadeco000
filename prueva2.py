import sqlite3
import tkinter as tk
from tkinter import ttk

def calcular_maquinas_posibles(base_modelo, tipo_base, modelo, lista_acciones):
    try:
        conn = sqlite3.connect("basedatospiezas.db")
        cursor = conn.cursor()
        
        cantidades = {}
        piezas_faltantes = []

        for pieza, cantidad in base_modelo.items():
            cursor.execute("SELECT cantidad, tipo_de_base FROM chapa WHERE modelo = ? AND piezas = ?", (modelo, pieza))
            resultado = cursor.fetchone()

            if resultado is not None:
                cantidad_disponible, tipo_base_pieza = resultado
                if tipo_base_pieza == tipo_base:
                    cantidades[pieza] = cantidad_disponible
                else:
                    piezas_faltantes.append(pieza)

        if len(cantidades) == len(base_modelo):
            cantidad_bases = min(cantidades.values()) // min(base_modelo.values())
            lista_acciones.insert(0, f"Se pueden armar {cantidad_bases} máquinas.")
        else:
            lista_acciones.insert(0, "No hay piezas suficientes para armar las máquinas.")
            if piezas_faltantes:
                lista_acciones.insert(1, f"Las siguientes piezas no tienen tipo_de_base {tipo_base}: {', '.join(piezas_faltantes)}")
            
        conn.close()

    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        lista_acciones.insert(0, "Error en la base de datos.")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora de Máquinas Posibles")

# Crear un marco para los botones
caja_botones = ttk.Frame(ventana)
caja_botones.grid(row=0, column=0)

# Crear una lista para mostrar mensajes
lista_acciones = tk.Listbox(ventana, width=60)
lista_acciones.grid(row=1, column=0)

# Definir las bases de modelos
base_inox_330 = {
    "chapa_principal_330": 1,
    "lateral_L_330": 1,
    "lateral_R_330": 1,
    "varilla_330": 1,
    "planchuela_330": 1,
    "portaeje": 1,
    "arandela": 1
}

base_inox_300 = {
    "chapa_principal_300": 1,
    "lateral_L_300": 1,
    "lateral_R_300": 1,
    "varilla_300": 1,
    "planchuela_300": 1,
    "portaeje": 1,
    "arandela": 1
}

# Botones para calcular máquinas posibles
btn_i_330 = ttk.Button(caja_botones, text="Inox 330", command=lambda: calcular_maquinas_posibles(base_inox_330, "acero", "330", lista_acciones))
btn_i_330.grid(row=1, column=0)

btn_i_300 = ttk.Button(caja_botones, text="Inox 300", command=lambda: calcular_maquinas_posibles(base_inox_300, "acero", "300", lista_acciones))
btn_i_300.grid(row=1, column=1)

ventana.mainloop()
