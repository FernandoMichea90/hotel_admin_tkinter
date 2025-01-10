import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def crear_grafico_barras():
    # Crear una nueva ventana para mostrar el gráfico
    ventana_grafico = tk.Toplevel(window)
    ventana_grafico.title("Gráfico de Barras")

    # Crear figura y ejes
    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange', 'kiwi', 'strawberry', 'grape', 'pineapple', 'mango', 'peach']
    counts = [40, 100, 30, 55, 60, 90, 70, 50, 85, 65]
    bar_labels = ['red', 'blue', 'red', 'orange', 'green', 'red', 'purple', 'yellow', 'orange', 'pink']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', '#32CD32', 'tab:red', '#8A2BE2', 'tab:green', '#FFA500', 'tab:pink']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    # Usar el backend de Tkinter para mostrar el gráfico
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
    canvas.get_tk_widget().pack(fill="both", expand=True)
    canvas.draw()

# Crear ventana principal
window = tk.Tk()
window.title("Ventana Principal")

# Botón para crear gráfico
button = tk.Button(window, text="Mostrar Gráfico", command=crear_grafico_barras)
button.pack(pady=20)

# Iniciar bucle principal
window.mainloop()
