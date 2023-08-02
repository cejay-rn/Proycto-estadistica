import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
data = pd.read_csv('Database evaluadas/android-games.csv')

# Seleccionar una muestra aleatoria del 20% de los datos
sample_data = data.sample(frac=0.05, random_state=42)

# Gráfico de barras: Total de Calificaciones por Juego
plt.figure(figsize=(10, 6))
plt.bar(sample_data['title'], sample_data['total ratings'], color='orange')
plt.xlabel('Juego')
plt.ylabel('Total de Calificaciones')
plt.title('Total de Calificaciones por Juego')
plt.xticks(rotation=90)
plt.tight_layout()

# Gráfico de dispersión: Calificación Promedio vs Instalaciones
plt.figure(figsize=(8, 6))
plt.scatter(sample_data['average rating'], sample_data['installs'], color='blue')
plt.xlabel('Calificación Promedio')
plt.ylabel('Instalaciones')
plt.title('Calificación Promedio vs Instalaciones')
plt.grid(True)
plt.tight_layout()

# Media y Desviación Estándar de Calificaciones
mean_ratings = sample_data['average rating'].mean()
std_ratings = sample_data['average rating'].std()

# Análisis de Crecimiento
mean_growth_30 = sample_data['growth (30 days)'].mean()
mean_growth_60 = sample_data['growth (60 days)'].mean()

# Análisis de Relación entre Calificación y Crecimiento
correlation = sample_data['average rating'].corr(sample_data['growth (30 days)'])

# Imprimir resultados
print(f"Media de Calificaciones: {mean_ratings:.2f}")
print(f"Desviación Estándar de Calificaciones: {std_ratings:.2f}")
print(f"Media de Crecimiento en 30 días: {mean_growth_30:.2f}%")
print(f"Media de Crecimiento en 60 días: {mean_growth_60:.2f}%")
print(f"Correlación entre Calificación y Crecimiento (30 días): {correlation:.2f}")

# Mostrar los gráficos
plt.show()
