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
        self.dashboard_frame.pack(fill="both",side="left", expand=True, pady=20)

        # LabelFrame para "Ingresos"
        self.ingresos_frame = tk.LabelFrame(self.dashboard_frame, text="Ingresos", padx=10, pady=10)
        self.ingresos_frame.pack(fill="x",side="top", padx=10, pady=10)

       

        # Crear LabelFrames para cada sección
        self.crear_labelframe(self.ingresos_frame, "Reservas", "0", "total_reservas")
        self.crear_labelframe(self.ingresos_frame, "Ingresos", "0", "total_precio")
        self.crear_labelframe(self.ingresos_frame, "Pernoctaciones", "0", "total_noches")
        self.crear_labelframe(self.ingresos_frame, "Promedio Ventas/Noche", "0", "promedio_ventas_por_noche")

        # Llamada inicial para mostrar los datos
        self.mostrar_datos_mes()

    def crear_labelframe(self, parent, titulo, valor_inicial, clave):
        """Crea y distribuye un LabelFrame con un Label de datos."""
        frame = tk.LabelFrame(parent, text=titulo, padx=10, pady=10)
        frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        label = tk.Label(frame, text=valor_inicial, font=("Arial", 12, "bold"))
        label.pack(anchor="center")
        
        setattr(self, f"resultado_{clave}", label)  # Dinámicamente almacena las referencias a los labels

    def formatear_moneda(self, valor):
        """Formatea el valor en pesos chilenos con separador de miles y sin decimales."""
        return f"${valor:,.0f}".replace(",", ".")

    def mostrar_datos_mes(self):
        # Llamar al controller para obtener los resultados
        resultados = obtener_datos_del_mes()

        # Actualizar las etiquetas con los resultados
        self.resultado_total_reservas.config(text=f"{resultados['total_reservas']}")
        self.resultado_total_precio.config(text=f"{self.formatear_moneda(resultados['total_precio'])}")
        self.resultado_total_noches.config(text=f"{resultados['total_noches']}")
        self.resultado_promedio_ventas_por_noche.config(text=f"{self.formatear_moneda(resultados['promedio_ventas_por_noche'])}")
