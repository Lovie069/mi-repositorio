import math

Pi=math.pi

#VOLÚMENES (1):

#CUBO:
def volumenCubo(a):
    return a**3

def volumenCubo1(vol):
    return vol**(1/3)


#PARALELEPÍPEDO:
def volumenParalelepipedo(a,b,c):
    return a*b*c

def volumenParalelepipedo1(vol,b,c):
    return vol/(b*c)

def volumenParalelepipedo2(vol,a,c):
    return vol/(a*c)

def volumenParalelepipedo3(vol,a,b):
    return vol/(a*b)


#PIRAMIDE:
def volumenPiramide(a,b,h):
    return (1/3)*a*b*h

def volumenPiramide1(vol,b,h):
    return vol*3/(b*h)

def volumenPiramide2(vol,a,h):
    return vol*3/(a*h)

def volumenPiramide3(vol,a,b):
    return vol*3/(a*b)


#ESFERA:
def volumenEsfera(r):
    return (4/3)*Pi*(r**3)

def volumenEsfera1(vol):
    return (vol*(3/4)/Pi)**(1/3)


#CONO CILINDRICO:
def volumenConoCilindrico(r,h):
    return (1/3)*Pi*(r**2)*h

def volumenConoCilindrico1(vol,h):
    return (vol*(3/(Pi*h)))**(1/2)

def volumenConoCilindrico2(vol,r):
    return vol*(3/(Pi*(r**2)))


#VOLÚMENES (2):

#CILINDRO:
def volumenCilindro(R,h):
    return Pi*(R**2)*h

def volumenCilindro1(vol,h):
    return (vol/(Pi*h))**(1/2)

def volumenCilindro2(vol,R):
    return vol/(Pi*(R**2))


#CONO TRUNCADO:
def volumenConoTruncado(R,r,h):
    return (1/3)*(Pi*h)*((R**2)+(r**2)+(R*r))

def volumenConoTruncado1(vol,r,h):
    return (1/2)*(-r+((r**2)-4*((r**2)-(3/Pi)*(vol/h)))**(1/2))

def volumenConoTruncado2(vol,R,h):
    return (1/2)*(-R+((R**2)-4*((R**2)-(3/Pi)*(vol/h)))**(1/2))

def volumenConoTruncado3(vol,R,r):
    return (3/Pi)*vol*(1/((R**2)+(r**2)+(R*r)))


#PIRAMIDE TRUNCADA:
def volumenPiramideTruncada(a,b,c,d,h):
    return (h/3)*((a*b)+(c*d)+((a*b)*(c*d))**(1/2))

def volumenPiramideTruncada1(vol,b,c,d,h):
    return ((1/(2*b))*((-(b*c*d)**(1/2))+((b*c*d)-4*b*(c*d-3*(vol/h)))**(1/2)))**2

def volumenPiramideTruncada2(vol,a,c,d,h):
    return ((1/(2*a))*((-(a*c*d)**(1/2))+((a*c*d)-4*a*(c*d-3*(vol/h)))**(1/2)))**2

def volumenPiramideTruncada3(vol,a,b,d,h):
    return ((1/(2*d))*((-(b*a*d)**(1/2))+((b*a*d)-4*b*(a*d-3*(vol/h)))**(1/2)))**2

def volumenPiramideTruncada4(vol,a,b,c,h):
    return ((1/(2*c))*((-(b*a*c)**(1/2))+((b*a*c)-4*b*(a*c-3*(vol/h)))**(1/2)))**2

def volumenPiramideTruncada5(vol,a,b,c,d):
    return 3*vol*(1/((a*b)+(c*d)+((a*b)*(c*d))**(1/2)))


#TETRAEDRO:
def volumenTetraedro(a):
    return ((2**(1/2))/12)*(a**3)

def volumenTetraedro1(vol):
    return ((12/(2**(1/2)))*vol)**(1/3)


#PRISMA RECTO:
def volumenPrismaRecto(n,a,b,h):
    return (n*b*a/2)*h
    
def volumenPrismaRecto1(vol,a,b,h):
    return vol*2/(b*a*h)

def volumenPrismaRecto2(vol,n,b,h):
    return vol*2/(b*n*h)

def volumenPrismaRecto3(vol,n,a,h):
    return vol*2/(n*a*h)

def volumenPrismaRecto4(vol,n,a,b):
    return vol*2/(b*a*n)
