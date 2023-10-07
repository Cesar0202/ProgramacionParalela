# Imports
import cv2
import numpy as np
import threading
import requests
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from timeit import default_timer

# Codigo para la pregunta 1


def aplicar_filtro(img, kernel, resultado, indice):
    img_filtrada = cv2.filter2D(img, -1, kernel)
    resultado[indice] = img_filtrada


def guardar_imagen(nombre_archivo, img):
    cv2.imwrite(nombre_archivo, img)


def cargar_imagen(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_img = BytesIO(respuesta.content)
        img = cv2.imdecode(np.frombuffer(datos_img.read(), np.uint8), -1)
        return img


def main1():
    url = "https://4.bp.blogspot.com/--2T-iuayG6g/VpWPGoNO8jI/AAAAAAAABWM/hEZmGxlAXYo/s640/unmsm.jpg"
    img = cargar_imagen(url)

    if img is None:
        return

    # Filtro de suavizado
    kernel_suavizado = np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]]) / 9.0

    # Filtro de detección de bordes
    kernel_bordes = np.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])

    num_hilos = 4
    alto, ancho, _ = img.shape
    alto_parte = alto // num_hilos
    partes = []
    resultados_suavizado = [None] * num_hilos
    resultados_bordes = [None] * num_hilos

    for i in range(num_hilos):
        fila_inicio = i * alto_parte
        fila_fin = (i + 1) * alto_parte if i < num_hilos - 1 else alto
        parte = img[fila_inicio:fila_fin, :, :]
        partes.append(parte)

    hilos_suavizado = []
    hilos_bordes = []

    for i in range(num_hilos):
        hilo_suavizado = threading.Thread(target=aplicar_filtro, args=(
            partes[i], kernel_suavizado, resultados_suavizado, i))
        hilo_bordes = threading.Thread(target=aplicar_filtro, args=(
            partes[i], kernel_bordes, resultados_bordes, i))
        hilos_suavizado.append(hilo_suavizado)
        hilos_bordes.append(hilo_bordes)

    for hilo in hilos_suavizado:
        hilo.start()

    for hilo in hilos_suavizado:
        hilo.join()

    for hilo in hilos_bordes:
        hilo.start()

    for hilo in hilos_bordes:
        hilo.join()

    img_filtrada_suavizado = np.vstack(resultados_suavizado)
    img_filtrada_bordes = np.vstack(resultados_bordes)

    # Guardar las imágenes filtradas como archivos JPEG
    guardar_imagen("imagen_suavizada.jpg", img_filtrada_suavizado)
    guardar_imagen("imagen_con_bordes.jpg", img_filtrada_bordes)

# Codigo para la pregunta 2


def aplicar_filtro(img, kernel, resultado, indice):
    img_filtrada = cv2.filter2D(img, -1, kernel)
    resultado[indice] = img_filtrada


def guardar_imagen(nombre_archivo, img):
    cv2.imwrite(nombre_archivo, img)


def cargar_imagen(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_img = BytesIO(respuesta.content)
        img = cv2.imdecode(np.frombuffer(datos_img.read(), np.uint8), -1)
        return img


def main2():
    url = "https://4.bp.blogspot.com/--2T-iuayG6g/VpWPGoNO8jI/AAAAAAAABWM/hEZmGxlAXYo/s640/unmsm.jpg"
    img = cargar_imagen(url)

    if img is None:
        return

    # Filtro de suavizado
    kernel_suavizado = np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]]) / 9.0

    # Filtro de detección de bordes
    kernel_bordes = np.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])

    num_hilos = 4
    alto, ancho, _ = img.shape
    alto_parte = alto // num_hilos
    partes = []
    resultados_suavizado = [None] * num_hilos
    resultados_bordes = [None] * num_hilos

    for i in range(num_hilos):
        fila_inicio = i * alto_parte
        fila_fin = (i + 1) * alto_parte if i < num_hilos - 1 else alto
        parte = img[fila_inicio:fila_fin, :, :]
        partes.append(parte)

    hilos_suavizado = []
    hilos_bordes = []

    for i in range(num_hilos):
        hilo_suavizado = threading.Thread(target=aplicar_filtro, args=(
            partes[i], kernel_suavizado, resultados_suavizado, i))
        hilo_bordes = threading.Thread(target=aplicar_filtro, args=(
            partes[i], kernel_bordes, resultados_bordes, i))
        hilos_suavizado.append(hilo_suavizado)
        hilos_bordes.append(hilo_bordes)

    for hilo in hilos_suavizado:
        hilo.start()

    for hilo in hilos_suavizado:
        hilo.join()

    for hilo in hilos_bordes:
        hilo.start()

    for hilo in hilos_bordes:
        hilo.join()

    img_filtrada_suavizado = np.vstack(resultados_suavizado)
    img_filtrada_bordes = np.vstack(resultados_bordes)

    # Guardar las imágenes filtradas como archivos JPEG
    guardar_imagen("imagen_suavizada.jpg", img_filtrada_suavizado)
    guardar_imagen("imagen_con_bordes.jpg", img_filtrada_bordes)

# Codigo para la pregunta 3


def aplicar_filtro(img, kernel):
    img_filtrada = cv2.filter2D(img, -1, kernel)
    return img_filtrada


def cargar_imagen(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_img = BytesIO(respuesta.content)
        img = cv2.imdecode(np.frombuffer(datos_img.read(), np.uint8), -1)
        return img


def main3():
    url = "https://4.bp.blogspot.com/--2T-iuayG6g/VpWPGoNO8jI/AAAAAAAABWM/hEZmGxlAXYo/s640/unmsm.jpg"
    img = cargar_imagen(url)

    if img is None:
        return

    # Filtro de suavizado
    kernel_suavizado = np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]]) / 9.0

    # Filtro de detección de bordes
    kernel_bordes = np.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])

    num_hilos = 4
    alto, ancho, _ = img.shape
    alto_parte = alto // num_hilos
    partes = []

    for i in range(num_hilos):
        fila_inicio = i * alto_parte
        fila_fin = (i + 1) * alto_parte if i < num_hilos - 1 else alto
        parte = img[fila_inicio:fila_fin, :, :]
        partes.append(parte)

    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        partes_filtradas_suavizado = list(executor.map(
            lambda x: aplicar_filtro(x, kernel_suavizado), partes))
        partes_filtradas_bordes = list(executor.map(
            lambda x: aplicar_filtro(x, kernel_bordes), partes))

    img_filtrada_suavizado = np.vstack(partes_filtradas_suavizado)
    img_filtrada_bordes = np.vstack(partes_filtradas_bordes)

    cv2.imwrite("imagen_suavizada_tareas.jpg", img_filtrada_suavizado)
    cv2.imwrite("imagen_con_bordes_tareas.jpg", img_filtrada_bordes)


# Ejecución pregunta 1
inicio_A = default_timer()
main1()
fin_A = default_timer()

print("Tiempo de ejecucion pregunta 1: ")
print(fin_A - inicio_A, "segundos")

# Ejecución pregunta 2
inicio_B = default_timer()
main2()
fin_B = default_timer()

print("Tiempo de ejecucion pregunta 2: ")
print(fin_B - inicio_B, "segundos")

# Ejecución pregunta 3
inicio_C = default_timer()
main3()
fin_C = default_timer()

print("Tiempo de ejecucion pregunta 3: ")
print(fin_C - inicio_C, "segundos")
