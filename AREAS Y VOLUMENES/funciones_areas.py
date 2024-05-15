import math

#FUNCIONES PARA EL CÁLCULO DE ÁREAS GEOMÉTRICAS:
Pi=math.pi

#ÁREAS (1):

#CUADRADO:
def areaCuadrado(a):
    return a**2

def areaCuadrado1(ar):
    return ar**(1/2)
        

#RECTÁNGULO:
def areaRectangulo(a,b):
    return a*b

def areaRectangulo1(ar,b):
    return ar/b

def areaRectangulo2(ar,a):
    return ar/a


#TRIÁNGULO:
def areaTriangulo(b,h):
    return b*h/2

def areaTriangulo1(ar,h):
    return ar*2/h

def areaTriangulo2(ar,b):
    return ar*2/b


#CÍRCULO:
def areaCirculo(r):
    return Pi*(r**2)

def areaCirculo1(ar):
    return (ar/Pi)**(1/2)


#TRAPECIO:
def areaTrapecio(B,b,h):
    return (B+b)*h/2

def areaTrapecio1(ar,b,h):
    return ar*(2/h)-b

def areaTrapecio2(ar,B,h):
    return ar*(2/h)-B

def areaTrapecio3(ar,B,b):
    return ar*2/(B+b)



#ÁREAS (2):

#PARALELOGRAMO:
def areaParalelogramo(a,b):
    return a*b

def areaParalelogramo1(ar,b):
    return ar/b

def areaParalelogramo2(ar,a):
    return ar/a


#COMETA / ROMBO:
def areaCometa(b,h):
    return b*h/2

def areaCometa1(ar,h):
    return ar*2/h

def areaCometa2(ar,b):
    return ar*2/b


#POLÍGONO REGULAR:
def areaPoligonoRegular(n,a,b):
    return n*b*a/2

def areaPoligonoRegular1(ar,a,b):
    return ar*2/(b*a)

def areaPoligonoRegular2(ar,n,b):
    return ar*2/(n*b)

def areaPoligonoRegular3(ar,n,a):
    return ar*2/(n*a)


#ANILLO:
def areaAnillo(R,r):
    return Pi*((R**2)-(r**2))

def areaAnillo1(ar,r):
    return ((ar/Pi)+(r**2))**(1/2)

def areaAnillo2(ar,R):
    return (-(ar/Pi)+(R**2))**(1/2)


#SECTOR CIRLCULAR:
def areaSectorCircular(R,n):
    return Pi*(R**2)*n/360

def areaSectorCircular1(ar,n):
    return (ar*360/(Pi*n))**(1/2)

def areaSectorCircular2(ar,R):
    return ar*360/((R**2)*Pi)