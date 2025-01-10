import tkinter as tk
import random

# Datos
fruits = ['apple', 'blueberry', 'cherry', 'orange', 'kiwi', 'strawberry', 'grape', 'pineapple', 'mango', 'peach']
counts = [40, 100, 30, 55, 60, 90, 70, 50, 85, 65]
bar_labels = ['red', 'blue', 'red', 'orange', 'green', 'red', 'purple', 'yellow', 'orange', 'pink']
bar_colors = ['#FF0000', '#0000FF', '#FF0000', '#FFA500', '#32CD32', '#FF0000', '#8A2BE2', '#FFFF00', '#FFA500', '#FFC0CB']

# Crear ventana principal
window = tk.Tk()
window.title("Gráfico de Barras Simple")

# Crear canvas para el dibujo
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Definir espacio y márgenes
margin = 50
bar_width = 50
spacing = 20
max_height = canvas_height - 2 * margin

# Dibujar barras
for i in range(len(fruits)):
    bar_height = (counts[i] / max(counts)) * max_height
    x1 = margin + i * (bar_width + spacing)
    y1 = canvas_height - margin - bar_height
    x2 = x1 + bar_width
    y2 = canvas_height - margin

    color = bar_colors[i]  # Usar colores desde bar_colors
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    canvas.create_text(x1 + bar_width // 2, y2 + 10, text=fruits[i], anchor=tk.W)
    canvas.create_text(x1 + bar_width // 2, y1 - 20, text=str(counts[i]), anchor=tk.W)

# Iniciar bucle principal
window.mainloop()
