from sys import stdin

def suma(realA,realB,imaA,imaB):
    respuestareal=0
    respuestaima=0
    respuestareal=realA+realB
    respuestaima=imaA+imaB
    print(str(respuestareal)+"+"+str(respuestaima)+"i")

def resta(realA,realB,imaA,imaB):
    respuestareal=0
    respuestaima=0
    respuestareal=realA-realB
    respuestaima=imaA-imaB
    print(str(respuestareal)+"-"+str(respuestaima)+"i")

def multiplicacion(realA,realB,imaA,imaB):
    parteuno=realA*realB-imaA*imaB
    partedos=realA*imaB+realB*imaA
    print(str(parteuno)+"+"+str(partedos)+"i")

def divi(realA,realB,imaA,imaB):
    parteuno=((realA*realB+imaA*imaB)/(realB**2+imaB**2))
    partedos=((realB*imaA-realA*imaB)/(realB**2+imaB**2))
    print(str(parteuno)+"+"+str(partedos)+"i")

def conjugado(real,imaginario):
    if imaginario<0 :
        print(str(real)+"+"+str(abs(imaginario))+"i")
    else:
        print((str(real)+"-"+str(imaginario)+"i"))


def modulo(real,imaginario):
    respuesta= ((real**2+imaginario**2)**0.5)
    print(respuesta)


def sumaVecto(vec1,vec2):
    pass
    
    
    

