from Controller.reserva_controller import ReservasController
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


class ReservaOrmView:
    def __init__(self,master):
        self.master = master
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack(fill="both", expand=True)
        self.reserva_controller = ReservasController()
        # Etiquetas de entrada de fechas
        self.label_inicio = ctk.CTkLabel(self.frame, text="Fecha Inicio (YYYY-MM-DD):", font=("Arial", 12))
        self.label_inicio.pack(pady=5)

        self.entry_inicio = ctk.CTkEntry(self.frame, font=("Arial", 12))
        self.entry_inicio.pack(pady=5)

        self.label_fin = ctk.CTkLabel(self.frame, text="Fecha Fin (YYYY-MM-DD):", font=("Arial", 12))
        self.label_fin.pack(pady=5)

        self.entry_fin = ctk.CTkEntry(self.frame, font=("Arial", 12))
        self.entry_fin.pack(pady=5)

        # Botón para filtrar
        self.btn_filtrar = ctk.CTkButton(self.frame, text="Filtrar", font=("Arial", 12))
        self.btn_filtrar.pack(pady=10)

        # Tabla para mostrar las reservas
        self.tree = ttk.Treeview(self.frame, columns=("id", "codigo", "nombre", "check_in", "check_out"), show="headings", selectmode="browse")
        self.tree.heading("id", text="ID")
        self.tree.heading("codigo", text="Código")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("check_in", text="Check-In")
        self.tree.heading("check_out", text="Check-Out")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Llenar la tabla con las reservas
        reservas_listas=self.reserva_controller.listar_reservas_orm()
        self.fill_table(reservas_listas)
        

    def fill_table(self, reservas):
        """Llena la tabla con los datos de las reservas."""
        # Limpiar la tabla antes de insertar nuevas reservas
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar las reservas en la tabla
        for reserva in reservas:
            self.tree.insert("", tk.END, values=(reserva.id, reserva.codigo, f"{reserva.nombre} {reserva.apellido}", reserva.check_in, reserva.check_out))
