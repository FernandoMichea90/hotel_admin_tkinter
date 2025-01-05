from tkinter import *
from tkinter import ttk
from sqlalchemy.orm import sessionmaker
from Utils.Database import engine
from Controller.categoria_controller import crear_categoria, listar_categorias, eliminar_categoria
from Controller.gasto_controller import listar_gastos

# Crear la sesión de la base de datos
Session = sessionmaker(bind=engine)
db = Session()

class gastosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Gastos")

        # Categorías
        Label(root, text="Categorías").grid(row=0, column=0, padx=10, pady=10)
        self.categoria_entry = Entry(root)
        self.categoria_entry.grid(row=0, column=1, padx=10, pady=10)
        Button(root, text="Agregar Categoría", command=self.agregar_categoria).grid(row=0, column=2, padx=10, pady=10)

        self.categorias_list = ttk.Treeview(root, columns=("ID", "Nombre"), show="headings")
        self.categorias_list.heading("ID", text="ID")
        self.categorias_list.heading("Nombre", text="Nombre")
        self.categorias_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Cargar categorías
        self.cargar_categorias()

    def cargar_categorias(self):
        for item in self.categorias_list.get_children():
            self.categorias_list.delete(item)

        categorias = listar_categorias(db)
        for cat in categorias:
            self.categorias_list.insert("", "end", values=(cat.id, cat.nombre))

    def agregar_categoria(self):
        nombre = self.categoria_entry.get()
        if nombre:
            crear_categoria(db, nombre)
            self.cargar_categorias()
            self.categoria_entry.delete(0, END)

