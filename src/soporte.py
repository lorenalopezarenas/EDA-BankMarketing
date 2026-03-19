# Tratamiento de datos
import pandas as pd 
from IPython.display import display

# Visualización de librerías
import seaborn as sns
import matplotlib.pyplot as plt


# ------------------------------FUNCIONES------------------------------

# Función para un análisis rápido
def analisis_rapido (df, n=3):
    """Función que genera un análisis rápido del DataFrame.

    Args:
        df: Dataframe
        n: número de filas (por defecto = 3)
    """
    print(f'\nLas {n} primeras filas del Dataframe son:')
    display(df.head(n))

    print(f'\nLa información básica del Dataframe es la siguiente:')
    display(df.info())

    print(f'\nEl número de nulos por columna del Dataframe es:')
    display(df.isnull().sum())



# Función para un análisis de columnas
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



# Función para mostrar gráficos de barras de columnas categóricas
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
        height = 3
        plt.figure(figsize=(width, height))
        
        sns.countplot(x=col, data=df, order=df[col].value_counts().index, color='darkmagenta')
        plt.title(f"Distribución de {col}")
        plt.xlabel(col)
        plt.ylabel("Frecuencia")
        
        # Rotar solo las columnas indicadas
        if rotar_columnas and col in rotar_columnas:
            plt.xticks(rotation=angulo, ha='right')
        
        plt.show()




