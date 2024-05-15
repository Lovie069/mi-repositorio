'''SOFTWARE PARA EL CÁLCULO DE ÁREAS Y VOLÚMENES DE FIGURAS GEOMÉTRICAS
    INCLUYE:
    
    1) EL CÁLCULO DE CADA UNA DE LAS DIMENSIONES A PARTIR DEL DESPEJE DE ECUACIONES
    DE LA ECUACIÓN ORIGINAL. ESTO PERMITE IR ITERANDO HASTA OBTENER EL VALOR DESEADO.
    
    2) RESULTADOS EN UNIDADES DE ÁREA Y VOLÚMENES ALTERNATIVAS.
    
    3) SE PERMITE INGRESAR EL VALOR DEL VOLÚMEN EN OTRAS UNIDADES DIFERENTES A LAS DERIVADAS DE LAS LONGITUDES
    PARA FACILITAR LAS ITERACIONES.'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

from PIL import ImageTk, Image

from funciones_areas import *
from funciones_volumenes import *
from conversionUnidades import *
from funcionesEspecialesAV import *

# import sys
# print(sys.executable)

#CREACIÓN DE VENTANAS:
raiz=Tk()

#CONFIGURACION DE LA VENTANA RAIZ:
ancho_ventana = 600
alto_ventana = 698

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)

# raiz.geometry("700x750"+100,100)
raiz.config(bg="blue",padx=10,pady=10)
raiz.title("Integrador")
raiz.resizable(0,0)

#CARACTERES GLOBALES:
digito=StringVar()
digito1=StringVar()
digito2=StringVar()
digito3=StringVar()
digito4=StringVar()
digito9=StringVar()

area=StringVar()
volumen=StringVar()

resultado0=""
resultado=""
resultado1=""
resultado2=""
resultado3=""

unidadesFinalesArea=StringVar()
enCentimetrosCuadrados=StringVar()
enMetrosCuadrados=StringVar()

unidadesFinalesVolumen=StringVar()
enCentimetrosCubicos=StringVar()
enMetrosCubicos=StringVar()
enLitros=StringVar()

comentario=StringVar()

dimensiones1 = ["mm","cm","m"]
dimensiones2 = ["cc (ml)","m^3","litros"]


#MANEJO DE RUTAS EN LA PC:
'''https://programacionfacil.org/blog/manejo-de-imagenes-y-rutas-con-python-y-tkinter/'''
#CARPETA principal
carpeta_principal = os.path.dirname(__file__)
#CARPETA de imágenes
carpeta_imagenes= os.path.join(carpeta_principal,"Imagenes")

#ESTABLECEMOS EL ICONO DE LA PANTALLA PRINCIPAL:
raiz.iconbitmap(os.path.join(carpeta_principal, "Imagenes/icono_app.ico"))

#CARGAMOS LAS IMAGENES A USAR:
l1=50 #Dimensión imagen
l2=l1

#IMÁGENES PARA CÁLCULOS:
l3=100
l4=l3

#IMÁGENES BOTONES DE ÁREAS (1):
imgCuadrado=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCuadrado.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgRectangulo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgRectangulo.jpg"))).resize((2*l1,l2),Image.Resampling.LANCZOS))
imgTriangulo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgTriangulo.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgCirculo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCirculo.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgTrapecio=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgTrapecio.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))

#IMÁGENES BOTONES DE ÁREAS (2):
imgParalelogramo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgParalelogramo.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgCometa=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCometa.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgPoligonoRegular=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPoligonoRegular.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgAnillo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgAnillo.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgSectorCircular=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgSectorCircular.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))

#IMÁGENES BOTONES DE VOLÚMENES (1):
imgCubo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCubo.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgParalelepipedo=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgParalelepipedo.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgPiramide=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPiramide.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgEsfera=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgEsfera.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgCilindro=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCilindro.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgConoCilindrico=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgConoCilindrico.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))

#IMÁGENES BOTONES DE VOLÚMENES (2):
imgCilindro=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCilindro.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgConoTruncado=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgConoTruncado1.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgOctaedro=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgOctaedro1.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgPiramideTruncada=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPiramideTruncada1.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgPrismaRecto=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPrismaRecto1.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))
imgTetraedro=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgTetraedro1.jpg"))).resize((l1,l2),Image.Resampling.LANCZOS))


#IMÁGENES CÁLCULOS DE ÁREAS (1):
imgCuadrado1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCuadrado1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgRectangulo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgRectangulo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgTriangulo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgTriangulo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgCirculo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCirculo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgTrapecio1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgTrapecio1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))

#IMÁGENES CÁLCULOS DE ÁREAS (2):
imgParalelogramo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgParalelogramo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgCometa1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCometa1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgPoligonoRegular1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPoligonoRegular1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgAnillo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgAnillo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgSectorCircular1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgSectorCircular1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))


#IMÁGENES CÁLCULOS DE VOLÚMENES (1):
imgCubo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCubo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgParalelepipedo1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgParalelepipedo1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgPiramide1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPiramide1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgEsfera1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgEsfera1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
# imgCilindro1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCilindro1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgConoCilindrico1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgConoCilindrico1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))

#IMÁGENES CÁLCULOS DE VOLÚMENES (2):
imgCilindro1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgCilindro1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgConoTruncado1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgConoTruncado1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgPiramideTruncada1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPiramideTruncada1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgTetraedro1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgTetraedro1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgOctaedro1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgOctaedro1.jpg"))).resize((l3,l4),Image.Resampling.LANCZOS))
imgPrismaRecto1=ImageTk.PhotoImage((Image.open(os.path.join(carpeta_imagenes,"imgPrismaRecto1.jpg"))).resize((2*l3,l4),Image.Resampling.LANCZOS))

# create frame style
# s = ttk.Style()
# s.configure('new.TFrame', background='red')
# ventanaGeometria=ttk.Frame(raiz, width=200, height=200, cursor='pirate',padding=(10,10,15,25), style='new.TFrame')
ventanaGeometria=Frame(raiz, cursor='cross',relief="sunken",borderwidth=5,padx=10,pady=5)
#TIPOS DE BORDES: raised, sunken, flat, groove, ridge, solid

recuadroGemetricos=ttk.LabelFrame(ventanaGeometria,text="Geométricos",padding=(10,5))
recuadroGemetricos.pack(fill="both",expand=1)

#NOTEBOOK:
notebookGeometricos = ttk.Notebook(recuadroGemetricos,padding=1)
notebookGeometricos.grid(column=0,row=0,columnspan=2,sticky='nsew')

areas1 = ttk.Frame(notebookGeometricos,padding=(10,5)) #PRIMERA PÁGINA
areas2 = ttk.Frame(notebookGeometricos,padding=(10,5)) #SEGUNDA PÁGINA
volumenes1 = ttk.Frame(notebookGeometricos,padding=(10,5)) #TERCERA PÁGINA
volumenes2 = ttk.Frame(notebookGeometricos,padding=(10,5)) #CUARTA PÁGINA

notebookGeometricos.add(areas1, text='Áreas (1)')
notebookGeometricos.add(areas2, text='Áreas (2)')
notebookGeometricos.add(volumenes1, text='Volúmenes (1)')
notebookGeometricos.add(volumenes2, text='Volúmenes (2)')

#LISTBOX
# unidades = ["mm", "cm", "m"]
# choicesvar = StringVar(value=unidades)

#COMBO BOX:
listadoUnidades = StringVar()
listadoUnidades1 = StringVar()

#ANCHO DE GIDGETS EN VENTANA DE ÁREAS:
h1=80 #Alto de botones
h2=1 #Alto filas frame áreas y volúmenes
w1=100 #Ancho botones
w2=400 #Ancho pantalla de cálculo
w3=100 #Ancho imágenes
w4=15 #Ancho label datos

#ALTO DE SEPARACIÓN ENTRE GIDGETS
factor1=20
factor2=62

u1="nsew" #Ubicación figuras geométricas
u2="nsew"    #Ubicación de Gitgets en frame calculos de áreas y volúmenes

#COLORES FONDO:
fondoBotones="white" #Botones figuras geométricas
fondoFrameCalculos="grey" # Ventana cálculo de áreas
# fondoResultados="#A9CCE3"
fondoResultados="White"
# fondoUnidades="#5499C7"
# fondoUnidades="#3498DB"
fondoUnidades="#BDBDBD"
fondoBotonIngresar="#3498DB"
fondoBotonBorrar="#E59866"
fondoBotonCalcular="#01579B"
# fondoSubTitulos="#A9CCE3"
fondoSubTitulos="#64B5F6"

#COLORES DE LETRAS:
fuenteBotonCalcular="white"

#FUENTES DE LETRAS:
'''https://blog.hubspot.es/website/fuentes-html'''
letraBotonCalcular= ('Tahoma', 9, 'bold')



#PADDING:
x1=10 #Padx Ventana cálculo de áreas
y1=10 #Pady Ventana cálculo de áreas

x2=20 #Padx Ventana botones
y2=20 #Pady Ventana botones

#AVISOS:
A1 = "Campos llenos, favor reiniciar la operación"
A2 = "Campos vacíos, favor indicar las dimensiones"
A3 = "Favor indicar la unidades principales"
A4 = "Fin de la Operación"

B1 = "Resultados alternativos de Área"
B2 = "Resultados alternativos de Volúmen"
B3 = "Ingresa aquí el valor de volúmen (SÓLO si lo tienes):"

F1 = "Falta 1 dato por llenar"
F2 = "Faltan 2 datos por llenar"
F3 = "Faltan 3 datos por llenar"
F4 = "Faltan 4 datos por llenar"

U1 = "Campos de unidades vacíos"
U2 = "Favor indicar las unidades a medir"
U3 = "Favor indicar la unidad de volúmen"

#TEXTO EN BOTONES:
ingresar = "INGRESAR"
borrar = "Borrar Campos"
calcular = "CALCULAR"

#BOTONES (CÁLCULOS DE ÁREAS (1)):
Button(areas1,image=imgCuadrado,width=w1,height=h1,bg=fondoBotones,command=lambda:abrirVentanaCuadrado()).grid(column=0,row=0,sticky=u1)
Label(areas1,text="Cuadrado").grid(column=0,row=1,sticky=u1)

Button(areas1,image=imgRectangulo,height=h1,bg=fondoBotones,command=lambda:abrirVentanaRectangulo()).grid(column=0,row=2,sticky=u1)
Label(areas1,text="Rectángulo").grid(column=0,row=3,sticky=u1)

Button(areas1,image=imgTriangulo,height=h1,bg=fondoBotones,command=lambda:abrirVentanaTriangulo()).grid(column=0,row=4,sticky=u1)
Label(areas1,text="Triángulo").grid(column=0,row=5,sticky=u1)

Button(areas1,image=imgCirculo,height=h1,bg=fondoBotones,command=lambda:abrirVentanaCirculo()).grid(column=0,row=6,sticky=u1)
Label(areas1,text="Círculo").grid(column=0,row=7,sticky=u1)

Button(areas1,image=imgTrapecio,height=h1,bg=fondoBotones,command=lambda:abrirVentanaTrapecio()).grid(column=0,row=8,sticky=u1)
Label(areas1,text="Trapecio").grid(column=0,row=9,sticky=u1)

#BOTONES (CÁLCULOS DE ÁREAS (2)):
Button(areas2,image=imgParalelogramo,width=w1,height=h1,bg=fondoBotones,command=lambda:abrirVentanaParalelogramo()).grid(column=0,row=0,sticky=u1)
Label(areas2,text="Paralelogramo").grid(column=0,row=1,sticky=u1)

Button(areas2,image=imgCometa,height=h1,bg=fondoBotones,command=lambda:abrirVentanaCometa()).grid(column=0,row=2,sticky=u1)
Label(areas2,text="Cometa (Rombo)").grid(column=0,row=3,sticky=u1)

Button(areas2,image=imgPoligonoRegular,height=h1,bg=fondoBotones,command=lambda:abrirVentanaPoligonoRegular()).grid(column=0,row=4,sticky=u1)
Label(areas2,text="Polígono Regular").grid(column=0,row=5,sticky=u1)

Button(areas2,image=imgAnillo,height=h1,bg=fondoBotones,command=lambda:abrirVentanaAnillo()).grid(column=0,row=6,sticky=u1)
Label(areas2,text="Anillo").grid(column=0,row=7,sticky=u1)

Button(areas2,image=imgSectorCircular,height=h1,bg=fondoBotones,command=lambda:abrirVentanaSectorCircular()).grid(column=0,row=8,sticky=u1)
Label(areas2,text="Sector Circular").grid(column=0,row=9,sticky=u1)

#VENTANAS PARA CÁLCULOS DE ÁREAS (1):
frameAreaCuadrado=Frame(areas1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaRectangulo=Frame(areas1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaTriangulo=Frame(areas1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaCirculo=Frame(areas1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaTrapecio=Frame(areas1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)

#VENTANAS PARA CÁLCULOS DE ÁREAS (2):
frameAreaParalelogramo=Frame(areas2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaCometa=Frame(areas2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaPoligonoRegular=Frame(areas2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaAnillo=Frame(areas2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameAreaSectorCircular=Frame(areas2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)


#VENTANA CÁLCULO ÁREA CUADRADO:
Label(frameAreaCuadrado,image=imgCuadrado1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaCuadrado,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaCuadrado,width=w4,text="Unidades",justify="center").grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaCuadrado, textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaCuadrado,text="Lado (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaCuadrado,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameAreaCuadrado,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaCuadrado,text="Área",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaCuadrado,justify="center",bg=fondoResultados,textvariable=area).grid(column=1,row=8,sticky=u2)
Label(frameAreaCuadrado,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=8,sticky=u2)

Frame(frameAreaCuadrado,bg=fondoFrameCalculos,height=171*h2).grid(column=0,row=9,columnspan=3)

Label(frameAreaCuadrado,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=10,columnspan=3,sticky=u2)
Label(frameAreaCuadrado,text="(1)",justify="center",height=h2).grid(column=0,row=11,sticky=u2)
Label(frameAreaCuadrado,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=11,sticky=u2)
Label(frameAreaCuadrado,text="m^2",justify="center",height=h2).grid(column=2,row=11,sticky=u2)

Frame(frameAreaCuadrado,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=12,columnspan=3)

Button(frameAreaCuadrado,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=13,sticky=u2)
Button(frameAreaCuadrado,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA1D(area,digito,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,areaCuadrado,areaCuadrado1)).grid(column=2,row=13,sticky=u2)

Label(frameAreaCuadrado,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=14,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA RECTÁNGULO:
Label(frameAreaRectangulo,image=imgRectangulo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaRectangulo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaRectangulo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaRectangulo, textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaRectangulo,text="Lado (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaRectangulo,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaRectangulo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaRectangulo,text="Lado (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaRectangulo,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaRectangulo,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaRectangulo,text="Área",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaRectangulo,justify="center",bg=fondoResultados,textvariable=area).grid(column=1,row=9,sticky=u2)
Label(frameAreaRectangulo,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameAreaRectangulo,bg=fondoFrameCalculos,height=150*h2).grid(column=0,row=10,columnspan=3)

Label(frameAreaRectangulo,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)
Label(frameAreaRectangulo,text="(1)",justify="center",height=h2).grid(column=0,row=12,sticky=u2)
Label(frameAreaRectangulo,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=12,sticky=u2)
Label(frameAreaRectangulo,text="m^2",justify="center",height=h2).grid(column=2,row=12,sticky=u2)

Frame(frameAreaRectangulo,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=13,columnspan=3)

Button(frameAreaRectangulo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=14,sticky=u2)
Button(frameAreaRectangulo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,areaRectangulo,areaRectangulo1,areaRectangulo2)).grid(column=2,row=14,sticky=u2)

Label(frameAreaRectangulo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=15,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA TRIÁNGULO:
Label(frameAreaTriangulo,image=imgTriangulo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaTriangulo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaTriangulo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaTriangulo, textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaTriangulo,text="Base (b)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaTriangulo,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaTriangulo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaTriangulo,text="Altura (h)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaTriangulo,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaTriangulo,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaTriangulo,text="Área",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaTriangulo,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaTriangulo,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameAreaTriangulo,bg=fondoFrameCalculos,height=150*h2).grid(column=0,row=10,columnspan=3)

Label(frameAreaTriangulo,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)
Label(frameAreaTriangulo,text="(1)",justify="center",height=h2).grid(column=0,row=12,sticky=u2)
Label(frameAreaTriangulo,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=12,sticky=u2)
Label(frameAreaTriangulo,text="m^2",justify="center",height=h2).grid(column=2,row=12,sticky=u2)

Frame(frameAreaTriangulo,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=13,columnspan=3)

Button(frameAreaTriangulo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=14,sticky=u2)
Button(frameAreaTriangulo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,areaTriangulo,areaTriangulo1,areaTriangulo2)).grid(column=2,row=14,sticky=u2)

Label(frameAreaTriangulo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=15,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA CÍRCULO:
Label(frameAreaCirculo,image=imgCirculo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaCirculo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaCirculo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaCirculo,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaCirculo,text="Radio (r)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaCirculo,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaCirculo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaCirculo,text="Área",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaCirculo,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaCirculo,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=8,sticky=u2)

Frame(frameAreaCirculo,bg=fondoFrameCalculos,height=171*h2).grid(column=0,row=9,columnspan=3)

Label(frameAreaCirculo,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=10,columnspan=3,sticky=u2)
Label(frameAreaCirculo,text="(1)",justify="center",height=h2).grid(column=0,row=11,sticky=u2)
Label(frameAreaCirculo,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=11,sticky=u2)
Label(frameAreaCirculo,text="m^2",justify="center",height=h2).grid(column=2,row=11,sticky=u2)

Frame(frameAreaCirculo,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=12,columnspan=3)

Button(frameAreaCirculo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=13,sticky=u2)
Button(frameAreaCirculo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA1D(area,digito,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,areaCirculo,areaCirculo1)).grid(column=2,row=13,sticky=u2)

Label(frameAreaCirculo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=14,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA TRAPECIO:
Label(frameAreaTrapecio,image=imgTrapecio1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaTrapecio,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaTrapecio,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaTrapecio,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaTrapecio,text="Base Mayor (B)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaTrapecio,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaTrapecio,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaTrapecio,text="Base menor (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaTrapecio,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaTrapecio,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaTrapecio,text="Altura (h)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaTrapecio,width=w4,textvariable=digito2,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaTrapecio,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameAreaTrapecio,text="Área",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameAreaTrapecio,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=10,sticky=u2)
Label(frameAreaTrapecio,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=10,sticky=u2)

Frame(frameAreaTrapecio,bg=fondoFrameCalculos,height=129*h2).grid(column=0,row=11,columnspan=3)

Label(frameAreaTrapecio,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=12,columnspan=3,sticky=u2)
Label(frameAreaTrapecio,text="(1)",justify="center",height=h2).grid(column=0,row=13,sticky=u2)
Label(frameAreaTrapecio,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=13,sticky=u2)
Label(frameAreaTrapecio,text="m^2",justify="center",height=h2).grid(column=2,row=13,sticky=u2)

Frame(frameAreaTrapecio,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=14,columnspan=3)

Button(frameAreaTrapecio,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=15,sticky=u2)
Button(frameAreaTrapecio,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA3D(area,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,F2,areaTrapecio,areaTrapecio1,areaTrapecio2,areaTrapecio3)).grid(column=2,row=15,sticky=u2)

Label(frameAreaTrapecio,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=16,columnspan=3,sticky=u2)


#(CÁLCULOS DE ÁREAS (2)):

#VENTANA CÁLCULO ÁREA PARALELOGRAMO:
Label(frameAreaParalelogramo,image=imgParalelogramo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaParalelogramo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaParalelogramo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaParalelogramo,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaParalelogramo,text="Base (b)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaParalelogramo,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaParalelogramo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaParalelogramo,text="Altura (h)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaParalelogramo,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaParalelogramo,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaParalelogramo,text="Área",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaParalelogramo,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaParalelogramo,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameAreaParalelogramo,bg=fondoFrameCalculos,height=150*h2).grid(column=0,row=10,columnspan=3)

Label(frameAreaParalelogramo,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)
Label(frameAreaParalelogramo,text="(1)",justify="center",height=h2).grid(column=0,row=12,sticky=u2)
Label(frameAreaParalelogramo,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=12,sticky=u2)
Label(frameAreaParalelogramo,text="m^2",justify="center",height=h2).grid(column=2,row=12,sticky=u2)

Frame(frameAreaParalelogramo,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=13,columnspan=3)

Button(frameAreaParalelogramo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=14,sticky=u2)
Button(frameAreaParalelogramo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,areaParalelogramo,areaParalelogramo1,areaParalelogramo2)).grid(column=2,row=14,sticky=u2)

Label(frameAreaParalelogramo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=15,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA COMETA:
Label(frameAreaCometa,image=imgCometa1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaCometa,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaCometa,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaCometa,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaCometa,text="Lado Mayor (D)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaCometa,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaCometa,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaCometa,text="Lado menor (d)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaCometa,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaCometa,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaCometa,text="Área",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaCometa,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaCometa,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameAreaCometa,bg=fondoFrameCalculos,height=150*h2).grid(column=0,row=10,columnspan=3)

Label(frameAreaCometa,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)
Label(frameAreaCometa,text="(1)",justify="center",height=h2).grid(column=0,row=12,sticky=u2)
Label(frameAreaCometa,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=12,sticky=u2)
Label(frameAreaCometa,text="m^2",justify="center",height=h2).grid(column=2,row=12,sticky=u2)

Frame(frameAreaCometa,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=13,columnspan=3)

Button(frameAreaCometa,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=14,sticky=u2)
Button(frameAreaCometa,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,areaCometa,areaCometa1,areaCometa2)).grid(column=2,row=14,sticky=u2)

Label(frameAreaCometa,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=15,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA POLIGONO REGULAR:
Label(frameAreaPoligonoRegular,image=imgPoligonoRegular1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaPoligonoRegular,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaPoligonoRegular,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaPoligonoRegular,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaPoligonoRegular,text="Nro. Lados (n)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaPoligonoRegular,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaPoligonoRegular,width=w4,text="Lados",justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaPoligonoRegular,text="Base (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaPoligonoRegular,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaPoligonoRegular,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaPoligonoRegular,text="Apotema (a)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaPoligonoRegular,width=w4,textvariable=digito2,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaPoligonoRegular,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameAreaPoligonoRegular,text="Área",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameAreaPoligonoRegular,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=10,sticky=u2)
Label(frameAreaPoligonoRegular,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=10,sticky=u2)

Frame(frameAreaPoligonoRegular,bg=fondoFrameCalculos,height=129*h2).grid(column=0,row=11,columnspan=3)

Label(frameAreaPoligonoRegular,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=12,columnspan=3,sticky=u2)
Label(frameAreaPoligonoRegular,text="(1)",justify="center",height=h2).grid(column=0,row=13,sticky=u2)
Label(frameAreaPoligonoRegular,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=13,sticky=u2)
Label(frameAreaPoligonoRegular,text="m^2",justify="center",height=h2).grid(column=2,row=13,sticky=u2)

Frame(frameAreaPoligonoRegular,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=14,columnspan=3)

Button(frameAreaPoligonoRegular,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=15,sticky=u2)
Button(frameAreaPoligonoRegular,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA3D(area,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,F2,areaPoligonoRegular,areaPoligonoRegular1,areaPoligonoRegular2,areaPoligonoRegular3)).grid(column=2,row=15,sticky=u2)

Label(frameAreaPoligonoRegular,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=16,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA ANILLO:
Label(frameAreaAnillo,image=imgAnillo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaAnillo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaAnillo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaAnillo,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaAnillo,text="Radio exterior (R)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaAnillo,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaAnillo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaAnillo,text="Radio interior (r)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaAnillo,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaAnillo,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaAnillo,text="Área",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaAnillo,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaAnillo,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameAreaAnillo,bg=fondoFrameCalculos,height=150*h2).grid(column=0,row=10,columnspan=3)

Label(frameAreaAnillo,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)
Label(frameAreaAnillo,text="(1)",justify="center",height=h2).grid(column=0,row=12,sticky=u2)
Label(frameAreaAnillo,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=12,sticky=u2)
Label(frameAreaAnillo,text="m^2",justify="center",height=h2).grid(column=2,row=12,sticky=u2)

Frame(frameAreaAnillo,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=13,columnspan=3)

Button(frameAreaAnillo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=14,sticky=u2)
Button(frameAreaAnillo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,areaAnillo,areaAnillo1,areaAnillo2)).grid(column=2,row=14,sticky=u2)

Label(frameAreaAnillo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=15,columnspan=3,sticky=u2)


#VENTANA CÁLCULO ÁREA SECTOR CIRCULAR:
Label(frameAreaSectorCircular,image=imgSectorCircular1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameAreaSectorCircular,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameAreaSectorCircular,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameAreaSectorCircular,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameAreaSectorCircular,text="Radio (R)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameAreaSectorCircular,textvariable=digito,justify="center").grid(column=1,row=7,sticky=u2)
Label(frameAreaSectorCircular,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameAreaSectorCircular,text="Ángulo (n°)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameAreaSectorCircular,textvariable=digito1,justify="center").grid(column=1,row=8,sticky=u2)
Label(frameAreaSectorCircular,text="Grados",justify="left").grid(column=2,row=8,sticky=u2)

Label(frameAreaSectorCircular,text="Área",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameAreaSectorCircular,bg=fondoResultados,textvariable=area,justify="center").grid(column=1,row=9,sticky=u2)
Label(frameAreaSectorCircular,textvariable=unidadesFinalesArea,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameAreaSectorCircular,bg=fondoFrameCalculos,height=150*h2).grid(column=0,row=10,columnspan=3)

Label(frameAreaSectorCircular,text=B1,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)
Label(frameAreaSectorCircular,text="(1)",justify="center",height=h2).grid(column=0,row=12,sticky=u2)
Label(frameAreaSectorCircular,textvariable=enMetrosCuadrados,justify="center",height=h2).grid(column=1,row=12,sticky=u2)
Label(frameAreaSectorCircular,text="m^2",justify="center",height=h2).grid(column=2,row=12,sticky=u2)

Frame(frameAreaSectorCircular,bg=fondoFrameCalculos,height=factor2*h2).grid(column=0,row=13,columnspan=3)

Button(frameAreaSectorCircular,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=14,sticky=u2)
Button(frameAreaSectorCircular,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionA2D(area,digito,digito1,listadoUnidades,comentario,enCentimetrosCuadrados,enMetrosCuadrados,unidadesFinalesArea,A1,A2,A3,A4,F1,areaSectorCircular,areaSectorCircular1,areaSectorCircular2)).grid(column=2,row=14,sticky=u2)

Label(frameAreaSectorCircular,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=15,columnspan=3,sticky=u2)


#BOTONES (CÁLCULOS DE VOLÚMENES (1)):
Button(volumenes1,image=imgCubo,width=w1,height=h1,bg=fondoBotones,command=lambda:abrirVentanaCubo()).grid(column=0,row=0,sticky=u1)
Label(volumenes1,text="Cubo").grid(column=0,row=1,sticky=u1)

Button(volumenes1,image=imgParalelepipedo,width=w1,height=h1,bg=fondoBotones,command=lambda:abrirVenanaParalelepipedo()).grid(column=0,row=2,sticky=u1)
Label(volumenes1,text="Paralelepípedo").grid(column=0,row=3,sticky=u1)

Button(volumenes1,image=imgPiramide,height=h1,bg=fondoBotones,command=lambda:abrirVentanaPiramide()).grid(column=0,row=4,sticky=u1)
Label(volumenes1,text="Pirámide").grid(column=0,row=5,sticky=u1)

Button(volumenes1,image=imgEsfera,height=h1,bg=fondoBotones,command=lambda:abrirVentanaEsfera()).grid(column=0,row=6,sticky=u1)
Label(volumenes1,text="Esfera").grid(column=0,row=7,sticky=u1)

Button(volumenes1,image=imgConoCilindrico,height=h1,bg=fondoBotones,command=lambda:abrirVentanaConoCilindrico()).grid(column=0,row=8,sticky=u1)
Label(volumenes1,text="Cono Cilíndrico").grid(column=0,row=9,sticky=u1)


#BOTONES (CÁLCULOS DE VOLÚMENES (2)):
Button(volumenes2,image=imgCilindro,width=w1,height=h1,bg=fondoBotones,command=lambda:abrirVentanaCilindro()).grid(column=0,row=0,sticky=u1)
Label(volumenes2,text="Cilindro").grid(column=0,row=1,sticky=u1)

Button(volumenes2,image=imgConoTruncado,width=w1,height=h1,bg=fondoBotones,command=lambda:abrirVentanaConoTruncado()).grid(column=0,row=2,sticky=u1)
Label(volumenes2,text="Cono Truncado").grid(column=0,row=3,sticky=u1)

Button(volumenes2,image=imgPiramideTruncada,height=h1,bg=fondoBotones,command=lambda:abrirVentanaPiramideTruncada()).grid(column=0,row=4,sticky=u1)
Label(volumenes2,text="Pirámide Truncada").grid(column=0,row=5,sticky=u1)

Button(volumenes2,image=imgTetraedro,height=h1,bg=fondoBotones,command=lambda:abrirVentanaTetraedro()).grid(column=0,row=6,sticky=u1)
Label(volumenes2,text="Tetraedro").grid(column=0,row=7,sticky=u1)

Button(volumenes2,image=imgOctaedro,height=h1,bg=fondoBotones,command=lambda:abrirVentanaOctaedro()).grid(column=0,row=8,sticky=u1)
Label(volumenes2,text="Octaedro").grid(column=0,row=9,sticky=u1)

Button(volumenes2,image=imgPrismaRecto,height=h1,bg=fondoBotones,command=lambda:abrirVentanaPrismaRecto()).grid(column=0,row=8,sticky=u1)
Label(volumenes2,text="Prisma Recto").grid(column=0,row=9,sticky=u1)

#VENTANA CÁLCULO DE VOLÚMENES (1):

frameVolumenCubo=Frame(volumenes1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenParalelepipedo=Frame(volumenes1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenPiramide=Frame(volumenes1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenEsfera=Frame(volumenes1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenConoCilindrico=Frame(volumenes1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenCilindro=Frame(volumenes1,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)

#VENTANA CÁLCULO DE VOLÚMENES (2):

frameVolumenCilindro=Frame(volumenes2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenConoTruncado=Frame(volumenes2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenPiramideTruncada=Frame(volumenes2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenTetraedro=Frame(volumenes2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenOctaedro=Frame(volumenes2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)
frameVolumenPrismaRecto=Frame(volumenes2,width=w2,bg=fondoFrameCalculos,padx=x1,pady=y1)


#VENTANA CÁLCULO VOLUMEN CUBO:
Label(frameVolumenCubo,image=imgCubo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenCubo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenCubo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenCubo,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenCubo,text="Lado (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenCubo,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenCubo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenCubo,text="Volúmen",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenCubo,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=8,sticky=u2)
Label(frameVolumenCubo,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=8,sticky=u2)

Frame(frameVolumenCubo,bg=fondoFrameCalculos,height=104*h2).grid(column=0,row=9,columnspan=3)

Label(frameVolumenCubo,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=10,columnspan=3,sticky=u2)

Entry(frameVolumenCubo,justify="center",textvariable=digito9).grid(column=0,row=11,sticky=u2)
ttk.Combobox(frameVolumenCubo,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=11,sticky=u2)
Button(frameVolumenCubo,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=11,sticky=u2)

Frame(frameVolumenCubo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=12,columnspan=3)

Label(frameVolumenCubo,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=13,columnspan=3,sticky=u2)

Label(frameVolumenCubo,text="(1)",justify="center",height=h2).grid(column=0,row=14,sticky=u2)
Label(frameVolumenCubo,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=14,sticky=u2)
Label(frameVolumenCubo,text="cc (ml)",justify="center",height=h2).grid(column=2,row=14,sticky=u2)

Label(frameVolumenCubo,text="(2)",justify="center",height=h2).grid(column=0,row=15,sticky=u2)
Label(frameVolumenCubo,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=15,sticky=u2)
Label(frameVolumenCubo,text="m^3",justify="center",height=h2).grid(column=2,row=15,sticky=u2)

Label(frameVolumenCubo,text="(3)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenCubo,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenCubo,text="Litros",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Frame(frameVolumenCubo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=17,columnspan=3)

Button(frameVolumenCubo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=18,sticky=u2)
Button(frameVolumenCubo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV1D(volumen,digito,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,volumenCubo,volumenCubo1)).grid(column=2,row=18,sticky=u2)

Label(frameVolumenCubo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=19,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN PARALELEPIPEDO:
Label(frameVolumenParalelepipedo,image=imgParalelepipedo1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenParalelepipedo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenParalelepipedo,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenParalelepipedo,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenParalelepipedo,text="Lado (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenParalelepipedo,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenParalelepipedo,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenParalelepipedo,text="Lado (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenParalelepipedo,width=w4,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenParalelepipedo,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenParalelepipedo,text="Lado (c)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenParalelepipedo,width=w4,justify="center",textvariable=digito2).grid(column=1,row=9,sticky=u2)
Label(frameVolumenParalelepipedo,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameVolumenParalelepipedo,text="Volúmen",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameVolumenParalelepipedo,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=10,sticky=u2)
Label(frameVolumenParalelepipedo,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=10,sticky=u2)

Frame(frameVolumenParalelepipedo,bg=fondoFrameCalculos,height=62*h2).grid(column=0,row=11,columnspan=3)

Label(frameVolumenParalelepipedo,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=12,columnspan=3,sticky=u2)

Entry(frameVolumenParalelepipedo,justify="center",textvariable=digito9).grid(column=0,row=13,sticky=u2)
ttk.Combobox(frameVolumenParalelepipedo,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=13,sticky=u2)
Button(frameVolumenParalelepipedo,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=13,sticky=u2)

Frame(frameVolumenParalelepipedo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=14,columnspan=3)

Label(frameVolumenParalelepipedo,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=15,columnspan=3,sticky=u2)

Label(frameVolumenParalelepipedo,text="(1)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenParalelepipedo,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenParalelepipedo,text="cc (ml)",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Label(frameVolumenParalelepipedo,text="(2)",justify="center",height=h2).grid(column=0,row=17,sticky=u2)
Label(frameVolumenParalelepipedo,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=17,sticky=u2)
Label(frameVolumenParalelepipedo,text="m^3",justify="center",height=h2).grid(column=2,row=17,sticky=u2)

Label(frameVolumenParalelepipedo,text="(3)",justify="center",height=h2).grid(column=0,row=18,sticky=u2)
Label(frameVolumenParalelepipedo,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=18,sticky=u2)
Label(frameVolumenParalelepipedo,text="Litros",justify="center",height=h2).grid(column=2,row=18,sticky=u2)

Frame(frameVolumenParalelepipedo,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=19,columnspan=3)

Button(frameVolumenParalelepipedo,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=20,sticky=u2)
Button(frameVolumenParalelepipedo,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV3D(volumen,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,volumenParalelepipedo,volumenParalelepipedo1,volumenParalelepipedo2,volumenParalelepipedo3)).grid(column=2,row=20,sticky=u2)

Label(frameVolumenParalelepipedo,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=21,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN PIRAMIDE:
Label(frameVolumenPiramide,image=imgPiramide1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenPiramide,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenPiramide,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenPiramide,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenPiramide,text="Lado 1 (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenPiramide,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenPiramide,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenPiramide,text="Lado 2 (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenPiramide,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenPiramide,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenPiramide,text="Altura (h)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenPiramide,width=w4,justify="center",textvariable=digito2).grid(column=1,row=9,sticky=u2)
Label(frameVolumenPiramide,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameVolumenPiramide,text="Volúmen",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameVolumenPiramide,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=10,sticky=u2)
Label(frameVolumenPiramide,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=10,sticky=u2)

Frame(frameVolumenPiramide,bg=fondoFrameCalculos,height=62*h2).grid(column=0,row=11,columnspan=3)

Label(frameVolumenPiramide,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=12,columnspan=3,sticky=u2)

Entry(frameVolumenPiramide,justify="center",textvariable=digito9).grid(column=0,row=13,sticky=u2)
ttk.Combobox(frameVolumenPiramide,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=13,sticky=u2)
Button(frameVolumenPiramide,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=13,sticky=u2)

Frame(frameVolumenPiramide,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=14,columnspan=3)

Label(frameVolumenPiramide,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=15,columnspan=3,sticky=u2)

Label(frameVolumenPiramide,text="(1)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenPiramide,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenPiramide,text="cc (ml)",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Label(frameVolumenPiramide,text="(2)",justify="center",height=h2).grid(column=0,row=17,sticky=u2)
Label(frameVolumenPiramide,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=17,sticky=u2)
Label(frameVolumenPiramide,text="m^3",justify="center",height=h2).grid(column=2,row=17,sticky=u2)

Label(frameVolumenPiramide,text="(3)",justify="center",height=h2).grid(column=0,row=18,sticky=u2)
Label(frameVolumenPiramide,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=18,sticky=u2)
Label(frameVolumenPiramide,text="Litros",justify="center",height=h2).grid(column=2,row=18,sticky=u2)

Frame(frameVolumenPiramide,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=19,columnspan=3)

Button(frameVolumenPiramide,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=20,sticky=u2)
Button(frameVolumenPiramide,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV3D(volumen,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,volumenPiramide,volumenPiramide1,volumenPiramide2,volumenPiramide3)).grid(column=2,row=20,sticky=u2)

Label(frameVolumenPiramide,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=21,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN ESFERA:
Label(frameVolumenEsfera,image=imgEsfera1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenEsfera,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenEsfera,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenEsfera,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenEsfera,text="Radio (R)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenEsfera,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenEsfera,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenEsfera,text="Volumen",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenEsfera,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=8,sticky=u2)
Label(frameVolumenEsfera,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=8,sticky=u2)

Frame(frameVolumenEsfera,bg=fondoFrameCalculos,height=104*h2).grid(column=0,row=9,columnspan=3)

Label(frameVolumenEsfera,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=10,columnspan=3,sticky=u2)

Entry(frameVolumenEsfera,justify="center",textvariable=digito9).grid(column=0,row=11,sticky=u2)
ttk.Combobox(frameVolumenEsfera,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=11,sticky=u2)
Button(frameVolumenEsfera,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=11,sticky=u2)

Frame(frameVolumenEsfera,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=12,columnspan=3)

Label(frameVolumenEsfera,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=13,columnspan=3,sticky=u2)

Label(frameVolumenEsfera,text="(1)",justify="center",height=h2).grid(column=0,row=14,sticky=u2)
Label(frameVolumenEsfera,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=14,sticky=u2)
Label(frameVolumenEsfera,text="cc (ml)",justify="center",height=h2).grid(column=2,row=14,sticky=u2)

Label(frameVolumenEsfera,text="(2)",justify="center",height=h2).grid(column=0,row=15,sticky=u2)
Label(frameVolumenEsfera,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=15,sticky=u2)
Label(frameVolumenEsfera,text="m^3",justify="center",height=h2).grid(column=2,row=15,sticky=u2)

Label(frameVolumenEsfera,text="(3)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenEsfera,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenEsfera,text="Litros",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Frame(frameVolumenEsfera,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=17,columnspan=3)

Button(frameVolumenEsfera,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=18,sticky=u2)
Button(frameVolumenEsfera,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV1D(volumen,digito,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,volumenEsfera,volumenEsfera1)).grid(column=2,row=18,sticky=u2)

Label(frameVolumenEsfera,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=19,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN CONO CILINDRICO:
Label(frameVolumenConoCilindrico,image=imgConoCilindrico1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenConoCilindrico,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenConoCilindrico,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenConoCilindrico,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenConoCilindrico,text="Radio (R)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenConoCilindrico,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenConoCilindrico,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenConoCilindrico,text="Altura (h)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenConoCilindrico,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenConoCilindrico,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenConoCilindrico,text="Volumen",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenConoCilindrico,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=9,sticky=u2)
Label(frameVolumenConoCilindrico,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameVolumenConoCilindrico,bg=fondoFrameCalculos,height=83*h2).grid(column=0,row=10,columnspan=3)

Label(frameVolumenConoCilindrico,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)

Entry(frameVolumenConoCilindrico,justify="center",textvariable=digito9).grid(column=0,row=12,sticky=u2)
ttk.Combobox(frameVolumenConoCilindrico,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=12,sticky=u2)
Button(frameVolumenConoCilindrico,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=12,sticky=u2)

Frame(frameVolumenConoCilindrico,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=13,columnspan=3)

Label(frameVolumenConoCilindrico,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=14,columnspan=3,sticky=u2)

Label(frameVolumenConoCilindrico,text="(1)",justify="center",height=h2).grid(column=0,row=15,sticky=u2)
Label(frameVolumenConoCilindrico,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=15,sticky=u2)
Label(frameVolumenConoCilindrico,text="cc (ml)",justify="center",height=h2).grid(column=2,row=15,sticky=u2)

Label(frameVolumenConoCilindrico,text="(2)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenConoCilindrico,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenConoCilindrico,text="m^3",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Label(frameVolumenConoCilindrico,text="(3)",justify="center",height=h2).grid(column=0,row=17,sticky=u2)
Label(frameVolumenConoCilindrico,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=17,sticky=u2)
Label(frameVolumenConoCilindrico,text="Litros",justify="center",height=h2).grid(column=2,row=17,sticky=u2)

Frame(frameVolumenConoCilindrico,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=18,columnspan=3)

Button(frameVolumenConoCilindrico,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=19,sticky=u2)
Button(frameVolumenConoCilindrico,text=calcular,justify="center",height=h2,command=lambda:funcionV2D(volumen,digito,digito1,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,volumenConoCilindrico,volumenConoCilindrico1,volumenConoCilindrico2),bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular).grid(column=2,row=19,sticky=u2)

Label(frameVolumenConoCilindrico,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=20,columnspan=3,sticky=u2)


#CÁLCULOS VOLUMEN (2):

#VENTANA CÁLCULO VOLUMEN CILINDRO:
Label(frameVolumenCilindro,image=imgCilindro1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenCilindro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenCilindro,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenCilindro,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenCilindro,text="Radio (R)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenCilindro,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenCilindro,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenCilindro,text="Altura (h)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenCilindro,width=w4,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenCilindro,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenCilindro,text="Volúmen",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenCilindro,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=9,sticky=u2)
Label(frameVolumenCilindro,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=9,sticky=u2)

Frame(frameVolumenCilindro,bg=fondoFrameCalculos,height=83*h2).grid(column=0,row=10,columnspan=3)

Label(frameVolumenCilindro,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=11,columnspan=3,sticky=u2)

Entry(frameVolumenCilindro,justify="center",textvariable=digito9).grid(column=0,row=12,sticky=u2)
ttk.Combobox(frameVolumenCilindro,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=12,sticky=u2)
Button(frameVolumenCilindro,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=12,sticky=u2)

Frame(frameVolumenCilindro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=13,columnspan=3)

Label(frameVolumenCilindro,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=14,columnspan=3,sticky=u2)

Label(frameVolumenCilindro,text="(1)",justify="center",height=h2).grid(column=0,row=15,sticky=u2)
Label(frameVolumenCilindro,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=15,sticky=u2)
Label(frameVolumenCilindro,text="cc (ml)",justify="center",height=h2).grid(column=2,row=15,sticky=u2)

Label(frameVolumenCilindro,text="(2)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenCilindro,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenCilindro,text="m^3",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Label(frameVolumenCilindro,text="(3)",justify="center",height=h2).grid(column=0,row=17,sticky=u2)
Label(frameVolumenCilindro,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=17,sticky=u2)
Label(frameVolumenCilindro,text="Litros",justify="center",height=h2).grid(column=2,row=17,sticky=u2)

Frame(frameVolumenCilindro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=18,columnspan=3)

Button(frameVolumenCilindro,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=19,sticky=u2)
Button(frameVolumenCilindro,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV2D(volumen,digito,digito1,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,volumenCilindro,volumenCilindro1,volumenCilindro2)).grid(column=2,row=19,sticky=u2)

Label(frameVolumenCilindro,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=20,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN CONO TRUNCADO:
Label(frameVolumenConoTruncado,image=imgConoTruncado1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenConoTruncado,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenConoTruncado,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenConoTruncado,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenConoTruncado,text="Radio Mayor (R)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenConoTruncado,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenConoTruncado,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenConoTruncado,text="Radio menor (r)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenConoTruncado,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenConoTruncado,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenConoTruncado,text="Altura (h)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenConoTruncado,width=w4,justify="center",textvariable=digito2).grid(column=1,row=9,sticky=u2)
Label(frameVolumenConoTruncado,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameVolumenConoTruncado,text="Volúmen",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameVolumenConoTruncado,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=10,sticky=u2)
Label(frameVolumenConoTruncado,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=10,sticky=u2)

Frame(frameVolumenConoTruncado,bg=fondoFrameCalculos,height=62*h2).grid(column=0,row=11,columnspan=3)

Label(frameVolumenConoTruncado,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=12,columnspan=3,sticky=u2)

Entry(frameVolumenConoTruncado,justify="center",textvariable=digito9).grid(column=0,row=13,sticky=u2)
ttk.Combobox(frameVolumenConoTruncado,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=13,sticky=u2)
Button(frameVolumenConoTruncado,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=13,sticky=u2)

Frame(frameVolumenConoTruncado,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=14,columnspan=3)

Label(frameVolumenConoTruncado,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=15,columnspan=3,sticky=u2)

Label(frameVolumenConoTruncado,text="(1)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenConoTruncado,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenConoTruncado,text="cc (ml)",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Label(frameVolumenConoTruncado,text="(2)",justify="center",height=h2).grid(column=0,row=17,sticky=u2)
Label(frameVolumenConoTruncado,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=17,sticky=u2)
Label(frameVolumenConoTruncado,text="m^3",justify="center",height=h2).grid(column=2,row=17,sticky=u2)

Label(frameVolumenConoTruncado,text="(3)",justify="center",height=h2).grid(column=0,row=18,sticky=u2)
Label(frameVolumenConoTruncado,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=18,sticky=u2)
Label(frameVolumenConoTruncado,text="Litros",justify="center",height=h2).grid(column=2,row=18,sticky=u2)

Frame(frameVolumenConoTruncado,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=19,columnspan=3)

Button(frameVolumenConoTruncado,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=20,sticky=u2)
Button(frameVolumenConoTruncado,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV3D(volumen,digito,digito1,digito2,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,volumenConoTruncado,volumenConoTruncado1,volumenConoTruncado2,volumenConoTruncado3)).grid(column=2,row=20,sticky=u2)

Label(frameVolumenConoTruncado,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=21,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN PIRAMIDE TRUNCADA:
Label(frameVolumenPiramideTruncada,image=imgPiramideTruncada1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenPiramideTruncada,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenPiramideTruncada,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenPiramideTruncada,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenPiramideTruncada,text="Lado 1 (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenPiramideTruncada,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenPiramideTruncada,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenPiramideTruncada,text="Lado 2 (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenPiramideTruncada,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenPiramideTruncada,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenPiramideTruncada,text="Lado 3 (c)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenPiramideTruncada,justify="center",textvariable=digito2).grid(column=1,row=9,sticky=u2)
Label(frameVolumenPiramideTruncada,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameVolumenPiramideTruncada,text="Lado 4 (d)",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameVolumenPiramideTruncada,justify="center",textvariable=digito3).grid(column=1,row=10,sticky=u2)
Label(frameVolumenPiramideTruncada,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=10,sticky=u2)

Label(frameVolumenPiramideTruncada,text="Altura (h)",justify="right",height=h2).grid(column=0,row=11,sticky=u2)
Entry(frameVolumenPiramideTruncada,width=w4,justify="center",textvariable=digito4).grid(column=1,row=11,sticky=u2)
Label(frameVolumenPiramideTruncada,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=11,sticky=u2)

Label(frameVolumenPiramideTruncada,text="Volúmen",justify="right",height=h2).grid(column=0,row=12,sticky=u2)
Entry(frameVolumenPiramideTruncada,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=12,sticky=u2)
Label(frameVolumenPiramideTruncada,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=12,sticky=u2)

Frame(frameVolumenPiramideTruncada,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=13,columnspan=3)

Label(frameVolumenPiramideTruncada,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=14,columnspan=3,sticky=u2)

Entry(frameVolumenPiramideTruncada,justify="center",textvariable=digito9).grid(column=0,row=15,sticky=u2)
ttk.Combobox(frameVolumenPiramideTruncada,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=15,sticky=u2)
Button(frameVolumenPiramideTruncada,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=15,sticky=u2)

Frame(frameVolumenPiramideTruncada,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=16,columnspan=3)

Label(frameVolumenPiramideTruncada,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=17,columnspan=3,sticky=u2)

Label(frameVolumenPiramideTruncada,text="(1)",justify="center",height=h2).grid(column=0,row=18,sticky=u2)
Label(frameVolumenPiramideTruncada,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=18,sticky=u2)
Label(frameVolumenPiramideTruncada,text="cc (ml)",justify="center",height=h2).grid(column=2,row=18,sticky=u2)

Label(frameVolumenPiramideTruncada,text="(2)",justify="center",height=h2).grid(column=0,row=19,sticky=u2)
Label(frameVolumenPiramideTruncada,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=19,sticky=u2)
Label(frameVolumenPiramideTruncada,text="m^3",justify="center",height=h2).grid(column=2,row=19,sticky=u2)

Label(frameVolumenPiramideTruncada,text="(3)",justify="center",height=h2).grid(column=0,row=20,sticky=u2)
Label(frameVolumenPiramideTruncada,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=20,sticky=u2)
Label(frameVolumenPiramideTruncada,text="Litros",justify="center",height=h2).grid(column=2,row=20,sticky=u2)

Frame(frameVolumenPiramideTruncada,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=21,columnspan=3)

Button(frameVolumenPiramideTruncada,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=22,sticky=u2)
Button(frameVolumenPiramideTruncada,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV5D(volumen,digito,digito1,digito2,digito3,digito4,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,F3,F4,volumenPiramideTruncada,volumenPiramideTruncada1,volumenPiramideTruncada2,volumenPiramideTruncada3,volumenPiramideTruncada4,volumenPiramideTruncada5)).grid(column=2,row=22,sticky=u2)

Label(frameVolumenPiramideTruncada,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=23,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN TETRAEDRO:
Label(frameVolumenTetraedro,image=imgTetraedro1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenTetraedro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenTetraedro,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenTetraedro,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenTetraedro,text="Lado (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenTetraedro,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenTetraedro,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenTetraedro,text="Volúmen",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenTetraedro,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=8,sticky=u2)
Label(frameVolumenTetraedro,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=8,sticky=u2)

Frame(frameVolumenTetraedro,bg=fondoFrameCalculos,height=104*h2).grid(column=0,row=9,columnspan=3)

Label(frameVolumenTetraedro,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=10,columnspan=3,sticky=u2)

Entry(frameVolumenTetraedro,justify="center",textvariable=digito9).grid(column=0,row=11,sticky=u2)
ttk.Combobox(frameVolumenTetraedro,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=11,sticky=u2)
Button(frameVolumenTetraedro,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=11,sticky=u2)

Frame(frameVolumenTetraedro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=12,columnspan=3)

Label(frameVolumenTetraedro,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=13,columnspan=3,sticky=u2)

Label(frameVolumenTetraedro,text="(1)",justify="center",height=h2).grid(column=0,row=14,sticky=u2)
Label(frameVolumenTetraedro,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=14,sticky=u2)
Label(frameVolumenTetraedro,text="cc (ml)",justify="center",height=h2).grid(column=2,row=14,sticky=u2)

Label(frameVolumenTetraedro,text="(2)",justify="center",height=h2).grid(column=0,row=15,sticky=u2)
Label(frameVolumenTetraedro,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=15,sticky=u2)
Label(frameVolumenTetraedro,text="m^3",justify="center",height=h2).grid(column=2,row=15,sticky=u2)

Label(frameVolumenTetraedro,text="(3)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenTetraedro,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenTetraedro,text="Litros",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Frame(frameVolumenTetraedro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=17,columnspan=3)

Button(frameVolumenTetraedro,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=18,sticky=u2)
Button(frameVolumenTetraedro,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV1D(volumen,digito,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,volumenTetraedro,volumenTetraedro1)).grid(column=2,row=18,sticky=u2)

Label(frameVolumenTetraedro,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=19,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN OCTAEDRO:
Label(frameVolumenOctaedro,image=imgOctaedro1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenOctaedro,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenOctaedro,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenOctaedro,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenOctaedro,text="Lado (a)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenOctaedro,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenOctaedro,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenOctaedro,text="Volúmen",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenOctaedro,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=8,sticky=u2)
Label(frameVolumenOctaedro,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=8,sticky=u2)

Frame(frameVolumenOctaedro,bg=fondoFrameCalculos,height=50*h2).grid(column=0,row=9,columnspan=3)

Label(frameVolumenOctaedro,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=10,columnspan=3,sticky=u2)

Entry(frameVolumenOctaedro,justify="center",textvariable=digito9).grid(column=0,row=11,sticky=u2)
ttk.Combobox(frameVolumenOctaedro,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=11,sticky=u2)
Button(frameVolumenOctaedro,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=11,sticky=u2)

Frame(frameVolumenOctaedro,bg=fondoFrameCalculos,height=20*h2).grid(column=0,row=12,columnspan=3)

Label(frameVolumenOctaedro,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=13,columnspan=3,sticky=u2)

Label(frameVolumenOctaedro,text="(1)",justify="center",height=h2).grid(column=0,row=14,sticky=u2)
Label(frameVolumenOctaedro,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=14,sticky=u2)
Label(frameVolumenOctaedro,text="cc (ml)",justify="center",height=h2).grid(column=2,row=14,sticky=u2)

Label(frameVolumenOctaedro,text="(2)",justify="center",height=h2).grid(column=0,row=15,sticky=u2)
Label(frameVolumenOctaedro,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=15,sticky=u2)
Label(frameVolumenOctaedro,text="m^3",justify="center",height=h2).grid(column=2,row=15,sticky=u2)

Label(frameVolumenOctaedro,text="(3)",justify="center",height=h2).grid(column=0,row=16,sticky=u2)
Label(frameVolumenOctaedro,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=16,sticky=u2)
Label(frameVolumenOctaedro,text="Litros",justify="center",height=h2).grid(column=2,row=16,sticky=u2)

Frame(frameVolumenOctaedro,bg=fondoFrameCalculos,height=20*h2).grid(column=0,row=17,columnspan=3)

Button(frameVolumenOctaedro,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=18,sticky=u2)
Button(frameVolumenOctaedro,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular).grid(column=2,row=18,sticky=u2)

Label(frameVolumenOctaedro,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=19,columnspan=3,sticky=u2)


#VENTANA CÁLCULO VOLUMEN PRISMA RECTO:
Label(frameVolumenPrismaRecto,image=imgPrismaRecto1,justify="center").grid(column=0,row=0,columnspan=3,rowspan=4,sticky=u2)

Frame(frameVolumenPrismaRecto,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=5,columnspan=3)

Label(frameVolumenPrismaRecto,width=w4,text="Unidades",justify="center",height=h2).grid(column=0,row=6,sticky=u2)
ttk.Combobox(frameVolumenPrismaRecto,textvariable=listadoUnidades,width=w4,height=1,values=dimensiones1,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=6,sticky=u2)

Label(frameVolumenPrismaRecto,text="Nro. Lados (n)",justify="right",height=h2).grid(column=0,row=7,sticky=u2)
Entry(frameVolumenPrismaRecto,justify="center",textvariable=digito).grid(column=1,row=7,sticky=u2)
Label(frameVolumenPrismaRecto,width=w4,text="Lados",justify="left").grid(column=2,row=7,sticky=u2)

Label(frameVolumenPrismaRecto,text="Lado (b)",justify="right",height=h2).grid(column=0,row=8,sticky=u2)
Entry(frameVolumenPrismaRecto,justify="center",textvariable=digito1).grid(column=1,row=8,sticky=u2)
Label(frameVolumenPrismaRecto,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=8,sticky=u2)

Label(frameVolumenPrismaRecto,text="Apotema (a)",justify="right",height=h2).grid(column=0,row=9,sticky=u2)
Entry(frameVolumenPrismaRecto,justify="center",textvariable=digito2).grid(column=1,row=9,sticky=u2)
Label(frameVolumenPrismaRecto,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=9,sticky=u2)

Label(frameVolumenPrismaRecto,text="Altura (h)",justify="right",height=h2).grid(column=0,row=10,sticky=u2)
Entry(frameVolumenPrismaRecto,justify="center",textvariable=digito3).grid(column=1,row=10,sticky=u2)
Label(frameVolumenPrismaRecto,width=w4,textvariable=listadoUnidades,justify="left").grid(column=2,row=10,sticky=u2)

Label(frameVolumenPrismaRecto,text="Volúmen",justify="right",height=h2).grid(column=0,row=11,sticky=u2)
Entry(frameVolumenPrismaRecto,justify="center",bg=fondoResultados,textvariable=volumen).grid(column=1,row=11,sticky=u2)
Label(frameVolumenPrismaRecto,textvariable=unidadesFinalesVolumen,justify="left").grid(column=2,row=11,sticky=u2)

Frame(frameVolumenPrismaRecto,bg=fondoFrameCalculos,height=41*h2).grid(column=0,row=12,columnspan=3)

Label(frameVolumenPrismaRecto,width=w4,text=B3,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=13,columnspan=3,sticky=u2)

Entry(frameVolumenPrismaRecto,justify="center",textvariable=digito9).grid(column=0,row=14,sticky=u2)
ttk.Combobox(frameVolumenPrismaRecto,textvariable=listadoUnidades1,width=w4,height=1,values=dimensiones2,state="readonly",justify="center",background=fondoUnidades).grid(column=1,row=14,sticky=u2)
Button(frameVolumenPrismaRecto,text=ingresar,justify="center",height=h2,bg=fondoBotonIngresar,command=lambda:verificacionUnidades(listadoUnidades,listadoUnidades1,digito9,volumen,unidadesFinalesVolumen,comentario,U1,U2,U3)).grid(column=2,row=14,sticky=u2)

Frame(frameVolumenPrismaRecto,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=15,columnspan=3)

Label(frameVolumenPrismaRecto,text=B2,justify="left",height=h2,bg=fondoSubTitulos).grid(column=0,row=16,columnspan=3,sticky=u2)

Label(frameVolumenPrismaRecto,text="(1)",justify="center",height=h2).grid(column=0,row=17,sticky=u2)
Label(frameVolumenPrismaRecto,textvariable=enCentimetrosCubicos,justify="center",height=h2).grid(column=1,row=17,sticky=u2)
Label(frameVolumenPrismaRecto,text="cc (ml)",justify="center",height=h2).grid(column=2,row=17,sticky=u2)

Label(frameVolumenPrismaRecto,text="(2)",justify="center",height=h2).grid(column=0,row=18,sticky=u2)
Label(frameVolumenPrismaRecto,textvariable=enMetrosCubicos,justify="center",height=h2).grid(column=1,row=18,sticky=u2)
Label(frameVolumenPrismaRecto,text="m^3",justify="center",height=h2).grid(column=2,row=18,sticky=u2)

Label(frameVolumenPrismaRecto,text="(3)",justify="center",height=h2).grid(column=0,row=19,sticky=u2)
Label(frameVolumenPrismaRecto,textvariable=enLitros,justify="center",height=h2).grid(column=1,row=19,sticky=u2)
Label(frameVolumenPrismaRecto,text="Litros",justify="center",height=h2).grid(column=2,row=19,sticky=u2)

Frame(frameVolumenPrismaRecto,bg=fondoFrameCalculos,height=factor1*h2).grid(column=0,row=20,columnspan=3)

Button(frameVolumenPrismaRecto,text=borrar,command=lambda:borrarCampos(),bg=fondoBotonBorrar).grid(column=0,row=21,sticky=u2)
Button(frameVolumenPrismaRecto,text=calcular,justify="center",height=h2,bg=fondoBotonCalcular,fg=fuenteBotonCalcular,font=letraBotonCalcular,command=lambda:funcionV4D(volumen,digito,digito1,digito2,digito3,listadoUnidades,comentario,enCentimetrosCubicos,enMetrosCubicos,enLitros,unidadesFinalesVolumen,A1,A2,A3,A4,F1,F2,F3,volumenPrismaRecto,volumenPrismaRecto1,volumenPrismaRecto2,volumenPrismaRecto3,volumenPrismaRecto4)).grid(column=2,row=21,sticky=u2)

Label(frameVolumenPrismaRecto,textvariable=comentario,justify="center",height=h2,fg="red").grid(column=0,row=22,columnspan=3,sticky=u2)


#CREACIÓN BOTÓN CERRAR VENTANAS GEOMÉTRICOS:
b_cerrar_geometricos=Button(recuadroGemetricos,width=73,text="Cerrar",command=lambda:cerrarVentanaGeometria())
b_cerrar_geometricos.grid(column=0,row=1,sticky=u1,padx=10,pady=10)

#AJUSTAR TAMAÑOS DE GIDGETS:
# frame.pack(fill="x")
# frame.pack(fill="y")
# frame.pack(fill="both",expand=1)

#CONFIGURACION DEL MENU PRINCIPAL:
barra_menu=Menu(raiz)
# raiz["menu"]=barra_menu
raiz.config(menu=barra_menu)

#COMANDO PARA ELIMINAR LA LÍNEA DE LÁGRIMA DEL MENÚ:
raiz.option_add("*tearOff",False)

#CREANDO LAS PESTAÑAS DEL MENÚ PRINCIPAL:
menu_Archivo=Menu(barra_menu)
menu_Calculos=Menu(barra_menu)
menu_Acerca=Menu(barra_menu)
menu_Contactanos=Menu(barra_menu)

#AGREGANDO LAS PESTAÑAS AL MENÚ PRINCIPAL:
barra_menu.add_cascade(menu=menu_Archivo,label="Archivo")
barra_menu.add_cascade(menu=menu_Calculos,label="Cálculos")
barra_menu.add_cascade(menu=menu_Acerca,label="Acerca de")
barra_menu.add_cascade(menu=menu_Contactanos,label="Ayuda")

#CREANDO Y AGREGANDO LOS SUB MENÚS DE LA PESTAÑA "Archivo":
menu_Archivo.add_command(label="Nuevo")
menu_Archivo.add_command(label="Abrir")

menu_Archivo.add_separator()

menu_Archivo.add_command(label="Guardar")
menu_Archivo.add_command(label="Guardar como...")

menu_Archivo.add_separator()

menu_Archivo.add_command(label="Salir",command=lambda:cerrarRaiz())


#CREANDO Y AGREGANDO LOS SUB MENÚS DE LA PESTAÑA "Cálculos":
menu_Equipos=Menu(menu_Calculos)
menu_Numericos=Menu(menu_Calculos)

menu_Calculos.add_cascade(menu=menu_Equipos,label="Equipos")
menu_Calculos.add_cascade(menu=menu_Numericos,label="Numéricos")

#CREANDO Y AGREGANDO LAS OPCIONES A LA PESTAÑA "Equipos"
menu_Equipos.add_command(label="Agitación")
menu_Equipos.add_command(label="Compuertas")
menu_Equipos.add_command(label="Puentes Barredores")
menu_Equipos.add_command(label="Seditubos")

#CREANDO Y AGREGANDO LAS OPCIONES A LA PESTAÑA "Numéricos"
menu_Numericos.add_command(label="Geométricos",command=lambda:abrirVentanaGeometria())

#CREANDO Y AGREGANDO LOS SUB MENÚS DE LA PESTAÑA "Acerca de":
menu_Acerca.add_command(label="Contáctanos",command=lambda:mensajeContacto())
menu_Acerca.add_command(label="Versión",command=lambda:mensajeVersion())


#CREACIÓN DE FUNCIONES:

#Mensaje de contacto:
def mensajeContacto():
    messagebox.showinfo("Contáctanos","Para mayor información favor escribir al siguiente email:\n\nrodriguezcolmenaresl@gmail.com")

#Mensaje de versión info:
def mensajeVersion():
    messagebox.showinfo("Info. Versión","Versión 1.0 \n \nMes/Año: 04/2024")


#ABRIR Y CERRAR VENTANAS (GIDGETS):
'''https://es.stackoverflow.com/questions/413724/puedo-ocultar-widgets-con-tkinter-en-pyhton'''

#ABRIR VENTANAS PRINCIPALES:

def abrirVentanaGeometria():
    ventanaGeometria.pack(fill="both",expand=1)
    
#ABRIR VENTANAS DE ÁREAS (1):

def abrirVentanaCuadrado():
    borrarCampos()
    cerrarVentanaRectangulo()
    cerrarVentanaTriangulo()
    cerrarVentanaCirculo()
    cerrarVentanaTrapecio()
    frameAreaCuadrado.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaRectangulo():
    borrarCampos()
    cerrarVentanaCuadrado()
    cerrarVentanaTriangulo()
    cerrarVentanaCirculo()
    cerrarVentanaTrapecio()
    frameAreaRectangulo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaTriangulo():
    borrarCampos()
    cerrarVentanaCuadrado()
    cerrarVentanaRectangulo()
    cerrarVentanaCirculo()
    cerrarVentanaTrapecio()
    frameAreaTriangulo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaCirculo():
    borrarCampos()
    cerrarVentanaCuadrado()
    cerrarVentanaRectangulo()
    cerrarVentanaTriangulo()
    cerrarVentanaTrapecio()
    frameAreaCirculo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaTrapecio():
    borrarCampos()
    cerrarVentanaCuadrado()
    cerrarVentanaRectangulo()
    cerrarVentanaTriangulo()
    cerrarVentanaCirculo()
    frameAreaTrapecio.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

#ABRIR VENTANAS DE ÁREAS (2):

def abrirVentanaParalelogramo():
    borrarCampos()
    cerrarVentanaCometa()
    cerrarVentanaPoligonoRegular()
    cerrarVentanaAnillo()
    cerrarVentanaSectorCircular()

    frameAreaParalelogramo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaCometa():
    borrarCampos()
    cerrarVentanaParalelogramo()
    cerrarVentanaPoligonoRegular()
    cerrarVentanaAnillo()
    cerrarVentanaSectorCircular()

    frameAreaCometa.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaPoligonoRegular():
    borrarCampos()
    cerrarVentanaParalelogramo()
    cerrarVentanaCometa()
    cerrarVentanaAnillo()
    cerrarVentanaSectorCircular()

    frameAreaPoligonoRegular.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaAnillo():
    borrarCampos()
    cerrarVentanaParalelogramo()
    cerrarVentanaCometa()
    cerrarVentanaPoligonoRegular()
    cerrarVentanaSectorCircular()

    frameAreaAnillo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaSectorCircular():
    borrarCampos()
    cerrarVentanaParalelogramo()
    cerrarVentanaCometa()
    cerrarVentanaPoligonoRegular()
    cerrarVentanaAnillo()

    frameAreaSectorCircular.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)


#ABRIR VENTANAS VOLUMEN (1):
def abrirVentanaCubo():
    borrarCampos()
    cerrarVenanaParalelepipedo()
    cerrarVentanaPiramide()
    cerrarVentanaEsfera()
    cerrarVentanaConoCilindrico()
    cerrarVentanaCilindro()
    frameVolumenCubo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVenanaParalelepipedo():
    borrarCampos()
    cerrarVentanaCubo()
    cerrarVentanaPiramide()
    cerrarVentanaEsfera()
    cerrarVentanaConoCilindrico()
    cerrarVentanaCilindro()
    frameVolumenParalelepipedo.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaPiramide():
    borrarCampos()
    cerrarVentanaCubo()
    cerrarVenanaParalelepipedo()
    cerrarVentanaEsfera()
    cerrarVentanaConoCilindrico()
    cerrarVentanaCilindro()
    frameVolumenPiramide.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaEsfera():
    borrarCampos()
    cerrarVentanaCubo()
    cerrarVenanaParalelepipedo()
    cerrarVentanaPiramide()
    cerrarVentanaConoCilindrico()
    cerrarVentanaCilindro()
    frameVolumenEsfera.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaConoCilindrico():
    borrarCampos()
    cerrarVentanaCubo()
    cerrarVenanaParalelepipedo()
    cerrarVentanaPiramide()
    cerrarVentanaEsfera()
    cerrarVentanaCilindro()
    frameVolumenConoCilindrico.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)


#ABRIR VENTANAS VOLUMEN (2):

def abrirVentanaCilindro():
    borrarCampos()
    cerrarVenanaConoTruncado()
    cerrarVentanaPiramideTruncada()
    cerrarVentanaTetraedro()
    cerrarVentanaOctaedro()
    cerrarVentanaPrismaRecto()

    frameVolumenCilindro.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaConoTruncado():
    borrarCampos()
    cerrarVentanaCilindro()
    cerrarVentanaPiramideTruncada()
    cerrarVentanaTetraedro()
    cerrarVentanaOctaedro()
    cerrarVentanaPrismaRecto()
    
    frameVolumenConoTruncado.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)


def abrirVentanaPiramideTruncada():
    borrarCampos()
    cerrarVentanaCilindro()
    cerrarVenanaConoTruncado()
    cerrarVentanaTetraedro()
    cerrarVentanaOctaedro()
    cerrarVentanaPrismaRecto()

    frameVolumenPiramideTruncada.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaTetraedro():
    borrarCampos()
    cerrarVentanaCilindro()
    cerrarVenanaConoTruncado()
    cerrarVentanaPiramideTruncada()
    cerrarVentanaOctaedro()
    cerrarVentanaPrismaRecto()

    frameVolumenTetraedro.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaOctaedro():
    borrarCampos()
    cerrarVentanaCilindro()
    cerrarVenanaConoTruncado()
    cerrarVentanaPiramideTruncada()
    cerrarVentanaTetraedro()
    cerrarVentanaPrismaRecto()
    
    frameVolumenOctaedro.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)

def abrirVentanaPrismaRecto():
    borrarCampos()
    cerrarVentanaCilindro()
    cerrarVenanaConoTruncado()
    cerrarVentanaPiramideTruncada()
    cerrarVentanaTetraedro()
    cerrarVentanaOctaedro()

    frameVolumenPrismaRecto.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u2,padx=20)


def borrarCampos():
    area.set("")
    volumen.set("")
    digito.set("")
    digito1.set("")
    digito2.set("")
    digito3.set("")
    digito4.set("")
    digito9.set("")
    comentario.set("")
    enCentimetrosCuadrados.set("")
    enMetrosCuadrados.set("")
    enCentimetrosCubicos.set("")
    enMetrosCubicos.set("")
    enLitros.set("")
    unidadesFinalesArea.set("")
    unidadesFinalesVolumen.set("")
    listadoUnidades.set("")
    listadoUnidades1.set("")


#CERRAR VENTANAS PRINCIPALES:
def cerrarRaiz():
    raiz.destroy()

def cerrarVentanaGeometria():
    ventanaGeometria.pack_forget()

#CERRAR VENTANAS DE ÁREAS (1):
def cerrarVentanaCuadrado():
    frameAreaCuadrado.grid_remove()
    
def cerrarVentanaRectangulo():
    frameAreaRectangulo.grid_remove()
    
def cerrarVentanaTriangulo():
    frameAreaTriangulo.grid_remove()

def cerrarVentanaCirculo():
    frameAreaCirculo.grid_remove()

def cerrarVentanaTrapecio():
    frameAreaTrapecio.grid_remove()


#CERRAR VENTANAS DE ÁREAS (2):
def cerrarVentanaParalelogramo():
    frameAreaParalelogramo.grid_remove()

def cerrarVentanaCometa():
    frameAreaCometa.grid_remove()

def cerrarVentanaPoligonoRegular():
    frameAreaPoligonoRegular.grid_remove()

def cerrarVentanaAnillo():
    frameAreaAnillo.grid_remove()

def cerrarVentanaSectorCircular():
    frameAreaSectorCircular.grid_remove()


#CERRAR VENTANAS DE VOLÚMENES (1):
def cerrarVentanaCubo():
    frameVolumenCubo.grid_remove()

def cerrarVenanaParalelepipedo():
    frameVolumenParalelepipedo.grid_remove()

def cerrarVentanaPiramide():
    frameVolumenPiramide.grid_remove()

def cerrarVentanaEsfera():
    frameVolumenEsfera.grid_remove()

def cerrarVentanaConoCilindrico():
    frameVolumenConoCilindrico.grid_remove()

def cerrarVentanaCilindro():
    frameVolumenCilindro.grid_remove()


#CERRAR VENTANAS DE VOLÚMENES (2):
def cerrarVentanaCilindro():
    frameVolumenCilindro.grid_remove()

def cerrarVenanaConoTruncado():
    frameVolumenConoTruncado.grid_remove()

def cerrarVentanaPiramideTruncada():
    frameVolumenPiramideTruncada.grid_remove()

def cerrarVentanaTetraedro():
    frameVolumenTetraedro.grid_remove()

def cerrarVentanaOctaedro():
    frameVolumenOctaedro.grid_remove()

def cerrarVentanaPrismaRecto():
    frameVolumenPrismaRecto.grid_remove()


raiz.mainloop()




