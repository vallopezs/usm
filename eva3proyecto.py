import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


os.system("clear")
print(pd.__version__)

#asignaturas
asignaturas = ["Matemáticas", "Ciencias", "Historia"]


# notas por estudiantes
notas = np.array([
    [80, 75, 90],  # Estudiante1
    [85, 88, 82],  # Estudiante2
    [70, 80, 85],  # Estudiante3
    [90, 85, 88],  # Estudiante4
    [95, 92, 93]   # Estudiante5
])
print("\n" + "Notas:")
print("-" * 50)
print(f"{'Estudiante':<15}", end="")
for asignatura in asignaturas:
    print(f"{asignatura:<12}", end="")

print("\n" + "-" * 50)

for i, fila in enumerate(notas, start=1):
    print(f"Estudiante{i:<12}", end="")
    for nota in fila:
        print(f"{nota:<12}", end="")
    print()

print("-" * 50)



#promedio por estudiante
promedio_por_estudiante = np.mean(notas, axis=1)
print("\n" + "Promedio por Estudiante:")
print("-" * 50)
for i, promedio in enumerate(promedio_por_estudiante, start=1):
    print(f"Estudiante{i:<12}: {promedio:2f}")
print()

#promedio por asignatura
promedio_por_asignatura = np.mean(notas, axis=0)
print("\n" + "Promedio por Asignatura:")
print("-" * 50)
for asignatura, promedio in zip(asignaturas, promedio_por_asignatura):
    print(f"{asignatura:<12}: {promedio:.2f}")
print()

#desviación estándar de todas las notas
desviacion_estandar = np.std(notas)
print(f"\nDesviación Estándar de las notas: {desviacion_estandar:.2f}")
print()

print("Pandas")
print("-" * 70)

#Convierte el array en un DataFrame de Pandas.
df_notas = pd.DataFrame(
    notas,
    columns=asignaturas,
    index=["Estudiante1", "Estudiante2", "Estudiante3", "Estudiante4", "Estudiante5"]
)
#Agrega una columna llamada Promedio_Estudiante que muestre el promedio de cada estudiante.
df_notas["Promedio_Estudiante"] = promedio_por_estudiante

#Ordena a los estudiantes de mayor a menor según su promedio.
df_notas_ordenado = df_notas.sort_values(by="Promedio_Estudiante", ascending=False)
print(df_notas_ordenado)
print()

print("Matplotlib")
print("-" * 70)

# Crear un gráfico de barras para mostrar el promedio de cada estudiante
plt.figure(figsize=(10, 6))
plt.bar(df_notas_ordenado.index, df_notas_ordenado["Promedio_Estudiante"], color="skyblue")

#etiquetas y título
plt.title("Promedio de Cada Estudiante", fontsize=20)
plt.xlabel("Estudiantes", fontsize=16)
plt.ylabel("Promedio", fontsize=16)
plt.show()


print("Scikit-Learn")
print("-" * 70)
# Usar StandardScaler para estandarizar las notas de los estudiantes
scaler = StandardScaler()
notas_estandarizadas = scaler.fit_transform(notas)

# Convertir las notas estandarizadas en un DataFrame para mejor visualización
df_notas_estandarizadas = pd.DataFrame(
    notas_estandarizadas,
    columns=asignaturas,
    index=["Estudiante1", "Estudiante2", "Estudiante3", "Estudiante4", "Estudiante5"]
)

print("Notas Estandarizadas de los Estudiantes:")
print(df_notas_estandarizadas)