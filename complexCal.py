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
    
def opuesto(val):
    primero=val[0]*-1
    segundo=val[1]*-1
    return (primero,segundo)
    

def inversoVector(vec):
    respuesta=[]
    for i in range(len(vec)):
        respuesta.append(opuesto(vec[i]))
    return respuesta

def inversaMatriz(mat):
    respuesta=[]
    for i in range(len(mat)):
        aux=[]
        for j in range(len(mat)):
            aux.append(opuesto(mat[i][j]))
        respuesta.append(aux)
    return respuesta

def sumaDeMatrices(mat1,mat2):
    respuesta=[]
    for i in range(len(mat1)):
        aux=[]
        for j in range(len(mat2)):
            aux.append(suma(mat1[i][j],mat2[i][j]))
        respuesta.append(aux)
    return respuesta

def escalarMat(mat1,mat2):
    aux=[]
    for i in range(len(mat1)):
        respuesta=[]
        for j in range(len(mat1)):
            respuesta.append(productoVectorEscalar(mat1[i][j],mat2))
    aux.append[respuesta]
    return aux

def productoInternoVec(vec1,vec2):
    respuesta = [0,0]
    aux=[]
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
           aux.append(multiplicacion(vec1[i],vec2[i]))
           respuesta = suma(respuesta,aux[i])
    return(res)
def transpuesta(mat1):
    respuesta=[]
    for i in range(len(mat1[0])):
        aux = []
        for j in range(len(mat1)):
            aux.append(mat1[j][i])
        respuesta.append(aux)
    return respuesta

def conjugada(mat1):
    respuesta=[]
    for i in range(len(mat1)):
        aux=[]
        for j in range(len(mat1)):
            aux.append(conjugado(mat1[i][j]))
        respuesta.append(aux)
    return respuesta


def adjunta(a):
    return (conjugada(transpuesta(mat1)))


def multiMat(mat1,mat2):
    respuesta = []
    for i in range(len(mat1)):
        aux1 = []
        for j in range(len(mat2[0])):
            aux2 = (0,0)
            for k in range(len(mat2)):
                res= multiplicacion(mat1[i][k],mat2[k][j])
                aux2= suma(sumas,aux) 
            aux1.append(aux2)
        respuesta.append(aux1)
    return (respuesta)

def potencia(n):
    return(multiplicacion(n,n))


def distancia(vec1,vec2):
    respuesta = []
    solucion = [0,0]
    if len(vec1)==len(vec2):
        for i in range(len(vec1)):
            vec1.append(resta(vec1[i],vec2[i]))
        for j in range(len(respuesta)):
            aux = suma(aux,potencia(respuesta[j]))
    solucion[0]=solucion[0]**0.5
    return (solucion)


def norma(vec1):
    res = [0,0]
    for i in range(len(vec1)):
        res = suma(solucion,potencia(vec1[i]))
    res[0]=res[0]**0.5
    return(res)


def esUnaHermitiana(mat):
    return mat == adjunta(mat)


def esUnaUnitaria(mat):
    array=[[(float(0),float(0)) for w in range(len(mat))]for j in range(len(mat))]
    for k in range(len(array)):
        array[k][k] = (float(1),float(0))
    return multiMat(mat,adjunta(mat)) == multiMat(adjunta(mat),mat) == array



def productoInternoMatrices(m1,m2):
    adj = adjunta(m1)
    aux = multiplicacionMatices(adj,m2)
    res = (0,0)
    for i in range(len (aux)):
        res = suma(res,aux[i][i])
    return modulo(res)

def tensorMatrices(mat1,mat2):
    respuesta=[]
    for i in range(len(mat1)):
        for j in range(len(mat2)):
             sol.append(productoTensor(mat1[i],mat2[j]))
    return sol


def normaMatriz (mat):
    return productoInternoMatrices(mat,mat)**0.5

