# Tratamiento de datos
import pandas as pd 
from IPython.display import display

# Visualización de librerías
import seaborn as sns
import matplotlib.pyplot as plt



# -------------Función para un análisis de columnas-------------
def columnas_df(df):
    """Función que nos proporciona un análisis de las columnas del DataFrame.

    Args:
        df: DataFrame
    """

    print("\n\nLas columnas del DataFrame que estamos analizando son:\n")
    display(df.columns)
    print('------------------------------------------------------------------\n')

    print("Información básica de las columnas:\n")
    df.info()
    print('------------------------------------------------------------------\n')

    col_num = df.select_dtypes(include='number').columns
    print("\nVariables numéricas:\n\n", col_num)
    col_cat = df.select_dtypes(include=['category', 'str']).columns
    print("\n\nVariables categóricas:\n\n", col_cat)
    print('------------------------------------------------------------------\n')

    print("\nEstadísticos de las variables numéricas:\n")
    display(df.describe().round(2).T)
    print("\n\nEstadísticos de las variables categóricas:\n")
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