import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Datos de ejemplo
data = {
    'check_in': ['martes, 1 de octubre de 2024', 'sábado, 5 de octubre de 2024', 'sábado, 5 de octubre de 2024', 'sábado, 5 de octubre de 2024'],
    'checkout': ['02-oct', '06-oct', '06-oct', '06-oct'],
    'nombre': ['Juan', 'Daniela', 'Karina', 'Mauricio'],
    'apellido': ['Madaria', 'Prado', 'Espinoza', 'Toledo'],
    'Pais': ['Chile', 'Chile', 'Chile', 'Chile'],
    'Precio': [45000, 73000, 59000, 52000],
    'Noches': [1, 1, 1, 1],
    'Estado_pago': ['Pagado', 'Pendiente', 'Pendiente', 'Pendiente'],
}

df = pd.DataFrame(data)

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Dashboard de Reservas")

# Crear el frame para los gráficos
frame_graficos = ttk.Frame(root)
frame_graficos.grid(row=0, column=0, padx=20, pady=20)

# Función para crear un gráfico de barras de precios por cliente
def crear_grafico_barras():
    fig, ax = plt.subplots()
    ax.bar(df['nombre'], df['Precio'], color='skyblue')
    ax.set_title('Precios por Cliente')
    ax.set_xlabel('Cliente')
    ax.set_ylabel('Precio')
    return fig

# Función para crear un gráfico lineal de precios por fecha de check-in
def crear_grafico_lineal():
    fig, ax = plt.subplots()
    ax.plot(df['check_in'], df['Precio'], marker='o', color='green')
    ax.set_title('Evolución de Precios por Fecha de Check-In')
    ax.set_xlabel('Fecha de Check-In')
    ax.set_ylabel('Precio')
    ax.set_xticklabels(df['check_in'], rotation=45, ha='right')
    return fig

# Función para crear un gráfico circular de estado de pago
def crear_grafico_circular():
    estado_pago_counts = df['Estado_pago'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(estado_pago_counts, labels=estado_pago_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    ax.set_title('Distribución de Estado de Pago')
    return fig

# Función para crear un gráfico KPI de total de reservas y precio promedio
def crear_grafico_kpi():
    total_reservas = len(df)
    precio_promedio = df['Precio'].mean()
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.text(0.5, 0.6, f"Total de Reservas: {total_reservas}", fontsize=14, ha='center')
    ax.text(0.5, 0.4, f"Precio Promedio: ${precio_promedio:.2f}", fontsize=14, ha='center')
    return fig

# Función para crear un gráfico de barras apiladas de noches por estado de pago
def crear_grafico_barras_apiladas():
    noches_estado_pago = df.groupby('Estado_pago')['Noches'].sum()
    fig, ax = plt.subplots()
    noches_estado_pago.plot(kind='bar', stacked=True, color=['#ff9999', '#66b3ff'], ax=ax)
    ax.set_title('Noches por Estado de Pago')
    ax.set_xlabel('Estado de Pago')
    ax.set_ylabel('Total Noches')
    return fig

# Función para mostrar un gráfico en la ventana de Tkinter
def mostrar_grafico(fig, row, col):
    canvas = FigureCanvasTkAgg(fig, master=frame_graficos)
    canvas.draw()
    canvas.get_tk_widget().grid(row=row, column=col)

# Mostrar los gráficos en la interfaz
mostrar_grafico(crear_grafico_barras(), 0, 0)
mostrar_grafico(crear_grafico_lineal(), 0, 1)
mostrar_grafico(crear_grafico_circular(), 1, 0)
mostrar_grafico(crear_grafico_kpi(), 1, 1)
mostrar_grafico(crear_grafico_barras_apiladas(), 2, 0)

# Iniciar la aplicación
root.mainloop()
