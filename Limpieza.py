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


# LIMPIEZA DE DATOS
df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1) #Se crea la columna promedio que es el promedio de las 3 columnas de calificaciones
df["average_score"]= df["average_score"].round(2) #Se redondea a 2 decimales la columna promedio
print(df.head())


# CLASIFICACION
df["rendimiento"] = pd.cut(
    df["average_score"], 
    bins=[0, 60, 80, 100], #Se clasifican los rangos
    labels=["Bajo", "Medio", "Alto"]) #Aqui cree la columna rendimiento que clasifica el promedio en Bajo, Medio y Alto

print(df.head())