import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.geometry("400x200")  # Tamaño de la ventana

# Crear un Frame principal
main_frame = tk.Frame(root, bg="lightgray", width=400, height=200)
main_frame.pack(fill="both", expand=True)  # Ocupa todo el espacio disponible

# Crear un Frame a la izquierda (sin márgenes extra)
left_frame = tk.Frame(main_frame, bg="lightblue", width=200, height=200)
left_frame.pack(side="left", fill="y", padx=0, pady=0)  # Eliminar margenes
left_frame.pack_propagate(False)  # Evitar que el Frame se ajuste al tamaño de los widgets internos
# Crear un Frame a la derecha (sin márgenes extra)
right_frame = tk.Frame(main_frame, bg="lightgreen", width=200, height=200)
right_frame.pack(side="right", fill="y", padx=0, pady=0)  # Eliminar margenes
right_frame.pack_propagate(False)  # Evitar que el Frame se ajuste al tamaño de los widgets internos

# Agregar un Label dentro del Frame izquierdo
label_left = tk.Label(left_frame, text="Frame Izquierdo", bg="lightblue")
label_left.pack(padx=10, pady=10)

# Agregar un Label dentro del Frame derecho
label_right = tk.Label(right_frame, text="Frame Derecho", bg="lightgreen")
label_right.pack(padx=10, pady=10)

root.mainloop()
