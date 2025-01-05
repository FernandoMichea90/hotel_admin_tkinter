from tkinter import Tk
from tkhtmlview import HTMLLabel

root = Tk()

# Crear un widget HTMLLabel para mostrar emojis coloridos
html_content = "<p style='font-size: 40px;'>🙂 🎉 ❤️</p>"
label = HTMLLabel(root, html=html_content)
label.pack()

root.mainloop()
