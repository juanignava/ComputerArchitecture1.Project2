"""
Script que corresponde al encargado de leer el txt
generado en la simulación de Quartus y convertilo en
una imagen
"""

# función que puede leer el archivo linea por linea
import numpy as np
import imageio

def leer_mif(ruta):
    """
    Esta función permite leer el archivo .mif para conseguir los
    datos guardados por el procesador al correr la simulación. Estos
    datos se guardarán en una lista que contiene la imagen con el
    zoom aplicado
    """
    f = open(ruta, "r")

    add_flag = False
    result_list = []
    for line in f:
        if (line[0:6] == "\t33135"):
            add_flag = True
        if add_flag:
            pixel = line[9:-2]
            result_list.append(int(pixel))
        if (line[0:6] == "\t65534"):
            add_flag = False
    
    return result_list

def completar_cero(bin):
    """
    Esta función completa el binario a un string de 32 elementos
    completando con ceros
    """
    i = 0
    result = ""
    while (i < 32):
        if (i < len(bin)):
            result = result + bin[i]

        else:
            result = '0' + result
        
        i += 1

    return result

def separar_bits(lista_dec):
    """
    Esta función convierte la lista decimal a una lista más grande con
    los 4 valores de 8 bits separados en otra lista para su posterior
    análisis en imágenes.
    """

    # la lista será 4 veces más grande
    i = 0
    result_list = []
    while (i < len(lista_dec)):
        j = 0
        elem = lista_dec[i]
        elem = str(format(elem, "b"))
        elem = completar_cero(elem)
        for j in range(4):
            if (j == 0):
                elem_bin = elem[-8*(j+1):]
            else:
                elem_bin = elem[-8*(j+1):-8*j]
            elem_dec = int(elem_bin, 2)
            result_list.append(elem_dec)
        i += 1
    
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



# función que separa los valores contenidos en un número
# de 32 bits en 4 valores de números de 8 bits que componen
# la escala de grises



# con la lista de la escala de grises generar la nueva imagen
# con el zoom respectivo.

result_list = leer_mif("mem_data.mif")


result_sep_list = separar_bits(result_list)

guardar_imagen("images/test-image-grises.bmp", result_sep_list)