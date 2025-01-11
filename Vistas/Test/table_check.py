import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Treeview with Checkboxes")

    # Creating a Treeview widget
    tree = ttk.Treeview(root, columns=('Name', 'Age', 'Gender'), show='headings')
    tree.pack()

    # Defining columns
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Gender', text='Gender')

    # Sample data
    data = [
        ('John', 25, 'Male'),
        ('Sara', 30, 'Female'),
        ('Mike', 28, 'Male'),
        ('Emma', 22, 'Female'),
    ]

    # Adding rows with checkboxes
    for row in data:
        tree.insert('', tk.END, values=row, tags=('checked',))

    # Adding checkboxes
    def toggle_checkbox(event):
        item = tree.selection()[0]
        if 'checked' in tree.item(item, 'tags'):
            tree.item(item, tags=())
        else:
            tree.item(item, tags=('checked',))

    tree.bind('<ButtonRelease-1>', toggle_checkbox)

    root.mainloop()

if __name__ == "__main__":
    main()
