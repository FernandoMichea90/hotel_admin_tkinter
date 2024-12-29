import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import customtkinter as ctk
from Controller.reserva_controller import ReservasController
def crear_reservas(self):
    """Mostrar contenido del panel derecho para Reservas."""
    # Limpiar contenido actual
    for widget in self.content_frame.winfo_children():
        widget.destroy()

    # Conectar al controlador
    controller = ReservasController()

    # Conjunto de campos del formulario
    stepper = ttk.Notebook(self.content_frame)
    stepper.pack(fill="both", expand=True, padx=20, pady=10)

    # Paso 1: Información General
    step1 = ctk.CTkFrame(stepper, fg_color="white")
    stepper.add(step1, text="Paso 1: Datos Pasajeros")

    campos_step1 = [
        ("Nombre", ctk.CTkEntry(step1, width=300)),
        ("Apellido", ctk.CTkEntry(step1, width=300)),
        ("Correo", ctk.CTkEntry(step1, width=300)),
        ("Celular", ctk.CTkEntry(step1, width=300)),
        ("Dirección", ctk.CTkEntry(step1, width=300)),
        ("RUT/Pasaporte", ctk.CTkEntry(step1, width=300)),
        ("País", ctk.CTkEntry(step1, width=300)),
    ]

    for idx, (label_text, widget) in enumerate(campos_step1):
        tk.Label(
            step1, text=label_text, font=("Arial", 12), bg="white"
        ).grid(row=idx, column=0, sticky="w", pady=5)
        widget.grid(row=idx, column=1, sticky="w", padx=10, pady=5)

    # Paso 2: Detalles de la Reserva
    step2 = ctk.CTkFrame(stepper, fg_color="white")
    stepper.add(step2, text="Paso 2: Detalles de la Reserva")

    campos_step2 = [
        ("Check-in", DateEntry(step2, date_pattern="yyyy-mm-dd")),
        ("Check-out", DateEntry(step2, date_pattern="yyyy-mm-dd")),
        ("Habitación", ctk.CTkEntry(step2, width=300)),
        ("Adultos", ctk.CTkEntry(step2, width=300)),
        ("Niños", ctk.CTkEntry(step2, width=300)),
        ("Precio", ctk.CTkEntry(step2, width=300)),
    ]

    for idx, (label_text, widget) in enumerate(campos_step2):
        tk.Label(
            step2, text=label_text, font=("Arial", 12), bg="white"
        ).grid(row=idx, column=0, sticky="w", pady=5)
        widget.grid(row=idx, column=1, sticky="w", padx=10, pady=5)

    # Paso 3: Procedencia y Pago
    step3 = ctk.CTkFrame(stepper, fg_color="white")
    stepper.add(step3, text="Paso 3: Procedencia y Pago")

    procedencia_options = ["Booking", "Pagina web", "Whatsapp", "Walking","Pendiente"]
    pago_options = ["Tarjeta", "Transferencia", "Efectivo","Pendiente"]
    tipo_documento_options = ["Factura", "Factura de exportacion", "Boleta", "Efectivo","Pendiente"]
    estado_options = ["Pagado", "Pendiente"]

    campos_step3 = [
        ("Procedencia", ctk.CTkOptionMenu(step3, values=procedencia_options)),
        ("Método de Pago", ctk.CTkOptionMenu(step3, values=pago_options)),
        ("DTE", ctk.CTkOptionMenu(step3, values=tipo_documento_options)),
        ("Folio DTE", ctk.CTkEntry(step3, width=300)),
        ("Facturado", ctk.CTkCheckBox(step3, text="Facturado")),
        ("Transbank", ctk.CTkEntry(step3, width=300)),
        ("Estado Pago", ctk.CTkOptionMenu(step3,values=estado_options))
    ]

    for idx, (label_text, widget) in enumerate(campos_step3):
        tk.Label(
            step3, text=label_text, font=("Arial", 12), bg="white"
        ).grid(row=idx, column=0, sticky="w", pady=5)
        widget.grid(row=idx, column=1, sticky="w", padx=10, pady=5)

    # Botón de guardar en el último paso
    save_btn = ctk.CTkButton(
        step3, text="Guardar Reserva", cursor="hand2",
        font=("Arial", 12, "bold"), fg_color="green", hover_color="darkgreen",
        text_color="white", command=lambda: guardar_reserva(campos_step1, campos_step2, campos_step3, controller)
    )
    save_btn.grid(row=len(campos_step3), column=0, columnspan=2, pady=20)

def guardar_reserva(campos_step1, campos_step2, campos_step3, controller):
    """Función para recoger los datos y guardar la reserva."""
    # Recoger los datos del formulario
    reserva_data = {
        "nombre": campos_step1[0][1].get(),
        "apellido": campos_step1[1][1].get(),
        "correo": campos_step1[2][1].get(),
        "celular": campos_step1[3][1].get(),
        "direccion": campos_step1[4][1].get(),
        "rut_pasaporte": campos_step1[5][1].get(),
        "pais": campos_step1[6][1].get(),
        "check_in": campos_step2[0][1].get_date(),
        "check_out": campos_step2[1][1].get_date(),
        "habitacion": campos_step2[2][1].get(),
        "adultos": int(campos_step2[3][1].get() or 0),
        "ninos": int(campos_step2[4][1].get() or 0),
        "precio": int(campos_step2[5][1].get() or 0),
        "procedencia": campos_step3[0][1].get(),
        "pago": campos_step3[1][1].get(),
        "tipo_documento": campos_step3[2][1].get(),
        "folio_factura": campos_step3[3][1].get() or 0,
        "facturado": campos_step3[4][1].get(),
        "transbank": campos_step3[5][1].get() or 0,
        "estado2": campos_step3[6][1].get()
    }

    # Llamar al controlador para agregar la reserva
    response = controller.agregar_reserva(reserva_data)

    # Mostrar mensaje al usuario
    if response["status"] == "success":
        messagebox.showinfo("Éxito", response["message"])
    else:
        messagebox.showerror("Error", response["message"])
