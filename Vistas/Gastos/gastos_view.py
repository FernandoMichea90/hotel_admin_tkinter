import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Controller.gasto_controller import crear_gasto, listar_gastos, eliminar_gasto, actualizar_gasto
from Controller.categoria_controller import listar_categorias
from Vistas.Categorias_Gastos.Categorias_Gastos import Categorias_Vista

class VistaGasto:
    def __init__(self, master):
        
        self.master = master
        self.master.focus_set()  # Establecer el foco en la ventana de configuración
        self.master.bind("<Control-c>", lambda event: self.abrir_configuracion())
        self.frame_padre = tk.Frame(self.master, padx=10, pady=10)
        self.frame_padre.pack(fill="both", expand=True)

        # Crear una nueva sesión con la base de datos        
        # frame para titulo y boton configuracion
        self.frame_titulo = tk.Frame(self.frame_padre)
        self.frame_titulo.pack(fill="x", pady=10)
        # Titulo
        self.titulo = tk.Label(self.frame_titulo, text="Gestión de Gastos", font=("Arial", 15))
        self.titulo.pack(side="left")
        # Boton Configuracion
        self.configuracion_btn = tk.Button(self.frame_titulo, text="Configuración", command=self.abrir_configuracion)
        self.configuracion_btn.pack(side="right")

        # Frame para Información del Gasto y Botones
        self.frame_info_y_botones = tk.Frame(self.frame_padre)
        self.frame_info_y_botones.pack(fill="x", pady=10)

        # Frame para la información del gasto
        self.info_gasto_frame = tk.LabelFrame(self.frame_info_y_botones, text="Información del Gasto", padx=10, pady=10)
        self.info_gasto_frame.pack(side="left", fill="x", expand=True, padx=10)

        # Descripción del Gasto
        self.label_descripcion = tk.Label(self.info_gasto_frame, text="Descripción del Gasto:")
        self.label_descripcion.grid(row=0, column=0, sticky="w")
        self.descripcion_entry = tk.Entry(self.info_gasto_frame)
        self.descripcion_entry.grid(row=0, column=1, sticky="ew", padx=5)

        # Categoría (Con ComboBox)
        self.label_categoria = tk.Label(self.info_gasto_frame, text="Categoría:")
        self.label_categoria.grid(row=1, column=0, sticky="w")
        
        # Cargar categorías desde la base de datos
        self.categorias = listar_categorias()
        self.categorias_nombres = [categoria.nombre for categoria in self.categorias]

        self.categoria_combobox = ttk.Combobox(self.info_gasto_frame, values=self.categorias_nombres)
        self.categoria_combobox.grid(row=1, column=1, sticky="ew", padx=5)

        # Monto del Gasto
        self.label_monto = tk.Label(self.info_gasto_frame, text="Monto del Gasto:")
        self.label_monto.grid(row=2, column=0, sticky="w")
        self.monto_entry = tk.Entry(self.info_gasto_frame)
        self.monto_entry.grid(row=2, column=1, sticky="ew", padx=5)

        # Fecha del Gasto (Formato YYYY-MM-DD)
        self.label_fecha = tk.Label(self.info_gasto_frame, text="Fecha (YYYY-MM-DD):")
        self.label_fecha.grid(row=3, column=0, sticky="w")
        self.fecha_entry = tk.Entry(self.info_gasto_frame)
        self.fecha_entry.grid(row=3, column=1, sticky="ew", padx=5)

        # Método de pago
        self.label_metodo_pago = tk.Label(self.info_gasto_frame, text="Método de Pago:")
        self.label_metodo_pago.grid(row=4, column=0, sticky="w")
        self.metodo_pago_entry = tk.Entry(self.info_gasto_frame)
        self.metodo_pago_entry.grid(row=4, column=1, sticky="ew", padx=5)

        # Proveedor
        self.label_proveedor = tk.Label(self.info_gasto_frame, text="Proveedor:")
        self.label_proveedor.grid(row=5, column=0, sticky="w")
        self.proveedor_entry = tk.Entry(self.info_gasto_frame)
        self.proveedor_entry.grid(row=5, column=1, sticky="ew", padx=5)

        # Notas
        self.label_notas = tk.Label(self.info_gasto_frame, text="Notas:")
        self.label_notas.grid(row=6, column=0, sticky="w")
        self.notas_entry = tk.Entry(self.info_gasto_frame)
        self.notas_entry.grid(row=6, column=1, sticky="ew", padx=5)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.frame_info_y_botones)
        self.frame_botones= tk.LabelFrame(self.frame_info_y_botones, text="Acción",  padx=10, pady=10)
        self.frame_botones.pack(side="right", padx=10, fill="y")

        # Botones
        self.agregar_btn = tk.Button(self.frame_botones, text="Agregar Gasto", command=self.agregar_gasto)
        self.agregar_btn.grid(row=0, column=0, pady=5, sticky="ew")

        self.listar_btn = tk.Button(self.frame_botones, text="Listar Gastos", command=self.listar_gastos)
        self.listar_btn.grid(row=1, column=0, pady=5, sticky="ew")

        self.eliminar_btn = tk.Button(self.frame_botones, text="Eliminar Gasto", command=self.eliminar_gasto)
        self.eliminar_btn.grid(row=2, column=0, pady=5, sticky="ew")
        
        
         # Frame para la tabla de gastos
        self.frame_lista_gastos = tk.Frame(self.frame_padre)  # Frame padre para la tabla
        self.frame_lista_gastos.pack(fill="both", expand=True, padx=10, pady=10)

        # LabelFrame para la lista de gastos
        self.label_frame_lista = tk.LabelFrame(self.frame_lista_gastos, text="Lista de Gastos", padx=10, pady=10)
        self.label_frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        # Tabla para mostrar los gastos usando Treeview
        self.treeview = ttk.Treeview(self.label_frame_lista, columns=("ID", "Descripción", "Categoría", "Monto", "Fecha", "Método de Pago", "Proveedor", "Notas"), show="headings")
        # ajustar el ancho de las columnas 
        self.treeview.column("ID", width=50, anchor="center")
        self.treeview.column("Descripción", width=150)
        self.treeview.column("Categoría", width=100)
        self.treeview.column("Monto", width=100, anchor="center")
        self.treeview.column("Fecha", width=100, anchor="center")
        self.treeview.column("Método de Pago", width=100)
        self.treeview.column("Proveedor", width=100)
        self.treeview.column("Notas", width=100)
        
        
        # Configurar las columnas de la tabla
        self.treeview.heading("ID", text="ID", anchor="center")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.heading("Categoría", text="Categoría")
        self.treeview.heading("Monto", text="Monto")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Método de Pago", text="Método de Pago")
        self.treeview.heading("Proveedor", text="Proveedor")
        self.treeview.heading("Notas", text="Notas")
        
        # crear scroll vertical
        self.scroll_y = ttk.Scrollbar(self.label_frame_lista, orient="vertical", command=self.treeview.yview)
        self.scroll_y.pack(side="right", fill="y")
        self.treeview.configure(yscrollcommand=self.scroll_y.set)
        # crear scroll horizontal
        self.scroll_x = ttk.Scrollbar(self.label_frame_lista, orient="horizontal", command=self.treeview.xview)
        self.scroll_x.pack(side="bottom", fill="x")
        self.treeview.configure(xscrollcommand=self.scroll_x.set)
        
        
        self.treeview.pack(fill="both", expand=True)
        
        self.listar_gastos()
    
   
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

        nuevo_gasto = crear_gasto( descripcion, categoria_id, monto, fecha, metodo_pago, proveedor, notas)
        messagebox.showinfo("Éxito", f"Gasto '{nuevo_gasto.descripcion}' agregado correctamente.")
        self.limpiar_campos()
        self.listar_gastos()

    def abrir_configuracion(self):
        # abrir ventana de configuracion de categorias en una nueva ventana
        # limpiar la ventana principal
        for widget in self.master.winfo_children():
            widget.destroy()
        # crear nuevo frame
        Categorias_Vista(self.master)
        

    def listar_gastos(self):
        # Limpiar las filas existentes en el Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        
        # Obtener los gastos desde la base de datos
        gastos = listar_gastos()
        
        # monta en formato de entero y en formato de miles 
    
        
        # Insertar los datos en el Treeview
        for gasto in gastos:
            int_monto = int(gasto.monto)
            # separar por miles chile 
            monto_chileno = f"{int_monto:,}".replace(",", ".")  # Usa coma como separador y reemplaza por punto

            self.treeview.insert("", "end", values=(
                gasto.id,
                gasto.descripcion,
                gasto.categoria.nombre,  # Asumiendo que 'categoria' es un objeto con 'nombre'
                monto_chileno,
                gasto.fecha,
                gasto.metodo_pago,
                gasto.proveedor,
                gasto.notas
            ))

    def eliminar_gasto(self):
        #gastos seleccionados 
        selected_gasto = self.treeview.selection()
        if selected_gasto:
            gasto_id = self.treeview.item(selected_gasto)['values'][0]
            gasto = eliminar_gasto( int(gasto_id))
            messagebox.showinfo("Éxito", f"Gasto con ID {gasto_id} eliminado.")
            self.listar_gastos()
            self.listar_gastos()
    def limpiar_campos(self):
        self.descripcion_entry.delete(0, tk.END)
        self.categoria_combobox.set('')
        self.monto_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.metodo_pago_entry.delete(0, tk.END)
        self.proveedor_entry.delete(0, tk.END)
        self.notas_entry.delete(0, tk.END)


