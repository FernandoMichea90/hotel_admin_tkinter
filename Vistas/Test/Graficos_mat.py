import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Crear ventana principal
root = tk.Tk()
root.title("Dashboard del Hotel")
root.geometry("800x600")

# Función para mostrar gráficos
def mostrar_grafico(tipo):
    fig.clear()  # Limpia cualquier gráfico previo
    ax = fig.add_subplot(111)

    if tipo == "barras":
        # Gráfico de barras: Ocupación mensual
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
        ocupacion = [75, 90, 85, 70, 95]
        ax.bar(meses, ocupacion, color="skyblue")
        ax.set_title("Ocupación Mensual (%)")
        ax.set_ylabel("Porcentaje")

    elif tipo == "lineas":
        # Gráfico de líneas: Ingresos mensuales
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
        ingresos = [10000, 15000, 12000, 18000, 20000]
        ax.plot(meses, ingresos, marker="o", color="green", linestyle="--")
        ax.set_title("Ingresos Mensuales ($)")
        ax.set_ylabel("Ingresos en USD")

    elif tipo == "pastel":
        # Gráfico de pastel: Distribución de clientes
        nacionalidades = ["Nacionales", "Extranjeros"]
        distribucion = [60, 40]
        ax.pie(distribucion, labels=nacionalidades, autopct="%1.1f%%", colors=["gold", "lightcoral"])
        ax.set_title("Distribución de Clientes")

    canvas.draw()  # Redibuja el gráfico en el canvas

# Configurar área de gráficos
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Crear botones para cambiar gráficos
frame_botones = ttk.Frame(root)
frame_botones.pack(side=tk.BOTTOM, fill=tk.X)

btn_barras = ttk.Button(frame_botones, text="Gráfico de Barras", command=lambda: mostrar_grafico("barras"))
btn_barras.pack(side=tk.LEFT, padx=10, pady=5)

btn_lineas = ttk.Button(frame_botones, text="Gráfico de Líneas", command=lambda: mostrar_grafico("lineas"))
btn_lineas.pack(side=tk.LEFT, padx=10, pady=5)

btn_pastel = ttk.Button(frame_botones, text="Gráfico de Pastel", command=lambda: mostrar_grafico("pastel"))
btn_pastel.pack(side=tk.LEFT, padx=10, pady=5)

# Mostrar la ventana principal
root.mainloop() 