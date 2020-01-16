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

