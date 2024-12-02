import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Conectar a la base de datos MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",      # Reemplaza con tu usuario de MySQL
        password="123",  # Reemplaza con tu contraseña de MySQL
        database="hotel_ecomusic"  # Reemplaza con el nombre de tu base de datos
    )

# Función para insertar un registro
def insertar_registro():
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO reservas_tkinter (codigo, check_in, checkout, nombre, apellido, pais, rut_pasaporte, celular, direccion, correo, estado, tipo, habitacion, adultos, ninos, procedencia, pago, estado2, precio, noches, estado_pago, precio_unitario, transbank, comentario, facturado, tipo_documento, folio_factura)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (codigo_entry.get(), check_in_entry.get(), checkout_entry.get(), nombre_entry.get(), apellido_entry.get(), pais_entry.get(), rut_pasaporte_entry.get(), celular_entry.get(), direccion_entry.get(), correo_entry.get(), estado_entry.get(), tipo_entry.get(), habitacion_entry.get(), adultos_entry.get(), ninos_entry.get(), procedencia_entry.get(), pago_entry.get(), estado2_entry.get(), precio_entry.get(), noches_entry.get(), estado_pago_entry.get(), precio_unitario_entry.get(), transbank_entry.get(), comentario_entry.get(), facturado_entry.get(), tipo_documento_entry.get(), folio_factura_entry.get())
        cursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Éxito", "Registro insertado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al insertar el registro: {e}")
    finally:
        cursor.close()
        conn.close()

# Función para listar registros
def listar_registros():
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM reservas_tkinter"
        cursor.execute(query)
        registros = cursor.fetchall()
        
        # Limpiar lista de registros
        for row in registros_listbox.get(0, tk.END):
            registros_listbox.delete(0)

        # Insertar registros en el Listbox
        for row in registros:
            registros_listbox.insert(tk.END, row)
    except Exception as e:
        messagebox.showerror("Error", f"Error al listar registros: {e}")
    finally:
        cursor.close()
        conn.close()

# Función para eliminar un registro
def eliminar_registro():
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        registro_seleccionado = registros_listbox.get(tk.ACTIVE)  # Obtener el registro seleccionado
        if not registro_seleccionado:
            messagebox.showwarning("Advertencia", "Selecciona un registro para eliminar.")
            return
        
        id_registro = registro_seleccionado[0]  # El primer valor (id) es el que se usa para eliminar
        query = "DELETE FROM reservas_tkinter WHERE id = %s"
        cursor.execute(query, (id_registro,))
        conn.commit()
        messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
        listar_registros()  # Actualizar la lista
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar el registro: {e}")
    finally:
        cursor.close()
        conn.close()

# Crear ventana de Tkinter
root = tk.Tk()
root.title("Reservas Tkinter")


button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

insertar_button = tk.Button(button_frame, text="Insertar Registro", command=insertar_registro)
insertar_button.grid(row=0, column=0, padx=5)

listar_button = tk.Button(button_frame, text="Listar Registros", command=listar_registros)
listar_button.grid(row=0, column=1, padx=5)

eliminar_button = tk.Button(button_frame, text="Eliminar Registro", command=eliminar_registro)
eliminar_button.grid(row=0, column=2, padx=5)

# Crear Listbox para mostrar registros
registros_listbox = tk.Listbox(root, height=10, width=100)
registros_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la interfaz gráfica
root.mainloop()
