# CNYT
Curso ciencias naturales y tecnologia 
## lab01 
En este laboratorio realizamos la codificacion de una libreria para calcular **operaciones entre numeros complejos**,algunas operaciones implementadas fueron :
- Suma
- Resta
- Multiplicacion
- Division
- Conjugada
- Modulo
- Cartesiano a polares
- Polar a cartesiano
- Retornar fase



Adiciono mi codigo main realizado en python,el codigo main va implementado en caso de querer tener un menu para la ejecucion de la Calculadora de numeros complejos 


```
def main():
    a= [int (i) for i in input("ingrese los primeros numeros: ").strip().split()]
    b= [int (i) for i in input("ingrese los segundos  numeros: ").strip().split()]
    realA=a[0]
    realB=b[0]
    imaA=a[1]
    imaB=b[1]
    operacion=str(input("ingrese que operacion desea hacer: "))
    if operacion == "+":
        suma(realA,realB,imaA,imaB)
    elif operacion =="-":
        resta(realA,realB,imaA,imaB)
    elif operacion =="*":
        multiplicacion(realA,realB,imaA,imaB)
    elif operacion=="/":
        divi(realA,realB,imaA,imaB)
    elif operacion =="conjugado":
        op1=int(input("desea conocer el conjugado 1 o 2 : "))
        if op1==1:
            conjugado(realA,imaA)
        else:
            conjugado(realB,imaB)
    elif operacion =="modulo":
        op1=int(input("desea conocer el modulo 1 o 2 : "))
        if op1==1:
            modulo(realA,imaA)
        else:
            modulo(realB,imaB)
    elif operacion == " cartesianas":
        cartesianas(realA,realB,imaA,imaB):
main()
```
## lab02
Como complemento de la calculadora de complejos, descubrimos que tambien podemos modelar el mundo cuantico con operaciones sobre vectores y matriciales,algunas de estas operaciones implementadas son :

- Adición de vectores complejos.
- Inverso (aditivo) de un vector complejo.
- multiplicación de un escalar por un vector complejo.
- Adición de matrices complejas.
- versa (aditiva) de una matriz compleja.
- Multiplicación de un escalar por una matriz compleja.
- Transpuesta de una matriz/vector
- Conjugada de una matriz/vector
- Adjunta (daga) de una matriz/vector
- Producto de dos matrices (de tamaños compatibles)
- Función para calcular la "acción" de una matriz sobre un vector.
- Producto interno de dos vectores
- Norma de un vector
- Distancia entre dos vectores
- Revisar si una matriz es unitaria
- Revisar si una matriz es Hermitiana
- Producto tensor de dos matrices/vectores


## Test

Para la comprension de la libreria fueron implementadas algunas pruebas sobre cada una de las funciones de la calculadora, si estas no indican un error significa que la implementacion y ejecucuion de las funciones es correcta.

Un ejemplo del codigo de la  implementacion de las pruebas es el siguiente:

```
class TestCases(unittest.TestCase):
    def test_DeberiaSumar(self):
        self.assertEqual(complexCal.suma((-3,-2),(7,-2)),(4, -4))

```
lo que indica es que se va a realizar la prueba de los dos siguientes numeros complejos: (-3-2i),(7-2i) y el resultado es (4-4i).
para cada una de las funciones implementadas en la libreria hay una prueba que muestra la correcta implementacion de esta.




## ¿Para que la importancia de la calculadora de complejos en el mundo cuantico ?

La razon es sencilla y es debido a que todo el mundo cuantico esta represantado por qBits, y estos qBits los podemos representar usando numeros complejos y cualquier variedad de operaciones que podemos hacer sobre ellos , operaciones matriciales,vectoriales y basicas como las que son implementadas en esta calculadora cuantica.


 ![image](https://cdn.pixabay.com/photo/2015/11/15/07/47/geometry-1044090_960_720.jpg) 
 
 
 Foto creada por https://pixabay.com/es/users/geralt-9301/
