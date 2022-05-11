"""
Script que corresponde al encargado de leer el txt
generado en la simulación de Quartus y convertilo en
una imagen
"""

# función que puede leer el archivo linea por linea
import numpy as np
import imageio

def leer_mem_data_output(ruta):
    """
    Esta función permite leer el archivo .txt para conseguir los
    datos guardados por el procesador al correr la simulación. Estos
    datos se guardarán en una lista que contiene la imagen con el
    zoom aplicado
    """
    f = open(ruta, "r")

    add_flag = False
    result_list = []
    for line in f:
        if (line[0] != '/'):
            if(line[0] != 'x'):
                result_list.append(int(line, 16))
            else:
                result_list.append(0)

    return result_list


def guardar_imagen(ruta, lista):
    """
    Esta funcion guarda la imagen especificada en una lista como escala de grises
    en la ruta espcificada.
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



# MAIN
# se deben cargar los resultados en una lista para su analisis
result_list = leer_mem_data_output("imageOutput.txt")

# se guarda la imagen ya procesada
guardar_imagen("images/test-image-grises.bmp", result_list)
