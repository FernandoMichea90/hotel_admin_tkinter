import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Definir una configuración común
configuracion = {"side": "left", "padx": 10, "pady": 10, "fill": "x", "expand": True}
configuracion2 = {"side": "right", "padx": 10, "pady": 10, "fill": "x", "expand": True}

# Crear etiquetas y aplicar el pack con la configuración
label1 = tk.Label(root, text="Etiqueta 1", bg="lightblue")
label1.pack(**configuracion)

label2 = tk.Label(root, text="Etiqueta 2", bg="lightgreen")
label2.pack(**configuracion)

label3 = tk.Label(root, text="Etiqueta 3", bg="lightyellow")
label3.pack(**configuracion)

# Crear etiquetas y aplicar el pack con la configuración
label4= tk.Label(root, text="Etiqueta 1", bg="lightblue")
label4.pack(**configuracion2)

label5 = tk.Label(root, text="Etiqueta 2", bg="lightgreen")
label5.pack(**configuracion2)

label6 = tk.Label(root, text="Etiqueta 3", bg="lightyellow")
label6.pack(**configuracion2)

root.mainloop()
