import pandas as pd
import random
import matplotlib.pyplot as plt

# Definir la ruta del archivo CSV
ruta_archivo_csv = 'Database evaluadas/History_of_Mass_Shootings_in_the_USA.csv'

# Leer el archivo CSV en un DataFrame
dataframe = pd.read_csv(ruta_archivo_csv)

# Calcular el tamaño de muestra como el 10% de los datos
tamano_muestra = int(len(dataframe) * 0.1)

# Escoger una muestra aleatoria del DataFrame
muestra_aleatoria = dataframe.sample(n=tamano_muestra)

# Descripción de Variables
print("Descripción de Variables:")
print(dataframe.dtypes)

# Media y Desviación Estándar
columnas_numericas = ['Dead', 'Injured', 'Total']
print("\nMedia y Desviación Estándar:")
for columna in columnas_numericas:
    media = dataframe[columna].mean()
    desviacion_estandar = dataframe[columna].std()
    print(f"{columna}: Media = {media:.2f}, Desviación Estándar = {desviacion_estandar:.2f}")

# Histogramas
print("\nHistogramas:")
dataframe.hist(column=columnas_numericas, bins=10, figsize=(10, 6))
plt.tight_layout()
plt.show()

# Paretograma u otro medio de determinación de priorización para delimitar o segmentar la muestra
print("\nParetograma u otro medio de determinación de priorización para delimitar o segmentar la muestra:")
print(muestra_aleatoria)

# Análisis de Conversión de distribución discreta a distribución continua
# Aquí puedes realizar el análisis si las categorías del histograma son más de 30

# Análisis de Correlación
correlacion = dataframe[['Dead', 'Injured']].corr()
print("\nAnálisis de Correlación:")
print(correlacion)

# Análisis de Regresión Lineal
# Aquí puedes realizar el análisis de regresión lineal si es relevante para el conjunto de datos
