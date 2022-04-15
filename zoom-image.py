# imports

from weakref import ref
import numpy as np
import imageio
from psutil import ZombieProcess

# variables globales
NOMBRE_IMAGEN = "test-image.bmp"

# funcion para leer la imagen
def leer_imagen(ruta):
    return np.array(imageio.imread(ruta), dtype='int').tolist()

# funcion para guardar la imagen
def guardar_imagen(ruta, lista):
    matriz = []
    for y in range(389):
        tempList = []
        for x in range(392):
            elem = y*392 + x
            tempList.append(lista[elem])
        matriz.append(tempList)

    return imageio.imwrite(ruta, np.array(matriz, dtype="uint8"))

def escala_grises(nombre_imagen):
    matriz = leer_imagen(nombre_imagen)
    ancho = 392
    alto = 392
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
    """
    dir_inicial = seccion * 98
    lista_zoom = [0] * (153664 - 3 * 392)

    # Para añadir elementos que ya se conocen de
    contador = 0 
    while (contador < 153664):
        elem = 0
        numFila = contador // 392
        numColumna = contador % 392
        if (numFila % 4 == 0):
            if(numColumna % 4 == 0):
                ref = dir_inicial + contador // 4
                lista_zoom[contador] = lista[ref]

        contador += 1

    # Para completar elementos en las columnas
    
    contador = 0
    while (contador < 153664 - 3*392):
        numFila = contador // 392
        numColumna = contador % 392
        if (numFila % 4 != 0):
            if(numColumna % 4 == 0):
                #ref1 = dir_inicial + (numFila // 4) * 392 + (numColumna // 4)
                #ref2 = dir_inicial + ((numFila // 4) + 4) * 392 + (numColumna // 4)
                ref1 = contador - (numFila % 4 * 392)
                ref2 = ref1 + 392 * 4

                """
                print("Informacion para contador: ", contador)
                print("ref1: ", ref1)
                print("ref2: ", ref2)
                print("\n")
                """
                sum1 = ((ref2 - contador) / (ref2 - ref1)) * lista_zoom[ref1]
                sum2 = ((contador - ref1) / (ref2 - ref1)) * lista_zoom[ref2]
                lista_zoom[contador] = int(sum1 + sum2)

        contador += 1

    # Para completar el resto de elementos
    
    contador = 0
    while (contador < 153664 - 3*392 - 4):
        numFila = contador // 392
        numColumna = contador % 392

        if(numColumna % 4 != 0):
            #ref1 = dir_inicial + (numFila // 4) * 392 + (numColumna // 4)
            #ref2 = dir_inicial + ((numFila // 4) + 4) * 392 + (numColumna // 4)
            ref1 = contador - (numColumna % 4)
            ref2 = ref1 + 4

            """
            print("Informacion para contador: ", contador)
            print("ref1: ", ref1)
            print("ref2: ", ref2)
            print("\n")
            """
            sum1 = ((ref2 - contador) / (ref2 - ref1)) * lista_zoom[ref1]
            sum2 = ((contador - ref1) / (ref2 - ref1)) * lista_zoom[ref2]
            lista_zoom[contador] = int(sum1 + sum2)

        contador += 1
        
    
    #print(lista_zoom)

    return lista_zoom


lista_grises = escala_grises(NOMBRE_IMAGEN)
lista_zoom = zoom_imagen(lista_grises, 9)
guardar_imagen("test-image-grises.bmp", lista_grises)