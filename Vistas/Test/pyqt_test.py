import sys
import random
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
    QTableWidget, QTableWidgetItem, QWidget
)
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas
)
from matplotlib.figure import Figure


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard con Gráficos y Tablas 💻")
        self.setGeometry(100, 100, 800, 600)

        # Crear el widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layout principal
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Gráficos (parte superior)
        chart_layout = QHBoxLayout()
        main_layout.addLayout(chart_layout)

        # Gráfico de barras
        self.bar_chart = self.create_bar_chart()
        chart_layout.addWidget(self.bar_chart)

        # Gráfico de líneas
        self.line_chart = self.create_line_chart()
        chart_layout.addWidget(self.line_chart)

        # Tabla (parte inferior)
        self.table = self.create_table()
        main_layout.addWidget(self.table)

    def create_bar_chart(self):
        """Crea un gráfico de barras."""
        figure = Figure(figsize=(5, 3))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()

        # Datos para el gráfico
        categories = ["A", "B", "C", "D", "E"]
        values = [random.randint(10, 100) for _ in categories]

        # Crear el gráfico
        ax.bar(categories, values, color="skyblue")
        ax.set_title("Gráfico de Barras ✔️")
        ax.set_xlabel("Categorías")
        ax.set_ylabel("Valores")

        return canvas

    def create_line_chart(self):
        """Crea un gráfico de líneas."""
        figure = Figure(figsize=(5, 3))
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot()

        # Datos para el gráfico
        x = list(range(1, 11))
        y = [random.randint(10, 100) for _ in x]

        # Crear el gráfico
        ax.plot(x, y, marker="o", color="orange", label="Línea de datos")
        ax.set_title("Gráfico de Líneas")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()

        return canvas

    def create_table(self):
        """Crea una tabla con datos aleatorios."""
        table = QTableWidget()
        table.setRowCount(10)  # Número de filas
        table.setColumnCount(3)  # Número de columnas
        table.setHorizontalHeaderLabels(["Columna 1", "Columna 2", "Columna 3"])

        # Llenar la tabla con datos
        for row in range(10):
            for col in range(3):
                item = QTableWidgetItem(str(random.randint(1, 100))+f"📌")
                table.setItem(row, col, item)

        return table


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())
