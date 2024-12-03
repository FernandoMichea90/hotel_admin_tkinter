import customtkinter
import tkinter as tk
import customtkinter as ctk
from datetime import date
from Controller.reserva_controller import ReservasController

class MyScrollableCardFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.values = values
        self.cards = []

        for i, value in enumerate(self.values):
            # Crear un "card" como un CTkFrame
            card = customtkinter.CTkFrame(self, corner_radius=10, fg_color="white")
            card.pack(fill="x", padx=10, pady=(10, 0))

            # Agregar texto dentro de la tarjeta
            label = customtkinter.CTkLabel(card, text=value['nombre'])
            label.pack(side="left", padx=10, pady=10)
            label2 = customtkinter.CTkLabel(card, text="codigo")
            label2.pack(side="left", padx=10, pady=1)

            # Agregar un botón de acción opcional
            button = customtkinter.CTkButton(card, text="Action", width=100, command=lambda v=value: self.card_action(v))
            button.pack(side="right", padx=10, pady=10)

            self.cards.append(card)

    def card_action(self, value):
        print(f"Action on card: {value}")


class ReservaView:
    def __init__(self, master):
        self.master = master
        self.frame = customtkinter.CTkFrame(master)
        self.frame.pack(fill="both", expand=True)  # Usamos pack

        self.content_frame = tk.Frame(self.frame, bg="white")
        self.content_frame.pack(fill="both", expand=False)  # Usamos pack aquí también
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
        )
        button.pack(side="right", padx=10)
        
        reserva_controller=ReservasController()   
        print(reserva_controller.listar_reservas())     
        self.scrollable_card_frame = MyScrollableCardFrame(self.frame, title="Reservas", values=reserva_controller.listar_reservas())
        self.scrollable_card_frame.pack(fill="both", expand=True, padx=0, pady=0)


if __name__ == "__main__":
    root = tk.Tk()
    app = ReservaView(root)
    app.mostrar_reservas()
    root.mainloop()
