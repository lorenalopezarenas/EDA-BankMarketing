
# <span style="color:darkmagenta">PROYECTO EDA - BANK MARKETING</span>

## <span style="color:gray">**Objetivo del proyecto** 🚀</span>

El objetivo de este proyecto es realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos relacionado con campañas de marketing telefónico realizadas por una institución bancaria portuguesa, con el fin de comprender el comportamiento de los clientes y detectar patrones que puedan influir en la suscripción de un depósito a plazo.

Para ello, se utilizarán Python y la biblioteca Pandas para realizar la transformación, limpieza y análisis descriptivo de los datos, así como la visualización de la información para identificar tendencias, relaciones entre variables y características relevantes de los clientes contactados.

---

## <span style="color:gray">**Fuentes de datos** 📂</span>

Para la realización de este proyecto se han utilizado dos conjuntos de datos relacionados con el comportamiento y perfil de clientes:

### Dataset 1: Bank Marketing Campaign (bank-additional.csv)

Este conjunto de datos contiene información relacionada con las campañas de marketing directo realizadas por el banco, las cuales se llevaron a cabo principalmente mediante llamadas telefónicas a los clientes con el objetivo de promocionar la suscripción de un depósito a plazo.

Cada registro representa una interacción entre el banco y un cliente durante una campaña de marketing. El dataset incluye variables relacionadas con:

- Datos demográficos del cliente, como edad, ocupación, estado civil y nivel educativo.

- Información financiera, como la existencia de préstamos personales o hipotecarios.

- Datos de la campaña de marketing, como el número de contactos realizados o la duración de la llamada.

- Indicadores económicos, como la tasa de variación del empleo o el índice de precios al consumidor.

- Resultado de la campaña, que indica si el cliente finalmente suscribió o no el producto ofrecido.

Este dataset es fundamental para analizar el comportamiento de los clientes durante las campañas de marketing y los factores que influyen en la decisión de contratar el producto.

### Dataset 2: Customer Details (customer-details.xlsx)

Este archivo se encuentra en formato Excel y está dividido en tres hojas, cada una correspondiente a clientes que se incorporaron al banco en diferentes años (2012, 2013 y 2014).

Este conjunto de datos proporciona información adicional sobre el perfil y comportamiento de clientes del banco, incluye:

- Perfil económico (Income)

- Estructura familiar (Kidhome, Teenhome)

- Antigüedad como cliente (Dt_Customer)

- Nivel de interacción digital (NumWebVisitsMonth)

Este dataset complementa la información del primero, permitiendo analizar con mayor profundidad el perfil socioeconómico de los clientes y su comportamiento digital, lo que puede ayudar a entender mejor qué tipo de clientes tienen mayor probabilidad de suscribir productos financieros.

---

## <span style="color:gray">**Estructura del Proyecto** 🗂️</span>

├── data/ # Datos crudos y procesados

├── notebooks/ # Notebooks de Jupyter con el análisis

├── src/ # Funciones

├── README.md # Descripción del proyecto

---

## <span style="color:gray">**Instalación y requisitos** 🛠️</span>

Este proyecto usa Python Python 3.14.0 y requiere las siguientes bibliotecas:
- pandas
- numpy
- matplotlib
- seaborn

---

## <span style="color:gray">**Resultados y conclusiones** 📊</span>

- Las variables macroeconómicas (`employment_variation_rate` y `euribor_3m_rate`) y el historial de campañas (`previous_campaign_outcome`) son los principales factores que influyen en la suscripción.

- Variables personales (`age`, `income`) y financieras (`housing_loan`, `personal_loan`, `default`) tienen poco impacto por sí solas.

- Más contactos en campañas no siempre aumenta suscripciones, por lo que se recomienda optimizar la estrategia de contacto.

- Los modelos predictivos deberían enfocarse en historial de campañas, canal de contacto y variables económicas clave, evitando redundancia por multicolinealidad.
  
---

## <span style="color:gray">**Autor** ✒️</span>
 
Lorena López Arenas