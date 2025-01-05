import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Controller.gasto_controller import crear_gasto, listar_gastos, eliminar_gasto, actualizar_gasto
from Controller.categoria_controller import listar_categorias
from Utils.Database import SessionLocal

class VistaGasto:
    def __init__(self, master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="both", expand=True)

        # Crear una nueva sesión con la base de datos
        self.db = SessionLocal()

        # Descripción del Gasto
        self.label_descripcion = tk.Label(self.frame, text="Descripción del Gasto")
        self.label_descripcion.pack()
        self.descripcion_entry = tk.Entry(self.frame)
        self.descripcion_entry.pack()

        # Categoría (Con ComboBox)
        self.label_categoria = tk.Label(self.frame, text="Categoría")
        self.label_categoria.pack()
        
        # Cargar categorías desde la base de datos
        self.categorias = listar_categorias(self.db)
        self.categorias_nombres = [categoria.nombre for categoria in self.categorias]

        self.categoria_combobox = ttk.Combobox(self.frame, values=self.categorias_nombres)
        self.categoria_combobox.pack()

        # Monto del Gasto
        self.label_monto = tk.Label(self.frame, text="Monto del Gasto")
        self.label_monto.pack()
        self.monto_entry = tk.Entry(self.frame)
        self.monto_entry.pack()

        # Fecha del Gasto (Formato YYYY-MM-DD)
        self.label_fecha = tk.Label(self.frame, text="Fecha (YYYY-MM-DD)")
        self.label_fecha.pack()
        self.fecha_entry = tk.Entry(self.frame)
        self.fecha_entry.pack()

        # Método de pago
        self.label_metodo_pago = tk.Label(self.frame, text="Método de Pago")
        self.label_metodo_pago.pack()
        self.metodo_pago_entry = tk.Entry(self.frame)
        self.metodo_pago_entry.pack()

        # Proveedor
        self.label_proveedor = tk.Label(self.frame, text="Proveedor")
        self.label_proveedor.pack()
        self.proveedor_entry = tk.Entry(self.frame)
        self.proveedor_entry.pack()

        # Notas
        self.label_notas = tk.Label(self.frame, text="Notas")
        self.label_notas.pack()
        self.notas_entry = tk.Entry(self.frame)
        self.notas_entry.pack()

        # Botones
        self.agregar_btn = tk.Button(self.frame, text="Agregar Gasto", command=self.agregar_gasto)
        self.agregar_btn.pack()

        self.listar_btn = tk.Button(self.frame, text="Listar Gastos", command=self.listar_gastos)
        self.listar_btn.pack()

        self.eliminar_btn = tk.Button(self.frame, text="Eliminar Gasto", command=self.eliminar_gasto)
        self.eliminar_btn.pack()

        # Listbox para mostrar los gastos
        self.gastos_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.gastos_listbox.pack()

    def agregar_gasto(self):
        descripcion = self.descripcion_entry.get()
        categoria_nombre = self.categoria_combobox.get()
        monto = self.monto_entry.get()
        fecha = self.fecha_entry.get()
        metodo_pago = self.metodo_pago_entry.get()
        proveedor = self.proveedor_entry.get()
        notas = self.notas_entry.get()

        if not descripcion or not categoria_nombre or not monto or not fecha:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            categoria_id = next((categoria.id for categoria in self.categorias if categoria.nombre == categoria_nombre), None)
            if categoria_id is None:
                raise ValueError("Categoría no válida")

            monto = float(monto)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        nuevo_gasto = crear_gasto(self.db, descripcion, categoria_id, monto, fecha, metodo_pago, proveedor, notas)
        messagebox.showinfo("Éxito", f"Gasto '{nuevo_gasto.descripcion}' agregado correctamente.")
        self.limpiar_campos()

    def listar_gastos(self):
        self.gastos_listbox.delete(0, tk.END)
        gastos = listar_gastos(self.db)
        for gasto in gastos:
            self.gastos_listbox.insert(tk.END, f"{gasto.descripcion} - {gasto.monto} - {gasto.fecha}")

    def eliminar_gasto(self):
        selected_gasto = self.gastos_listbox.curselection()
        if selected_gasto:
            gasto_id = self.gastos_listbox.get(selected_gasto[0]).split(" - ")[0]  # Se asume que el ID es la primera parte del string
            gasto = eliminar_gasto(self.db, int(gasto_id))
            messagebox.showinfo("Éxito", f"Gasto con ID {gasto_id} eliminado.")
            self.listar_gastos()

    def limpiar_campos(self):
        self.descripcion_entry.delete(0, tk.END)
        self.categoria_combobox.set('')
        self.monto_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.metodo_pago_entry.delete(0, tk.END)
        self.proveedor_entry.delete(0, tk.END)
        self.notas_entry.delete(0, tk.END)


