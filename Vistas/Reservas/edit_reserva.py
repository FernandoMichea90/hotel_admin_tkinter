from tkinter import messagebox, ttk
import tkinter as tk
from tkcalendar import DateEntry
import customtkinter as ctk
from Controller.reserva_controller import ReservasController

def editar_reserva(self, reserva_id, frame=None,window=None,update_table=None):
    """Mostrar contenido del panel derecho para editar una reserva."""

    # Crear un frame para el contenido
    if frame is None:     
        self.content_frame = self.master.master
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    else:
        self.content_frame = frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()    
    # Conectar al controlador
    controller = ReservasController()

    print('Este es el id de la reserva', reserva_id)

    # Obtener los datos existentes de la reserva
    reserva_data = controller.get_reserva(reserva_id)
    if not reserva_data:
        messagebox.showerror("Error", "No se encontraron datos para la reserva seleccionada.")
        return

    stepper = ttk.Notebook(self.content_frame)
    stepper.pack(fill="both", expand=True, padx=20, pady=10)

    # Paso 1: Información General
    step1 = ctk.CTkFrame(stepper, fg_color="white")
    stepper.add(step1, text="Paso 1: Datos Pasajeros")

    # Campos manuales para Paso 1
    nombre_entry = ctk.CTkEntry(step1, width=300)
    nombre_label = tk.Label(step1, text="Nombre", font=("Arial", 12), bg="white")
    nombre_label.grid(row=0, column=0, sticky="w", pady=5)
    nombre_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
    nombre_entry.insert(0, reserva_data.nombre)

    apellido_entry = ctk.CTkEntry(step1, width=300)
    apellido_label = tk.Label(step1, text="Apellido", font=("Arial", 12), bg="white")
    apellido_label.grid(row=1, column=0, sticky="w", pady=5)
    apellido_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
    apellido_entry.insert(0, reserva_data.apellido)

    correo_entry = ctk.CTkEntry(step1, width=300)
    correo_label = tk.Label(step1, text="Correo", font=("Arial", 12), bg="white")
    correo_label.grid(row=2, column=0, sticky="w", pady=5)
    correo_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
    correo_entry.insert(0, reserva_data.correo)

    celular_entry = ctk.CTkEntry(step1, width=300)
    celular_label = tk.Label(step1, text="Celular", font=("Arial", 12), bg="white")
    celular_label.grid(row=3, column=0, sticky="w", pady=5)
    celular_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)
    celular_entry.insert(0, reserva_data.celular)

    direccion_entry = ctk.CTkEntry(step1, width=300)
    direccion_label = tk.Label(step1, text="Dirección", font=("Arial", 12), bg="white")
    direccion_label.grid(row=4, column=0, sticky="w", pady=5)
    direccion_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)
    direccion_entry.insert(0, reserva_data.direccion)

    rut_pasaporte_entry = ctk.CTkEntry(step1, width=300)
    rut_pasaporte_label = tk.Label(step1, text="RUT/Pasaporte", font=("Arial", 12), bg="white")
    rut_pasaporte_label.grid(row=5, column=0, sticky="w", pady=5)
    rut_pasaporte_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)
    rut_pasaporte_entry.insert(0, reserva_data.rut_pasaporte)

    pais_entry = ctk.CTkEntry(step1, width=300)
    pais_label = tk.Label(step1, text="País", font=("Arial", 12), bg="white")
    pais_label.grid(row=6, column=0, sticky="w", pady=5)
    pais_entry.grid(row=6, column=1, sticky="w", padx=10, pady=5)
    pais_entry.insert(0, reserva_data.pais)

    # Paso 2: Detalles de la Reserva
    step2 = ctk.CTkFrame(stepper, fg_color="white")
    stepper.add(step2, text="Paso 2: Detalles de la Reserva")

    checkin_entry = DateEntry(step2, date_pattern="yyyy-mm-dd")
    checkin_label = tk.Label(step2, text="Check-in", font=("Arial", 12), bg="white")
    checkin_label.grid(row=0, column=0, sticky="w", pady=5)
    checkin_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
    checkin_entry.set_date(reserva_data.check_in)

    checkout_entry = DateEntry(step2, date_pattern="yyyy-mm-dd")
    checkout_label = tk.Label(step2, text="Check-out", font=("Arial", 12), bg="white")
    checkout_label.grid(row=1, column=0, sticky="w", pady=5)
    checkout_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
    checkout_entry.set_date(reserva_data.check_out)

    habitacion_entry = ctk.CTkEntry(step2, width=300)
    habitacion_label = tk.Label(step2, text="Habitación", font=("Arial", 12), bg="white")
    habitacion_label.grid(row=2, column=0, sticky="w", pady=5)
    habitacion_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
    habitacion_entry.insert(0, reserva_data.habitacion)

    adultos_entry = ctk.CTkEntry(step2, width=300)
    adultos_label = tk.Label(step2, text="Adultos", font=("Arial", 12), bg="white")
    adultos_label.grid(row=3, column=0, sticky="w", pady=5)
    adultos_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)
    adultos_entry.insert(0, reserva_data.adultos)

    ninos_entry = ctk.CTkEntry(step2, width=300)
    ninos_label = tk.Label(step2, text="Niños", font=("Arial", 12), bg="white")
    ninos_label.grid(row=4, column=0, sticky="w", pady=5)
    ninos_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)
    ninos_entry.insert(0, reserva_data.ninos)

    precio_entry = ctk.CTkEntry(step2, width=300)
    precio_label = tk.Label(step2, text="Precio", font=("Arial", 12), bg="white")
    precio_label.grid(row=5, column=0, sticky="w", pady=5)
    precio_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)
    precio_entry.insert(0, reserva_data.precio)

    # Paso 3: Procedencia y Pago
    step3 = ctk.CTkFrame(stepper, fg_color="white")
    stepper.add(step3, text="Paso 3: Procedencia y Pago")

    procedencia_options = ["Booking", "Pagina web", "Whatsapp", "Walking", "Pendiente"]
    metodo_pago_options = ["Tarjeta", "Transferencia", "Efectivo", "Pendiente"]
    dte_options = ["Factura", "Factura de exportacion", "Boleta", "Efectivo", "Pendiente"]
    estado_pago_options = ["Pagado", "Pendiente"]

    procedencia_entry = ctk.CTkOptionMenu(step3, values=procedencia_options)
    procedencia_label = tk.Label(step3, text="Procedencia", font=("Arial", 12), bg="white")
    procedencia_label.grid(row=0, column=0, sticky="w", pady=5)
    procedencia_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)
    procedencia_entry.set(reserva_data.procedencia)

    metodo_pago_entry = ctk.CTkOptionMenu(step3, values=metodo_pago_options)
    metodo_pago_label = tk.Label(step3, text="Método de Pago", font=("Arial", 12), bg="white")
    metodo_pago_label.grid(row=1, column=0, sticky="w", pady=5)
    metodo_pago_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
    metodo_pago_entry.set(reserva_data.pago)

    dte_entry = ctk.CTkOptionMenu(step3, values=dte_options)
    dte_label = tk.Label(step3, text="DTE", font=("Arial", 12), bg="white")
    dte_label.grid(row=2, column=0, sticky="w", pady=5)
    dte_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)
    dte_entry.set(reserva_data.tipo_documento)

    estado_pago_entry = ctk.CTkOptionMenu(step3, values=estado_pago_options)
    estado_pago_label = tk.Label(step3, text="Estado Pago", font=("Arial", 12), bg="white")
    estado_pago_label.grid(row=3, column=0, sticky="w", pady=5)
    estado_pago_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)
    estado_pago_entry.set(reserva_data.estado2)

    # Botón para actualizar
    save_btn = ctk.CTkButton(
        step3,
        text="Guardar Cambios",
        command=lambda: actualizar_reserva(
            reserva_id,
            nombre_entry.get(), apellido_entry.get(), correo_entry.get(),
            celular_entry.get(), direccion_entry.get(), rut_pasaporte_entry.get(),
            pais_entry.get(), checkin_entry.get_date(), checkout_entry.get_date(),
            habitacion_entry.get(), adultos_entry.get(), ninos_entry.get(),
            precio_entry.get(), procedencia_entry.get(), metodo_pago_entry.get(),
            dte_entry.get(), estado_pago_entry.get(),window,update_table,self.content_frame
        )
    )
    save_btn.grid(row=4, columnspan=2, pady=20)
    
def get_parent_of_parent(widget):
    # Get the first parent
    first_parent = widget.winfo_parent()
    # If there's a parent, get its parent
    if first_parent:
        parent_of_parent = widget.nametowidget(first_parent).winfo_parent()
        if parent_of_parent:
            return widget.nametowidget(parent_of_parent)
    return None

def actualizar_reserva(reserva_id, nombre, apellido, correo, celular, direccion, rut_pasaporte, pais, checkin, checkout, habitacion, adultos, ninos, precio, procedencia, metodo_pago, dte, estado_pago="Pendiente",window=None,update_table=None,frame=None):
    """Actualizar los datos de una reserva existente."""
    
    # Imprimir los valores de las variables antes de enviarlas al controlador
    print("Datos a actualizar:")
    print(f"Reserva ID: {reserva_id}")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Correo: {correo}")
    print(f"Celular: {celular}")
    print(f"Dirección: {direccion}")
    print(f"Rut/Pasaporte: {rut_pasaporte}")
    print(f"País: {pais}")
    print(f"Check-in: {checkin}")
    print(f"Check-out: {checkout}")
    print(f"Habitación: {habitacion}")
    print(f"Adultos: {adultos}")
    print(f"Niños: {ninos}")
    print(f"Precio: {precio}")
    print(f"Procedencia: {procedencia}")
    print(f"Método de pago: {metodo_pago}")
    print(f"DTE: {dte}")
    print(f"Estado de pago: {estado_pago}")
    print('---------------------------------------')
    
    # Llamada al controlador para actualizar la reserva
    controller = ReservasController()
    updated = controller.actualizar_reserva(reserva_id, nombre, apellido, correo, celular, direccion, rut_pasaporte, pais, checkin, checkout, habitacion, adultos, ninos, precio, procedencia, metodo_pago, dte, estado_pago)
    if updated:
        messagebox.showinfo("Éxito", "Reserva actualizada correctamente.")
        if window:
            update_table()
            window.destroy()
        else:
            from Vistas.Reservas.reserva_view import ReservaView
            #obtener frame padre 
            frame_parent = get_parent_of_parent(frame)
            for widget in frame_parent.winfo_children():
                widget.destroy()  # Elimina todos los widgets del padre
            rv = ReservaView(frame_parent)  # Crea una nueva instancia de ReservaView en el frame padre
            rv.mostrar_reservas()
            
    else:
        messagebox.showerror("Error", "No se pudo actualizar la reserva.")
