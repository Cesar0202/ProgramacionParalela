import cv2
import numpy as np
import threading
import requests
from io import BytesIO

def aplicar_filtro(img, kernel):
    img_filtrada = cv2.filter2D(img, -1, kernel)
    return img_filtrada

def guardar_imagen(nombre_archivo, img):
    cv2.imwrite(nombre_archivo, img)

def cargar_imagen(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos_img = BytesIO(respuesta.content)
        img = cv2.imdecode(np.frombuffer(datos_img.read(), np.uint8), -1)
        return img

def main():
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

    num_hilos = 4  # Puedes ajustar el número de hilos según tus necesidades
    resultados_suavizado = [None] * num_hilos
    resultados_bordes = [None] * num_hilos

    hilos_suavizado = []
    hilos_bordes = []

    for i in range(num_hilos):
        hilo_suavizado = threading.Thread(target=lambda i=i: resultados_suavizado.__setitem__(i, aplicar_filtro(img, kernel_suavizado)))
        hilo_bordes = threading.Thread(target=lambda i=i: resultados_bordes.__setitem__(i, aplicar_filtro(img, kernel_bordes)))
        hilos_suavizado.append(hilo_suavizado)
        hilos_bordes.append(hilo_bordes)

    for hilo in hilos_suavizado:
        hilo.start()

    for hilo in hilos_bordes:
        hilo.start()

    for hilo in hilos_suavizado:
        hilo.join()

    for hilo in hilos_bordes:
        hilo.join()

    img_filtrada_suavizado = resultados_suavizado[0]
    img_filtrada_bordes = resultados_bordes[0]

    # Guardar las imágenes filtradas como archivos JPEG
    if img_filtrada_suavizado is not None:
        guardar_imagen("imagen_suavizada_hilos.jpg", img_filtrada_suavizado)
    if img_filtrada_bordes is not None:
        guardar_imagen("imagen_con_bordes_hilos.jpg", img_filtrada_bordes)

if __name__ == "__main__":
    main()
