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


 ![image](https://cdn.pixabay.com/photo/2015/11/15/07/47/geometry-1044090_960_720.jpg) 
 
 
 Foto creada por https://pixabay.com/es/users/geralt-9301/
