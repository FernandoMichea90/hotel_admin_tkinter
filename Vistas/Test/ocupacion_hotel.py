import tkinter as tk
from datetime import datetime, timedelta

# Crear ventana principal
root = tk.Tk()
root.title("Ocupación del Hotel")

# Configuración inicial
NUM_DIAS = 2  # Número de días por bloque
offset = 0  # Desplazamiento para navegación

# Lista de habitaciones
habitaciones = list(range(21, 30)) + list(range(31, 37))

# Datos ficticios de ocupación (puedes reemplazar con datos reales)
ocupaciones = {
    21: {"2024-12-23": "Juan", "2024-12-24": "Ana María Specter Litt"},
    22: {"2024-12-26": "Luis"},
    31: {"2024-12-28": "Carlos", "2024-12-29": "María"},
}

# Frame para la tabla
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Función para actualizar la tabla
def actualizar_tabla():
    # Limpiar el frame existente
    for widget in frame.winfo_children():
        widget.destroy()

    # Generar fechas a partir del desplazamiento
    fechas = [
        (datetime.now() + timedelta(days=offset + i)).strftime("%Y-%m-%d")
        for i in range(NUM_DIAS)
    ]

    # Crear encabezados de columnas (fechas)
    tk.Label(frame, text="Habitación", borderwidth=1, relief="solid", width=15).grid(row=0, column=0)
    for col, fecha in enumerate(fechas, start=1):
        tk.Label(frame, text=fecha, borderwidth=1, relief="solid", width=35).grid(row=0, column=col)

    # Rellenar filas con habitaciones y ocupaciones
    for row, habitacion in enumerate(habitaciones, start=1):
        # Columna de habitación
        tk.Label(frame, text=f"Habitación {habitacion}", borderwidth=1, relief="solid", width=15).grid(row=row, column=0)
        # Columnas de ocupación
        for col, fecha in enumerate(fechas, start=1):
            cliente = ocupaciones.get(habitacion, {}).get(fecha, "")  # Obtener cliente o vacío
            tk.Label(frame, text=cliente, borderwidth=1, relief="solid", width=35).grid(row=row, column=col)

# Función para manejar los botones de navegación
def cambiar_dias(direccion):
    global offset
    offset += direccion
    actualizar_tabla()

# Botones de navegación
botones_frame = tk.Frame(root)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Atrás", command=lambda: cambiar_dias(-1)).pack(side=tk.LEFT, padx=5)
tk.Button(botones_frame, text="Adelante", command=lambda: cambiar_dias(1)).pack(side=tk.LEFT, padx=5)

# Inicializar la tabla
actualizar_tabla()

# Ejecutar la aplicación
root.mainloop()
