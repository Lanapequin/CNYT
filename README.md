# CNYT 2024-2
## PRIMER CORTE
### Libreria de números complejos
#### Descripción
Esta librería está diseñada para manejar números complejos, que son fundamentales en la computación cuántica, encontrarás herramientas para realizar operaciones básicas con números complejos, como suma, resta, multiplicación y división, así como funciones para calcular el conjugado, el módulo, conversión entre representaciones polar y cartesiano, en los dos sentidos y la fase de un número complejo.
#### Prerrequisitos
Es necesario tener instalado [Python 3.8](https://www.python.org/)
<p>Para ejecutar las pruebas automaticas es necesario descargar TestLibCplx.py y LibreriaCplx.py, ambos archivos deben estar en una misma carpeta para que se puedan ejecutar las pruebas</p>

#### Ejecutando las pruebas
<p>Para ejecutar las pruebas automaticas se debe abrir el archivo TestLibCplx.py y correrlo.</p>

![alt text](image-1.png)

Para ejecutar cada funcion por tu cuenta solo necesitas pegar el siguiente codigo en LibreriaCplx.py, donde __a__ es un número complejo que se debe representar en forma de pares ordenados, **b** se debe representar de la misma manera.</p>


```python
if __name__ == '__main__':
    a=(3,2.8)
    b=(1.5,-2)
    partReal,partImag=sumaC(a,b)
    prettyPrintingC(partReal,partImag)
    partReal,partImag=multC(a,b)  
    prettyPrintingC(partReal,partImag)
    partReal,partImag=divC(a,b)
    prettyPrintingC(partReal,partImag)
    partReal,partImag=restaC(a,b)
    prettyPrintingC(partReal,partImag)
    print(moduloC(5,2))
    print(conjugadoC(5,-2))
    print(polarC(5,2))
    print(cartesianoC(5,0.6))
    print(faseC(5,2))
```

<p>Puedes usar las funciones que desees y modificar los valores de acuerdo a tus necesidades.</p>

#### Construido con
Este proyecto fue construido con [Python 3.8](https://www.python.org/)
#### Colaboradores
Laura Natalia Perilla Quintero [Lanapequin](https://github.com/Lanapequin)
