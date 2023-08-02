import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Leer el archivo CSV
data = pd.read_csv('Database evaluadas/Netflix Userbase.csv')

# Elegir una muestra aleatoria del 20% del conjunto de datos
sample_size = int(len(data) * 0.2)
random_sample = data.sample(sample_size, random_state=42)

# Análisis Visual: Gráfico de barras para mostrar la distribución de los tipos de suscripción
subscription_counts = random_sample['Subscription Type'].value_counts()
subscription_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Tipo de Suscripción')
plt.ylabel('Cantidad de Usuarios')
plt.title('Distribución de Tipos de Suscripción')
plt.show()

# Descripción de Variables
print("Descripción de Variables:")
print("Ingresos Mensuales:\n", random_sample['Monthly Revenue'].describe())
print("\nEdades:\n", random_sample['Age'].describe())

# Histogramas de Ingresos Mensuales y Edades
plt.hist(random_sample['Monthly Revenue'], bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Ingresos Mensuales')
plt.ylabel('Frecuencia')
plt.title('Histograma de Ingresos Mensuales')
plt.show()

plt.hist(random_sample['Age'], bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.title('Histograma de Edades')
plt.show()

# Media y Desviación Estándar de Ingresos Mensuales y Edades
print("\nMedia de Ingresos Mensuales:", random_sample['Monthly Revenue'].mean())
print("Desviación Estándar de Ingresos Mensuales:", random_sample['Monthly Revenue'].std())
print("\nMedia de Edades:", random_sample['Age'].mean())
print("Desviación Estándar de Edades:", random_sample['Age'].std())

# Análisis de Correlación (No se implementará en este código)

# Análisis de Conversión de Distribución (No se implementará en este código)

# Análisis de Regresión (No se implementará en este código)
