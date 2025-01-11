from tkinter  import  *
from tkinter import ttk
from tkinter import messagebox
from sqlalchemy.orm import sessionmaker
from Controller.categoria_controller import crear_categoria, listar_categorias, eliminar_categoria, actualizar_categoria, obtener_categoria_por_id
from Controller.gasto_controller import listar_gastos

class Categorias_Vista:
    def __init__(self, master):
        self.master = master
        # Frame Padre
        self.main = Frame(self.master, padx=10, pady=10)
        self.main.pack(fill="both", expand=True)
        
        
        self.frame_titulo =Frame(self.main)
        self.frame_titulo.pack(fill="x", pady=10)
        # Titulo
        self.titulo =Label(self.frame_titulo, text="Gestión de Categorias Gastos", font=("Arial", 15))
        self.titulo.pack(side="left")
        # Boton Configuracion
        self.configuracion_btn =Button(self.frame_titulo, text="Gastos", command=self.abrir_gastos)
        self.configuracion_btn.pack(side="right")
        
        self.main=LabelFrame(self.main, text="Categorías de Gastos", padx=10, pady=10)
        self.main.pack(fill='x', padx=10, pady=10)
        
        # Frame principal para el formulario y botones
        self.frame_form = Frame(self.main)
        # agregar label para el frame
        self.frame_form.pack(fill="x", padx=10, pady=10)

        # Campo para agregar categoría
        Label(self.frame_form, text="Categoría:").pack(side=LEFT, padx=10, pady=10)
        self.categoria_entry = Entry(self.frame_form)
        self.categoria_entry.pack(side=LEFT, fill="x", padx=10, pady=10, expand=True)

        # Crear los botones
        self.frame_botones = Frame(self.main)
        self.frame_botones.pack(fill="x", padx=10, pady=10)

        # Botón Agregar Categoría
        Button(self.frame_botones, text="Agregar Categoría", command=self.agregar_categoria).pack(side=LEFT, padx=10)

        # Botón para actualizar categoría
        Button(self.frame_botones, text="Actualizar Categoría", command=self.mostrar_categoria_para_actualizar).pack(side=LEFT, padx=10)

        # Botón para eliminar categoría
        Button(self.frame_botones, text="Eliminar Categoría", command=self.confirmar_eliminar_categoria).pack(side=LEFT, padx=10)

        # Frame para la lista de categorías
        self.frame_lista = Frame(self.main)
        self.frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        # Lista de categorías (Treeview)
        self.categorias_list = ttk.Treeview(self.frame_lista, columns=("ID", "Nombre"), show="headings")
        self.categorias_list.heading("ID", text="ID")
        self.categorias_list.heading("Nombre", text="Nombre")
        self.categorias_list.pack(fill="both", expand=True)

        # Cargar las categorías desde la base de datos
        self.cargar_categorias()

    def cargar_categorias(self):
        # Limpiar la lista actual
        for item in self.categorias_list.get_children():
            self.categorias_list.delete(item)

        # Obtener categorías desde la base de datos
        categorias = listar_categorias()
        for cat in categorias:
            self.categorias_list.insert("", "end", values=(cat.id, cat.nombre))

    def agregar_categoria(self):
        nombre = self.categoria_entry.get()
        if nombre:
            crear_categoria(nombre)
            self.cargar_categorias()
            self.categoria_entry.delete(0, END)

    def confirmar_eliminar_categoria(self):
        # Obtener el ID de la categoría seleccionada
        selected_item = self.categorias_list.selection()
        if selected_item:
            item_id = self.categorias_list.item(selected_item)["values"][0]

            # Confirmación antes de eliminar
            confirmacion = messagebox.askyesno("Confirmar Eliminación", 
                                               "¿Estás seguro de que deseas eliminar esta categoría?\nEsto eliminará también los gastos asociados.")
            if confirmacion:
                eliminar_categoria(item_id)
                self.cargar_categorias()

    def mostrar_categoria_para_actualizar(self):
        # Obtener el ID de la categoría seleccionada
        selected_item = self.categorias_list.selection()
        if selected_item:
            item_id = self.categorias_list.item(selected_item)["values"][0]
            categoria = self.obtener_categoria_por_id(item_id)
            if categoria:
                self.ventana_actualizar(categoria, item_id)

    def ventana_actualizar(self, categoria, item_id):
        # Crear ventana emergente para actualizar
        ventana_actualizar = Toplevel(self.root)
        ventana_actualizar.title("Actualizar Categoría")
        
        Label(ventana_actualizar, text="Nuevo Nombre de Categoría:").pack(padx=10, pady=10)
        nueva_categoria_entry = Entry(ventana_actualizar)
        nueva_categoria_entry.insert(0, categoria.nombre)  # Prellenar con el nombre actual
        nueva_categoria_entry.pack(padx=10, pady=10)

        # Botón para guardar la actualización
        Button(ventana_actualizar, text="Actualizar", 
               command=lambda: self.actualizar_categoria(item_id, nueva_categoria_entry.get(), ventana_actualizar)).pack(pady=10)

    def actualizar_categoria(self, item_id, nuevo_nombre, ventana_actualizar):
        if nuevo_nombre:
            actualizar_categoria(item_id, nuevo_nombre)
            self.cargar_categorias()
            ventana_actualizar.destroy()  # Cerrar la ventana emergente

    def obtener_categoria_por_id(self, categoria_id):
        # Buscar la categoría en la base de datos por ID
        categoria = obtener_categoria_por_id(categoria_id)
        return categoria
    def abrir_gastos(self):
        # abrir ventana de configuracion de categorias en una nueva ventana
        # limpiar la ventana principal
        for widget in self.master.winfo_children():
            widget.destroy()
        from Vistas.Gastos.gastos_view import VistaGasto
        VistaGasto(self.master)


    