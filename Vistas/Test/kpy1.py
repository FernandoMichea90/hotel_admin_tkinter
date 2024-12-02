import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para actualizar el KPI dinámicamente
def actualizar_kpi():
    valor_actual.set("75%")  # Aquí podrías usar datos en tiempo real
    root.after(5000, actualizar_kpi)  # Actualiza cada 5 segundos

# Configuración de la ventana principal
root = tk.Tk()
root.title("KPI Dashboard")
root.geometry("400x300")

# Frame principal
frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Indicador del KPI
ttk.Label(frame, text="Tasa de Éxito:", font=("Arial", 14)).pack(anchor="w")
valor_actual = tk.StringVar(value="75%")
ttk.Label(frame, textvariable=valor_actual, font=("Arial", 20, "bold"), foreground="green").pack(anchor="w")

# Gráfico de barras
fig = Figure(figsize=(4, 2), dpi=100)
ax = fig.add_subplot(111)
ax.bar(["Enero", "Febrero", "Marzo"], [70, 80, 75], color="skyblue")
ax.set_title("Progreso Mensual")
ax.set_ylim(0, 100)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

# Llama a la función de actualización
actualizar_kpi()

# Ejecuta la aplicación
root.mainloop()
