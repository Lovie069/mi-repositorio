from tkinter import *

raiz=Tk()
raiz.title("Calculadora")
raiz.geometry("250x300")
raiz.config(bg="blue")

# raiz.resizable(False,False) #Impide cambiar el tamaño
# raiz.minsize(100,100) #Establece un tamaño Mínimo
# raiz.maxsize(600,600) #Establece un tamaño Máximo

#Establece pantalla completa
# raiz.attributes("-fullscreen",1) #Despues no puedes minimizar.

#Iconifying and Withdrawing:
thestate=raiz.state()
raiz.state("normal")
# raiz.iconify() #La app inicia minimizada
# raiz.deiconify() #La app se muestra al inciar
# raiz.withdraw() #La app nunca se muestra


#Muestra la informacion del tamaño de la ventana:
# print(raiz.winfo_reqwidth())
# print(raiz.winfo_reqheight())

#Protocolo para advertirle al usuario que debe guardar antes de cerrar
# raiz.protocol("WM_DELETE_WINDOOW",callback) #callback debe ser una funcion

#Transparencia de una ventana: va de 0.0 a 1
# raiz.attributes("-alpha",0.9)

miFrame=Frame(raiz)
miFrame.pack()

# VARIABLES GLOBALES
caracter=StringVar()

resultado=0
operacion=""
reset_pantalla=False

d=0

print(resultado)
print(operacion)
print(reset_pantalla)


# FUNCIÓN PARA INSERTAR DIGITOS EN LA PANTALLA
def presionarBoton(digito):

    global operacion, resultado, reset_pantalla, d

    if reset_pantalla==True:
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= resultado
            operacion=operacion            
            # caracter.set(digito)
            # reset_pantalla=False

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            operacion=""

        caracter.set(digito)
        reset_pantalla=False        

    elif reset_pantalla==False:

        if d==0:

            if digito==".":
                caracter.set(caracter.get() + digito)

                d+=1

            elif digito!=".":
                caracter.set(caracter.get() + digito)

        else:
            if digito==".":
                caracter.set(caracter.get())

            elif digito!=".":
                caracter.set(caracter.get() + digito)

      
    print(resultado)
    print(operacion)
    print(reset_pantalla)


# FUNCIÓN SUMAR:
    
def suma():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado=resultado + float(caracter.get())
        
        elif operacion=="restar":
            resultado= resultado - float(caracter.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(caracter.get())
        
        elif operacion=="":
            resultado= float(caracter.get())

        elif operacion=="dividir":
            try:
                resultado= resultado / float(caracter.get())
        
            except ZeroDivisionError:
                resultado="INF"

#RESULTA:
        operacion="sumar"
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()=="":
        resultado=resultado
        operacion="sumar"
        reset_pantalla=True
        caracter.set(resultado)
        
#SI NO:
    elif reset_pantalla==True:
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= float(caracter.get())
            operacion="sumar"
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            caracter.set("")

    print(resultado)
    print(operacion)
    print(reset_pantalla)
  

# FUNCIÓN RESTAR:
    
def resta():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False  and caracter.get()!="":

        if operacion=="sumar":
            resultado=resultado + float(caracter.get())
        
        elif operacion=="restar":
            resultado= resultado - float(caracter.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(caracter.get())
        
        elif operacion=="":
            resultado= float(caracter.get())

        elif operacion=="dividir":
            try:
                resultado= resultado / float(caracter.get())
        
            except ZeroDivisionError:
                resultado="INF"

#RESULTA:
        operacion="restar"
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()=="":
        resultado=resultado
        operacion="restar"
        reset_pantalla=True
        caracter.set(resultado)
            
#SI NO:
    elif reset_pantalla==True:
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= float(caracter.get())
            operacion="restar"
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            caracter.set("")

    print(resultado)
    print(operacion)
    print(reset_pantalla)


# FUNCIÓN MULTIPLICAR:
    
def multiplica():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado=resultado + float(caracter.get())
        
        elif operacion=="restar":
            resultado= resultado - float(caracter.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(caracter.get())      

        elif operacion=="":
            resultado= float(caracter.get())
      
        elif operacion=="dividir":
            try:
                resultado= resultado / float(caracter.get())
        
            except ZeroDivisionError:
                resultado="INF"

#RESULTA:
        operacion="multiplicar"
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()=="":
        resultado=resultado
        operacion="multiplicar"
        reset_pantalla=True
        caracter.set(resultado)
        
#SI NO:
    elif reset_pantalla==True:
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= float(caracter.get())
            operacion="multiplicar"
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            caracter.set("")

    print(resultado)
    print(operacion)
    print(reset_pantalla)


# FUNCIÓN DIVIDIR:
    
def divide():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado=resultado + float(caracter.get())
        
        elif operacion=="restar":
            resultado= resultado - float(caracter.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(caracter.get())

        elif operacion=="":
            resultado= float(caracter.get())
        
        elif operacion=="dividir":
                try:
                    resultado= resultado / float(caracter.get())
            
                except ZeroDivisionError:
                    resultado= "INF"

#RESULTA:       
        operacion="dividir"
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()=="":
        resultado=resultado
        operacion="dividir"
        reset_pantalla=True
        caracter.set(resultado)
                 
#SI NO:
    elif reset_pantalla==True:
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= float(caracter.get())
            operacion="dividir"
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            caracter.set("")

    print(resultado)
    print(operacion)
    print(reset_pantalla)


# FUNCION RESULTADO:

def subTotal():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado= resultado + float(caracter.get())

        elif operacion=="restar":
            resultado= resultado - float(caracter.get())

        elif operacion=="multiplicar":
            resultado= resultado * float(caracter.get())
           
        elif operacion=="":
            resultado= float(caracter.get())
                  
        elif operacion=="dividir":
                try:
                    resultado= resultado / float(caracter.get())
            
                except ZeroDivisionError:
                    resultado= "INF"

#RESULTA:       
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()=="":
        resultado=resultado
        operacion=""
        reset_pantalla=True
        caracter.set(resultado)
        

#RESULTA (en True con todas las operaciones):

    elif reset_pantalla==True:
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= float(caracter.get())
            reset_pantalla=True
            caracter.set(resultado)
        
        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            reset_pantalla=False
            caracter.set("")

    operacion=""

    print(resultado)
    print(operacion)
    print(reset_pantalla)


#FUNCION CAMBIO DE SIGNO:
    
def cambio_signo():

    global operacion, resultado, reset_pantalla, d

    d=0
    
    if reset_pantalla==False and caracter.get()=="":
        
        resultado=resultado
        operacion=operacion
        reset_pantalla=True
        
    elif reset_pantalla==False and caracter.get()!="":
        
        caracter.set(-1 * float(caracter.get()))
            
        resultado=resultado
        operacion=operacion
        reset_pantalla=False

#RESULTA (en True con todas las operaciones):

    elif reset_pantalla==True and operacion=="":
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= -1 * float(caracter.get())
            operacion=""
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            operacion=""
            reset_pantalla=False
            caracter.set("")


    print(resultado)
    print(operacion)
    print(reset_pantalla)


######################################################

# FUNCION POTENCIA

def porcentaje():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()=="":
        
        resultado=resultado
        operacion=""
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado= resultado * (1 + float(caracter.get()) / 100)

        elif operacion=="restar":
            resultado= resultado * (1 - float(caracter.get()) / 100)

        elif operacion=="multiplicar":
            resultado= resultado * (1 * float(caracter.get()) / 100)

        elif operacion=="":
            resultado= resultado * (1 + float(caracter.get()) / 100)

        elif operacion=="dividir":
            try:
                resultado= resultado * (1 / (float(caracter.get()) / 100))
        
            except ZeroDivisionError:
                resultado= "INF"


    #RESULTA:
    
        reset_pantalla=True
        caracter.set(resultado)


#RESULTA (en True con todas las operaciones):

    elif reset_pantalla==True and operacion=="":
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= 0
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            reset_pantalla=False
            caracter.set("")


    operacion=""

    print(resultado)
    print(operacion)
    print(reset_pantalla)
   




#BORRAR ULTIMA OPERACIÓN:
    
def borrar_error():
    
    global operacion, resultado, reset_pantalla, d

    d=0

    resultado= resultado
    caracter.set("")
    reset_pantalla=False

    print(resultado)
    print(operacion)
    print(reset_pantalla)


#BORRAR ALL:
    
def borrar_todo():

    global operacion, resultado, reset_pantalla, d

    d=0

    resultado= 0
    operacion=""
    reset_pantalla=False
    caracter.set("")

    print(resultado)
    print(operacion)
    print(reset_pantalla)


#BORRAR ULTIMO DIGITO:
    
def borrar_ultimo():

    global operacion, resultado, reset_pantalla, d

    d=0

    if caracter.get()!="":
        caracter.set(caracter.get()[:-1])

    else:
        caracter.set("")

#########################################################

#FUNCION INVERSO:

def inv():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()=="":
        
        resultado=resultado
        operacion=""
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado= resultado + (1 / float(caracter.get()))

        elif operacion=="restar":
            resultado= resultado - (1 / float(caracter.get()))

        elif operacion=="multiplicar":
            resultado= resultado * (1 / float(caracter.get()))

        elif operacion=="":
            resultado= (1 / float(caracter.get()))

        elif operacion=="dividir":
            try:
                resultado= resultado / (1 / float(caracter.get()))
        
            except ZeroDivisionError:
                resultado= "INF"

    #RESULTA:
    
        reset_pantalla=True
        caracter.set(resultado)


#RESULTA (en True con todas las operaciones):

    elif reset_pantalla==True and operacion=="":
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= 1 / float(caracter.get())
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            reset_pantalla=False
            caracter.set("")


    operacion=""

    print(resultado)
    print(operacion)
    print(reset_pantalla)


# FUNCION POTENCIA

def potencia():

    global operacion, resultado, reset_pantalla, d

    d=0

    if reset_pantalla==False and caracter.get()=="":
        
        resultado=resultado
        operacion=""
        reset_pantalla=True
        caracter.set(resultado)

    elif reset_pantalla==False and caracter.get()!="":

        if operacion=="sumar":
            resultado= resultado + (float(caracter.get()) ** 2)

        elif operacion=="restar":
            resultado= resultado - (float(caracter.get()) ** 2)

        elif operacion=="multiplicar":
            resultado= resultado * (float(caracter.get()) ** 2)

        elif operacion=="":
            resultado= float(caracter.get()) ** 2

        elif operacion=="dividir":
            try:
                resultado= resultado / (float(caracter.get()) ** 2)
        
            except ZeroDivisionError:
                resultado= "INF"


    #RESULTA:
    
        reset_pantalla=True
        caracter.set(resultado)


#RESULTA (en True con todas las operaciones):

    elif reset_pantalla==True and operacion=="":
        if caracter.get()!="INF" or caracter.get()!="COMPLEJO":
            resultado= float(caracter.get()) ** 2
            reset_pantalla=True
            caracter.set(resultado)

        elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
            resultado= 0
            reset_pantalla=False
            caracter.set("")


    operacion=""

    print(resultado)
    print(operacion)
    print(reset_pantalla)
       

#FUNCIÓN RAÍZ CUADRADA:

def raiz_cuadrada():
    
    global operacion, resultado, reset_pantalla, d

    d=0

    if float(caracter.get())>=0:

        if reset_pantalla==False and caracter.get()=="":
            
            resultado=resultado
            # operacion=""
            reset_pantalla=True
            caracter.set(resultado)

        elif reset_pantalla==False and caracter.get()!="":

            if operacion=="sumar":
                resultado= resultado + (float(caracter.get()) ** 0.5)

            elif operacion=="restar":
                resultado= resultado - (float(caracter.get()) ** 0.5)

            elif operacion=="multiplicar":
                resultado= resultado * (float(caracter.get()) ** 0.5)

            elif operacion=="":
                resultado= float(caracter.get()) ** 0.5

            elif operacion=="dividir":
                try:
                    resultado= resultado / (float(caracter.get()) ** 0.5)
            
                except ZeroDivisionError:
                    resultado= "INF"


        #RESULTA:
            # operacion=""   
            reset_pantalla=True
            caracter.set(resultado)



    #RESULTA (en True con todas las operaciones):

        elif reset_pantalla==True:
                resultado= float(caracter.get()) ** 0.5
                reset_pantalla=True
                caracter.set(resultado)



    elif float(caracter.get())<0:
        resultado= "COMPLEJO"
        reset_pantalla=True
        caracter.set(resultado)

    elif caracter.get()=="INF" or caracter.get()=="COMPLEJO":
        resultado= 0
        reset_pantalla=False
        caracter.set("")
        
    operacion=""

    print(resultado)
    print(operacion)
    print(reset_pantalla)

############################################################

#UBICACIÓN DE CADA BOTÓN:

#ORDEN DE FILAS

fila1=1
fila2=2
fila3=3
fila4=4
fila5=5
fila6=6
fila7=7
fila8=8
fila9=9
fila10=10

# DIMENSION DE LOS BOTONES
ancho=6
alto=2



#********* PANTALLA = FILA 0 ***************************************
# pantalla1=Entry(miFrame, textvariable=resultado)
# pantalla1.grid(row=fila1, column=1,padx=10,pady=10, columnspan=4)
# pantalla1.config(background="#D7BDE2", fg="#6C3483",justify="right")

#********* PANTALLA = FILA 1 ***************************************
pantalla2=Entry(miFrame, textvariable=caracter, font= "Comic")
pantalla2.grid(row=fila1, column=1, padx=5, pady=5, columnspan=4)
pantalla2.config(background="white", fg="black", justify="right")

#********* FILA 2 *************************************************
botonP=Button(miFrame, text="%", width=ancho, height=alto, command=lambda:porcentaje())
botonCE=Button(miFrame, text="CE", width=ancho, height=alto, command=lambda:borrar_error())
botonC=Button(miFrame, text="C", width=ancho, height=alto, command=lambda:borrar_todo())
boton_borrar=Button(miFrame, text="DEL", width=ancho, height=alto, command=lambda:borrar_ultimo())

botonP.grid(row=fila2, column=1)
botonCE.grid(row=fila2, column=2)
botonC.grid(row=fila2, column=3)
boton_borrar.grid(row=fila2, column=4)

#********* FILA 3 *************************************************
botonINV=Button(miFrame, text="1/x", width=ancho, height=alto, command=lambda:inv())
botonPOT=Button(miFrame, text="x^2", width=ancho, height=alto, command=lambda:potencia())#"x^2"
botonRAIZ=Button(miFrame, text="x^(1/2)", width=ancho, height=alto, command=lambda:raiz_cuadrada())#"x^(1/2)"
boton_dividir=Button(miFrame, text="/", width=ancho, height=alto, command=lambda:divide())

botonINV.grid(row=fila3, column=1)
botonPOT.grid(row=fila3, column=2)
botonRAIZ.grid(row=fila3, column=3)
boton_dividir.grid(row=fila3, column=4)


#********* FILA 4 *************************************************
boton7=Button(miFrame, text="7", width=ancho, height=alto, command=lambda:presionarBoton("7"))
boton8=Button(miFrame, text="8", width=ancho, height=alto, command=lambda:presionarBoton("8"))
boton9=Button(miFrame, text="9", width=ancho, height=alto, command=lambda:presionarBoton("9"))
boton_multiplicar=Button(miFrame, text="x", width=ancho, height=alto, command=lambda:multiplica())

boton7.grid(row=fila4, column=1)
boton8.grid(row=fila4, column=2)
boton9.grid(row=fila4, column=3)
boton_multiplicar.grid(row=fila4, column=4)


#********* FILA 5 *************************************************
boton4=Button(miFrame, text="4", width=ancho, height=alto, command=lambda:presionarBoton("4"))
boton5=Button(miFrame, text="5", width=ancho, height=alto, command=lambda:presionarBoton("5"))
boton6=Button(miFrame, text="6", width=ancho, height=alto, command=lambda:presionarBoton("6"))
boton_restar=Button(miFrame, text="-", width=ancho, height=alto, command=lambda:resta())

boton4.grid(row=fila5, column=1)
boton5.grid(row=fila5, column=2)
boton6.grid(row=fila5, column=3)
boton_restar.grid(row=fila5, column=4)

#********* FILA 6 *************************************************
boton1=Button(miFrame, text="1", width=ancho, height=alto, command=lambda:presionarBoton("1"))
boton2=Button(miFrame, text="2", width=ancho, height=alto, command=lambda:presionarBoton("2"))
boton3=Button(miFrame, text="3", width=ancho, height=alto, command=lambda:presionarBoton("3"))
boton_sumar=Button(miFrame, text="+", width=ancho, height=alto, command=lambda:suma())

boton1.grid(row=fila6, column=1)
boton2.grid(row=fila6, column=2)
boton3.grid(row=fila6, column=3)
boton_sumar.grid(row=fila6, column=4)


#********* FILA 7 *************************************************
botonMM=Button(miFrame, text="+/-", width=ancho, height=alto, command=lambda:cambio_signo())
boton0=Button(miFrame, text="0", width=ancho, height=alto, command=lambda:presionarBoton("0"))
botonDecimal=Button(miFrame, text=".", width=ancho, height=alto, command=lambda:presionarBoton("."))
boton_igual=Button(miFrame, text="=", width=ancho, height=alto, command=lambda:subTotal())

botonMM.grid(row=fila7, column=1)
boton0.grid(row=fila7, column=2)
botonDecimal.grid(row=fila7, column=3)
boton_igual.grid(row=fila7, column=4)


#CÓDIGO PARA INGRESAR DATOS POR TECLADO:
#widget.bind(evento, callback)

# Numeros
for n in range(0, 10):
    raiz.bind(str(n), lambda event: presionarBoton(event.char))
    raiz.bind(f"<KP_{n}>", lambda event: presionarBoton(event.char))

# Punto decimal
raiz.bind(".", lambda event: presionarBoton(event.char))
raiz.bind("<KP_Decimal>", lambda event: presionarBoton(event.char))

# Operadores
raiz.bind("*", lambda _: multiplica())
raiz.bind("<KP_Multiply>", lambda _:  multiplica())
raiz.bind("/", lambda _: divide())
raiz.bind("<KP_Divide>", lambda _: divide())
raiz.bind("+", lambda _: suma())
raiz.bind("<KP_Add>", lambda _: suma())
raiz.bind("-", lambda _: resta())
raiz.bind("<KP_Subtract>", lambda _: resta())


# Clear (SUPR)
raiz.bind("<Delete>", lambda _: borrar_todo())


# Delete (BackSpace)
raiz.bind("<BackSpace>", lambda _: borrar_ultimo())


# = (Return/Intro)
raiz.bind("<Return>", lambda _: subTotal())
raiz.bind("<KP_Enter>", lambda _: subTotal())



raiz.mainloop()