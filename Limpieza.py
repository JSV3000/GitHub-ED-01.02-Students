import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')  #Sirve para cargar el archivo CSV a Python
print(df.head()) #Sirve para mostrar las primeras 5 filas del df


#Contar los primeros datos del df
print("Número de registros:", df.shape[0])
print("Número de columnas:", df.shape[1]) 

print(df.columns)