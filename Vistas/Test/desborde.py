import customtkinter

class MyScrollableCardFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.cards = []

        for i, value in enumerate(self.values):
            # Crear un "card" como un CTkFrame
            card = customtkinter.CTkFrame(self, corner_radius=10, fg_color="lightgray")
            card.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="ew")
            card.grid_columnconfigure(0, weight=1)

            # Agregar texto dentro de la tarjeta
            label = customtkinter.CTkLabel(card, text=value)
            label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
            label2 = customtkinter.CTkLabel(card, text="codigo")
            label2.grid(row=0, column=1, padx=10, pady=1, sticky="w")


            # Agregar un botón de acción opcional
            button = customtkinter.CTkButton(card, text="Action", width=100, command=lambda v=value: self.card_action(v))
            button.grid(row=0, column=2, padx=10, pady=10)

            self.cards.append(card)

    def card_action(self, value):
        print(f"Action on card: {value}")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scrollable Cards")
        self.geometry("400x400")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ["Card 1", "Card 2", "Card 3", "Card 4", "Card 5", "Card 6"]
        self.scrollable_card_frame = MyScrollableCardFrame(self, title="Values", values=values)
        self.scrollable_card_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="Print Values", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("Action triggered from main button.")

app = App()
app.mainloop()
