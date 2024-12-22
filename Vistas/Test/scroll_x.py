import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x200")  # Tamaño de la ventana principal

        # Frame principal
        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack(fill="both", expand=True)

        # Canvas para el scroll
        self.canvas = tk.Canvas(self.frame_principal)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Barra de desplazamiento horizontal
        self.scrollbar = ttk.Scrollbar(self.frame_principal, orient="horizontal", command=self.canvas.xview)
        self.scrollbar.pack(side="bottom", fill="x")

        # Configurar el canvas con la barra de desplazamiento
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        # Frame que contiene los elementos desplazables
        self.scrollable_frame = tk.Frame(self.canvas, bg="lightgray")
        
        # Colocar el Frame dentro del Canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Evento que ajusta el scrollregion
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)

        # Agregar varios widgets (etiquetas) al frame desplazable
        for i in range(20):  # Agrega 20 etiquetas horizontales
            label = tk.Label(self.scrollable_frame, text=f"Item {i+1}", bg="lightblue", padx=10, pady=10)
            label.grid(row=0, column=i, padx=5, pady=5)

    def on_frame_configure(self, event):
        """Este evento ajusta el scrollregion del canvas cuando se agrega contenido al frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

# Crear la ventana principal
root = tk.Tk()
app = App(root)
root.mainloop()
