#FUNCIONES PARA CONVERSION DE UNIDADES:

'''A CONTINUACIÓN SE MUESTRAN FUNCIONES QUE PERMITEN HACER
    EL CAMBIO DE UNIDADES SEGÚN LA COMBINACIÓN QUE SE TENGA
    EN EL SOFTWARE_01'''

#CONVERSION DE UNIDADES DE ÁREA:
def conversionAreas(a,b,c,d,e):
#conversionAreas(listadoUnidades,resultado,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea)

    if a.get()=="mm":
        resultado1 = b/(10**2)
        c.set(("{:_.2f}".format(resultado1)).replace(".",",").replace("_","."))

        resultado2 = b/(10**6)
        d.set(("{:_.2f}".format(resultado2)).replace(".",",").replace("_","."))

        e.set("mm^2")

    elif a.get()=="cm":
        resultado1 = b
        c.set(("{:_.2f}".format(resultado1)).replace(".",",").replace("_","."))

        resultado2 = b/(10**4)
        d.set(("{:_.2f}".format(resultado2)).replace(".",",").replace("_","."))

        e.set("cm^2")

    elif a.get()=="m":
        resultado1 = b*(10**4)
        c.set(("{:_.2f}".format(resultado1)).replace(".",",").replace("_","."))

        resultado2 = b
        d.set(("{:_.2f}".format(resultado2)).replace(".",",").replace("_","."))

        e.set("m^2")

#CONVERSION DE UNIDADES DE VOLÚMEN:
def conversionVolumenes(a,b,c,d,e,f):

    if a.get()=="mm":
        resultado1 = b/(10**3)
        c.set(("{:_.2f}".format(resultado1)).replace(".",",").replace("_","."))

        resultado2 = b/(10**9)
        d.set(("{:_.2f}".format(resultado2)).replace(".",",").replace("_","."))

        resultado3 = b/(10**6)
        e.set(("{:_.2f}".format(resultado3)).replace(".",",").replace("_","."))

        f.set("mm^3")

    elif a.get()=="cm":
        resultado1 = b
        c.set(("{:_.2f}".format(resultado1)).replace(".",",").replace("_","."))

        resultado2 = b/(10**6)
        d.set(("{:_.2f}".format(resultado2)).replace(".",",").replace("_","."))
        
        resultado3 = b/(10**3)
        e.set(("{:_.2f}".format(resultado3)).replace(".",",").replace("_","."))

        f.set("cm^3")

    elif a.get()=="m":
        resultado1 = b*(10**6)
        c.set(("{:_.2f}".format(resultado1)).replace(".",",").replace("_","."))

        resultado2 = b
        d.set(("{:_.2f}".format(resultado2)).replace(".",",").replace("_","."))

        resultado3 = b*(10**3)
        e.set(("{:_.2f}".format(resultado3)).replace(".",",").replace("_","."))

        f.set("m^3")