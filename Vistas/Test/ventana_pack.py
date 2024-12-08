import tkinter as tk



def distribucion_pack():
    root = tk.Tk()  # Crear ventana principal
    root.geometry("300x200")  # Definir tamaño de la ventana

    # Crear un widget Label
    label = tk.Label(root, text="Etiqueta en la parte superior", bg="lightblue")
    label.pack(side="top", fill="x", padx=10, pady=5)

    # Crear otro widget Label
    label2 = tk.Label(root, text="Etiqueta en la parte inferior", bg="lightgreen")
    label2.pack(side="bottom", fill="x", padx=10, pady=5)

    # Crear un botón que se expandirá
    button = tk.Button(root, text="Botón Expandido")
    button.pack(side="bottom", fill="both", expand=True)

    root.mainloop()
    
def pack_with_width():

    root = tk.Tk()
    root.geometry("500x400")  # Tamaño de la ventana

    # Crear un Frame con un ancho específico de 300px y un alto ajustable
    frame = tk.Frame(root, width=300, height=500, bg="lightblue", bd=2, relief="solid")  # 'bd' y 'relief' añaden un borde visible
    frame.pack_propagate(False)  # Evitar que el Frame se ajuste al tamaño de los widgets internos
    frame.pack(padx=20, pady=20,fill='y')

    # Crear un Label dentro del Frame
    label = tk.Label(frame, text="Este es un Label dentro de un Frame", bg="lightgreen")
    label.pack(padx=10, pady=10)

    root.mainloop()

# distribucion_pack()
pack_with_width()