import pandas as pd
import random
import matplotlib.pyplot as plt
import re

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv('Database evaluadas/coursea_data.csv')

# Obtener una muestra aleatoria del 30% del tamaño del conjunto de datos
random_sample = data.sample(frac=0.3, random_state=42)

# Función para convertir los valores en la columna 'course_students_enrolled' a números enteros
def convert_students_enrolled(value):
    # Buscar patrones de números con sufijos 'k' o 'M'
    pattern = r'^([\d.]+)([kM]?)$'
    match = re.match(pattern, value)
    if match:
        number = float(match.group(1))
        suffix = match.group(2)
        if suffix == 'k':
            return int(number * 1000)
        elif suffix == 'M':
            return int(number * 1000000)
        else:
            return int(number)
    else:
        return 0

# Aplicar la función a la columna 'course_students_enrolled'
random_sample['course_students_enrolled'] = random_sample['course_students_enrolled'].fillna('0').apply(convert_students_enrolled)

# Análisis Visual - Gráfico de barras para el nivel de dificultad
difficulty_counts = random_sample['course_difficulty'].value_counts()
plt.bar(difficulty_counts.index, difficulty_counts.values)
plt.xlabel('Nivel de Dificultad')
plt.ylabel('Cantidad de Cursos')
plt.title('Distribución de Nivel de Dificultad de Cursos en Muestra Aleatoria')
plt.show()

# Análisis Visual - Gráfico de dispersión para la calificación y número de estudiantes inscritos
plt.scatter(random_sample['course_rating'], random_sample['course_students_enrolled'], alpha=0.5)
plt.xlabel('Calificación del Curso')
plt.ylabel('Número de Estudiantes Inscritos')
plt.title('Relación entre Calificación del Curso y Número de Estudiantes Inscritos')
plt.show()

# Resto del análisis, descripción de variables, histogramas, etc. (como se mencionó anteriormente)



# Descripción de Variables
print("\nDescripción de Variables:")
print("-" * 30)
print("Cantidad total de cursos:", len(data))
print("Cantidad de cursos en muestra aleatoria:", len(random_sample))
print("\nDetalle de la muestra aleatoria:")
print(random_sample[['id', 'course_title', 'course_organization', 'course_rating', 'course_difficulty', 'course_students_enrolled']].to_string(index=False))

# Media y Desviación Estándar
print("\nMedia y Desviación Estándar:")
print("-" * 30)
print("Media de calificación del curso:", random_sample['course_rating'].mean())
print("Desviación estándar de calificación del curso:", random_sample['course_rating'].std())
print("Media de estudiantes inscritos:", random_sample['course_students_enrolled'].mean())
print("Desviación estándar de estudiantes inscritos:", random_sample['course_students_enrolled'].std())

# Análisis de Correlación
print("\nAnálisis de Correlación:")
print("-" * 30)
correlation = random_sample['course_rating'].corr(random_sample['course_students_enrolled'])
print("Correlación entre calificación del curso y estudiantes inscritos:", correlation)

# Histogramas
plt.hist(random_sample['course_rating'], bins=10, alpha=0.5, color='blue')
plt.xlabel('Calificación del Curso')
plt.ylabel('Frecuencia')
plt.title('Histograma de Calificación del Curso en Muestra Aleatoria')
plt.show()

plt.hist(random_sample['course_students_enrolled'], bins=10, alpha=0.5, color='green')
plt.xlabel('Número de Estudiantes Inscritos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Estudiantes Inscritos en Muestra Aleatoria')
plt.show()
