import customtkinter as ctk

class App:
    def __init__(self, root):
        # Frame principal
        self.frame_principal = ctk.CTkFrame(root, corner_radius=10)
        self.frame_principal.pack(padx=10, pady=10, fill="x", side="top")

        # Frame 1
        self.frame_1 = ctk.CTkFrame(self.frame_principal, corner_radius=10, fg_color="red")
        self.frame_1.pack(padx=10, pady=5, fill="x")
        label_1 = ctk.CTkLabel(self.frame_1, text="Frame 1", font=("Arial", 12))
        label_1.pack(padx=10, pady=10)

        # Frame 2
        self.frame_2 = ctk.CTkFrame(self.frame_principal, corner_radius=10, fg_color="green")
        self.frame_2.pack(padx=10, pady=5, fill="x")
        label_2 = ctk.CTkLabel(self.frame_2, text="Frame 2", font=("Arial", 12))
        label_2.pack(padx=10, pady=10)
        

        # Frame 3
        self.frame_3 = ctk.CTkFrame(self.frame_principal, corner_radius=10, fg_color="blue")
        self.frame_3.pack(padx=10, pady=5, fill="x")
        label_3 = ctk.CTkLabel(self.frame_3, text="Frame 3", font=("Arial", 12))
        label_3.pack(padx=10, pady=10)
# Configuración de la ventana principal
root = ctk.CTk()
root.geometry("400x400")
root.title("Frames con Pack y Colores")

app = App(root)

root.mainloop()
