import os
import numpy as np
import pandas as pd
import matplotlib

os.system("clear")
print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)

import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'entorno_ventas/ventas_productos.csv'

datos = pd.read_csv(csv_file)
print(datos.columns)
print("\n" + "-" * 50)
print("Datos CSV")
print(datos)

#Precio total por producto
datos['precio_total'] = datos['cantidad'] * datos['precio']
print("\n" + "-" * 50)
print(datos)

#gráfico precio total por producto
plt.figure(figsize=(10, 6))
plt.bar(datos['productos'], datos['precio_total'], color='skyblue')

#etiquetas y título
plt.title('Precio Total por Producto', fontsize=16)
plt.xlabel('Producto', fontsize=14)
plt.ylabel('Precio Total', fontsize=14)

#guarda gráfico como PNG
imagen_guardada = 'entorno_ventas/precio_total_por_producto.png'
plt.tight_layout()
plt.savefig(imagen_guardada)

#mostrar gráfico
plt.show()

# Confirmar tareas realizadas
imagen_guardada
print(imagen_guardada)