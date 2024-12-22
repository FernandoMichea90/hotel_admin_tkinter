import tkinter as tk

class DraggableListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag and Drop List")
        
        # Crear el contenedor de la lista
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)
        
        # Lista inicial de elementos
        self.items = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
        self.labels = []

        # Crear los widgets de la lista
        for index, item in enumerate(self.items):
            label = tk.Label(self.frame, text=item, bg="lightblue", width=20, height=2, relief="raised")
            label.pack(pady=2)
            label.bind("<ButtonPress-1>", self.on_start_drag)
            label.bind("<B1-Motion>", self.on_drag)
            label.bind("<ButtonRelease-1>", self.on_drop)
            self.labels.append(label)

        # Variable para rastrear el índice del elemento en movimiento
        self.dragging_index = None

    def on_start_drag(self, event):
        # Guardar el índice del elemento que se está arrastrando
        widget = event.widget
        self.dragging_index = self.labels.index(widget)
        widget.lift()

    def on_drag(self, event):
        # Mover el elemento con el puntero del ratón
        widget = event.widget
        widget.place(x=0, y=event.y_root - widget.winfo_height() // 2, relwidth=1)

    def on_drop(self, event):
        # Detectar la posición de soltado y reordenar los elementos
        widget = event.widget
        widget.place_forget()

        # Calcular el nuevo índice basado en la posición del ratón
        y_root = event.y_root - self.frame.winfo_rooty()
        new_index = min(len(self.labels) - 1, max(0, y_root // (widget.winfo_height() + 4)))

        # Reordenar elementos en la lista
        if new_index != self.dragging_index:
            self.labels.insert(new_index, self.labels.pop(self.dragging_index))
            self.dragging_index = None

        # Reorganizar visualmente la lista
        for label in self.labels:
            label.pack_forget()
        for label in self.labels:
            label.pack(pady=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DraggableListApp(root)
    root.mainloop()
