import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'Database evaluadas/Salary_Data.csv'  # Reemplazar 'ruta_del_archivo.csv' con la ruta real del archivo CSV
data = pd.read_csv(file_path)

# Seleccionar una muestra aleatoria del 30% de los datos
sample_data = data.sample(frac=0.3, random_state=42)

# Gráfico de barras para el género
gender_counts = sample_data['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values, color='green')
plt.title('Distribución de Empleados por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Empleados')
plt.show()

# Gráfico de barras para el nivel educativo
education_counts = sample_data['Education Level'].value_counts()
plt.bar(education_counts.index, education_counts.values, color='blue')
plt.title('Distribución de Empleados por Nivel Educativo')
plt.xlabel('Nivel Educativo')
plt.ylabel('Cantidad de Empleados')
plt.show()

# Gráfico de barras para el cargo
job_counts = sample_data['Job Title'].value_counts()
plt.bar(job_counts.index, job_counts.values, color='orange')
plt.title('Distribución de Empleados por Cargo')
plt.xlabel('Cargo')
plt.ylabel('Cantidad de Empleados')
plt.xticks(rotation=45, ha='right')
plt.show()

# Gráfico de dispersión para edad vs salario
plt.scatter(sample_data['Age'], sample_data['Salary'], color='purple')
plt.title('Edad vs Salario')
plt.xlabel('Edad')
plt.ylabel('Salario')
plt.show()

# Gráfico de dispersión para años de experiencia vs salario
plt.scatter(sample_data['Years of Experience'], sample_data['Salary'], color='red')
plt.title('Años de Experiencia vs Salario')
plt.xlabel('Años de Experiencia')
plt.ylabel('Salario')
plt.show()

# Media y desviación estándar del salario
mean_salary = sample_data['Salary'].mean()
std_salary = sample_data['Salary'].std()
print(f"Media del Salario: {mean_salary:.2f}")
print(f"Desviación Estándar del Salario: {std_salary:.2f}")

# Análisis de correlación
correlation_matrix = sample_data[['Age', 'Years of Experience', 'Salary']].corr()
print("Matriz de Correlación:")
print(correlation_matrix)

# Análisis comparativo de salario según género, nivel educativo y cargo
comparative_analysis = sample_data.groupby(['Gender', 'Education Level', 'Job Title'])['Salary'].mean()
print("Análisis Comparativo de Salario:")
print(comparative_analysis)
