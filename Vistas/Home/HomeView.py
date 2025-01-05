import tkinter as tk
from tkinter import messagebox
from Controller.reserva_controller import obtener_datos_del_mes

class HomeView:
    def __init__(self, master):
        self.master = master
        self.master.focus_set()
        self.main_frame = tk.Frame(self.master, padx=10, pady=10)
        self.main_frame.pack(fill="both", expand=True)
        
        
        # Agregar título
        self.titulo = tk.Label(self.main_frame, text="Resumen de Reservas del Mes", font=("Arial", 15))
        self.titulo.pack(side="top", pady=10)

       

        # Etiquetas para mostrar los resultados
        self.resultado_reservas = tk.Label(self.main_frame, text="Total Reservas: 0")
        self.resultado_reservas.pack(side="top", pady=5)

        self.resultado_precio = tk.Label(self.main_frame, text="Total Precio: $0")
        self.resultado_precio.pack(side="top", pady=5)

        self.resultado_noches = tk.Label(self.main_frame, text="Total Noches: 0")
        self.resultado_noches.pack(side="top", pady=5)

        self.resultado_promedio = tk.Label(self.main_frame, text="Promedio Ventas/Noche: $0")
        self.resultado_promedio.pack(side="top", pady=5)
        
        self.mostrar_datos_mes()

    def mostrar_datos_mes(self):
        # Llamar al controller para obtener los resultados
        resultados = obtener_datos_del_mes()

        # Actualizar las etiquetas con los resultados
        self.resultado_reservas.config(text=f"Total Reservas: {resultados['total_reservas']}")
        self.resultado_precio.config(text=f"Total Precio: ${resultados['total_precio']}")
        self.resultado_noches.config(text=f"Total Noches: {resultados['total_noches']}")
        self.resultado_promedio.config(text=f"Promedio Ventas/Noche: ${resultados['promedio_ventas_por_noche']:.2f}")