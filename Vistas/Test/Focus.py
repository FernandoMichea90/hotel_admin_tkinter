import tkinter as tk

class MiVentana:
    def __init__(self, master):
        self.master = master
        self.master.title("Foco en widgets")
        
        # Creamos un Label para mostrar quién tiene el foco
        self.label = tk.Label(self.master, text="Foco en: Ninguno")
        self.label.pack(pady=20)

        # Creamos algunos widgets Entry y Button
        self.entry1 = tk.Entry(self.master)
        self.entry1.bind("<Escape>", self.probar_escape)  # Corregido aquí
        self.entry1.pack(pady=10)
        self.entry2 = tk.Entry(self.master)
        self.entry2.pack(pady=10)
        self.button = tk.Button(self.master, text="Botón")
        self.button.pack(pady=10)

        # Llamamos a la función para gestionar el foco automáticamente
        self.configurar_foco_global()

    def configurar_foco_global(self):
        # Se usa `bind_all` para capturar eventos de foco en cualquier widget
        self.master.bind_all("<FocusIn>", self.actualizar_foco)
    
    def probar_escape(self, event):  # Modificado para recibir el evento
        print("Escape presionado")
        self.master.focus_set()
    
    def actualizar_foco(self, event):
        # Obtener el widget que tiene el foco y su tipo
        widget = event.widget
        
        # Asegurarse de que el texto solo se actualice si el widget tiene nombre
        widget_name = widget.winfo_name() if widget.winfo_name() else type(widget).__name__
        
        # Actualizar el texto del Label
        self.label.config(text=f"Foco en: {widget_name}")

# Crear la ventana principal
root = tk.Tk()
app = MiVentana(root)
root.mainloop()
