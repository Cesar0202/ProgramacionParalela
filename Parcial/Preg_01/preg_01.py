import cv2
import numpy as np
import threading
import requests
from io import BytesIO

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
        hilo_suavizado = threading.Thread(target=aplicar_filtro, args=(partes[i], kernel_suavizado, resultados_suavizado, i))
        hilo_bordes = threading.Thread(target=aplicar_filtro, args=(partes[i], kernel_bordes, resultados_bordes, i))
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

if __name__ == "__main__":
    main()