import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
root = tk.Tk()
root.title("Emojis con imágenes y texto")

# Crear un frame donde colocarás el contenido
canvas_frame = tk.Frame(root)
canvas_frame.pack(pady=20)

# Cargar la imagen del emoji
emoji_image = Image.open("image.png")  # Asegúrate de tener el archivo image.png
emoji_image = emoji_image.resize((9, 9))  # Ajustar el tamaño de la imagen
emoji_photo = ImageTk.PhotoImage(emoji_image)

# Lista de clientes (puedes agregar más elementos en esta lista)
clientes = ["Fer", "Ana", "Carlos", "Maria"]

# Crear los Labels con la imagen y el texto usando un for
for idx, cliente in enumerate(clientes):
    label = tk.Label(canvas_frame, text=cliente, image=emoji_photo, compound="left", font=("Segoe UI Emoji", 9), borderwidth=1, relief="solid", width=200)
    label.grid(row=idx, column=0, padx=5)  # Ubicamos las etiquetas en filas sucesivas

# Iniciar el bucle principal de la aplicación
root.mainloop()
