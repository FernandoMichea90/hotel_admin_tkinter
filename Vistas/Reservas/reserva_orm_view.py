from Controller.reserva_controller import ReservasController
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from datetime import datetime
from tkcalendar import DateEntry
from datetime import timedelta
from PIL import Image, ImageTk
from Vistas.Reservas.edit_reserva import editar_reserva


NUM_DIAS = 4  # Número de días por bloque

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
        #crear frame para  buscar, editar y eliminar 
        self.frame_botones = ctk.CTkFrame(self.frame_body)
        # crear input para buscar
        self.entry_buscar = ctk.CTkEntry(self.frame_botones, font=("Arial", 12))
        self.entry_buscar.pack(side="left", padx=10, pady=10)
        # crear boton para buscar
        self.btn_buscar = ctk.CTkButton(self.frame_botones, text="Buscar", font=("Arial", 12))
        self.btn_buscar.pack(side="left", padx=10, pady=10)
        # crear boton para editar
        self.btn_editar = ctk.CTkButton(self.frame_botones, text="Editar", font=("Arial", 12),command=self.edit_row)
        self.btn_editar.pack(side="left", padx=10, pady=10)
        # crear boton para eliminar
        self.btn_eliminar = ctk.CTkButton(self.frame_botones, text="Eliminar", font=("Arial", 12),command=self.delete_row)
        self.btn_eliminar.pack(side="left", padx=10, pady=10)
        self.frame_botones.pack(padx=10, pady=10, side="top", fill="x")
        
        
        # crear frame para la tabla
        self.table_frame = ctk.CTkFrame(self.frame_body,bg_color="purple")
        self.table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        # Tabla para mostrar las reservas
        self.tree = ttk.Treeview(self.table_frame, columns=("id", "codigo", "nombre", "check_in", "check_out", "habitacion", "estado", "precio", "transbank", "facturado", "tipo_documento", "folio_factura"), show="headings", selectmode="browse")
        self.tree.heading("id", text="ID")
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("check_in", text="Check-In")
        self.tree.heading("check_out", text="Check-Out")
        self.tree.heading("habitacion", text="Habitación")
        self.tree.heading("estado", text="Estado")
        self.tree.heading("precio", text="Precio")
        self.tree.heading("transbank", text="Transbank")
        self.tree.heading("facturado", text="Facturado")
        self.tree.heading("tipo_documento", text="Tipo Documento")
        self.tree.heading("folio_factura", text="Folio Factura")

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
        
    # funcion para actualizar la tabla
    # la funcion puede ser una funcion lambda
    def update_table(self):
        # Limpiar la tabla antes de insertar nuevas reservas
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar las reservas en la tabla
        reservas_listas = self.reserva_controller.listar_reservas_orm()
        self.fill_table(reservas_listas)
        
    
        
    def edit_row(self):
        """Abre una ventana para editar la fila seleccionada."""
        # Obtener la fila seleccionada
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor selecciona una fila para editar.")
            return

        # Obtener los valores de la fila seleccionada
        values = self.tree.item(selected_item, "values")
        print(values)
        # Crear una ventana para editar la fila
        edit_window = tk.Toplevel(self.master)
        edit_window.title("Editar Reserva")
        # crear frame para el contenido
        frame_content_window = ctk.CTkFrame(edit_window, corner_radius=10)
        frame_content_window.pack(padx=10, pady=10, fill="both", expand=True)
        # Llamar a la función para editar la reserva
        editar_reserva(self,int(values[0]), frame_content_window,edit_window,self.update_table)
    
    # eliminar una reserva
    def delete_row(self):
        """Elimina la fila seleccionada."""
        # Obtener la fila seleccionada
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor selecciona una fila para eliminar.")
            return

        # Obtener el ID de la fila seleccionada
        reserva_id = self.tree.item(selected_item, "values")[0]
        # Confirmar si se desea eliminar la reserva
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar esta reserva?")
        if confirmar:
            # Eliminar la reserva
            resultado = self.reserva_controller.delete_reserva(reserva_id)
            if resultado["status"] == "success":
                messagebox.showinfo("Éxito", resultado["message"])
                self.update_table()
            else:
                messagebox.showerror("Error", resultado["message"])
      
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
        self.frame_header = ctk.CTkFrame(self.frame_body,bg_color="pink")
        self.frame_header.pack(pady=10, padx=10, side="top", fill="x")
        #crear un frame para el body 
        self.frame_main_body = ctk.CTkFrame(self.frame_body)
        self.frame_main_body.pack(pady=10, padx=10, side="top", fill="both", expand=True)
        # Agregar un título a la vista
        label_titulo = ctk.CTkLabel(self.frame_header, text="Vista Semanal", font=("Arial", 14, "bold"), text_color="green")
        label_titulo.pack(padx=10, pady=10, side="left")
        
        # Agregar un boton hacia atras y adelante
        button_adelante = ctk.CTkButton(self.frame_header, text="➡️", font=("Arial", 12),command=lambda: self.update_week_table(NUM_DIAS))
        button_adelante.pack(side="right", padx=10)
        button_atras = ctk.CTkButton(self.frame_header, text="⬅️", font=("Arial", 12),command=lambda: self.update_week_table(-NUM_DIAS))
        button_atras.pack(side="right", padx=10)
        button_calendario = ctk.CTkButton(self.frame_header, text="📆", font=("Arial", 12),command=lambda:self.date_selection(),width=10)
        button_calendario.pack(side="right")
        
        #datepicker
        self.date_picker = DateEntry(self.frame_header, font=("Arial", 12), date_pattern="dd-mm-yyyy")
        self.date_picker.pack(side="right", padx=10)
          # Asocia un evento onchange al DateEntry
        self.date_picker.bind("<<DateEntrySelected>>", self.date_selection)
        
        self.start_date = datetime.now()-timedelta(days=1)  # Fecha inicial de la tabla
        self.create_week_table(self.start_date)
        
        
   
    def date_selection(self,event=None):
        #obtener la fecha seleccionada
        date = self.date_picker.get_date()
        #mostran en una ventana emergente
        self.start_date = date
        self.create_week_table(self.start_date)
        
        
    
    def create_week_table(self, start_date):
        for widget in self.frame_main_body.winfo_children():
            widget.destroy()
        # Generar fechas desde hoy hasta los próximos 7 días
        fechas = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(NUM_DIAS)]
        # Lista de habitaciones
        habitaciones = list(range(21, 30)) + list(range(31, 37))    
        # la fecha de inicio y fin debe estar en formato YYYY-MM-DD
        inicio = start_date.strftime("%Y-%m-%d")
        fin = (start_date + timedelta(days=NUM_DIAS - 1)).strftime("%Y-%m-%d")
        ocupaciones = self.reserva_controller.obtener_ocupaciones_por_fecha(inicio, fin)
        # Crear un Frame para lreserva_controllera tabla
        frame_week_table = ctk.CTkFrame(self.frame_main_body, bg_color="red")
        frame_week_table.pack(fill="both", expand=True)

        # Frame contenedor para Canvas y scrollbar vertical
        canvas_frame = tk.Frame(frame_week_table)
        canvas_frame.pack(side="top", fill="both", expand=True)
        # Agregar scroll al frame
        # crear el canvas
        canvas = tk.Canvas(canvas_frame)
        canvas.pack(side="left",fill="both",expand=True)
        #agrergar el scrollbar
        scrollbar_vertical = ttk.Scrollbar(canvas_frame,orient="vertical" , command=canvas.yview)
        scrollbar_vertical.pack(side="right", fill="y")
        
        scrollbar_horizontal = ttk.Scrollbar(frame_week_table,orient="horizontal" , command=canvas.xview)
        scrollbar_horizontal.pack(side="bottom", fill="x")

        #configurar el canvas
        canvas.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas_frame = ctk.CTkFrame(canvas, bg_color="blue")
        canvas.create_window((0,0), window=canvas_frame, anchor="nw")
        
            # Cargar la imagen del emoji
        try:
            emoji_image = Image.open("image.png")  # Asegúrate de tener el archivo image.png
            emoji_image = emoji_image.resize((9, 9))  # Ajustar tamaño de la imagen
            emoji_photo = ImageTk.PhotoImage(emoji_image)
            red_image = Image.open("utils/img/red.png")  # Asegúrate de tener el archivo image.png
            red_image = red_image.resize((9, 9))  # Ajustar tamaño de la imagen
            red_photo = ImageTk.PhotoImage(red_image)
            green_image = Image.open("utils/img/green.png")  # Asegúrate de tener el archivo image.png
            green_image = green_image.resize((9, 9))  # Ajustar tamaño de la imagen
            green_photo = ImageTk.PhotoImage(green_image)
            yellow_image = Image.open("utils/img/yellow.png")  # Asegúrate de tener el archivo image.png
            yellow_image = yellow_image.resize((9, 9))  # Ajustar tamaño de la imagen
            yellow_photo = ImageTk.PhotoImage(yellow_image)
        except FileNotFoundError:
            print("La imagen 'image.png' no se encuentra.")
            return
                    
        # Crear encabezados de columnas (fechas)
        tk.Label(canvas_frame, text="Habitación", borderwidth=1, relief="solid", width=15,height=2).grid(row=0, column=0)
        columna_final=NUM_DIAS+1
        for col, fecha in enumerate(fechas, start=1):
            tk.Label(canvas_frame, text=fecha, borderwidth=1, relief="solid", width=35,height=2).grid(row=0, column=col)
        tk.Label(canvas_frame, text="Habitación", borderwidth=1, relief="solid", width=15,height=2).grid(row=0, column=columna_final)

        
        # Rellenar filas con habitaciones y ocupaciones
        for row, habitacion in enumerate(habitaciones, start=1):
            # Columna de habitación
            tk.Label(canvas_frame, text=f"{habitacion}", borderwidth=1, relief="solid", width=15,height=2).grid(row=row, column=0)
            # Columnas de ocupación
            for col, fecha in enumerate(fechas, start=1):
                ocupacion = ocupaciones.get(habitacion, {}).get(fecha, "")  # Obtener cliente o vacío
                if ocupacion:
                    cliente = ocupacion["cliente"]
                    pagado = ocupacion["pagado"]
                    if pagado:
                        _photo = green_photo
                    else:
                        if fecha == datetime.now().strftime("%Y-%m-%d"):
                            _photo = red_photo
                        else:
                            _photo = yellow_photo
                    label=tk.Label(canvas_frame,text=cliente,image=_photo,compound="left", borderwidth=1, relief="solid", width=200,font=("Segoe UI Emoji", 9),height=2)
                    label.grid(row=row, column=col,sticky="nsew")
                    label.image = _photo  # Esto mantiene la referencia
                else:
                    tk.Label(canvas_frame, text="", borderwidth=1, relief="solid", width=35,height=2).grid(row=row, column=col,sticky="nsew")
            tk.Label(canvas_frame, text=f"{habitacion}", borderwidth=1, relief="solid", width=15,height=2).grid(row=row, column=columna_final)

                

    def update_week_table(self, days):
        self.start_date += timedelta(days=days)  # Ajustar la fecha inicial en ±1 día
        self.create_week_table(self.start_date)         
                        
    def fill_table(self, reservas):
        """Llena la tabla con los datos de las reservas."""
        # Limpiar la tabla antes de insertar nuevas reservas
        for row in self.tree.get_children():
            self.tree.delete(row)
        # agregrar estilo a la tabla
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Oddrow", background="#f2f2f2") 
        style.configure("Evenrow", background="white")
        # estilo pago pendiente
        style.configure("PagoPendiente", background="#ffbdb8")
        
        for i, reserva in enumerate(reservas, start=1):
            if reserva.estado2 == "Pendiente":
                tag = "PagoPendiente"
            else:
                if i % 2 == 0:
                    tag = "Evenrow"
                else:
                    tag = "Oddrow"
            facturado= "❌"
            if reserva.facturado:
                facturado = "✔️"
            self.tree.insert("", tk.END, values=(reserva.id, reserva.codigo, f"{reserva.nombre} {reserva.apellido}", reserva.check_in, reserva.check_out, reserva.habitacion, reserva.estado2,reserva.precio,reserva.transbank, facturado,reserva.tipo_documento,reserva.folio_factura),tags=(tag,))
        self.tree.tag_configure("Oddrow", background="#f2f2f2")
        self.tree.tag_configure("Evenrow", background="white")
        self.tree.tag_configure("PagoPendiente", background="#ffbdb8")
       
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
            # filtrar las reservas por fecha de check-in y check-out
            reservas_filtradas = self.reserva_controller.listar_reservas_por_fecha(inicio, fin)
            self.fill_table(reservas_filtradas)
            
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