import customtkinter
import tkinter as tk
from tkinter import ttk  # Importar ttk para usar el componente de Tabs
import customtkinter as ctk
from datetime import date
from Controller.reserva_controller import ReservasController
from Vistas.Pasajeros.crear import crear_reservas

class MyScrollableCardFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values,reserva_view):
        super().__init__(master, label_text=title)
        self.reserva_view = reserva_view
        self.values = values
        self.cards = []

        for i, value in enumerate(self.values):
            # Crear un "card" como un CTkFrame
            card = customtkinter.CTkFrame(self, corner_radius=20, fg_color="white")
            card.pack(fill="both",expand=True, padx=10, pady=(10, 0))
            #Crear un left frame
            left_frame = tk.Frame(card, bg="white")
            left_frame.pack(side="left", fill="y", padx=(20,0), pady=0)  # Eliminar margenes
            #Crear un right frame
            right_frame = tk.Frame(card, bg="white")
            right_frame.pack(side="right", fill="y", padx=(0,20), pady=0)
            # Crera un centro frame
            center_frame = tk.Frame(card, bg="white")
            center_frame.pack(side="right", fill="y", padx=(0,20), pady=0)
            check_in = value['check_in']
            check_out = value['check_out']
            # Verifica si check_in no es None antes de aplicar strftime
            if check_in is not None:
                check_in = check_in.strftime("%d/%m/%Y")
           
            # Verifica si check_out no es None antes de aplicar strftime
            if check_out is not None:
                check_out = check_out.strftime("%d/%m/%Y")
          
            # Agregar un Label dentro del Frame izquierdo
            nombre_cliente = value['nombre'].strip() + " " + value['apellido'].strip()
            label3 = customtkinter.CTkLabel(left_frame, text=nombre_cliente,text_color="black",font=("Arial", 18, "bold"),height=22)
            label3.pack(side="top", padx=10, pady=(10,2),fill="x")
            if check_in is not None and check_out is not None:
                label_fecha = customtkinter.CTkLabel(left_frame, text=f"{check_in} - {check_out}",text_color="gray",font=("Arial", 10, "bold"),anchor="w",height=12)
                label_fecha.pack(side="top", padx=10, pady=(3,3),fill="x", expand=True)
            # Agregar texto dentro de la tarjeta
            label2 = customtkinter.CTkLabel(left_frame, text=value['codigo'],text_color='gray',font=("Arial",10,"normal"),anchor="w",height=10)
            label2.pack(side="top", padx=10,expand=True,fill="x")
            label4 = customtkinter.CTkLabel(left_frame, text=value['habitacion'],text_color='blue',font=("Arial",10,"normal"),anchor="w",height=11) 
            label4.pack(side="top", padx=10, pady=(0,10), expand=True,fill="x")
           # Agregar botón "Ver" con efecto hover invertido
            # Agregar un botón "Ver" con efecto hover usando un borde transparente
            button = customtkinter.CTkButton(
                right_frame,
                text="Ver",
                width=100,
                command=lambda v=value: self.show_reserva(v),
                anchor="center",
                fg_color="white",  # Color de fondo inicial
                border_color="green",  # Color del borde
                text_color="green",  # Color del texto
                border_width=2,
                hover_color="lightgray",  # Color de fondo al pasar el ratón (más transparente)
            )
            button.pack(side="top", padx=1, pady=1)

            # Agregar un botón "Editar" con efecto hover usando un borde transparente
            button = customtkinter.CTkButton(
                right_frame,
                text="Editar",
                width=100,
                command=lambda v=value: self.card_action(v),
                anchor="center",
                fg_color="white",  # Color de fondo inicial
                border_color="blue",  # Color del borde
                text_color="blue",  # Color del texto
                border_width=2,
                hover_color="lightgray",  # Color de fondo al pasar el ratón (más transparente)
            )
            button.pack(side="top", padx=1, pady=1)

            # Agregar un botón "Borrar" con efecto hover usando un borde transparente
            button = customtkinter.CTkButton(
                right_frame,
                text="Borrar",
                width=100,
                command=lambda v=value: self.card_action(v),
                anchor="center",
                fg_color="white",  # Color de fondo inicial
                border_color="red",  # Color del borde
                text_color="red",  # Color del texto
                border_width=2,
                hover_color="lightgray",  # Color de fondo al pasar el ratón (más transparente)
            )
            button.pack(side="top", padx=1, pady=1)
            self.cards.append(card)
    def card_action(self, value):
        print(f"Action on card: {value}")
    def show_reserva(self, value):
            self.reserva_view.clean()  # Llama al método clean en la instancia correcta
            print(value)
            self.reserva_view.mostrar_reserva(value['id'])

class ReservaView:
    def __init__(self, master):
        self.master = master
        self.frame = customtkinter.CTkFrame(master,fg_color="white")
        self.frame.pack(fill="both", expand=True)  # Usamos pack

        self.content_frame = tk.Frame(self.frame, bg="white")
        self.content_frame.pack(fill="both", expand=True)  # Usamos pack aquí también
        self.ReservaController= ReservasController()


  
    def mostrar_reservas(self):
        """Mostrar contenido del panel derecho para Reservas."""
        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        header_frame = tk.Frame(self.content_frame, bg="white")
        header_frame.pack(fill="x", pady=0, padx=0)  # Usamos pack

        label = tk.Label(
            header_frame,
            text="Gestión de Reservas",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="green",
            padx=10,
            pady=10
        )
        label.pack(side="left", padx=10)

        button = ctk.CTkButton(
            header_frame,
            text="Nuevo",
            font=("Arial", 18),
            fg_color="#4CAF50",
            hover_color="#45a049",
            width=100,
            height=40,
            border_width=0,
            corner_radius=10,
            text_color="#ffffff",
            command=self.clean
        )
        button.pack(side="right", padx=10)
        
        reserva_controller=ReservasController()   
        self.scrollable_card_frame = MyScrollableCardFrame(self.content_frame, title="Reservas", values=reserva_controller.listar_reservas(),reserva_view=self)
        self.scrollable_card_frame.pack(fill="both", expand=True, padx=20, pady=20)

    def mostrar_reserva_uno(self, id_reserva):
        """Mostrar contenido del panel derecho para Reservas."""
        # Limpiar contenido actual
     
        # Obtener la reserva
        reserva_controller = ReservasController()
        reserva = reserva_controller.get_reserva(id_reserva)
        
        if reserva is None:
            print('Error: No se encontró la reserva.')
            return  # Salir si no se encuentra la reserva
        # Crear el header_frame
        self.content_frame.pack(fill="both", pady=25, padx=25)  # Usamos pack
        datos_personales = [
            ("Código", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.codigo if reserva.codigo else "No disponible"),
            ("Nombre", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.nombre if reserva.nombre else "No disponible"),
            ("Apellido", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.apellido if reserva.apellido else "No disponible"),
            ("País", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.pais if reserva.pais else "No disponible"),
            ("RUT/Pasaporte", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.rut_pasaporte if reserva.rut_pasaporte else "No disponible"),
            ("Celular", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.celular if reserva.celular else "No disponible"),
            ("Dirección", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.direccion if reserva.direccion else "No disponible"),
            ("Correo", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.correo if reserva.correo else "No disponible")
        ]

        datos_reservas = [
            ("Check-in", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.check_in if reserva.check_in else "No disponible"),
            ("Check-out", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.check_out if reserva.check_out else "No disponible"),
            ("Estado", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.estado if reserva.estado else "No disponible"),
            ("Tipo", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.tipo if reserva.tipo else "No disponible"),
            ("Habitación", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.habitacion if reserva.habitacion else "No disponible"),
            ("Adultos", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.adultos if reserva.adultos else "No disponible"),
            ("Niños", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.ninos if reserva.ninos else "No disponible"),
            ("Procedencia", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.procedencia if reserva.procedencia else "No disponible")
        ]

        datos_pagos = [
            ("Pago", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.pago if reserva.pago else "No disponible"),
            ("Estado 2", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.estado2 if reserva.estado2 else "No disponible"),
            ("Precio", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.precio if reserva.precio else "No disponible"),
            ("Noches", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.noches if reserva.noches else "No disponible"),
            ("Estado Pago", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.estado_pago if reserva.estado_pago else "No disponible"),
            ("Precio Unitario", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.precio_unitario if reserva.precio_unitario else "No disponible"),
            ("Transbank", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.transbank if reserva.transbank else "No disponible"),
            ("Comentario", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.comentario if reserva.comentario else "No disponible"),
            ("Facturado", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.facturado if reserva.facturado else "No disponible"),
            ("Tipo Documento", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.tipo_documento if reserva.tipo_documento else "No disponible"),
            ("Folio Factura", ctk.CTkLabel(self.content_frame, width=300, text_color="black"), reserva.folio_factura if reserva.folio_factura else "No disponible")
        ]



       
        for idx, (label_text, widget, value) in enumerate(datos_personales):
            # Colocar las etiquetas (labels)
            tk.Label(
                self.content_frame, text=label_text, font=("Arial", 12)
            ).grid(row=idx, column=0, sticky="w", pady=5)
            
            # Colocar los widgets CTkLabel con el valor correspondiente
            widget.grid(row=idx, column=1, sticky="w", padx=10, pady=5)
            widget.configure(text=value)  # Usar configure para actualizar el texto

    def clean(self):
        print("clean")
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    def mostrar_reserva_dos(self, id_reserva):
        """Mostrar contenido del panel derecho para Reservas con un Stepper."""
        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Obtener la reserva
        reserva_controller = ReservasController()
        reserva = reserva_controller.get_reserva(id_reserva)

        if reserva is None:
            print('Error: No se encontró la reserva.')
            return  # Salir si no se encuentra la reserva

        # Datos organizados por pasos
        steps = [
            ("Datos Personales", [
                ("Código", reserva.codigo or "No disponible"),
                ("Nombre", reserva.nombre or "No disponible"),
                ("Apellido", reserva.apellido or "No disponible"),
                ("País", reserva.pais or "No disponible"),
                ("RUT/Pasaporte", reserva.rut_pasaporte or "No disponible"),
                ("Celular", reserva.celular or "No disponible"),
                ("Dirección", reserva.direccion or "No disponible"),
                ("Correo", reserva.correo or "No disponible"),
            ]),
            ("Datos de Reserva", [
                ("Check-in", reserva.check_in or "No disponible"),
                ("Check-out", reserva.check_out or "No disponible"),
                ("Estado", reserva.estado or "No disponible"),
                ("Tipo", reserva.tipo or "No disponible"),
                ("Habitación", reserva.habitacion or "No disponible"),
                ("Adultos", reserva.adultos or "No disponible"),
                ("Niños", reserva.ninos or "No disponible"),
                ("Procedencia", reserva.procedencia or "No disponible"),
            ]),
            ("Datos de Pagos", [
                ("Pago", reserva.pago or "No disponible"),
                ("Estado 2", reserva.estado2 or "No disponible"),
                ("Precio", reserva.precio or "No disponible"),
                ("Noches", reserva.noches or "No disponible"),
                ("Estado Pago", reserva.estado_pago or "No disponible"),
                ("Precio Unitario", reserva.precio_unitario or "No disponible"),
                ("Transbank", reserva.transbank or "No disponible"),
                ("Comentario", reserva.comentario or "No disponible"),
                ("Facturado", reserva.facturado or "No disponible"),
                ("Tipo Documento", reserva.tipo_documento or "No disponible"),
                ("Folio Factura", reserva.folio_factura or "No disponible"),
            ]),
        ]

        # Variables para controlar el step actual
        self.current_step = 0

        def mostrar_paso(step_index):
            """Mostrar el contenido del paso actual."""
            for widget in self.content_frame.winfo_children():
                widget.destroy()

            # Mostrar el título del paso
            step_title, step_data = steps[step_index]
            tk.Label(self.content_frame, text=step_title, font=("Arial", 16, "bold")).pack(pady=(0, 10))

            # Mostrar los datos del paso
            for label_text, value in step_data:
                frame = tk.Frame(self.content_frame)
                frame.pack(fill="x", pady=5)

                tk.Label(frame, text=label_text, font=("Arial", 12)).pack(side="left", padx=(0, 10))
                tk.Label(frame, text=value, font=("Arial", 12, "bold")).pack(side="left")

            # Mostrar botones de navegación
            nav_frame = tk.Frame(self.content_frame)
            nav_frame.pack(pady=20)

            if step_index > 0:
                tk.Button(nav_frame, text="Anterior", command=lambda: cambiar_paso(-1)).pack(side="left", padx=5)

            if step_index < len(steps) - 1:
                tk.Button(nav_frame, text="Siguiente", command=lambda: cambiar_paso(1)).pack(side="right", padx=5)

        def cambiar_paso(direction):
            """Cambiar al paso anterior o siguiente."""
            self.current_step += direction
            mostrar_paso(self.current_step)

    # Mostrar el primer paso al iniciar
        mostrar_paso(self.current_step)

    def mostrar_reserva(self, id_reserva):
        """Mostrar contenido del panel derecho para Reservas con Tabs."""
        # Limpiar contenido actual
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Obtener la reserva
        reserva_controller = ReservasController()
        reserva = reserva_controller.get_reserva(id_reserva)

        if reserva is None:
            print('Error: No se encontró la reserva.')
            return  # Salir si no se encuentra la reserva

        # Datos organizados por Tabs
        tabs_data = [
            ("Datos Personales", [
                ("Código", reserva.codigo or "No disponible"),
                ("Nombre", reserva.nombre or "No disponible"),
                ("Apellido", reserva.apellido or "No disponible"),
                ("País", reserva.pais or "No disponible"),
                ("RUT/Pasaporte", reserva.rut_pasaporte or "No disponible"),
                ("Celular", reserva.celular or "No disponible"),
                ("Dirección", reserva.direccion or "No disponible"),
                ("Correo", reserva.correo or "No disponible"),
            ]),
            ("Datos de Reserva", [
                ("Check-in", reserva.check_in or "No disponible"),
                ("Check-out", reserva.check_out or "No disponible"),
                ("Estado", reserva.estado or "No disponible"),
                ("Tipo", reserva.tipo or "No disponible"),
                ("Habitación", reserva.habitacion or "No disponible"),
                ("Adultos", reserva.adultos or "No disponible"),
                ("Niños", reserva.ninos or "No disponible"),
                ("Procedencia", reserva.procedencia or "No disponible"),
            ]),
            ("Datos de Pagos", [
                ("Pago", reserva.pago or "No disponible"),
                ("Estado 2", reserva.estado2 or "No disponible"),
                ("Precio", reserva.precio or "No disponible"),
                ("Noches", reserva.noches or "No disponible"),
                ("Estado Pago", reserva.estado_pago or "No disponible"),
                ("Precio Unitario", reserva.precio_unitario or "No disponible"),
                ("Transbank", reserva.transbank or "No disponible"),
                ("Comentario", reserva.comentario or "No disponible"),
                ("Facturado", reserva.facturado or "No disponible"),
                ("Tipo Documento", reserva.tipo_documento or "No disponible"),
                ("Folio Factura", reserva.folio_factura or "No disponible"),
            ]),
        ]

        # Crear las Tabs
        notebook =ttk.Notebook(self.content_frame)
        notebook.pack(fill="both", expand=True,padx=20, pady=20)

        for tab_title, tab_data in tabs_data:
            # Crear un frame para cada tab
            tab_frame =ttk.Frame(notebook)
            notebook.add(tab_frame, text=tab_title)
            print ('tab_data',tab_title)
            # Agregar contenido al tab
            for label_text, value in tab_data:
                row =ttk.Frame(tab_frame)
                print('label_text',label_text)
                row.pack(fill="x", pady=5,padx=25)
                ttk.Label(row, text=label_text, font=("Arial", 12)).pack(side="left", padx=(0, 10))
                ttk.Label(row, text=value, font=("Arial", 12, "bold")).pack(side="left")

        # Seleccionar la primera pestaña por defecto
        notebook.select(0)