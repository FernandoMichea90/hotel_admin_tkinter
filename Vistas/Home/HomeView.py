import tkinter as tk
from tkinter import messagebox
from Controller.reserva_controller import obtener_datos_del_mes

class HomeView:
    def __init__(self, master):
        self.master = master
        self.master.focus_set()
        self.main_frame = tk.Frame(self.master, padx=10, pady=10)
        self.main_frame.pack(fill="both", expand=True)
        
        # Título
        self.titulo = tk.Label(self.main_frame, text="Resumen de Reservas del Mes", font=("Arial", 15))
        self.titulo.pack(side="top", pady=10)
        
        # Frame principal para el dashboard
        self.dashboard_frame = tk.Frame(self.main_frame)
        self.dashboard_frame.pack(fill="both", expand=True, pady=20)

        # Crear LabelFrames para cada sección
        self.frame_reservas = tk.LabelFrame(self.dashboard_frame, text="Reservas", padx=10, pady=10)
        self.frame_reservas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.resultado_reservas = tk.Label(self.frame_reservas, text="0", font=("Arial", 12, "bold"))
        self.resultado_reservas.pack()

        self.frame_precio = tk.LabelFrame(self.dashboard_frame, text="Ingresos", padx=10, pady=10)
        self.frame_precio.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.resultado_precio = tk.Label(self.frame_precio, text="0", font=("Arial", 12, "bold"))
        self.resultado_precio.pack()

        self.frame_noches = tk.LabelFrame(self.dashboard_frame, text="Pernoctaciones", padx=10, pady=10)
        self.frame_noches.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.resultado_noches = tk.Label(self.frame_noches, text="0", font=("Arial", 12, "bold"))
        self.resultado_noches.pack()

        self.frame_promedio = tk.LabelFrame(self.dashboard_frame, text="Promedio Ventas/Noche", padx=10, pady=10)
        self.frame_promedio.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        self.resultado_promedio = tk.Label(self.frame_promedio, text="0", font=("Arial", 12, "bold"))
        self.resultado_promedio.pack()

        # Llamada inicial para mostrar los datos
        self.mostrar_datos_mes()

    def formatear_moneda(self, valor):
        """Formatea el valor en pesos chilenos con separador de miles y coma para decimales."""
        return f"${valor:,.0f}".replace(",", ".")

    def mostrar_datos_mes(self):
        # Llamar al controller para obtener los resultados
        resultados = obtener_datos_del_mes()

        # Actualizar las etiquetas con los resultados, sin texto adicional
        self.resultado_reservas.config(text=f"{resultados['total_reservas']}")
        self.resultado_precio.config(text=f"{self.formatear_moneda(resultados['total_precio'])}")
        self.resultado_noches.config(text=f"{resultados['total_noches']}")
        self.resultado_promedio.config(text=f"{self.formatear_moneda(resultados['promedio_ventas_por_noche'])}")
