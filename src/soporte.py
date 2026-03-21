# Tratamiento de datos
import pandas as pd 
from IPython.display import display

# Visualización de librerías
import seaborn as sns
import matplotlib.pyplot as plt


# ------------------------------FUNCIONES------------------------------

# -------------Función eda_preliminar-------------
def eda_preliminar(df):
    """Realiza un análisis exploratorio preliminar sobre un DataFrame dado.

       Este análisis incluye:
       - Muestra de las 3 primeras y últimas filas.
       - Muestra de 3 filas aleatorias.
       - Dimensión del DataFrame.
       - Información general del DataFrame (nulos, tipos de datos, etc.).
       - Valores nulos por columna (tanto en términos absolutos como relativos).
       - Conteo de valores duplicados.
       - Listado del nombre de las columnas.
       - Estadísticas descriptivas de las variables numéricas.
       - Estadísticas descriptivas de las variables categóricas.

    Args:
        df: DataFrame a analizar
    """

    print('\n\033[1m👀 Visualización de las primeras y últimas filas\033[0m\n')
    display(df.head(3))
    display(df.tail(3))

    print('\n\033[1m🎲 Visualización de filas aleatorias\033[0m\n')
    display(df.sample(3))

    print('\n\n\033[1m📏 Dimensión del DataFrame\033[0m\n')
    print(f'Número de filas del DataFrame: {df.shape[0]}')
    print(f'Número de columnas del DataFrame: {df.shape[1]}')
    
    print('\n\n\033[1m🧾 Información general\033[0m\n')
    df.info()

    print('\n\n\033[1m❌ Detección de nulos\033[0m\n')
    nulos = df.isnull().sum()
    print(f"El número de valores nulos de cada columna es: \n{nulos[nulos > 0]}\n")

    nulos_porcentaje = df.isnull().sum() / (df.shape[0])*100
    print(f"El porcentaje de valores nulos de cada columna es: \n{nulos_porcentaje[nulos_porcentaje > 0].round(2)}")

    print('\n\n\033[1m🔁 Detección de duplicados\033[0m\n')
    print(f'El número de duplicados del dataset es: {df.duplicated().sum()}')

    print('\n\n\033[1m🏷️ Nombres de las columnas\033[0m\n')
    display(df.columns)

    print('\n\n\033[1m🔢 Estadísticas descriptivas de las variables numéricas\033[0m\n')
    display(df.describe().round(2).T)

    print('\n\n\033[1m🔡 Estadísticas descriptivas de las variables categóricas\033[0m\n')
    display(df.describe(include=['category', 'str']).T)

#------------------------------------------------------------------------------------------

# -------------Función para un análisis rápido-------------
def analisis_rapido (df, n=3):
    """Función que genera un análisis rápido del DataFrame.

    Args:
        df: Dataframe
        n: número de filas (por defecto = 3)
    """
    print(f'\nLas {n} primeras filas del Dataframe son:')
    display(df.head(n))

    print(f'\nLa información básica del Dataframe es la siguiente:')
    df.info()

    print(f'\nEl número de nulos por columna del Dataframe es:')
    display(df.isnull().sum())

#------------------------------------------------------------------------------------------

# -------------Función para un análisis de columnas-------------
def columnas_df(df):
    """Función que nos proporciona un análisis de las columnas del DataFrame.

    Args:
        df: DataFrame
    """

    print("Las columnas del DataFrame que estamos analizando son:")
    display(df.columns)

    print("Información básica de las columnas:\n")
    df.info()

    col_num = df.select_dtypes(include='number').columns
    print("\nVariables numéricas:\n\n", col_num)
    col_cat = df.select_dtypes(include=['category', 'str']).columns
    print("\nVariables categóricas:\n\n", col_cat)

    print("\nEstadísticos de las variables numéricas:\n")
    display(df.describe().round(2).T)
    print("\nEstadísticos de las variables categóricas:\n")
    display(df.describe(include=['category', 'str']).T)

#------------------------------------------------------------------------------------------

# -------------Función para mostrar gráficos de bigotes de las columnas numéricas-------------
def boxplots(df):
    """Función que grafica todas las columnas numéricas de un DataFrame.

    Args:
        df: DataFame
    """
    col_num = df.select_dtypes(include='number').columns

    for col in col_num:
        plt.figure(figsize=(6, 1))
        sns.boxplot(x=df[col], color="darkmagenta")
        plt.title(col)
        plt.show()

#------------------------------------------------------------------------------------------

# -------------Función para mostrar gráficos de barras de columnas categóricas-------------
def graficos_categoricos(df, rotar_columnas=None, angulo=45):
    """Función que grafica todas las columnas categóricas de un DataFrame.
    
    Args:
        df: DataFrame
        rotar_columnas: lista de columnas cuyo eje X se debe rotar
        angulo: ángulo de rotación para esas columnas
    """
    
    # Seleccionamos todas las columnas categóricas
    col_cat = df.select_dtypes(include=['category', 'str'])
    
    for col in col_cat:
        num_categories = df[col].nunique()
        width = max(4, num_categories)
        height = 2
        plt.figure(figsize=(width, height))
        
        sns.countplot(x=col, data=df, order=df[col].value_counts().index, color='darkmagenta')
        plt.title(f"Distribución de {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        
        # Rotar solo las columnas indicadas
        if rotar_columnas and col in rotar_columnas:
            plt.xticks(rotation=angulo, ha='right')
        
        plt.show()

#------------------------------------------------------------------------------------------

# -------------Función para mostrar gráficos de caja y bigotes de la variable objetivo vs variable numérica-------------
def number_vs_target(df, target):
    col_num = df.select_dtypes(include='number').columns 
    
    for col in col_num:
            
        plt.figure(figsize=(6,4))
        sns.boxplot(x=target, y=col, data=df, color='darkmagenta')
        plt.title(f"{col} vs {target}")
        plt.show()

#------------------------------------------------------------------------------------------

# -------------Función parael porcentaje de conversión de variables categóricas-------------
def tasa_conversion_cat(df, target):

    col_cat = df.select_dtypes(include=['category', 'str']).columns

    for col in col_cat:
        if col == target:
            continue

        print(f'Variable: {col}')
        
        conversion_rate = df.groupby(col)[target].apply(lambda x: (x == 'yes').mean().round(4)*100) 
        conversion_rate = conversion_rate.sort_values(ascending=False)
        
        print(conversion_rate)
        print('-'*50)

#------------------------------------------------------------------------------------------

# -------------Función para mostrar gráficos de la tasa de conversión de variables categóricas-------------
def grafs_conversion_cat(df, target, rotar_columnas=None, angulo=45):
    """Función que grafica la tasa de conversión de cada categoría de las variables categóricas.

    Args:
        df: DataFrame
        rotar_columnas: lista de columnas cuyo eje X se debe rotar
        angulo: ángulo de rotación para esas columnas (45 por defecto)
    """

    # Seleccionamos todas las columnas categóricas
    col_cat = df.select_dtypes(include=['category', 'str'])

    for col in col_cat:
        if col == target:
            continue
        
        # Función de la tasa de conversión
        conversion_rate = df.groupby(col)[target].apply(lambda x: (x == 'yes').mean()*100).sort_values(ascending=False)
        
        # Ajustamos las gráficas al número de categorías
        num_categories = df[col].nunique()
        width = max(4, num_categories)
        height = 2
        plt.figure(figsize=(width, height))
        
        conversion_rate.plot(kind='bar', color='darkmagenta')
        plt.title(f'Tasa de Conversión por {col}')
        plt.ylabel('Tasa de Conversión (%)')
        plt.xlabel(col)
        
        # Rotar solo las columnas indicadas
        if rotar_columnas and col in rotar_columnas:
            plt.xticks(rotation=angulo, ha='right')
        else:
            plt.xticks(rotation=0, ha='center') 
        
        # Mostrar las gráficas
        plt.show()