"""
Este programa corresponde a un demo del proyecto en alto nivel. El objetivo es
obtener una idea básica de los scripts que se van a aplicar y también de las
instrucciones que se necesitan para realizar la interpolación.

Cada función se va a comentar para conocer su funcionalidad luego en el proyecto,
además la función que corresponde al algoritmo se va a comentar con más detalles para
conocer las instrucciones que se deben plantear en la arquitectura.
"""

# IMPORTACIONES

import numpy as np
import imageio

# VARIABLES GLOBALES

NOMBRE_IMAGEN = "images/test-image.bmp"
PIXELES_IMAGEN = 360
ZOOM = 4
PIXELES_NIMAGEN = PIXELES_IMAGEN // ZOOM

# FUNCIONES

def leer_imagen(ruta):
    """
    Esta funcion guarda la imagen especificada en la ruta en una lista
    que contiene el RGB de cada pixel.

    Es útil para poder obtener los valores que caracterizan cada pixel
    de la imagen.
    """
    return np.array(imageio.imread(ruta), dtype='int').tolist()

def guardar_imagen(ruta, lista):
    """
    Esta funcion guarda la imagen especificada en una lista como escala de grises
    en la ruta espcificada.

    Es útil para poder guardar como imagen la lista de valores en el archivo de salida
    del procesador.
    """

    # convertir la lista en una matriz que especifique las filas y columnas para la imagen
    matriz = []
    for y in range(357):
        tempList = []
        for x in range(360):
            elem = y * 360 + x
            tempList.append(lista[elem])
        matriz.append(tempList)

    return imageio.imwrite(ruta, np.array(matriz, dtype="uint8"))

def escala_grises(nombre_imagen):
    """
    Esta funcion convierte la imagen especificada de RGB a una
    lista en escala de grises. En esta lista retornada cada elemento
    corresponde a la escala de gris de un pixel.

    Es útil para traducir el RGB obtenido de la bibioteca a su equivalente en gris.
    """
    matriz = leer_imagen(nombre_imagen)
    ancho = 360
    alto = 360
    lista_grises = []

    for y in range(alto):
        for x in range(ancho):
            pixel = matriz[y][x]
            promedio = (pixel[0] + pixel[1] + pixel[2]) // 3
            lista_grises.append(promedio)

    return lista_grises

def zoom_imagen(lista, seccion):
    """
    Funcion que genera una lista del mismo tamaño a la inicial con un zoom
    en la seccion especificada por medio de interpolacion bilinial

    input:  lista -> la lista con la escala de grises de la imagen inicial
            seccion -> el numero de la seccion a la que se le hace zoom

    output: lista_zoom -> lista con el zoom aplicado

    Esta función corresponde a lo que se debe implementar como código ensamblador.
    """

    # se calcula el numero de pixel inicial del zoom de la imagen en la
    # imagen original
    dir_inicial = (seccion // 4) * 360 * 90 + (seccion % 4) * 90

    # esta lista ya en ensamblador solamente la consideramos como una
    # direccion de memoria
    lista_zoom = [0] * (360 ** 2 - 3 * 360) # para que cada pixel tenga valores conocidos a su lados se deben quitar las 3 últimas filas

    # Primero se añaden a la memoria los elementos de la imagen que ya se conocen
    # (reescribir los datos que ya se tienen de la imagen original)
    contador = 0
    while (contador < PIXELES_IMAGEN**2):
        numFila = contador // 360
        numColumna = contador % 360
        # Si el contador se ubica en una posicion de valor conocido entnoces ahi se copia el valor
        if (numFila % 4 == 0):
            if (numColumna % 4 == 0):
                # el valor a copiar se calcula con respecto a la direccion inicial
                ref = dir_inicial + contador // 4
                lista_zoom[contador] = lista[ref]

        contador += 1
    
    # Luego se añaden a la memoria los elementos de la imagen que completan las columnas
    # de la nueva imagen, sin estos valores no se pueden calcular el resto
    contador = 0
    while (contador < 360**2 - 3*360):
        numFila = contador // 360
        numColumna = contador % 360
        # Si el contador se ubica en una columna principal pero no en una fila principal
        if (numFila % 4 != 0):
            if(numColumna % 4 == 0):
                # ref1 y ref2 son las posiciones de los valores que se necesitan para calcular
                #   los valores de las columnas restantes.
                ref1 = contador - (numFila % 4 * 360)
                ref2 = ref1 + 360 * 4

                sum1 = ((ref2 - contador) / (ref2 - ref1)) * lista_zoom[ref1]
                sum2 = ((contador - ref1) / (ref2 - ref1)) * lista_zoom[ref2]
                lista_zoom[contador] = int(sum1 + sum2)

        contador += 1

    # Por ultimo, se añade el resto de los valores en la lista de resultado, se deben completar
    #   los valores de cada fila
    contador = 0
    while (contador < 129600 - 3*360 - 4):
        numFila = contador // 360
        numColumna = contador % 360

        if(numColumna % 4 != 0):
            # ref1 y ref2 son las posiciones de los valores que se necesitan para calcular
            #   los valores de las filas restantes.
            ref1 = contador - (numColumna % 4)
            ref2 = ref1 + 4

            sum1 = ((ref2 - contador) / (ref2 - ref1)) * lista_zoom[ref1]
            sum2 = ((contador - ref1) / (ref2 - ref1)) * lista_zoom[ref2]
            lista_zoom[contador] = int(sum1 + sum2)

        contador += 1
    
    
    return lista_zoom

def guardar_archivo(nombre_archivo, lista):
    """
    Esta funcion guarda la lista que se tiene hasta el momento en un archivo de forma ordenada.
    El objetivo es poder comprobar que se está guardando lo que se desea guardar.
    """
    f = open(nombre_archivo, 'w')

    # Los valores obtenidos se acomodan en filas y columnas de 360 valores
    result = ""
    cont = 0
    for item in lista:
        result += str(lista[cont]) + " "
        if ((cont + 1) % 360 == 0):
            result += "\n"
        
        cont += 1

    f.write(result)
    f.close()

# PROGRAMA

# guardar en memoria la lista de escala de grises
lista_grises = escala_grises(NOMBRE_IMAGEN)
guardar_archivo("text-files/matriz-gris.txt", lista_grises)

# crear la nueva imagen con el zoom en la posicion deseada
lista_zoom = zoom_imagen(lista_grises, 8)
guardar_archivo("text-files/matriz-zoom.txt", lista_zoom)

# guardar el resultado de la imagen
guardar_imagen("images/test-image-grises.bmp", lista_zoom)