# UN MODELO POBLACIONAL DE ACTIVACIÓN NEURONAL CON ACOPLAMIENTO DE VOLTAJE


En el siguiente repositorio se encuentran los códigos utilizados para realizar las simulaciones numéricas presentadas en este trabajo. Con el fin de facilitar su organización y consulta, el repositorio se divide en dos directorios principales, **SIMU** y **OTROSIMU**, cada uno destinado a un conjunto específico de experimentos numéricos. A su vez, cada directorio está estructurado de acuerdo con los objetivos particulares de las simulaciones que contiene, como se describe a continuación.


## OTROSIMU

La implementación numérica fue desarrollada en **Python** y está organizada en los siguientes archivos principales:

* **Funciones.py**: contiene las funciones auxiliares empleadas en la implementación de los algoritmos numéricos.
* **Main.py**: archivo principal desde el cual se ejecutan las simulaciones.
* **NT.py**: implementa los procedimientos numéricos específicos utilizados por el modelo.

El objetivo de esta implementación es verificar numéricamente la **conservación de masa** del modelo. Como es de esperarse, la masa total se conserva mientras el soporte de la solución permanezca contenido en el dominio computacional. Cuando dicho soporte alcanza el borde artificial introducido al truncar el dominio, comienzan a observarse pérdidas de masa debidas al truncamiento y no al modelo continuo.

El archivo **NT.py** realiza el cálculo de la masa total en cada instante de tiempo y almacena los resultados en el archivo **MM.xlsx**, el cual permite analizar la evolución de esta magnitud a lo largo de la simulación.
