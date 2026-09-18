import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')  #Sirve para cargar el archivo CSV a Python
print(df.head()) #Sirve para mostrar las primeras 5 filas del df


#Contar los primeros datos del df
print("Número de registros:", df.shape[0])
print("Número de columnas:", df.shape[1]) 


#CONOCER LOS DATOS

print(df.columns) #Muestra los nombres de las columnas

print(df.dtypes) #Tipo de dato de cada columna

print(df.isnull().sum()) #Sirve para monstrar los Valores faltantes

print("Duplicados:", df.duplicated().sum()) #Esto nos sirve para saber si hay registros duplicados en el df

print(df.describe()) #Muestra estadísticas descriptivas del df

