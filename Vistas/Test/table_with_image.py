import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Treeview con Paginación")
root.geometry("600x400")

# Datos de ejemplo
datos = [
    (i, f"Reserva {i}", "Confirmada" if i % 2 == 0 else "Pendiente")
    for i in range(1, 101)
]  # 100 filas de ejemplo

filas_por_pagina = 10
pagina_actual = 1

# Crear el Treeview
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=10)
tree.pack(fill=tk.BOTH, expand=True)

# Definir encabezados
tree.heading("col1", text="ID")
tree.heading("col2", text="Nombre")
tree.heading("col3", text="Estado")

# Función para cargar una página
def cargar_pagina(pagina):
    global pagina_actual
    pagina_actual = pagina

    # Limpiar el Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Obtener los datos de la página
    inicio = (pagina - 1) * filas_por_pagina
    fin = inicio + filas_por_pagina
    datos_pagina = datos[inicio:fin]

    # Insertar datos en el Treeview
    for fila in datos_pagina:
        tree.insert("", tk.END, values=fila)

    # Actualizar el label de la página
    label_pagina.config(text=f"Página {pagina_actual} de {total_paginas}")

# Función para cambiar de página
def cambiar_pagina(direccion):
    nueva_pagina = pagina_actual + direccion
    if 1 <= nueva_pagina <= total_paginas:
        cargar_pagina(nueva_pagina)

# Total de páginas
total_paginas = (len(datos) + filas_por_pagina - 1) // filas_por_pagina

# Botones de navegación
frame_botones = tk.Frame(root)
frame_botones.pack(fill=tk.X)

boton_anterior = tk.Button(frame_botones, text="Anterior", command=lambda: cambiar_pagina(-1))
boton_anterior.pack(side=tk.LEFT, padx=5, pady=5)

boton_siguiente = tk.Button(frame_botones, text="Siguiente", command=lambda: cambiar_pagina(1))
boton_siguiente.pack(side=tk.RIGHT, padx=5, pady=5)

# Etiqueta de la página actual
label_pagina = tk.Label(frame_botones, text="")
label_pagina.pack(side=tk.LEFT, expand=True)

# Cargar la primera página al inicio
cargar_pagina(1)

# Iniciar la aplicación
root.mainloop()
