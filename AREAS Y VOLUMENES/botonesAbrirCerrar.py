#Cerrar ventanas:
def cerrarRaiz():
    raiz.destroy()

def abrirVentanaGeometria():
    '''https://es.stackoverflow.com/questions/413724/puedo-ocultar-widgets-con-tkinter-en-pyhton'''
    ventanaGeometria.pack(fill="both",expand=1)
    
def cerrarVentanaGeometria():
    ventanaGeometria.pack_forget()

def cerrarVentanaCuadrado():
    frameAreas.grid_forget()

def cerrarVentanaRectangulo():
    frameAreas.grid_remove()

def abrirVentanaCuadrado():
    # cerrarVentanaRectangulo()
    frameAreas.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u,padx=20)

def abrirVentanaRectangulo():
    cerrarVentanaCuadrado()
    frameAreas.grid(column=1,row=0,columnspan=3,rowspan=10,sticky=u,padx=20)