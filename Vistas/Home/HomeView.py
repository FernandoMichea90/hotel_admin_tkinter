import tkinter as tk
from tkinter import messagebox
from Controller.reserva_controller import obtener_datos_del_mes
from Controller.gasto_controller import obtener_gastos_mes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

color = "white"
class HomeView:
    def __init__(self, master):
        self.master = master
        self.master.focus_set()
        self.screen_width = self.master.winfo_screenwidth()
        self.font_size=int(self.screen_width*0.02)
        self.main_frame = tk.Frame(self.master, padx=10, pady=10, bg="white")
        self.main_frame.pack(fill="both", expand=True)

        # Título
        self.titulo = tk.Label(self.main_frame, text="Resumen de Reservas del Mes", font=("Arial", self.font_size), bg=color)
        self.titulo.pack(side="top", pady=10)

        # Frame principal para el dashboard
        self.dashboard_frame = tk.Frame(self.main_frame, bg=color)
        self.dashboard_frame.pack(fill="both", side="left", expand=True, pady=20)

        # LabelFrame para "Ingresos"
        self.ingresos_frame = tk.LabelFrame(self.dashboard_frame, text="Ingresos", padx=10, pady=10, bg=color)
        self.ingresos_frame.pack(fill="x", side="top", padx=10, pady=10)

        # Crear LabelFrames para cada sección
        self.crear_labelframe(self.ingresos_frame, "Reservas", "0", "total_reservas")
        self.crear_labelframe(self.ingresos_frame, "Ingresos", "0", "total_precio")
        self.crear_labelframe(self.ingresos_frame, "Pernoctaciones", "0", "total_noches")
        self.crear_labelframe(self.ingresos_frame, "Promedio Ventas/Noche", "0", "promedio_ventas_por_noche")

        # LabelFrame para "Gastos"
        self.gastos_frame = tk.Frame(self.dashboard_frame, padx=10, pady=10, bg=color)
        self.gastos_frame.pack(fill="x", side="top", padx=10, pady=10)

        # Crear LabelFrames para cada sección
        self.crear_labelframe(self.gastos_frame, "Total Mes", "0", "total_gastos_mes")
        self.gastos_grafico_frame = tk.LabelFrame(self.dashboard_frame, text="data", padx=10, pady=10, bg=color) 
        self.gastos_grafico_frame.pack(fill="both", side="top")
        

        # Llamada inicial para mostrar los datos
        self.mostrar_datos_mes()

    def crear_labelframe(self, parent, titulo, valor_inicial, clave):
        """Crea y distribuye un LabelFrame con un Label de datos."""
        frame = tk.LabelFrame(parent, text=titulo, padx=10, pady=10, bg=color)
        frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        label = tk.Label(frame, text=valor_inicial, font=("Arial", 12, "bold"),bg=color)
        label.pack(anchor="center")

        setattr(self, f"resultado_{clave}", label)  # Dinámicamente almacena las referencias a los labels

    def formatear_moneda(self, valor):
        """Formatea el valor en pesos chilenos con separador de miles y sin decimales."""
        return f"${valor:,.0f}".replace(",", ".")

    def mostrar_datos_mes(self):
        # Llamar al controller para obtener los resultados
        resultados = obtener_datos_del_mes()
        resultados_gastos = obtener_gastos_mes()

        
        if resultados_gastos['gastos_por_categoria']:
            categorias = []
            totales = []
            
            for gasto in resultados_gastos['gastos_por_categoria']:
                print(gasto['categoria'], gasto['total'])
                categorias.append(gasto['categoria'])
                totales.append(gasto['total'])
            
            # Llamada para crear el gráfico de barras
            self.crear_grafico_barras(categorias, totales)

        # Actualizar las etiquetas con los resultados
        self.resultado_total_reservas.config(text=f"{resultados['total_reservas']}")
        self.resultado_total_precio.config(text=f"{self.formatear_moneda(resultados['total_precio'])}")
        self.resultado_total_noches.config(text=f"{resultados['total_noches']}")
        self.resultado_promedio_ventas_por_noche.config(text=f"{self.formatear_moneda(resultados['promedio_ventas_por_noche'])}")
        self.resultado_total_gastos_mes.config(text=f"{self.formatear_moneda(resultados_gastos['total_gastos_mes'])}")

    def crear_grafico_barras(self, categorias, totales):
        """Crea un gráfico de barras en Tkinter utilizando Matplotlib."""
        # Crear figura y ejes
        fig, ax = plt.subplots(figsize=(3, 2))
        
        total_dividio_miles=[]
        
        for total in totales:
            total_dividio_miles.append(int(total/1000))
        

        # Crear el gráfico de barras
        ax.bar(categorias, total_dividio_miles)

        # Agregar etiquetas y título
        ax.set_xlabel('Categorías')
        ax.set_ylabel('Total Gastado')
        ax.set_title('Gastos por Categoría')
        #fondo del grafico transparente
        # Colocar el gráfico en el interfaz de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.gastos_grafico_frame)  # Gastos frame para mostrar el gráfico
        canvas.get_tk_widget().pack()
        canvas.draw()

        canvas.get_tk_widget().configure(bg='red')

