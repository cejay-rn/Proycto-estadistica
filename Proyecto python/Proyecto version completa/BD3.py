import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Leer el archivo CSV
data = pd.read_csv('Database evaluadas/public_data.csv')

# Elegir una muestra aleatoria del 20% del conjunto de datos
sample_size = int(len(data) * 0.1)
random_sample = data.sample(sample_size, random_state=42)

# Análisis Visual: Gráfico de líneas para representar la tendencia de ventas a lo largo del tiempo
plt.plot(random_sample['DATE'], random_sample['AMOUNT'], marker='o')
plt.xlabel('Fecha de Transacción')
plt.ylabel('Monto Total de Ventas')
plt.title('Tendencia de Ventas a lo largo del Tiempo')
plt.xticks(rotation=45)
plt.show()

# Análisis Visual: Gráfico de barras para mostrar la distribución de los montos de ventas y los impuestos por día
plt.bar(random_sample['DATE'], random_sample['AMOUNT'], label='Monto de Ventas')
plt.bar(random_sample['DATE'], random_sample['TAXES'], label='Impuestos', bottom=random_sample['AMOUNT'])
plt.xlabel('Fecha de Transacción')
plt.ylabel('Montos')
plt.title('Distribución de Montos de Ventas y Impuestos por Día')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# Descripción de Variables
print("Descripción de Variables:")
print("Monto Total de Ventas (AMOUNT):\n", random_sample['AMOUNT'].describe())
print("\nImpuestos Asociados (TAXES):\n", random_sample['TAXES'].describe())

# Histogramas de Montos de Ventas y Impuestos
plt.hist(random_sample['AMOUNT'], bins=10, edgecolor='black', alpha=0.7, label='Monto de Ventas')
plt.hist(random_sample['TAXES'], bins=10, edgecolor='black', alpha=0.7, label='Impuestos')
plt.xlabel('Montos')
plt.ylabel('Frecuencia')
plt.title('Histogramas de Montos de Ventas e Impuestos')
plt.legend()
plt.show()

# Media y Desviación Estándar
print("\nMedia de Monto Total de Ventas (AMOUNT):", random_sample['AMOUNT'].mean())
print("Desviación Estándar de Monto Total de Ventas (AMOUNT):", random_sample['AMOUNT'].std())
print("\nMedia de Impuestos Asociados (TAXES):", random_sample['TAXES'].mean())
print("Desviación Estándar de Impuestos Asociados (TAXES):", random_sample['TAXES'].std())

# Análisis de Correlación
correlation_matrix = random_sample[['AMOUNT', 'TAXES']].corr()
print("\nMatriz de Correlación:\n", correlation_matrix)

# Análisis de Conversión de Distribución (No se implementará en este código)

# Análisis de Regresión (No se implementará en este código)
