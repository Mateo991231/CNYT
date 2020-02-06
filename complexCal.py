from sys import stdin
import math
def suma(a,b):
    realA=a[0]
    imaA=a[1]
    realB=b[0]
    imaB=b[1]
    respuestareal=0
    respuestaima=0
    respuestareal=realA+realB
    respuestaima=imaA+imaB
    return (respuestareal,respuestaima)

def resta(a,b):
    realA=a[0]
    imaA=a[1]
    realB=b[0]
    imaB=b[1]
    respuestareal=0
    respuestaima=0
    respuestareal=realA-realB
    respuestaima=imaA-imaB
    return (respuestareal,respuestaima)

def multiplicacion(a,b):
    realA=a[0]
    imaA=a[1]
    realB=b[0]
    imaB=b[1]
    parteuno=realA*realB-imaA*imaB
    partedos=realA*imaB+realB*imaA
    return (parteuno,partedos)

def divi(a,b):
    realA=a[0]
    imaA=a[1]
    realB=b[0]
    imaB=b[1]
    parteuno=((realA*realB+imaA*imaB)/(realB**2+imaB**2))
    partedos=((realB*imaA-realA*imaB)/(realB**2+imaB**2))
    return (parteuno,partedos)

def conjugado(a):
    real=a[0]
    imaginario=a[1]
    if imaginario<0 :
        return (real,(abs(imaginario)))
    else:
        return (real,imaginario)

def modulo(a):
    real=a[0]
    imaginario=a[1]
    respuesta= ((real**2+imaginario**2)**0.5)
    return (respuesta)

def polarCartesiano(polar):
    hipo=polar[0]
    angu=polar[1]
    return (hipo*math.cos(angu*(math.pi/180)),hipo*math.sin(angu*(math.pi/180)))


def cartesianoPolar(cartesiano):
    angulo=math.atan2(cartesiano[1],cartesiano[0])
    return((cartesiano[0]**2+cartesiano[1]**2)**5,angulo*(180/math.pi))


def fase(num):
    return math.atan2(num[1],num[0])

def sumaVector(a,b):
    par = []
    for i in range (len (a)):
        res = suma(a[i],b[i])
        par.append(res)
    return (par)

def productoVectorEscalar(a,b):
    array = []
    for i in range (len (b)):
        array.append(multiplicacion(a,b[i]))
    return (array)


def productoTensor (a,b):
     for i in range (len(a)):
          res=[]
          for j in range (len(b)):
               res.append(multiplicacion(a[i],b[j]))
          a[i]=res
     return a

