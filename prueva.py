def calcular_maquinas_acero_330():
    try:
        conn = sqlite3.connect("basedatospiezas.db")  # Reemplaza con el nombre de tu base de datos
        cursor = conn.cursor()

        # Define la estructura de una máquina de acero 330
        maquina_acero_330 = {
            "chapa_principal_330": 1,
            "lateral_L_330": 1,
            "lateral_R_330": 1,
            "varilla_330": 1,
            "planchuela_330": 1,
            "portaeje": 1
        }

        # Consulta las cantidades de las piezas en la base de datos
        cantidades = {}
        for pieza, cantidad in maquina_acero_330.items():
            cursor.execute("SELECT cantidad FROM chapa WHERE piezas = ?", (pieza,))
            resultado = cursor.fetchone()
            if resultado is not None:
                cantidad_disponible = resultado[0]
                cantidades[pieza] = cantidad_disponible

        # Calcula la cantidad máxima de máquinas que se pueden armar
        cantidad_maquinas = min(cantidades.values()) // min(maquina_acero_330.values())

        return cantidad_maquinas
    except sqlite3.Error as e:
        print("ERROR EN LA BASE DE DATOS:", e)
        return 0  # En caso de error, devuelve 0 máquinas
