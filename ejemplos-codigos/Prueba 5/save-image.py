"""
Script que toma la imagen a analizar y que le calcula
la escala de grises a cada pixel y luego altera el
archivo .mif de la memoria para añadirle la imagen
a analizar
"""
from msilib.schema import File
import numpy as np
import imageio
from sympy import true


### CONTANTS
ZOOM_SECTION = 0

# función de cambio de la imagen a escala de grises
def leer_imagen(ruta):
    """
    Esta funcion guarda la imagen especificada en la ruta en una lista
    que contiene el RGB de cada pixel.
    """
    return np.array(imageio.imread(ruta), dtype='int').tolist()

def escala_grises(nombre_imagen):
    """
    Esta funcion convierte la imagen especificada de RGB a una
    lista en escala de grises. En esta lista retornada cada elemento
    corresponde a la escala de gris de un pixel.
    """
    matriz = leer_imagen(nombre_imagen)
    ancho = 360
    alto = 360
    lista_grises = []

    for y in range(alto):
        for x in range(ancho):
            pixel = matriz[y][x]
            promedio = (pixel[0] + pixel[1] + pixel[2]) // 3
            numStr = str(hex(promedio))
            lista_grises.append(numStr[2:])

    return lista_grises

# función tomar 4 valores de escala de grises y convetirlos
# en un número de 32 bits con los valores fusionados

def completar_cero(bin_str):
    """
    Esta función completa un número en binario con ceros
    para que su tamaño sea de 8 bits
    """
    i = 0
    result = ""
    while (i < 8):
        if (i < len(bin_str)):
            result = result + bin_str[i]
        else:
            result = '0' + result
        i += 1

    return result


# función para alterar el archivo txt que corresponde
# a la memoria de instrucciones
def completar_ins_mem(ruta, lista_instr):
    """
    Esta función permite generar el archivo txt que sera usado
    por la memoria de instrucciones
    ruta -> nombre el archivo .txt a alterar
    lista_instr -> lista con las instrucciones
    """
    f = open(ruta, "w")

    cont = 0

    for ins in lista_instr:
        f.write(str(ins) +  "\n")
        cont += 1

    f.close()


def completar_data_mem(ruta, lista_datos):
    """
    Esta función permite generar el archivo txt que sera usado
    por la memoria de datos relacionada a la imagen de entrada

    ruta -> nombre del archivo .txt a alterar
    lista_datos -> lista con los datos de la imagen de entrada
    """
    f = open(ruta, "w")

    cont = 0
    begin_limit = ZOOM_SECTION * 8100
    end_limit = begin_limit + 8100

    while (cont < begin_limit):
        cont += 1

    while (cont < end_limit):
        f.write(str(lista_datos[cont]) +  "\n")
        cont += 1

    f.close()



def lectura_instr(ruta):
    """
    Esta función genera una lista con las instrucciones en decimal
    del codigo ensamblador.
    input:
    ruta -> ruta en la que se encuentra el archivo generado por el
    compilador.
    output:
    lista_bin -> lista con las instrucciones en decimal
    """
    f = open(ruta, "r")
    lista_ins = []
    for line in f:
        numStr = str(hex(int(line, 2)))
        lista_ins.append(numStr[2:])

    return lista_ins



# MAIN
# especificar la ruta de la imagena a analizar
lista_datos = escala_grises("images/test-image.bmp")

# especificar la ruta del txt con el binario de las instrucciones
lista_inst = lectura_instr("binaryCode.txt")

# crear el archivo que lee la memoria de instrucciones
completar_ins_mem("instructions.txt", lista_inst)

# crear el archivo que lee la memoria de datos para la imagen de entrada
completar_data_mem("imageData.txt", lista_datos)
