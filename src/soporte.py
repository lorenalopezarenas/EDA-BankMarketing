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



# Función para mostrar gráficos de bigotes de las columnas numéricas
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



def number_vs_target(df, target):
    col_num = df.select_dtypes(include='number').columns 
    
    for col in col_num:
            
        plt.figure(figsize=(6,4))
        sns.boxplot(x=target, y=col, data=df, color='darkmagenta')
        plt.title(f"{col} vs {target}")
        plt.show()



def category_vs_target(df, target):

     col_cat = df.select_dtypes(include=['category', 'str'])

     for col in col_cat:
          if col == target: 
               continue
          # Contamos los valores de cada categoría solo para 'yes'
          yes_counts = df[df[target]=='yes'][col].value_counts()
          # Ordenamos las categorías de mayor a menor según 'yes'
          order_categories = yes_counts.index.tolist()
     
          # Ajustamos las gráficas al número de categorías
          num_categories = df[col].nunique()
          width = max(4, num_categories)
          height = 2
          plt.figure(figsize=(width, height))

          # Definimos un palette personalizado 
          palette_custom = {'no': 'darkgray', 'yes': 'darkmagenta'}

          # Creamos los gráficos 
          sns.countplot(x=col, hue=target, data=df, palette=palette_custom, order=order_categories)
          plt.xticks(rotation=45)
          plt.title(f"{col} vs {target}")
          plt.show()
