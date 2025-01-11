import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Treeview con Ordenamiento")
root.geometry("600x400")

# Datos de ejemplo
datos = [
    (1, "Juan Pérez", "Confirmada"),
    (2, "Ana Gómez", "Pendiente"),
    (3, "Carlos López", "Confirmada"),
    (4, "María Torres", "Pendiente"),
]

# Estado de ordenamiento por columna
orden = {"col1": True, "col2": True, "col3": True}

# Crear el Treeview
tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=10)
tree.pack(fill=tk.BOTH, expand=True)

# Definir encabezados
tree.heading("col1", text="ID", command=lambda: ordenar_por_columna("col1", 0))
tree.heading("col2", text="Nombre", command=lambda: ordenar_por_columna("col2", 1))
tree.heading("col3", text="Estado", command=lambda: ordenar_por_columna("col3", 2))

# Insertar datos en el Treeview
def cargar_datos():
    for fila in tree.get_children():
        tree.delete(fila)
    for fila in datos:
        tree.insert("", tk.END, values=fila)

cargar_datos()

# Función para ordenar por columna
def ordenar_por_columna(columna, indice):
    global datos, orden
    datos = sorted(datos, key=lambda x: x[indice], reverse=orden[columna])
    orden[columna] = not orden[columna]  # Cambiar el sentido del orden
    cargar_datos()

# Iniciar la aplicación
root.mainloop()
