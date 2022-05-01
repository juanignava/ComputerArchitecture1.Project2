"""
Script que toma la imagen a analizar y que le calcula
la escala de grises a cada pixel y luego altera el
archivo .mif de la memoria para añadirle la imagen
a analizar
"""
import numpy as np
import imageio

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
            lista_grises.append(promedio)

    return lista_grises

# función tomar 4 valores de escala de grises y convetirlos
# en un número de 32 bits con los valores fusionados

def combinar_bits(lista):
    """
    Esta función recibe la lista de los pixeles de la
    imagen en escala de grises y combina cada 4 valores
    en un binario de 32 bits
    """
    
    # por cada 4 valores
    i = 0
    bin_list = []
    cant_elem = len(lista) - 1
    while (i < cant_elem):
        j = 0
        bin_str = ""
        for j in range(4):
            elem = lista[i]
            elem_bin = str(format(elem, "b"))
            bin_str = elem_bin + bin_str
            i += 1
        bin_list.append(int(bin_str, 2))

    return bin_list


# función para alterar el archivo .mif en las direcciones
# correspondientes de memoria

def completar_mif(ruta, lista_data, lista_instr):
    """
    Esta función permite generar el archivo .mif con los valores
    calculados previamente.
    ruta -> nombre el archivo .mif a alterar
    lista_data -> lista con la información a añadir en el archivo
    lista_instr -> lista con las instrucciones
    """
    pass


# opcional:
# este script también puede generar el .mif completo al
# añadir las líneas respectivas de las instrucciones
# para este caso se cuenta con la salida de las instrucciones
# en binario del compilador y ahora se convierten en decimal
# y por último se añaden en las primeras direcciones de memoria
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
    pass


# main
lista_grises = escala_grises("images/test-image.bmp")
print(len(lista_grises))

print(lista_grises[0], " ", lista_grises[1], " ", lista_grises[2], " ", lista_grises[3])

lista_bin = combinar_bits(lista_grises)

print(len(lista_bin))