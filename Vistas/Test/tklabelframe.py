import tkinter as tk
from tkinter import PhotoImage

class VistaGasto:
    def __init__(self, master):
        self.master = master
        self.frame_info_y_botones = tk.Frame(self.master)
        self.frame_info_y_botones.pack(fill="both", expand=True)

        # Crear un LabelFrame con texto
        self.frame_botones = tk.LabelFrame(self.frame_info_y_botones, text="")  # Sin texto aquí

        # Cargar la imagen del ícono (asegúrate de que sea un formato como .png o .gif)
        self.icono = PhotoImage(file="image.png")  # Reemplaza con la ruta de tu archivo .png o .gif
        self.icono = self.icono.subsample(20)  # Para reducir el tamaño, ajusta según lo necesites

        # Crear una etiqueta que combine texto y el icono dentro del LabelFrame
        self.etiqueta_con_icono = tk.Label(self.frame_botones, text=" Acción ", image=self.icono, compound="left")  # 'compound="left"' coloca la imagen a la izquierda del texto
        self.etiqueta_con_icono.pack()

        # Empacar el LabelFrame con el contenido
        self.frame_botones.pack(fill="both", expand=True, padx=10, pady=10)

# Ejecutar la ventana
root = tk.Tk()
vista_gasto = VistaGasto(root)
root.mainloop()
