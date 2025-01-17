import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.title("Ejemplo Tabla Responsiva")

        # Crear un Canvas con scroll horizontal
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Crear un CTkFrame dentro del Canvas
        self.canvas_frame = ctk.CTkFrame(self.canvas, bg_color="blue")
        self.canvas_window = self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")

        # Lista de fechas como columnas
        self.fechas = ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04"]

        # Configurar scroll
        self.scrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        # Redibujar la tabla al cambiar el tamaño del Canvas
        self.canvas.bind("<Configure>", self.resize_table)

        # Dibujar la tabla inicial
        self.create_labels()

    def create_labels(self):
        # Limpiar etiquetas existentes
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        print(self.winfo_width())
        # Obtener dimensiones dinámicas
        total_columns = len(self.fechas) + 2  # Columnas de fecha + 2 columnas de "Habitación"
        column_width = max(self.canvas.winfo_width() // total_columns, 10)

        # Crear encabezado de la primera columna
        tk.Label(self.canvas_frame, text="Habitación", borderwidth=1, relief="solid", 
                 width=int(column_width // 7), height=2).grid(row=0, column=0)

        # Crear las columnas de fecha
        for col, fecha in enumerate(self.fechas, start=1):
            tk.Label(self.canvas_frame, text=fecha, borderwidth=1, relief="solid", 
                     width=int(column_width // 7), height=2).grid(row=0, column=col)

        # Crear encabezado de la última columna
        tk.Label(self.canvas_frame, text="Habitación", borderwidth=1, relief="solid", 
                 width=int(column_width // 7), height=2).grid(row=0, column=total_columns - 1)

        # Ajustar tamaño del frame al contenido
        self.canvas_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def resize_table(self, event):
        self.create_labels()

if __name__ == "__main__":
    app = App()
    app.mainloop()
