import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Datos
fruits = ['apple', 'blueberry', 'cherry', 'orange', 'kiwi', 'strawberry', 'grape', 'pineapple', 'mango', 'peach']
counts = [40, 100, 30, 55, 60, 90, 70, 50, 85, 65]
bar_labels = ['red', 'blue', 'red', 'orange', 'green', 'red', 'purple', 'yellow', 'orange', 'pink']
bar_colors = ['red', 'blue', 'red', 'orange', '#32CD32', 'red', '#8A2BE2', 'yellow', '#FFA500', 'pink']

# Crear un dataframe para los datos
data = {
    'fruit': fruits,
    'count': counts,
    'color': bar_colors
}
df = pd.DataFrame(data)

# Configurar colores en Seaborn
palette = sns.color_palette(bar_colors)

# Crear gráfico de barras
plt.figure(figsize=(5, 3))
sns.barplot(x='fruit', y='count', palette=palette, data=df)

# Agregar etiquetas
plt.title('Gráfico de Barras de Frutas')
plt.xlabel('Frutas')
plt.ylabel('Contador')

# Mostrar gráfico
plt.show()
