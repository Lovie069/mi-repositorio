'''FUNCIONES QUE PERMITEN CALCULAR LAS ÁREAS Y VOLÚMENES
    A PARTIR DE LAS DIMENSIONES PROPORCIONADAS
    Y A SU VEZ MUESTRAN LOS RESULTADOS DE ÁREA Y VOLÚMEN
    EN OTRAS UNIDADES'''


from conversionUnidades import *
from funciones_areas import *

# FUNCIONES PARA EL CÁLCULO DE ÁREAS:
#TIPOS DE FORMATOS DECIMALES:
'''https://es.stackoverflow.com/questions/178990/c%C3%B3mo-puedo-dar-formato-de-n%C3%BAmeros-en-python-con-separador-de-miles-y-de-decima'''


#FUNCIÓN PARA VERIFICACIÓN DE UNIDADES INICIALES:
def verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3):

    if listadoUnidades.get()=="mm" and listadoUnidades1.get()=="cc (ml)":
        resultado0 = float(digito9.get())*(10**3)
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("mm^3")

    elif listadoUnidades.get()=="mm" and listadoUnidades1.get()=="m^3":
        resultado0 = float(digito9.get())*(10**9)
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("mm^3")

    elif listadoUnidades.get()=="mm" and listadoUnidades1.get()=="litros":
        resultado0 = float(digito9.get())*(10**6)
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("mm^3")


    elif listadoUnidades.get()=="cm" and listadoUnidades1.get()=="cc (ml)":
        resultado0 = float(digito9.get())
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("cm^3")

    elif listadoUnidades.get()=="cm" and listadoUnidades1.get()=="m^3":
        resultado0 = float(digito9.get())*(10**6)
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("cm^3")

    elif listadoUnidades.get()=="cm" and listadoUnidades1.get()=="litros":
        resultado0 = float(digito9.get())*(10**3)
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("cm^3")


    elif listadoUnidades.get()=="m" and listadoUnidades1.get()=="cc (ml)":
        resultado0 = float(digito9.get())*(1/(10**6))
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("m^3")

    elif listadoUnidades.get()=="m" and listadoUnidades1.get()=="m^3":
        resultado0 = float(digito9.get())
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("m^3")

    elif listadoUnidades.get()=="m" and listadoUnidades1.get()=="litros":
        resultado0 = float(digito9.get())*(1/(10**3))
        volumen.set(resultado0)
        unidadesFinalesVolumen.set("m^3")


    elif listadoUnidades.get()=="" and listadoUnidades1.get()=="":
        comentario.set(U1)

    elif listadoUnidades.get()=="" and listadoUnidades1.get()!="":
        comentario.set(U2)

    elif listadoUnidades.get()!="" and listadoUnidades1.get()=="":
        comentario.set(U3)






#EL NÚMERO ANTES DE LA LETRA "D EN LA PALABRA FUNCIÓN INDICA EL NÚMERO DE DIMENSIONES QUE TIENE LA FIGURA GEOMÉTRICA"

#EN ESTE GUPO "A1D" SE INCLUYEN:
'''CUADRADO
    CÍRCULO
'''

def funcionA1D(area,digito,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,funcionArea,funcionArea1):
    if area.get()=="" and digito.get()!="" and listadoUnidades.get()!="":
        resultado = funcionArea(float(digito.get()))
        area.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)
        
        conversionAreas(listadoUnidades,resultado,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()=="" and listadoUnidades.get()!="":
        resultado = funcionArea1(float(area.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,float(area.get()),enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()!="":
        comentario.set(A1)

    elif area.get()=="" and digito.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif area.get()!="" and digito.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)

    else:
        comentario.set(A2)

#EN ESTE GUPO "A2D" SE INCLUYEN:
'''RECTÁNGULO
    TRIÁNGULO
'''

def funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,funcionArea,funcionArea1,funcionArea2):
    if area.get()=="" and digito.get()!="" and digito1.get()!="" and listadoUnidades.get()!="":
        resultado = funcionArea(float(digito.get()),float(digito1.get()))
        area.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,resultado,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)
                
    elif area.get()!="" and digito.get()=="" and digito1.get()!="" and listadoUnidades.get()!="":
        resultado = funcionArea1(float(area.get()),float(digito1.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,float(area.get()),enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()!="" and digito1.get()=="" and listadoUnidades.get()!="":
        resultado = funcionArea2(float(area.get()),float(digito.get()))
        digito1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_","."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,float(area.get()),enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()!="" and digito1.get()!="":
        comentario.set(A1)

    elif area.get()!="" and digito.get()=="" and digito1.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif area.get()=="" and digito.get()!=""  and digito1.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif area.get()=="" and digito.get()==""  and digito1.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif area.get()!="" and digito.get()=="" and digito1.get()=="":
        comentario.set(F1)
    elif area.get()=="" and digito.get()=="" and digito1.get()!="":
        comentario.set(F1)
    elif area.get()=="" and digito.get()!="" and digito1.get()=="":
        comentario.set(F1)

    else:
        comentario.set(A2)



def funcionA3D(area,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,F2,funcionArea,funcionArea1,funcionArea2,funcionArea3):

    if area.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and listadoUnidades.get()!="":
        resultado = funcionArea(float(digito.get()),float(digito1.get()),float(digito2.get()))
        area.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)
        
        conversionAreas(listadoUnidades,resultado,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and listadoUnidades.get()!="":
        resultado = funcionArea1(float(area.get()),float(digito1.get()),float(digito2.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,float(area.get()),enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)


    elif area.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and listadoUnidades.get()!="":
        resultado = funcionArea2(float(area.get()),float(digito.get()),float(digito2.get()))
        digito1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,float(area.get()),enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and listadoUnidades.get()!="":
        resultado = funcionArea3(float(area.get()),float(digito.get()),float(digito1.get()))
        digito2.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionAreas(listadoUnidades,float(area.get()),enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    elif area.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="":
        comentario.set(A1)

    elif area.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif area.get()=="" and digito.get()!=""  and digito1.get()=="" and digito2.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif area.get()=="" and digito.get()==""  and digito1.get()!="" and digito2.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif area.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif area.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="":
        comentario.set(F2)
    elif area.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="":
        comentario.set(F2)
    elif area.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="":
        comentario.set(F2)
    elif area.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="":
        comentario.set(F2)

    elif area.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="":
        comentario.set(F1)
    elif area.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="":
        comentario.set(F1)
    elif area.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="":
        comentario.set(F1)
    elif area.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="":
        comentario.set(F1)

    else:
        comentario.set(A2)



#EN ESTE GUPO "V1D" SE INCLUYEN:
'''CUBO
    ESFERA
    TETRAEDRO
    OCTAEDRO
'''

def funcionV1D(volumen,digito,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,funcionVolumen,funcionVolumen1):

    if volumen.get()=="" and digito.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen(float(digito.get()))
        volumen.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,resultado,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()=="" and listadoUnidades.get()!="":
        resultado = funcionVolumen1(float(volumen.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="":
        comentario.set(A1)

    elif volumen.get()=="" and digito.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif volumen.get()!="" and digito.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)

    else:
        comentario.set(A2)


def funcionV2D(volumen,digito,digito1,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,funcionVolumen,funcionVolumen1,funcionVolumen2):

    if volumen.get()=="" and digito.get()!="" and digito1.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen(float(digito.get()),float(digito1.get()))
        volumen.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,resultado,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen1(float(volumen.get()),float(digito1.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and listadoUnidades.get()!="":
        resultado = funcionVolumen2(float(volumen.get()),float(digito.get()))
        digito1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="":
        comentario.set(A1)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()!=""  and digito1.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="":
        comentario.set(F1)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="":
        comentario.set(F1)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="":
        comentario.set(F1)

    else:
        comentario.set(A2)


def funcionV3D(volumen,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,funcionVolumen,funcionVolumen1,funcionVolumen2,funcionVolumen3):
    
    if volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen(float(digito.get()),float(digito1.get()),float(digito2.get()))
        volumen.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,resultado,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen1(float(volumen.get()),float(digito1.get()),float(digito2.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen2(float(volumen.get()),float(digito.get()),float(digito2.get()))
        digito1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and listadoUnidades.get()!="":
        resultado = funcionVolumen3(float(volumen.get()),float(digito.get()),float(digito1.get()))
        digito2.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="":
        comentario.set(A1)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()!=""  and digito1.get()=="" and digito2.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()!="" and digito2.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="":
        comentario.set(F1)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="":
        comentario.set(F1)

    else:
        comentario.set(A2)



def funcionV4D(volumen,digito,digito1,digito2,digito3,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,F3,funcionVolumen,funcionVolumen1,funcionVolumen2,funcionVolumen3,funcionVolumen4):

    if volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen(float(digito.get()),float(digito1.get()),float(digito2.get()),float(digito3.get()))
        volumen.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,resultado,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen1(float(volumen.get()),float(digito1.get()),float(digito2.get()),float(digito3.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen2(float(volumen.get()),float(digito.get()),float(digito2.get()),float(digito3.get()))
        digito1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen3(float(volumen.get()),float(digito.get()),float(digito1.get()),float(digito3.get()))
        digito2.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="" and listadoUnidades.get()!="":
        resultado = funcionVolumen4(float(volumen.get()),float(digito.get()),float(digito1.get()),float(digito2.get()))
        digito3.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="":
        comentario.set(A1)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()!=""  and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="":
        comentario.set(F3)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="":
        comentario.set(F2)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="":
        comentario.set(F1)

    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F1)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="":
        comentario.set(F1)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="":
        comentario.set(F1)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="":
        comentario.set(F1)

    else:
        comentario.set(A2)



def funcionV5D(volumen,digito,digito1,digito2,digito3,digito4,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,F3,F4,funcionVolumen,funcionVolumen1,funcionVolumen2,funcionVolumen3,funcionVolumen4,funcionVolumen5):

    if volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen(float(digito.get()),float(digito1.get()),float(digito2.get()),float(digito3.get()),float(digito4.get()))
        volumen.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,resultado,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen1(float(volumen.get()),float(digito1.get()),float(digito2.get()),float(digito3.get()),float(digito4.get()))
        digito.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen2(float(volumen.get()),float(digito.get()),float(digito2.get()),float(digito3.get()),float(digito4.get()))
        digito1.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen3(float(volumen.get()),float(digito.get()),float(digito1.get()),float(digito3.get()),float(digito4.get()))
        digito2.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        resultado = funcionVolumen4(float(volumen.get()),float(digito.get()),float(digito1.get()),float(digito2.get()),float(digito4.get()))
        digito3.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        resultado = funcionVolumen5(float(volumen.get()),float(digito.get()),float(digito1.get()),float(digito2.get()),float(digito3.get()))
        digito4.set(("{:_.2f}".format(resultado)).replace(".",",").replace("_", "."))
        comentario.set(A4)

        conversionVolumenes(listadoUnidades,float(volumen.get()),enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="":
        comentario.set(A1)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()==""  and digito3.get()==""  and digito4.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()!=""  and digito1.get()=="" and digito2.get()==""  and digito3.get()==""  and digito4.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()!="" and digito2.get()==""  and digito3.get()==""  and digito4.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()!=""  and digito3.get()==""  and digito4.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()==""  and digito3.get()!=""  and digito4.get()=="" and listadoUnidades.get()=="":
        comentario.set(A3)
    elif volumen.get()=="" and digito.get()==""  and digito1.get()=="" and digito2.get()==""  and digito3.get()==""  and digito4.get()!="" and listadoUnidades.get()=="":
        comentario.set(A3)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F4)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F4)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F4)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F4)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F4)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F4)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F3)

    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F3)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F3)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F3)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F3)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F3)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F2)

    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()=="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)

    elif volumen.get()=="" and digito.get()!="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()=="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()=="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()!="" and digito2.get()=="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)

    elif volumen.get()=="" and digito.get()=="" and digito1.get()!="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()=="" and digito1.get()!="" and digito2.get()=="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)

    elif volumen.get()!="" and digito.get()=="" and digito1.get()=="" and digito2.get()!="" and digito3.get()!="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)
    elif volumen.get()!="" and digito.get()!="" and digito1.get()=="" and digito2.get()!="" and digito3.get()=="" and digito4.get()!="" and listadoUnidades.get()!="":
        comentario.set(F1)

    else:
        comentario.set(A2)
