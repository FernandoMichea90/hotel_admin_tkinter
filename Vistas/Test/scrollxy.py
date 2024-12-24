import tkinter as tk
from tkinter import ttk

# Crear ventana principal
root = tk.Tk()
root.title("Scrollbars Correctamente Posicionados")

# Frame contenedor principal
frame_week_table = tk.Frame(root)
frame_week_table.pack(fill="both", expand=True)

# Frame contenedor para Canvas y scrollbar vertical
canvas_frame = tk.Frame(frame_week_table)
canvas_frame.pack(side="top", fill="both", expand=True)

# Crear el canvas
canvas = tk.Canvas(canvas_frame, bg="pink")
canvas.pack(side="left", fill="both", expand=True)

# Scrollbar vertical
scrollbar_vertical = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
scrollbar_vertical.pack(side="right", fill="y")

# Scrollbar horizontal
scrollbar_horizontal = ttk.Scrollbar(frame_week_table, orient="horizontal", command=canvas.xview)
scrollbar_horizontal.pack(side="bottom", fill="x")

# Configurar el canvas para usar los scrollbars
canvas.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

# Crear un frame desplazable dentro del canvas
scrollable_frame = tk.Frame(canvas, bg="white")
scrollable_frame_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Agregar contenido al frame desplazable
for i in range(20):
    for j in range(10):
        tk.Label(scrollable_frame, text=f"Fila {i}, Columna {j}", bg="lightblue").grid(row=i, column=j, padx=5, pady=5)

# Ajustar el tamaño del canvas según el contenido del frame desplazable
def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", configure_scroll_region)

# Iniciar la aplicación
root.mainloop()
