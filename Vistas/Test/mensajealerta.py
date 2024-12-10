import tkinter as tk
from tkinter import messagebox

def eliminar_reserva(reserva_id):
    """
    Función para eliminar una reserva con confirmación.
    """
    # Usamos el messagebox de tkinter para la confirmación
    respuesta = messagebox.askyesno(
        "Confirmación requerida",
        f"¿Estás seguro de que deseas eliminar la reserva con ID {reserva_id}? Esta acción no se puede deshacer."
    )
    if respuesta:  # Si la respuesta es "Yes"
        # Aquí iría el código para eliminar la reserva
        # Simulación: solo mostramos un mensaje
        messagebox.showinfo(
            "Reserva Eliminada",
            f"La reserva con ID {reserva_id} ha sido eliminada."
        )
    else:
        # Si el usuario selecciona "No", mostramos un mensaje de cancelación
        messagebox.showinfo("Operación Cancelada", "La reserva no ha sido eliminada.")


def mostrar_reserva(content_frame, id_reserva):
    """
    Simulación para mostrar detalles de la reserva con botón de eliminar.
    """
    # Limpiar el contenido del frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Crear la interfaz
    tk.Label(content_frame, text=f"Reserva ID: {id_reserva}", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(content_frame, text="Detalles de la reserva...", font=("Helvetica", 12)).pack(pady=5)

    # Botón para eliminar reserva
    eliminar_btn = tk.Button(
        content_frame,
        text="Eliminar Reserva",
        bg="red",
        fg="white",
        command=lambda: eliminar_reserva(id_reserva)
    )
    eliminar_btn.pack(pady=20)


# Configuración de ventana principal con tkinter
root = tk.Tk()
root.geometry("400x300")
root.title("Gestión de Reservas")

# Frame de contenido
content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack(fill="both", expand=True)

# Mostrar una reserva simulada
mostrar_reserva(content_frame, 12345)

# Ejecutar la aplicación
root.mainloop()
