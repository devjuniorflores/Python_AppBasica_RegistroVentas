#IMPORTANDO LAS LIBRERIAS NECESARIAS PARA EL PROYECTO
from tkinter import *
import tkinter

#CREACION DE LA VENTANA PARA EL INGRESO DE DATOS
raiz = Tk()
raiz.geometry("750x450")
raiz.title("Trabajo Final")

#CREACION DEL TITULO DE LA VENTANA DE INGRESO DE DATOS
bienvenido = Label(raiz, text="Ferreteria 'El Martillo Feliz'")
bienvenido.pack(side=tkinter.TOP)
bienvenido.config(font=('ARIAL',16))

#CREACION DEL FRAME PARA LA VENTANA DEL INGRESO DE DATOS
miFrame = Frame()
miFrame.pack()

#CREACION DEL LABEL DNI Y EL CUADRO DE TEXTO PARA INGRESAR LOS DATOS
dni_label = Label(miFrame, text="DNI: ")
dni_label.grid(row=1,column=0)
dni_label.config(padx=10,pady=10)
cuadro_dni = tkinter.Entry(miFrame)
cuadro_dni.grid (row=1, column=1)

#CREACION DEL LABEL APELLIDOS Y EL CUADRO DE TEXTO PARA INGRESAR LOS DATOS
apellido_label = Label(miFrame, text="Apellidos: ")
apellido_label.grid(row=2, column=0)
apellido_label.config(padx=10, pady=10)
cuadro_Apellido = Entry(miFrame)
cuadro_Apellido.grid(row=2, column=1)

#CREACION DEL LABEL NOMBRES Y EL CUADRO DE TEXTO PARA INGRESAR LOS DATOS
nombre_label = Label(miFrame, text="Nombres: ")
nombre_label.grid(row=2, column=2)
nombre_label.config(padx=10, pady=10)
cuadro_nombre = Entry(miFrame)
cuadro_nombre.grid(row=2, column=3)

#CREACION DEL LABEL DIRECCION Y EL CUADRO DE TEXTO PARA INGRESAR LOS DATOS
direccion = Label(miFrame, text="Direccion: ")
direccion.grid(row=3, column=0)
direccion.config(padx=10, pady=10)
cuadro_Direcccion = Entry(miFrame)
cuadro_Direcccion.grid(row=3, column=1)

#CREACION DEL LABEL TELEFONO Y EL CUADRO DE TEXTO PARA INGRESAR LOS DATOS
telefono = Label(miFrame, text="Telefono: ")
telefono.grid(row=4, column=0)
telefono.config(padx=10, pady=10)
cuadro_Telefono = Entry(miFrame)
cuadro_Telefono.grid(row=4, column=1)

#CREACION DE LA COLUMNA PARA LOS CODIGOS DEL PRODUCTO
cod_Producto = Label(miFrame, text="Cod_Producto")
cod_Producto.grid(row=5, column=0)
cod_Producto.config(padx=10, pady=10)

#CREACION DE LAS CAJAS DE TEXTO PARA EL INGRESO DEL COD DEL PRODUCT
cuadro_Prod1 = Entry(miFrame)
cuadro_Prod1.grid(row=6, column=0)

cuadro_Prod2 = Entry(miFrame)
cuadro_Prod2.grid(row=7, column=0,pady=10)

cuadro_Prod3 = Entry(miFrame)
cuadro_Prod3.grid(row=8, column=0)

#CREACION DE LA COLUMNA PARA LA DESCRIPCION DEL PRODUCTO
descripcion = Label(miFrame, text="Descripcion")
descripcion.grid(row=5, column=1)
descripcion.config(padx=10, pady=10)

#CREACION DE LOS LABEL PARA LA SALIDA DE LA DESCRICPION DEL PRODUCTO
salida_descripcion1 = Label(miFrame)
salida_descripcion1.grid(row=6, column=1)

salida_descripcion2 = Label(miFrame)
salida_descripcion2.grid(row=7, column=1)

salida_descripcion3 = Label(miFrame)
salida_descripcion3.grid(row=8, column=1)


#CREACION DE LA COLUMNA PARA LA CATEGORIA DEL PRODUCTO
categoria = Label(miFrame, text="Categoria")
categoria.grid(row=5, column=2)
categoria.config(padx=10, pady=10)

#CREACION DE LOS LABEL PARA LA SALIDA DE LA CATEGORIA DEL PRODUCTO
salida_categoria1 = Label(miFrame)
salida_categoria1.grid(row=6, column=2)

salida_categoria2 = Label(miFrame)
salida_categoria2.grid(row=7, column=2)

salida_categoria3 = Label(miFrame)
salida_categoria3.grid(row=8, column=2)


#CREACION DE LA COLUMNA PARA LA CANTIDAD DEL PRODUCTO
cantidad = Label(miFrame, text="Cantidad")
cantidad.grid(row=5, column=3)
cantidad.config(padx=10, pady=10)

#CREACION DE LAS CAJAS DE TEXTO PARA LA CANTIDAD DEL PRODUCTO
cuadro_Cantidad = Entry(miFrame)
cuadro_Cantidad.grid(row=6, column=3)

cuadro_Cantidad1 = Entry(miFrame)
cuadro_Cantidad1.grid(row=7, column=3)

cuadro_Cantidad2 = Entry(miFrame)
cuadro_Cantidad2.grid(row=8, column=3)


#CREACION DE LA COLUMNA PARA EL PRECIO DEL PRODUCTO
precio = Label(miFrame, text="Precio")
precio.grid(row=5, column=4)
precio.config(padx=10, pady=10)

#CREACION DE LOS LABEL PARA LA SALIDA DEL PRECIO DEL PRODUCTO
salida_precio1 = Label(miFrame)
salida_precio1.grid(row=6, column=4)

salida_precio2 = Label(miFrame)
salida_precio2.grid(row=7, column=4)

salida_precio3 = Label(miFrame)
salida_precio3.grid(row=8, column=4)

#CREACION DE LA COLUMNA PARA EL SUBTOTAL DE LA COMPRA
subtotal = Label(miFrame, text="Subtotal")
subtotal.grid(row=5, column=5)
subtotal.config(padx=10, pady=10)

#CREACION DE LOS LABEL PARA LA SALIDA DEL SUBTOTAL DE LA COMPRA
salida_subtotal1 = Label(miFrame)
salida_subtotal1.grid(row=6, column=5)

salida_subtotal2 = Label(miFrame)
salida_subtotal2.grid(row=7, column=5)

salida_subtotal3 = Label(miFrame)
salida_subtotal3.grid(row=8, column=5)


#CREACION DE LA COLUMNA PARA EL TOTAL DE LA COMPRA
total = Label(miFrame, text="Total")
total.grid(row=9, column=5)
total.config(padx=10, pady=10)

#CREACCION DEL LABEL PARA LA SALIDA DEL TOTAL DE LA COMPRA 
salida_total = Label(miFrame)
salida_total.grid(row=9,column=6)

#CREACION DE LA FUNCION PROCESAR
def procesar():
    #INICIALIZACION DE LAS VARIABLES DEL SUBTOTAL 
    s1 = 0
    s2 = 0
    s3 = 0

    #OBTENIENDO LOS DATOS DEL CUADRO DE TEXTO PARA SU LECTURA
    if (cuadro_Prod1.get() != ""):
        codProducto1 = cuadro_Prod1.get()
        cant = cuadro_Cantidad.get()

        #GENERANDO LA LOGICA PARA SALIDA DE LOS LABEL DEL PRODUCTO
        if codProducto1 == "C01":
            textProductoDescripcion = "Martillo"
            textDescricpcion = "Herramienta de construcción"
            textPrecio = "S/30.50"
            textSubtotal = float(cant) * 30.50
            s1 = textSubtotal

        elif codProducto1 == "C02":
            textProductoDescripcion = "Desarmador"
            textDescricpcion = "Herramienta de mano"
            textPrecio = "S/6.00"
            textSubtotal = float(cant) * 6.00
            s1 = textSubtotal

        elif codProducto1 == "C03":
            textProductoDescripcion = "Brocha"
            textDescricpcion = "Herramienta de pintura"
            textPrecio = "S/36.90"
            textSubtotal = float(cant) * 36.90
            s1 = textSubtotal

        elif codProducto1 == "C04":
            textProductoDescripcion = "Pintura"
            textDescricpcion = "Pintura de alto rendimiento"
            textPrecio = "S/55.50"
            textSubtotal = float(cant) * 55.50
            s1 = textSubtotal

        #ASIGNANDO LOS VALORES CORRESPONDIENTES PARA CADA LABEL DEL PRODUCTO
        salida_descripcion1["text"] = textProductoDescripcion
        salida_categoria1["text"] = textDescricpcion
        salida_precio1["text"] = textPrecio  
        salida_subtotal1["text"] = textSubtotal

    #OBTENIENDO LOS DATOS DEL CUADRO DE TEXTO PARA SU LECTURA
    if (cuadro_Prod2.get() != ""):
        codProducto2 = cuadro_Prod2.get()
        cant = cuadro_Cantidad1.get()

        #GENERANDO LA LOGICA PARA SALIDA DE LOS LABEL DEL PRODUCTO
        if codProducto2 == "C01":
            textProductoDescripcion = "Martillo"
            textDescricpcion = "Herramienta de construcción"
            textPrecio = "S/30.50"
            textSubtotal = float(cant) * 30.50
            s2 = textSubtotal

        elif codProducto2 == "C02":
            textProductoDescripcion = "Desarmador"
            textDescricpcion = "Herramienta de mano"
            textPrecio = "S/6.00"
            textSubtotal = float(cant) * 6.00
            s2 = textSubtotal

        elif codProducto2 == "C03":
            textProductoDescripcion = "Brocha"
            textDescricpcion = "Herramienta de pintura"
            textPrecio = "S/36.90"
            textSubtotal = float(cant) * 36.90
            s2 = textSubtotal

        elif codProducto2 == "C04":
            textProductoDescripcion = "Pintura"
            textDescricpcion = "Pintura de alto rendimiento"
            textPrecio = "S/55.50"
            textSubtotal = float(cant) * 55.50
            s2 = textSubtotal
        
        #ASIGNANDO LOS VALORES CORRESPONDIENTES PARA CADA LABEL DEL PRODUCTO
        salida_descripcion2["text"] = textProductoDescripcion
        salida_categoria2["text"] = textDescricpcion
        salida_precio2["text"] = textPrecio  
        salida_subtotal2["text"] = textSubtotal

    #OBTENIENDO LOS DATOS DEL CUADRO DE TEXTO PARA SU LECTURA
    if (cuadro_Prod3.get() != ""):
        codProducto3 = cuadro_Prod3.get()
        cant = cuadro_Cantidad2.get()

        #GENERANDO LA LOGICA PARA SALIDA DE LOS LABEL DEL PRODUCTO
        if codProducto3 == "C01":
            textProductoDescripcion = "Martillo"
            textDescricpcion = "Herramienta de construcción"
            textPrecio = "S/30.50"
            textSubtotal = float(cant) * 30.50
            s3 = textSubtotal

        elif codProducto3 == "C02":
            textProductoDescripcion = "Desarmador"
            textDescricpcion = "Herramienta de mano"
            textPrecio = "S/6.00"
            textSubtotal = float(cant) * 6.00
            s3 = textSubtotal

        elif codProducto3 == "C03":
            textProductoDescripcion = "Brocha"
            textDescricpcion = "Herramienta de pintura"
            textPrecio = "S/36.90"
            textSubtotal = float(cant) * 36.90
            s3 = textSubtotal

        elif codProducto3 == "C04":
            textProductoDescripcion = "Pintura"
            textDescricpcion = "Pintura de alto rendimiento"
            textPrecio = "S/55.50"
            textSubtotal = float(cant) * 55.50
            s3 = textSubtotal

        #ASIGNANDO LOS VALORES CORRESPONDIENTES PARA CADA LABEL DEL PRODUCTO      
        salida_descripcion3["text"] = textProductoDescripcion
        salida_categoria3["text"] = textDescricpcion
        salida_precio3["text"] = textPrecio  
        salida_subtotal3["text"] = textSubtotal

    #CREANDO LA LOGICA PARA EL TOTAL DE LA COMPRA
    totalCompra = "S/" + str(s1 + s2 + s3)
    
    #ASIGNANDO EL VALOR AL LABEL DEL TOTAL DE LA COMPRA
    salida_total["text"] = totalCompra


    #PROCESO DE SALIDA, CREACION DE LA VENTANA DE IMPRESIÓN/SALIDA
    ventana = Tk()
    ventana.geometry("850x350")
    ventana.title("Salida/Impresion")

    bienvenido2 = Label(ventana, text="ORDEN DE COMPRA")
    bienvenido2.grid(row=0,column=3)
    bienvenido2.config(font=('ARIAL',16),pady=15)

    #CREACION DE LOS LABEL DE SALIDA
    salida_dni_texto = Label(ventana, text="DNI:")
    salida_dni_texto.grid(row=1, column=0)
    salida_dni_texto.config(padx=5)

    salida_dni = Label(ventana)
    salida_dni.grid(row=1, column=1)

    salida_nombre_texto = Label(ventana, text="NOMBRES:")
    salida_nombre_texto.grid(row=2, column=0)
    salida_nombre_texto.config(padx=5)

    salida_nombre = Label(ventana)
    salida_nombre.grid(row=2, column=1)

    salida_apellidos_texto = Label(ventana, text="APELLIDOS:")
    salida_apellidos_texto.grid(row=3, column=0)
    salida_apellidos_texto.config(padx=5)

    salida_apellidos = Label(ventana)
    salida_apellidos.grid(row=3, column=1)

    salida_direccion_texto = Label(ventana, text="DIRECCION:")
    salida_direccion_texto.grid(row=1, column=3)
    salida_direccion_texto.config(padx=10)

    salida_direccion = Label(ventana)
    salida_direccion.grid(row=1, column=4)

    salida_telefono_texto = Label(ventana, text="TELEFONO:")
    salida_telefono_texto.grid(row=2, column=3)
    salida_telefono_texto.config(padx=10,pady=10)

    salida_telefono = Label(ventana)
    salida_telefono.grid(row=2, column=4)

    salida_columna_codProducto = Label(ventana, text="COD_PRODUCTO")
    salida_columna_codProducto.grid(row=4,column=0)
    salida_columna_codProducto.config(pady=15,padx=20)

    salida_codProducto1 = Label(ventana)
    salida_codProducto1.grid(row=5, column=0)

    salida_codProducto2 = Label(ventana)
    salida_codProducto2.grid(row=6, column=0)

    salida_codProducto3 = Label(ventana)
    salida_codProducto3.grid(row=7, column=0)

    salida_columna_cantidad = Label(ventana, text="CANTIDAD")
    salida_columna_cantidad.grid(row=4,column=2)
    salida_columna_cantidad.config(pady=15)

    salida_cantidad1 = Label(ventana)
    salida_cantidad1.grid(row=5, column=2)

    salida_cantidad2 = Label(ventana)
    salida_cantidad2.grid(row=6, column=2)

    salida_cantidad3 = Label(ventana)
    salida_cantidad3.grid(row=7, column=2)

    salida_columna_descripcion = Label(ventana, text="DESCRIPCION")
    salida_columna_descripcion.grid(row=4,column=3)
    salida_columna_descripcion.config(pady=15)

    salida_descripcion_item1 = Label(ventana)
    salida_descripcion_item1.grid(row=5, column=3)

    salida_descripcion_item2 = Label(ventana)
    salida_descripcion_item2.grid(row=6, column=3)

    salida_descripcion_item3 = Label(ventana)
    salida_descripcion_item3.grid(row=7, column=3)

    salida_columna_precio = Label(ventana, text="PRECIO")
    salida_columna_precio.grid(row=4,column=4)
    salida_columna_precio.config(pady=15)

    salida_precio_item1 = Label(ventana)
    salida_precio_item1.grid(row=5, column=4)

    salida_precio_item2 = Label(ventana)
    salida_precio_item2.grid(row=6, column=4)

    salida_precio_item3 = Label(ventana)
    salida_precio_item3.grid(row=7, column=4)

    salida_columna_subtotal = Label(ventana, text="SUBTOTAL")
    salida_columna_subtotal.grid(row=4,column=5)
    salida_columna_subtotal.config(pady=15, padx=20)

    salida_subtotal_item1 = Label(ventana)
    salida_subtotal_item1.grid(row=5, column=5)

    salida_subtotal_item2 = Label(ventana)
    salida_subtotal_item2.grid(row=6, column=5)

    salida_subtotal_item3 = Label(ventana)
    salida_subtotal_item3.grid(row=7, column=5)

    salida_columna_total = Label(ventana, text="TOTAL")
    salida_columna_total.grid(row=7,column=6)
    salida_columna_total.config(pady=0)

    salida_total_items = Label(ventana)
    salida_total_items.grid(row=7, column=7)

    #ASIGNANDO LOS DATOS A LOS LABEL DE SALIDA/IMPRESIÓN
    dni = cuadro_dni.get()
    salida_dni["text"] = dni

    apellidos = cuadro_Apellido.get()
    salida_apellidos["text"] = apellidos

    nombre = cuadro_nombre.get()
    salida_nombre["text"] = nombre

    direcciones = cuadro_Direcccion.get()
    salida_direccion["text"] = direcciones

    telefonos = cuadro_Telefono.get()
    salida_telefono["text"] = telefonos

    codProducto1 = cuadro_Prod1.get()
    salida_codProducto1["text"] = codProducto1

    codProducto2 = cuadro_Prod2.get()
    salida_codProducto2["text"] = codProducto2

    codProducto3 = cuadro_Prod3.get()
    salida_codProducto3["text"] = codProducto3

    cantidadProducto1 = cuadro_Cantidad.get()
    salida_cantidad1["text"] = cantidadProducto1

    cantidadProducto2 = cuadro_Cantidad1.get()
    salida_cantidad2["text"] = cantidadProducto2

    cantidadProducto3 = cuadro_Cantidad2.get()
    salida_cantidad3["text"] = cantidadProducto3

    salida_descripcion_item1["text"] = salida_descripcion1["text"]
    salida_descripcion_item2["text"] = salida_descripcion2["text"]
    salida_descripcion_item3["text"] = salida_descripcion3["text"]

    salida_precio_item1["text"] = salida_precio1["text"]
    salida_precio_item2["text"] = salida_precio2["text"]
    salida_precio_item3["text"] = salida_precio3["text"]

    salida_subtotal_item1["text"] = salida_subtotal1["text"]
    salida_subtotal_item2["text"] = salida_subtotal2["text"]
    salida_subtotal_item3["text"] = salida_subtotal3["text"]

    salida_total_items["text"]  = salida_total["text"]
    
    #EJECUCION DE LA VENTANA PARA LA SALIDA/IMPRESIÓN DE DATOS
    ventana.mainloop()

#CREACION DEL BOTON PROCESAR LA CUAL EJECUTA LA FUNCION PROCESAR
botonProcesar = tkinter.Button(raiz, text="Procesar", command=procesar, bg="gray")
botonProcesar.pack()

#EJECUCION DE LA VENTANA PARA EL INGRESO DE DATOS
raiz.mainloop()
