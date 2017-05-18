# Reto Wisconsin Diagnostic Breast Cancer (WDBC)
## Descripcion
El [Wisconsin Diagnostic Breast Cancer (WDBC) dataset](http://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29) es un conjunto de datos de características de imagenes de lunares cancerigenos o no.

Este dataset contiene alrededror de 500 muestras de características extraidas de lunares para determinar cancer de piel. 
El reto es construir un clasificador de que sea capaz de reconocer si el lunar es maligno o benigno


### Variables

la base de datos consiste en 30 desriptores extraidos sobre las imagenes de los lunares. Una descripción puede obtenerse en el archivo `Info_datacancer.txt`



### Objetivo
1. Crear un algoritmo que tome características de entrada, y retorne la clase a la que pertencen los datos (lunar maligno o lunar benigno).
1. Entrenar este algoritmo utilizando los datos de entrenamiento`.
1. Medir el desempeño del algoritmo utilizando los datos de test. El desempeño debe ser medido como
```python
score = n_aciertos / n_audios * 100
```
donde `n_aciertos` es el numero de audios clasificados de forma correcta y `n_audios` es el numero total de audios en el conjunto de test.

### Notas Teoricas
* Esta es una base de datos pequeña, se recomienda el uso de técnicas clasicas de machine learning como arboles de decision o maquinas de soprte vectorial.

### Ejemplo de procesmiento de los datos
Ver procedimiento de [ejemplo](https://github.com/jcvasquezc/supervised-cancer/blob/master/supervised-cancer.ipynb).

##### Requerimientos
*Indica los requerimientos para utilizar el codigo de tu solucion.*

##### Procedimiento
*Indica el procedimiento que se debe seguir para reproducir tu solucion.*

##### Metodo
*Indica el metodo que utilizaste para solucionar el reto.*

##### Resultados
*Indica el metodo que utilizaste para solucionar el reto.*

## Getting Started
Para resolver este reto primero has un [fork](https://help.github.com/articles/fork-a-repo/) de este repositorio y [clona](https://help.github.com/articles/cloning-a-repository/) el fork en tu maquina.

```bash
git clone https://github.com/{username}/supervised-cancer
cd colomb-ia-emoDB
```

*Nota: reemplaza `{username}` con tu nombre de usuario de Github.*

### Requerimientos

* numpy
* jupyter
* scikit-learn

# Starter Code Python
Para iniciar con este reto puedes correr el codigo de Python en Jupyter del archivo `supervised-cancer.ipynb`. Este código que ayudará a cargar y visualizar los datos.

Para iniciar el código solo hay que prender Jupyter en esta carpeta

```bash
jupyter notebook .
```
y abrir el archivo `supervised-cancer.ipynb`.

