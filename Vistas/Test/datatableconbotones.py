import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EditableTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla Editable")
        
        # Crear Treeview
        self.tree = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings", height=8)
        self.tree.heading("col1", text="ID")
        self.tree.heading("col2", text="Nombre")
        self.tree.heading("col3", text="Edad")
        self.tree.column("col1", width=100)
        self.tree.column("col2", width=150)
        self.tree.column("col3", width=100)
        self.tree.pack(pady=10)
        
        # Datos iniciales
        self.data = [
            (1, "Alice", 25),
            (2, "Bob", 30),
            (3, "Charlie", 35),
        ]
        
        # Insertar datos en la tabla
        for row in self.data:
            self.tree.insert("", "end", values=row)
        
        # Botones
        frame = tk.Frame(root)
        frame.pack(pady=10)
        tk.Button(frame, text="Editar", command=self.edit_row).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Eliminar", command=self.delete_row).grid(row=0, column=1, padx=5)
        
    def edit_row(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor selecciona una fila para editar.")
            return
        
        values = self.tree.item(selected_item, "values")
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Fila")
        
        tk.Label(edit_window, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(edit_window)
        id_entry.insert(0, values[0])
        id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(edit_window, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, values[1])
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(edit_window, text="Edad:").grid(row=2, column=0, padx=5, pady=5)
        age_entry = tk.Entry(edit_window)
        age_entry.insert(0, values[2])
        age_entry.grid(row=2, column=1, padx=5, pady=5)
        
        def save_changes():
            new_values = (id_entry.get(), name_entry.get(), age_entry.get())
            self.tree.item(selected_item, values=new_values)
            edit_window.destroy()
        
        tk.Button(edit_window, text="Guardar", command=save_changes).grid(row=3, column=0, columnspan=2, pady=10)
    
    def delete_row(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Por favor selecciona una fila para eliminar.")
            return
        
        confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar esta fila?")
        if confirm:
            self.tree.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = EditableTableApp(root)
    root.mainloop()
