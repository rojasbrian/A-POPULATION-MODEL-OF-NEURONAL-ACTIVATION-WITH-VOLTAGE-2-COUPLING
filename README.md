# UN MODELO POBLACIONAL DE ACTIVACIÓN NEURONAL CON ACOPLAMIENTO DE VOLTAJE


En el siguiente repositorio se encuentran los códigos utilizados para realizar las simulaciones numéricas presentadas en este trabajo. Con el fin de facilitar su organización y consulta, el repositorio se divide en dos directorios principales, **SIMU** y **OTROSIMU**, cada uno destinado a un conjunto específico de experimentos numéricos. A su vez, cada directorio está estructurado de acuerdo con los objetivos particulares de las simulaciones que contiene, como se describe a continuación.

## PSEUDOCODIGO

## Esquema de volúmenes finitos

### Entrada

- `u_{i,k}^{0}`: promedios celulares iniciales de la densidad neuronal.
- `v_k^{0}`: aproximación inicial del potencial de membrana.
- `Δt`: paso temporal.
- `Δs`: tamaño de la discretización de la variable de edad.
- `Δx`: tamaño de la discretización espacial.
- `N_t`: número total de pasos de tiempo.

### Salida

- Aproximación numérica de la solución
  \((u_{i,k}^{n},\,v_k^{n})\) para todos los instantes
  \(n=0,\ldots,N_t\).

### Algoritmo

1. Calcular los promedios celulares de la condición inicial.
2. Para cada paso temporal \(n=0,\ldots,N_t-1\):
   1. Calcular los términos de interacción `G_{i,k}^n`.
   2. Calcular el término de interacción `H_k^n`.
   3. Actualizar la densidad neuronal `u_{i,k}^{n+1}`.
   4. Actualizar el potencial de membrana `v_k^{n+1}`.
   5. Imponer la condición de frontera para `u_{0,k}^{n+1}`.
3. Retornar la aproximación numérica completa
   \((u_{i,k}^{n},\,v_k^{n})\).

## OTROSIMU

La implementación numérica fue desarrollada en **Python** y está organizada en los siguientes archivos principales:

* **Funciones.py**: contiene las funciones auxiliares empleadas en la implementación de los algoritmos numéricos.
* **Main.py**: implementa los procedimientos numéricos específicos utilizados por el modelo.
* **NT.py**: archivo principal desde el cual se ejecutan las simulaciones.

El objetivo de esta implementación es verificar numéricamente la **conservación de masa** del modelo. Como es de esperarse, la masa total se conserva mientras el soporte de la solución permanezca contenido en el dominio computacional. Cuando dicho soporte alcanza el borde artificial introducido al truncar el dominio, comienzan a observarse pérdidas de masa debidas al truncamiento y no al modelo continuo.

El archivo **NT.py** realiza el cálculo de la masa total en cada instante de tiempo y almacena los resultados en el archivo **MM.xlsx**, el cual permite analizar la evolución de esta magnitud a lo largo de la simulación.


## SIMU

La implementación numérica fue desarrollada en **Python** y está organizada en los siguientes archivos principales:

* **Funciones.py**: contiene las funciones auxiliares empleadas en la implementación de los algoritmos numéricos.
* **Main.py**: implementa los procedimientos numéricos específicos utilizados por el modelo.
* **NT.py**: archivo principal desde el cual se ejecutan las simulaciones.

Además de estos archivos, este directorio contiene dos carpetas adicionales. En ellas se almacenan los resultados numéricos correspondientes a distintos escenarios de simulación. En particular, los archivos ubicados directamente en este directorio corresponden al **Escenario 0**, mientras que las carpetas anexas contienen los resultados asociados a los demás escenarios considerados.

La carpeta **ESCENARIO2** contiene las simulaciones correspondientes al **Escenario 1** presentado en el documento. Su objetivo es analizar el **período refractario** de las neuronas y estudiar el efecto que este fenómeno tiene sobre la dinámica del modelo.


La carpeta **ESCENARIO 4** contiene las simulaciones correspondientes al **Escenario 2** presentado en este documento. Su objetivo es analizar la influencia del **acoplamiento entre el voltaje y la función de densidad**. Para evidenciar este efecto, el modelo de voltaje se sometió a diferentes estímulos externos, con el fin de estudiar cómo las variaciones del potencial de membrana modifican la evolución de la densidad neuronal. En particular, las simulaciones muestran el impacto de dichos estímulos sobre la densidad de neuronas que acaban de generar un potencial de acción en cada instante de tiempo.



