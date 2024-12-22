from Controller.reserva_controller import ReservasController
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from datetime import datetime
from tkcalendar import DateEntry
from datetime import timedelta
from PIL import Image, ImageTk


NUM_DIAS = 3  # Número de días por bloque

class ReservaOrmView:
    def __init__(self,master):
        self.master = master
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(fill="both", expand=True)
        self.reserva_controller = ReservasController()
        
        #offset
        # Configuración inicial
        self.offset = 0  # Desplazamiento para navegación
        
        # Crear frame para el titulo 
        self.frame_titulo = ctk.CTkFrame(self.frame, corner_radius=10, fg_color="transparent")
        self.frame_titulo.pack(padx=10, pady=10, fill="x", side="top")
        label_titulo = ctk.CTkLabel(self.frame_titulo, text="Reservas", font=("Arial", 14,"bold"),text_color="green")
        label_titulo.pack(side="left",padx=10, pady=10)        
        button_calendario = ctk.CTkButton(self.frame_titulo, text="📆", font=("Arial", 12),command=self.open_reservations_view)
        button_calendario.pack(side="right")
        button_reservas = ctk.CTkButton(self.frame_titulo, text="🛎️", font=("Arial", 12),command=self.open_weekly_view)
        button_reservas.pack(side="right", padx=10)

        # Crear frame body 
        self.frame_body = ctk.CTkFrame(self.frame, corner_radius=10)
        self.frame_body.pack(padx=10, pady=10, fill="both", side="top",expand=True)
    
        self.main_body()
       
    
    
    def main_body(self):
        # Crear Frame Fechas 
        self.frame_fechas = ctk.CTkFrame(self.frame_body,corner_radius=10) 
        self.frame_fechas.pack(padx=10, pady=10,side='top',fill='x')
        
        
        # Etiquetas de entrada de fechas
        self.label_inicio = ctk.CTkLabel(self.frame_fechas, text="Fecha Inicio:", font=("Arial", 12))
        self.label_inicio.pack(side="left",padx=10, pady=10)

        self.entry_inicio = DateEntry (self.frame_fechas, font=("Arial", 12),date_pattern="yyyy-mm-dd")
        self.entry_inicio.pack(side="left",padx=10, pady=10)
        
       
        self.label_fin = ctk.CTkLabel(self.frame_fechas, text="Fecha Fin:", font=("Arial", 12))
        self.label_fin.pack(side="left",padx=10, pady=10)

        self.entry_fin = DateEntry(self.frame_fechas, font=("Arial", 12), date_pattern="yyyy-mm-dd")
        self.entry_fin.set_date(datetime.now() + timedelta(days=1))
        self.entry_fin.pack(side="left",padx=10, pady=10)

        # Botón para filtrar
        self.btn_filtrar = ctk.CTkButton(self.frame_fechas, text="Filtrar", font=("Arial", 12),command=self.filtrar_reservas)
        self.btn_filtrar.pack(side="right",padx=10, pady=10)
        # crear frame para la tabla
        self.table_frame = ctk.CTkFrame(self.frame_body)
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        # Tabla para mostrar las reservas
        self.tree = ttk.Treeview(self.table_frame, columns=("id", "codigo", "nombre", "check_in", "check_out"), show="headings", selectmode="browse")
        self.tree.heading("id", text="ID")
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("check_in", text="Check-In")
        self.tree.heading("check_out", text="Check-Out")

        # Crear scrollbar vertical
        vsb = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")

        # Crear scrollbar horizontal
        hsb = ttk.Scrollbar(self.table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=hsb.set)
        hsb.pack(side="bottom", fill="x")

        self.tree.pack(fill="both", expand=True)

        # Llenar la tabla con las reservas
        reservas_listas = self.reserva_controller.listar_reservas_orm()
        self.fill_table(reservas_listas)
        

    def clean_frame_body(self):
        for widget in self.frame_body.winfo_children():
            widget.destroy()
            
    def open_reservations_view(self):
        self.clean_frame_body()
        self.main_body()
    
    def open_weekly_view(self):
        self.clean_frame_body()
        self.weekly_view()

    def weekly_view(self):
        # Crear un frame para el header
        self.frame_header = ctk.CTkFrame(self.frame_body)
        self.frame_header.pack(pady=10, padx=10, side="top", fill="x")
        #crear un frame para el body 
        self.frame_main_body = ctk.CTkFrame(self.frame_body)
        self.frame_main_body.pack(pady=10, padx=10, side="top", fill="both", expand=True)
        # Agregar un título a la vista
        label_titulo = ctk.CTkLabel(self.frame_header, text="Vista Semanal", font=("Arial", 14, "bold"), text_color="green")
        label_titulo.pack(padx=10, pady=10, side="left")
        
        # Agregar un boton hacia atras y adelante
        button_adelante = ctk.CTkButton(self.frame_header, text="➡️", font=("Arial", 12),command=lambda: self.update_week_table(1))
        button_adelante.pack(side="right", padx=10)
        button_atras = ctk.CTkButton(self.frame_header, text="⬅️", font=("Arial", 12),command=lambda: self.update_week_table(-1))
        button_atras.pack(side="right", padx=10)
        
        self.start_date = datetime.now()  # Fecha inicial de la tabla
        self.create_week_table(self.start_date)
        
        
    
    
    def create_week_table(self, start_date):
        for widget in self.frame_main_body.winfo_children():
            widget.destroy()
        # Generar fechas desde hoy hasta los próximos 7 días
        fechas = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]

        # Lista de habitaciones
        habitaciones = list(range(21, 30)) + list(range(31, 37))
        
        # Datos ficticios de ocupación (puedes reemplazar con datos reales)
        ocupaciones = {
            21: {"2024-12-23": "Juan", "2024-12-24": "Ana María Specter Litt"},
            22: {"2024-12-26": "Luis"},
            31: {"2024-12-28": "Carlos", "2024-12-29": "María"},
        }
                
                # Datos ficticios de ocupación con estado de pago
        ocupaciones = {
            21: {
                "2024-12-23": {"cliente": "Juan", "pagado": True},
                "2024-12-24": {"cliente": "Ana María Specter Litt", "pagado": False}
            },
            22: {
                "2024-12-26": {"cliente": "Luis", "pagado": True}
            },
            31: {
                "2024-12-28": {"cliente": "Carlos", "pagado": False},
                "2024-12-29": {"cliente": "María", "pagado": True}
            },
        }
        # Crear un Frame para la tabla
        frame_week_table = ctk.CTkFrame(self.frame_main_body)
        frame_week_table.pack(pady=10, padx=10,side='left', fill="both", expand=True)

        # Agregar scroll al frame
        # crear el canvas
        canvas = tk.Canvas(frame_week_table)
        canvas.pack(fill="both", expand=True)
        
        #agrergar el scrollbar
        scrollbar = ttk.Scrollbar(frame_week_table,orient="horizontal" , command=canvas.xview,style="TScrollbar")
        scrollbar.pack(side="bottom", fill="x")
        
        #configurar el canvas
        canvas.configure(xscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas_frame = ctk.CTkFrame(canvas)
        canvas.create_window((0,0), window=canvas_frame, anchor="nw")
        
            # Cargar la imagen del emoji
        try:
            emoji_image = Image.open("image.png")  # Asegúrate de tener el archivo image.png
            emoji_image = emoji_image.resize((9, 9))  # Ajustar tamaño de la imagen
            emoji_photo = ImageTk.PhotoImage(emoji_image)
        except FileNotFoundError:
            print("La imagen 'image.png' no se encuentra.")
            return
                    
        # Crear encabezados de columnas (fechas)
        tk.Label(canvas_frame, text="Habitación", borderwidth=1, relief="solid", width=15).grid(row=0, column=0)
        for col, fecha in enumerate(fechas, start=1):
            tk.Label(canvas_frame, text=fecha, borderwidth=1, relief="solid", width=35).grid(row=0, column=col)

        # Rellenar filas con habitaciones y ocupaciones
        for row, habitacion in enumerate(habitaciones, start=1):
            # Columna de habitación
            tk.Label(canvas_frame, text=f"Habitación {habitacion}", borderwidth=1, relief="solid", width=15).grid(row=row, column=0)
            # Columnas de ocupación
            for col, fecha in enumerate(fechas, start=1):
                ocupacion = ocupaciones.get(habitacion, {}).get(fecha, "")  # Obtener cliente o vacío
                if ocupacion:
                    cliente = ocupacion["cliente"]
                    pagado = ocupacion["pagado"]
                    label=tk.Label(canvas_frame,text=cliente,image=emoji_photo,compound="left", borderwidth=1, relief="solid", width=200,font=("Segoe UI Emoji", 9))
                    label.grid(row=row, column=col,sticky="nsew")
                    label.image = emoji_photo  # Esto mantiene la referencia
                else:
                    tk.Label(canvas_frame, text="", borderwidth=1, relief="solid", width=35).grid(row=row, column=col,sticky="nsew")
                

    def update_week_table(self, days):
        self.start_date += timedelta(days=days)  # Ajustar la fecha inicial en ±1 día
        self.create_week_table(self.start_date)         
                        
    def fill_table(self, reservas):
        """Llena la tabla con los datos de las reservas."""
        # Limpiar la tabla antes de insertar nuevas reservas
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar las reservas en la tabla
        for reserva in reservas:
            self.tree.insert("", tk.END, values=(reserva.id, reserva.codigo, f"{reserva.nombre} {reserva.apellido}", reserva.check_in, reserva.check_out))

    def filtrar_reservas(self):
        """Filtra las reservas por fecha de check-in y check-out."""
        inicio = self.entry_inicio.get().strip()
        fin = self.entry_fin.get().strip()
            
            # Validar que los campos no estén vacíos
        if not inicio or not fin:
            messagebox.showerror("Error", "Ambas fechas deben ser ingresadas.")
            return

         # Validar formato de las fechas
        try:
            fecha_inicio = datetime.strptime(inicio, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fin, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Las fechas deben tener el formato YYYY-MM-DD.")
            return

        # Validar que check_out no sea menor o igual que check_in
        if fecha_fin <= fecha_inicio:
            messagebox.showerror("Error", "La fecha de check-out debe ser mayor que la fecha de check-in.")
            return

        # Si todo está correcto, filtrar las reservas
        reservas_filtradas = self.reserva_controller.listar_reservas_por_fecha(inicio, fin)
        self.fill_table(reservas_filtradas)
            
        reservas_filtradas = self.reserva_controller.listar_reservas_por_fecha(inicio, fin)
        self.fill_table(reservas_filtradas)