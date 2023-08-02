import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Leer el archivo CSV
data = pd.read_csv('Database evaluadas/Video_Games_Sales_as_at_22_Dec_2016.csv')

# Elegir una muestra aleatoria del 20% del conjunto de datos
sample_size = int(len(data) * 0.2)
random_sample = data.sample(sample_size, random_state=42)

# Análisis Visual: Gráfico de barras para comparar las ventas globales de videojuegos en diferentes plataformas
plt.bar(random_sample['Platform'], random_sample['Global_Sales'])
plt.xlabel('Plataforma')
plt.ylabel('Ventas Globales')
plt.title('Ventas Globales de Videojuegos en Diferentes Plataformas')
plt.xticks(rotation=90)
plt.show()

# Análisis Visual: Gráfico de dispersión para examinar la relación entre las puntuaciones de críticos y las ventas globales
plt.scatter(random_sample['Critic_Score'], random_sample['Global_Sales'])
plt.xlabel('Puntuación de Críticos')
plt.ylabel('Ventas Globales')
plt.title('Relación entre Puntuaciones de Críticos y Ventas Globales')
plt.show()

# Descripción de Variables
print("Descripción de Variables:")
print("Ventas Globales (Global_Sales):\n", random_sample['Global_Sales'].describe())
print("\nPuntuación de Críticos (Critic_Score):\n", random_sample['Critic_Score'].describe())

# Histograma de Puntuaciones de Críticos
plt.hist(random_sample['Critic_Score'], bins=10, edgecolor='black')
plt.xlabel('Puntuación de Críticos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Puntuaciones de Críticos')
plt.show()

# Media y Desviación Estándar
print("\nMedia de Ventas Globales (Global_Sales):", random_sample['Global_Sales'].mean())
print("Desviación Estándar de Ventas Globales (Global_Sales):", random_sample['Global_Sales'].std())
print("\nMedia de Puntuación de Críticos (Critic_Score):", random_sample['Critic_Score'].mean())
print("Desviación Estándar de Puntuación de Críticos (Critic_Score):", random_sample['Critic_Score'].std())

# Análisis de Correlación
correlation_matrix = random_sample[['Global_Sales', 'Critic_Score']].corr()
print("\nMatriz de Correlación:\n", correlation_matrix)

# Análisis de Conversión de Distribución (No se implementará en este código)

# Análisis de Regresión Lineal (No se implementará en este código)
