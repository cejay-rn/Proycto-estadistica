
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
file_path = "Database evaluadas/Sleep_health_and_lifestyle_dataset.csv"
data = pd.read_csv(file_path)

# Seleccionar una muestra aleatoria del 20% del total de datos
sample_data = data.sample(frac=0.2, random_state=42)

# Histograma de Duración del sueño (horas)
plt.figure(figsize=(8, 6))
plt.hist(sample_data['Sleep Duration'], bins=10, color='blue', edgecolor='black')
plt.xlabel('Duración del sueño (horas)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Duración del sueño')

# Calcular y mostrar la media, varianza y desviación estándar de la Duración del sueño
mean_sleep_duration = sample_data['Sleep Duration'].mean()
var_sleep_duration = sample_data['Sleep Duration'].var()
std_sleep_duration = sample_data['Sleep Duration'].std()
plt.axvline(mean_sleep_duration, color='red', linestyle='dashed', linewidth=2, label='Media')
plt.axvline(mean_sleep_duration - std_sleep_duration, color='orange', linestyle='dashed', linewidth=2, label='Desviación Estándar')
plt.axvline(mean_sleep_duration + std_sleep_duration, color='orange', linestyle='dashed', linewidth=2)
plt.legend()

plt.show()

# Gráfico de barras de Nivel de estrés (escala: 1-10)
plt.figure(figsize=(10, 6))
plt.bar(sample_data['Person ID'], sample_data['Stress Level'], color='purple')
plt.xlabel('ID de persona')
plt.ylabel('Nivel de estrés (escala: 1-10)')
plt.title('Nivel de estrés de las personas')
plt.xticks(rotation=90)
plt.show()

# Gráfico de dispersión de Duración del sueño vs. Calidad del sueño
plt.figure(figsize=(8, 6))
plt.scatter(sample_data['Sleep Duration'], sample_data['Quality of Sleep'], color='green')
plt.xlabel('Duración del sueño (horas)')
plt.ylabel('Calidad del sueño (escala: 1-10)')
plt.title('Relación entre Duración del sueño y Calidad del sueño')

# Calcular y mostrar la media, varianza y desviación estándar de la Calidad del sueño
mean_quality_of_sleep = sample_data['Quality of Sleep'].mean()
var_quality_of_sleep = sample_data['Quality of Sleep'].var()
std_quality_of_sleep = sample_data['Quality of Sleep'].std()
plt.axhline(mean_quality_of_sleep, color='red', linestyle='dashed', linewidth=2, label='Media')
plt.axhline(mean_quality_of_sleep - std_quality_of_sleep, color='orange', linestyle='dashed', linewidth=2, label='Desviación Estándar')
plt.axhline(mean_quality_of_sleep + std_quality_of_sleep, color='orange', linestyle='dashed', linewidth=2)
plt.legend()

plt.show()
