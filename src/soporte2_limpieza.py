# Tratamiento de datos
import pandas as pd 
from IPython.display import display

# -------------Función para estandarizar nombres de columnas-------------
def estandar_columns(df):
    """Función que estandariza los nombres de las columnas de un DataFrame dado:
       - Cambio a minúsculas
       - Eliminación de espacios al principio y al final
       - Cambio de espacios intermedios por "_"

    Args:
        df: DataFrame
    """
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

#------------------------------------------------------------------------------------------

# -------------Función para eliminar columnas-------------
def eliminar_columns(df, cols):
    """Función que elimina columnas específicas de un DataFrame dado.

    Args:
        df: DataFrame
        cols: columnas a eliminar
    """
    
    return df.drop(columns=cols)

#------------------------------------------------------------------------------------------

# -------------Función para pasar datos a minúscula-------------
def minus (df, cols):
    """Función que transforma los datos de columnas dadas de una DataFrame a minúsculas.

    Args:
        df: DataFrame
        cols: columnas a modificar
    """
    for col in cols:
        df[col] = df[col].str.lower().str.strip()

#------------------------------------------------------------------------------------------

# -------------Función para pasar sacar los datos únicos de columnas-------------
def datos_unicos(df, cols):
    """Función que muestra los datos únicos de las columnas dadas de un DataFram

    Args:
        df: DataFrame
        cols: columnas a analizar
    """
    for col in cols:
        print(f'\n\nLos datos únicos de la varible {col} son:\n\n {df[col].unique()}\n')
        print('\n-----------------------------------------------------------------')

#------------------------------------------------------------------------------------------

# -------------Función para reemplazar palabras o caracteres de columnas-------------
def reemplazar (df, cols, x, y):
    """Función que sirve para reemplazar palabras o caracteres de columnas dadas de un DataFrame.

    Args:
        df: DataFrame
        cols: columnas en las cuales queremos reemplazar datos
        x: dato a reemplazar
        y: dato por el que reemplazar
    """
    for col in cols:
        df[col] = df[col].str.replace(x,y)

#------------------------------------------------------------------------------------------

# -------------Función para rellenar nulos de columnas categóricas-------------
def rellenar_nulos_cat(df, cols, x):
    """Función que sirve para rellenar los nulos de unas columnas dadas por la categoría indicada.

    Args:
        df: DataFrame
        cols: columnas en las que rellenar los nulos
        x: categoría con la que rellenar (ej: "unknown")
    """
    for col in cols:
       df[col] = df[col].fillna(x) 

#------------------------------------------------------------------------------------------

# -------------Función para rellenar nulos de columnas numéricas-------------
def rellenar_nulos_num(df, cols):
    """Función que sirve para rellenar los nulos de unas columnas dadas por la media.

    Args:
        df: DataFrame
        cols: columnas en las que rellenar los nulos
    """
    for col in cols:
       df[col] = df[col].fillna(df[col].mean()) 

#------------------------------------------------------------------------------------------

# -------------Función para rellenar nulos con la moda-------------
def rellenar_nulos_moda(df, cols):
    """Función que sirve para rellenar los nulos de unas columnas dadas por la moda.

    Args:
        df: DataFrame
        cols: columnas en las que rellenar los nulos
    """
    for col in cols:
        df[col] = df[col].fillna(df[col].mode()[0])

#------------------------------------------------------------------------------------------

# -------------Función para un análisis rápido-------------
def analisis_rapido (df, n=3):
    """Función que genera un análisis rápido del DataFrame.

    Args:
        df: Dataframe
        n: número de filas (por defecto = 3)
    """
    print(f'\n\nLas {n} primeras filas del Dataframe son:\n')
    display(df.head(n))
    print('\n-----------------------------------------------------------')

    print(f'\nLa información básica del Dataframe es la siguiente:\n')
    df.info()
    print('\n-----------------------------------------------------------')

    print(f'\nEl número de nulos por columna del Dataframe es:\n')
    display(df.isnull().sum())

#------------------------------------------------------------------------------------------