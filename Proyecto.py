import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def cargar_excel():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])

    if file_path:
        try:
            data = pd.read_excel(file_path)
            print("Archivo Excel cargado exitosamente.")
            return data
        except Exception as e:
            print(f"Error al cargar el archivo Excel: {str(e)}")
            return None
    else:
        print("No se seleccionó ningún archivo.")
        return None

def graficas_bar():
    data = cargar_excel()
    if data is not None:
        # Aquí puedes realizar la creación de gráficas de barra para visualizar los datos.
        data.plot(kind='bar', x='Variable', y='Valor')
        plt.title('Gráfica de Barra')
        plt.show()

def graficas_pie():
    data = cargar_excel()
    if data is not None:
        # Aquí puedes realizar la creación de gráficas de pastel para visualizar los datos.
        data.plot(kind='pie', y='Valor', labels=data['Variable'], autopct='%1.1f%%')
        plt.title('Gráfica de Pastel')
        plt.show()

def describir_variables():
    data = cargar_excel()
    if data is not None:
        # Aquí puedes obtener información sobre las variables presentes en el DataFrame,
        # como su tipo (numérico o no numérico), formato de datos, etc.
        print("Información de las variables:")
        print(data.dtypes)
        print("\nResumen estadístico:")
        print(data.describe())

def histogramas_y_tablas_de_frecuencia():
    data = cargar_excel()
    if data is not None:
        # Aquí puedes generar los histogramas y las tablas de frecuencia.
        for column in data.columns:
            if data[column].dtype == 'float64' or data[column].dtype == 'int64':
                # Generar histograma
                plt.figure()
                plt.hist(data[column], bins='auto')
                plt.xlabel(column)
                plt.ylabel('Frecuencia')
                plt.title(f'Histograma de {column}')
                plt.show()

                # Generar tabla de frecuencia
                table = data[column].value_counts().reset_index()
                table.columns = ['Valor', 'Frecuencia']
                print(f"\nTabla de frecuencia de {column}:")
                print(table)
                print("------------------------")
                
            else:
                print(f"\nNo se puede generar el histograma de {column} porque no es una variable numérica.")

def pareto():
    data = cargar_excel()
    if data is not None:
        # Aquí puedes implementar el análisis con Paretograma u otro método de priorización y segmentación.
        # En este ejemplo, asumiremos que quieres aplicar el Paretograma a una columna específica del DataFrame.

        # Ingresa el nombre de la columna en la que deseas aplicar el Paretograma
        columna_paretograma = 'Nombre_Columna'

        if columna_paretograma not in data.columns:
            print(f"La columna '{columna_paretograma}' no está presente en el DataFrame.")
            return

        # Ordenar los datos en orden descendente con base en la columna del Paretograma
        data_sorted = data.sort_values(by=columna_paretograma, ascending=False)

        # Calcular la frecuencia acumulada y la frecuencia relativa acumulada
        data_sorted['Frecuencia_Acumulada'] = data_sorted[columna_paretograma].cumsum()
        data_sorted['Frecuencia_Relativa_Acumulada'] = data_sorted['Frecuencia_Acumulada'] / data_sorted[columna_paretograma].sum()

        # Generar el gráfico del Paretograma
        plt.figure()
        plt.bar(data_sorted.index, data_sorted[columna_paretograma], color='blue', label='Frecuencia')
        plt.plot(data_sorted.index, data_sorted['Frecuencia_Relativa_Acumulada'], color='red', marker='o', label='Frecuencia Relativa Acumulada')
        plt.xlabel('Muestra')
        plt.ylabel('Frecuencia')
        plt.title(f'Paretograma para {columna_paretograma}')
        plt.legend()
        plt.show()

        # Obtener la muestra prioritaria o segmentada
        # Por ejemplo, puedes tomar las primeras N filas según el criterio de priorización.
        N = 5  # Número de filas prioritarias o segmentadas
        muestra_prioritaria = data_sorted.head(N)
        print(f"\nMuestra prioritaria o segmentada en función de '{columna_paretograma}':")
        print(muestra_prioritaria)

# Las funciones para el análisis de conversión de distribución discreta a continua,
# análisis de correlación y análisis de regresión lineal serían más complejas y requerirían
# una descripción más detallada de los datos y la metodología a seguir.

# Puedes estructurar esas funciones siguiendo un enfoque similar al utilizado en las funciones anteriores.

# El código para analizar la distribución discreta a continua puede requerir la implementación de pruebas estadísticas.

# El análisis de correlación y regresión lineal puede involucrar el uso de la librería SciPy o scikit-learn para el cálculo.

def main():
    print("Bienvenido al programa de análisis de bases de datos.")
    while True:
        print("Selecciona una opción:")
        print("1. Presentar gráficas de barra.")
        print("2. Presentar gráficas de pastel.")
        print("3. Describir variables presentes en la base de datos.")
        print("4. Generar histogramas y tablas de frecuencia.")
        print("5. Realizar análisis de Paretograma u otro método de determinación de priorización.")
        print("6. Realizar análisis de correlación.")
        print("7. Realizar análisis de regresión lineal.")
        print("0. Salir")
        opcion = int(input("Opción: "))
        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            graficas_bar()
        elif opcion == 2:
            graficas_pie()
        elif opcion == 3:
            describir_variables()
        elif opcion == 4:
            histogramas_y_tablas_de_frecuencia()
        elif opcion == 5:
            pareto()
        elif opcion == 6:
            # Llamada a la función para análisis de correlación.
            pass
        elif opcion == 7:
            # Llamada a la función para análisis de regresión lineal.
            pass
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
