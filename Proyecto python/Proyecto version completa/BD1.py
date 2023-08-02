import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
data = pd.read_csv('Database evaluadas/LAC_gender_life_death_indices_20230703.csv')


# Análisis Visual: Gráficos de barra para comparar la esperanza de vida de las mujeres en diferentes países
plt.bar(data['country'], data['le_f'])
plt.xlabel('País')
plt.ylabel('Esperanza de Vida de las Mujeres')
plt.title('Esperanza de Vida de las Mujeres en Países de América Latina y el Caribe')
plt.xticks(rotation=90)
plt.show()

# Análisis Visual: Gráficos de pastel para mostrar la distribución de femicidios en la región
data['femicides_number'].plot(kind='pie', labels=data['country'], autopct='%1.1f%%')
plt.title('Distribución de Femicidios en Países de América Latina y el Caribe')
plt.ylabel('')
plt.show()

# Descripción de Variables
print("Descripción de Variables:")
print("Población Femenina (fem_pop):\n", data['fem_pop'].describe())
print("\nEsperanza de Vida de las Mujeres (le_f):\n", data['le_f'].describe())
print("\nTasa de Mortalidad Materna (mmr):\n", data['mmr'].describe())
print("\nÍndice de Paz Global (gpi):\n", data['gpi'].describe())
print("\nNúmero de Femicidios (femicides_number):\n", data['femicides_number'].describe())

# Histograma de la Tasa de Mortalidad Materna
plt.hist(data['mmr'], bins=10, edgecolor='black')
plt.xlabel('Tasa de Mortalidad Materna')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Tasa de Mortalidad Materna en América Latina y el Caribe')
plt.show()

# Media y Desviación Estándar
print("\nMedia de Esperanza de Vida de las Mujeres (le_f):", data['le_f'].mean())
print("Desviación Estándar de Esperanza de Vida de las Mujeres (le_f):", data['le_f'].std())
print("\nMedia de Tasa de Mortalidad Materna (mmr):", data['mmr'].mean())
print("Desviación Estándar de Tasa de Mortalidad Materna (mmr):", data['mmr'].std())

# Análisis de Correlación
correlation_matrix = data[['fem_pop', 'le_f', 'mmr', 'gpi', 'femicides_number']].corr()
print("\nMatriz de Correlación:\n", correlation_matrix)

# Análisis de Conversión de Distribución (No se implementará en este código)

# Análisis de Regresión Lineal (No se implementará en este código)
