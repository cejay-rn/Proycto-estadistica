import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV (cambiar 'ruta_del_archivo.csv' por la ruta correcta)
data = pd.read_csv('Database evaluadas/Cyber_security.csv')

# Obtener una muestra aleatoria del 10% de los datos
random_sample = data.sample(frac=0.1, random_state=42)

# Obtener información sobre las variables y tipos de datos
variables_info = random_sample.dtypes

# Análisis Visual
# Crear gráficas de barra para variables categóricas
categorical_columns = random_sample.select_dtypes(include=['object']).columns
for col in categorical_columns:
    sns.countplot(x=col, data=random_sample)
    plt.title(f'Gráfica de Barras para {col}')
    plt.xticks(rotation=45)
    plt.show()

# Crear gráficas de pastel para variables categóricas
for col in categorical_columns:
    random_sample[col].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
    plt.title(f'Gráfica de Pastel para {col}')
    plt.ylabel('')
    plt.show()

# Histogramas
numeric_columns = random_sample.select_dtypes(include=['float', 'int']).columns
random_sample[numeric_columns].hist(figsize=(10, 6), bins=10)
plt.suptitle('Histogramas de las Variables Numéricas', fontsize=16)
plt.subplots_adjust(top=0.9)
plt.show()

# Media y Desviación Estándar
means = random_sample[numeric_columns].mean()
stds = random_sample[numeric_columns].std()

# Análisis de Correlación
correlation_matrix = random_sample[numeric_columns].corr()

# Gráfica de Mapa de Calor para la Correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
plt.title('Mapa de Calor de Correlación', fontsize=16)
plt.show()

# Imprimir Descripción de Variables
print("Descripción de Variables:")
print(variables_info)

# Imprimir Media y Desviación Estándar
print("\nMedia de las variables numéricas:")
print(means)
print("\nDesviación Estándar de las variables numéricas:")
print(stds)

