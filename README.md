# GitHub-ED-01.02-Students
Analisis y prepocesamiento de datos del dataset Students Performance

# Análisis del rendimiento académico de estudiantes

## Descripción

Este proyecto realiza un análisis exploratorio de un conjunto de datos sobre el rendimiento académico de estudiantes.

El objetivo es analizar los resultados obtenidos en:

- Matemáticas
- Lectura
- Escritura

También se busca encontrar algunos patrones relacionados con el rendimiento de los estudiantes, como el curso de preparación y el nivel educativo de los padres.

## Tecnologías utilizadas

Para realizar el análisis se utilizaron:

- Python
- Pandas
- Matplotlib

## Dataset

El dataset utilizado es `StudentsPerformance.csv`.

El archivo contiene información de 1000 estudiantes y 8 variables:

- `gender`
- `race/ethnicity`
- `parental level of education`
- `lunch`
- `test preparation course`
- `math score`
- `reading score`
- `writing score`

## Análisis realizado

Primero se realizó una exploración inicial del dataset para conocer:

- Número de registros.
- Número de columnas.
- Nombres de las variables.
- Tipos de datos.
- Valores faltantes.
- Registros duplicados.
- Estadísticas descriptivas.

Después se creó una nueva variable llamada `average_score`, que representa el promedio de las calificaciones de Matemáticas, Lectura y Escritura de cada estudiante.

También se creó una clasificación del rendimiento académico:

| Promedio | Categoría |
|----------|-----------|
| 0 - 59   | Bajo      |
| 60 - 79  | Medio     |
| 80 - 100 | Alto      |

## Preguntas analizadas

Se realizaron diferentes análisis para responder preguntas sobre los datos:

1. ¿Cuál de las tres áreas tiene el promedio más alto?
2. ¿Los estudiantes que realizaron el curso de preparación presentan mejores resultados?
3. ¿Existen diferencias en el rendimiento según el nivel educativo de los padres?
4. ¿Qué porcentaje de estudiantes pertenece a cada nivel de rendimiento?

## Visualizaciones

Se realizaron tres gráficas utilizando Matplotlib:

1. Promedio de cada materia.
2. Cantidad de estudiantes por nivel de rendimiento.
3. Promedio según el curso de preparación.

## Resultados principales

El promedio más alto de las tres áreas corresponde a **Lectura**, con aproximadamente **69.17 puntos**.

Los estudiantes que completaron el curso de preparación obtuvieron un promedio mayor que los estudiantes que no lo realizaron.

También se encontraron diferencias en el promedio de los estudiantes dependiendo del nivel educativo de los padres.

En cuanto a la clasificación del rendimiento:

- 27.4% de los estudiantes tiene rendimiento bajo.
- 51.2% tiene rendimiento medio.
- 21.4% tiene rendimiento alto.

## Cómo ejecutar el proyecto

### 1. Instalar Python

Es necesario tener Python instalado en el equipo.

### 2. Instalar las librerías

Ejecutar:

```bash
pip install pandas matplotlib