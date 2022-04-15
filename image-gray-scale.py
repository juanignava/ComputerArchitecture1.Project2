"""
    https://parzibyte.me/blog
"""
import numpy as np
import imageio
NOMBRE_IMAGEN = "test-image.bmp"


def leer_imagen(ruta):
    return np.array(imageio.imread(ruta), dtype='int').tolist()


def guardar_imagen(ruta, matriz):
    return imageio.imwrite(ruta, np.array(matriz, dtype="uint8"))


def escala_grises(nombre_imagen):
    matriz = leer_imagen(nombre_imagen)
    ancho = len(matriz[0])
    alto = len(matriz)
    for y in range(alto):
        for x in range(ancho):
            pixel = matriz[y][x]
            # El doble / es para dividir y redondear a entero
            promedio = (pixel[0] + pixel[1] + pixel[2])//3
            matriz[y][x][0] = promedio
            matriz[y][x][1] = promedio
            matriz[y][x][2] = promedio
    return matriz


guardar_imagen("travel_escala_grises.bmp", escala_grises(NOMBRE_IMAGEN))