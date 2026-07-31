# UN MODELO POBLACIONAL DE ACTIVACIÓN NEURONAL CON ACOPLAMIENTO DE VOLTAJE


En el siguiente repositorio se encuentran los códigos utilizados para realizar las simulaciones numéricas presentadas en este trabajo. Con el fin de facilitar su organización y consulta, el repositorio se divide en dos directorios principales, **SIMU** y **OTROSIMU**, cada uno destinado a un conjunto específico de experimentos numéricos. A su vez, cada directorio está estructurado de acuerdo con los objetivos particulares de las simulaciones que contiene, como se describe a continuación.

## PSEUDOCODIGO

## Esquema de volúmenes finitos

**Entrada**

- Promedios celulares iniciales \(u_{i,k}^{0}\).
- Potencial de membrana inicial \(v_k^{0}\).
- Parámetros de la malla \(\Delta t\), \(\Delta s\) y \(\Delta x\).

**Salida**

- Solución aproximada
  $$
  \{(u_{i,k}^{n},v_k^{n})\}_{n=0}^{N_t}.
  $$

1. Calcular los promedios celulares de la densidad inicial.

2. Para \(n=0,\ldots,N_t-1\):

   1. Calcular los términos de interacción
      \(G_{i,k}^{\,n}\), para todo \((i,k)\in\mathbb{N}\times I_K\).

   2. Calcular el término de interacción
      \(H_k^{\,n}\), para todo \(k\in I_K\).

   3. Calcular
      \(u_{i,k}^{\,n+1}\), para todo \((i,k)\in\mathbb{N}\times I_K\).

   4. Calcular
      \(v_k^{\,n+1}\), para todo \(k\in I_K\).

   5. Calcular los valores de frontera
      \(u_{0,k}^{\,n+1}\), para todo \(k\in I_K\).

3. Retornar
   $$
   \{(u_{i,k}^{n},v_k^{n})\}_{n=0}^{N_t}.
   $$


## OTROSIMU

La implementación numérica fue desarrollada en **Python** y está organizada en los siguientes archivos principales:

* **Funciones.py**: contiene las funciones auxiliares empleadas en la implementación de los algoritmos numéricos.
* **Main.py**: archivo principal desde el cual se ejecutan las simulaciones.
* **NT.py**: implementa los procedimientos numéricos específicos utilizados por el modelo.

El objetivo de esta implementación es verificar numéricamente la **conservación de masa** del modelo. Como es de esperarse, la masa total se conserva mientras el soporte de la solución permanezca contenido en el dominio computacional. Cuando dicho soporte alcanza el borde artificial introducido al truncar el dominio, comienzan a observarse pérdidas de masa debidas al truncamiento y no al modelo continuo.

El archivo **NT.py** realiza el cálculo de la masa total en cada instante de tiempo y almacena los resultados en el archivo **MM.xlsx**, el cual permite analizar la evolución de esta magnitud a lo largo de la simulación.
