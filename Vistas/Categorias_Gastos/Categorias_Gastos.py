from tkinter import *
from tkinter import ttk
from sqlalchemy.orm import sessionmaker
from Controller.categoria_controller import crear_categoria, listar_categorias, eliminar_categoria, actualizar_categoria, obtener_categoria_por_id
from Controller.gasto_controller import listar_gastos

# Crear la sesión de la base de datos

class Categorias_Vista:
    def __init__(self, root):
        self.root = root
        # crear un frame
            # Frame principal para el formulario y botones
        self.frame_form = Frame(self.root)
        self.frame_form.pack(fill="x", padx=10, pady=10)

        # Campo para agregar categoría
        Label(self.frame_form, text="Categoría:").pack(side=LEFT, padx=10, pady=10)
        self.categoria_entry = Entry(self.frame_form)
        self.categoria_entry.pack(side=LEFT, fill="x", padx=10, pady=10, expand=True)

        # Crear los botones
        self.frame_botones = Frame(self.root)
        self.frame_botones.pack(fill="x", padx=10, pady=10)

        # Botón Agregar Categoría
        Button(self.frame_botones, text="Agregar Categoría", command=self.agregar_categoria).pack(side=LEFT, padx=10)

        # Botón para actualizar categoría
        Button(self.frame_botones, text="Actualizar Categoría", command=self.mostrar_categoria_para_actualizar).pack(side=LEFT, padx=10)

        # Botón para eliminar categoría
        Button(self.frame_botones, text="Eliminar Categoría", command=self.eliminar_categoria).pack(side=LEFT, padx=10)

        # Frame para la lista de categorías
        self.frame_lista = Frame(self.root)
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

    def eliminar_categoria(self):
        # Obtener el ID de la categoría seleccionada
        selected_item = self.categorias_list.selection()
        if selected_item:
            item_id = self.categorias_list.item(selected_item)["values"][0]
            eliminar_categoria( item_id)
            self.cargar_categorias()

    def mostrar_categoria_para_actualizar(self):
        # Obtener el ID de la categoría seleccionada
        selected_item = self.categorias_list.selection()
        if selected_item:
            item_id = self.categorias_list.item(selected_item)["values"][0]
            categoria = self.obtener_categoria_por_id(item_id)
            if categoria:
                self.categoria_entry.delete(0, END)
                self.categoria_entry.insert(0, categoria.nombre)
                # Cambiar el botón "Agregar" a "Actualizar"
                self.actualizar_categoria_btn = Button(self.root, text="Actualizar", command=lambda: self.actualizar_categoria(item_id))
                self.actualizar_categoria_btn.grid(row=0, column=2, padx=10, pady=10)

    def actualizar_categoria(self, item_id):
        # Obtener el nuevo nombre de la categoría desde el campo de entrada
        nuevo_nombre = self.categoria_entry.get()
        if nuevo_nombre:
            actualizar_categoria( item_id, nuevo_nombre)
            self.cargar_categorias()
            self.categoria_entry.delete(0, END)
            # Restablecer el botón "Actualizar" a "Agregar"
            self.actualizar_categoria_btn.grid_forget()
            Button(self.root, text="Agregar Categoría", command=self.agregar_categoria).grid(row=0, column=2, padx=10, pady=10)

    def obtener_categoria_por_id(self, categoria_id):
        # Buscar la categoría en la base de datos por ID
        categoria = obtener_categoria_por_id(categoria_id)
        return categoria
