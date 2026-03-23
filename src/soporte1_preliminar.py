# Tratamiento de datos
import pandas as pd 
from IPython.display import display

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

    print('\n\n\033[1m👀 Visualización de las primeras y últimas filas\033[0m\n')
    display(df.head(3))
    display(df.tail(3))
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m🎲 Visualización de filas aleatorias\033[0m\n')
    display(df.sample(3))
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m📏 Dimensión del DataFrame\033[0m\n')
    print(f'Número de filas del DataFrame: {df.shape[0]}')
    print(f'Número de columnas del DataFrame: {df.shape[1]}')
    print('\n\n------------------------------------------------------------------------')
    
    print('\n\n\033[1m🧾 Información general\033[0m\n')
    df.info()
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m❌ Detección de nulos\033[0m\n')
    nulos = df.isnull().sum()
    if nulos.any() > 0:
        print(f"El número de valores nulos de cada columna es: \n\n{nulos[nulos > 0]}\n")    
    else:
        print('No hay nulos')

    nulos_porcentaje = df.isnull().sum() / (df.shape[0])*100
    if nulos_porcentaje.any() > 0:
        print(f"El porcentaje de valores nulos de cada columna es: \n\n{nulos_porcentaje[nulos_porcentaje > 0].round(2)}")
    else:
       pass
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m🔁 Detección de duplicados\033[0m\n')
    print(f'El número de duplicados del dataset es: {df.duplicated().sum()}')
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m🏷️ Nombres de las columnas\033[0m\n')
    display(df.columns)
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m🔢 Estadísticas descriptivas de las variables numéricas\033[0m\n')
    display(df.describe().round(2).T)
    print('\n\n------------------------------------------------------------------------')

    print('\n\n\033[1m🔡 Estadísticas descriptivas de las variables categóricas\033[0m\n')
    display(df.describe(include=['category', 'str']).T)

#------------------------------------------------------------------------------------------