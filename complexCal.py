from sys import stdin
import math
def suma(realA,realB,imaA,imaB):
    respuestareal=0
    respuestaima=0
    respuestareal=realA+realB
    respuestaima=imaA+imaB
    return (respuestareal,respuestaima)

def resta(realA,realB,imaA,imaB):
    respuestareal=0
    respuestaima=0
    respuestareal=realA-realB
    respuestaima=imaA-imaB
    return (respuestareal,respuestaima)

def multiplicacion(realA,realB,imaA,imaB):
    parteuno=realA*realB-imaA*imaB
    partedos=realA*imaB+realB*imaA
    return (parteuno,partedos)

def divi(realA,realB,imaA,imaB):
    parteuno=((realA*realB+imaA*imaB)/(realB**2+imaB**2))
    partedos=((realB*imaA-realA*imaB)/(realB**2+imaB**2))
    return (parteuno,partedos)

def conjugado(real,imaginario):
    if imaginario<0 :
        return (real,(abs(imaginario)))
    else:
        return (real,imaginario)


def modulo(real,imaginario):
    respuesta= ((real**2+imaginario**2)**0.5)
    return (respuesta)

def polarCartesiano(polar):
    hipo=polar[0]
    angu=polar[1]
    return (hipo*math.cos(angu*(math.pi/180)),hipo*math.sin(angu*(math.pi/180)))


def cartesianoPolar(cartesiano):
    angulo=math.atan(cartesiano[1]/cartesiano[0])
    return((cartesiano[0]**2+cartesiano[1]**2)**5,angulo*(180/math.pi))


def fase(num):
    return math.atan2(num[1],num[0])
