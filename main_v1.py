import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import customtkinter as ctk
from Vistas.Pasajeros.crear import crear_reservas
from Vistas.Reservas.reserva_view import  ReservaView
from Vistas.Reservas.edit_reserva import editar_reserva
from Vistas.Reservas.reserva_orm_view import ReservaOrmView
from Utils.Database import Base, engine
from Vistas.Gastos.gastos_view import VistaGasto
from Vistas.Home.HomeView import HomeView


Base.metadata.create_all(bind=engine)


# Clase para la aplicación principal
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Reservas")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.geometry(f"{int(self.screen_width * 0.8)}x{int(self.screen_height * 0.8)}+50+50")
        self.title("Sistema de Reservas")
    
        # Configuración de la ventana principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)  # La columna derecha será expansible

        # Crear el panel izquierdo (menú)
        self.menu_frame = tk.Frame(self, bg="green", width=200)
        self.menu_frame.grid(row=0, column=0, sticky="ns")  # Ocupa toda la altura
        self.menu_frame.grid_propagate(False)  # Evitar que el tamaño cambie    

        # Crear el panel derecho (información)
        self.content_frame = tk.Frame(self, bg="white")
        self.content_frame.grid(row=0, column=1, sticky="nsew")  # Expandible

        # Configurar el contenido de los paneles
        self.configurar_menu()
        self.mostrar_home()

    @staticmethod
    def conectar_db():
        """Conectar a la base de datos."""
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="123",
            database="hotel_ecomusic"
        )

    def  mostrar_reservas_dos(self):
        """Mostrar contenido del panel derecho para Reservas."""
        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        reserva_view = ReservaView(self.content_frame)  # Crear una instancia de ReservaView
        reserva_view.mostrar_reservas() 
    def mostrar_orm_reservas(self):
        """Mostrar contenido del panel derecho para Reservas."""
        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        ReservaOrmView(self.content_frame)
        
    def edit_reserva(self,id):
        """Editar una reserva."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        rv=ReservaView(self.content_frame)
        rv.edit_reserva(id)
    
    
    
    def mostrar_reserva(self,id):
        """Mostrar la información de una reserva."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        rv=ReservaView(self.content_frame)
        rv.mostrar_reserva(id)  
    def mostrar_gastos(self):
        """Mostrar contenido del panel derecho para Gastos."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        rv=VistaGasto(self.content_frame)
        
    
    def configurar_menu(self):
        """Configurar botones del menú en el panel izquierdo."""
        botones = [
            ("🏠 Home", self.mostrar_home),
            ("📋 Hoy", self.mostrar_reservas_dos),
            ("📅 Reservas", self.mostrar_orm_reservas),
            ("💸 Gastos", self.mostrar_gastos)
            
        ]

        for text, command in botones:
            button = tk.Button(
                self.menu_frame,
                text=text,
                command=command,
                bg="green",
                fg="white",
                font=("Arial", 12),
                bd=0,
                activebackground="#005f00",
                activeforeground="white",
                anchor='w'
            )
            button.pack(fill="x", pady=5, padx=20)

    def mostrar_home(self):
        """Mostrar contenido del panel derecho para Home."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()  # Limpiar el contenido actual

        HomeView(self.content_frame)


    def mostrar_reservas(self):
        """Mostrar contenido del panel derecho para Reservas."""
        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        
        # Contenedor para la etiqueta y el botón (como un div)
        header_frame = tk.Frame(self.content_frame, bg="white")
        header_frame.pack(fill="x", pady=20,padx=20)

        # Etiqueta (Texto a la izquierda)
        label = tk.Label(
            header_frame,
            text="Gestión de Reservas",
            font=("Arial", 18,"bold"),
            bg="white",
            fg="green"
        )
        label.pack(side="left", padx=10)  # Alineado a la izquierda

        button = ctk.CTkButton(
            header_frame,
            text="Nuevo",
            font=("Arial",18),
            fg_color="#4CAF50",  # Color de fondo verde
            hover_color="#45a049",  # Color cuando se pasa el cursor sobre el botón
            width=100,  # Ancho del botón
            height=40,  # Alto del botón
            border_width=0,  # Sin borde
            corner_radius=10,  # Bordes redondeados
            text_color="#ffffff",
            command= lambda: crear_reservas(self=self)
            
        )
        button.pack(side="right", padx=10)  # Alineado a la derecha

        # Frame para contener el Canvas y el Scrollbar
        contenedor_scroll = tk.Frame(self.content_frame, bg="white")
        contenedor_scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # Crear el Canvas
        canvas = tk.Canvas(contenedor_scroll, bg="white")
        canvas.pack(side="left", fill="both", expand=True)

        # Agregar Scrollbar vertical
        scrollbar = ttk.Scrollbar(contenedor_scroll, orient="vertical", command=canvas.yview,width=20)
        scrollbar.pack(side="right", fill="y")

        # Conectar el Canvas con la Scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Frame dentro del Canvas para las tarjetas
        reservas_frame = tk.Frame(canvas, bg="white")
        canvas.create_window((0,0), window=reservas_frame, anchor="nw")


        # Cargar datos desde la base de datos
        try:
            conn = App.conectar_db()
            cursor = conn.cursor()
            query = """
                SELECT codigo, nombre, apellido, habitacion, precio
                FROM reservas_tkinter
            """
            cursor.execute(query)
            registros = cursor.fetchall()

            # Insertar registros como tarjetas
            for reserva in registros:
                self.mostrar_card(reserva, reservas_frame)

        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar los registros: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():  
                conn.close()

        # Hacer que el scroll funcione con la rueda del ratón
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * int(e.delta / 120), "units"))

   
    def mostrar_card(self, reserva, parent_frame):
        """Crear y mostrar una tarjeta con la información de una reserva."""
        card_frame = tk.Frame(parent_frame, bg="#f7f7f7", bd=0, relief="solid", padxr=10, pady=10)
        card_frame.pack(fill="x", pady=10)

        nombre = f"{reserva[1]} {reserva[2]}"
        habitacion = f"Habitación: {reserva[3]}"
        precio = f"Precio: {reserva[4]}"
        codigo = f"Código: {reserva[0]}"

        # Frame para la parte izquierda
        left_frame = tk.Frame(card_frame, bg="#f7f7f7")
        left_frame.pack(side="left", fill="y", padx=10)

        # Mostrar los datos de la reserva en el lado izquierdo
        tk.Label(left_frame, text=codigo, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")
        tk.Label(left_frame, text=nombre, font=("Arial", 12, "bold"), bg="#f7f7f7").pack(anchor="w")
        tk.Label(left_frame, text=habitacion, font=("Arial", 10), bg="#f7f7f7").pack(anchor="w")

        # Frame para la parte derecha (precio y botones)
        right_frame = tk.Frame(card_frame, bg="#f7f7f7")
        right_frame.pack(side="right", padx=10)

        # Mostrar el precio en el lado derecho
        tk.Label(right_frame, text=precio, font=("Arial", 12, "bold"), bg="#f7f7f7").pack(anchor="e")

        # Agregar botones Editar y Borrar en la parte derecha
        button_frame = tk.Frame(right_frame, bg="#f7f7f7")
        button_frame.pack(pady=10, anchor="e")

        # Botón Editar
        edit_button = tk.Button(
            button_frame,
            text="✏️",
            font=("Arial", 10),
            bg="lightblue",
            fg="black",
            activebackground="lightblue",
            cursor="hand2",
        )
        edit_button.pack(side="left", padx=5)

        # Botón Borrar
        delete_button = tk.Button(
            button_frame,
            text="❌",
            font=("Arial", 10),
            bg="red",
            fg="white",
            activebackground="#ff4d4d",
            cursor="hand2",
        )
        delete_button.pack(side="left", padx=5)

    def actualizar_ruta(self, ruta):
        """Actualizar la barra de navegación (ruta)"""
        # Crear el Frame para la barra de navegación (breadcrumb) solo cuando se necesite
        breadcrumb_frame = tk.Frame(self.content_frame, bg="white")
        breadcrumb_frame.pack(fill="x", pady=10)

        # Limpiar la ruta actual (si ya existe alguna barra de navegación en breadcrumb_frame)
        for widget in breadcrumb_frame.winfo_children():
            widget.destroy()

        # Crear las etiquetas de la ruta
        ruta_labels = [tk.Label(breadcrumb_frame, text=etapa, font=("Arial", 12), bg="white", fg="green") for etapa in ruta]
        
        for i, label in enumerate(ruta_labels):
            label.pack(side="left", padx=5)
            if i < len(ruta_labels) - 1:
                # Añadir ">" entre las etiquetas
                separator = tk.Label(breadcrumb_frame, text=">", font=("Arial", 12), bg="white", fg="green")
                separator.pack(side="left", padx=5)

