import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import requests
from io import BytesIO

def aplicar_filtro(img, kernel):
    img_filtrada = cv2.filter2D(img, -1, kernel)
    return img_filtrada

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

    for i in range(num_hilos):
        fila_inicio = i * alto_parte
        fila_fin = (i + 1) * alto_parte if i < num_hilos - 1 else alto
        parte = img[fila_inicio:fila_fin, :, :]
        partes.append(parte)

    with ThreadPoolExecutor(max_workers=num_hilos) as executor:
        partes_filtradas_suavizado = list(executor.map(lambda x: aplicar_filtro(x, kernel_suavizado), partes))
        partes_filtradas_bordes = list(executor.map(lambda x: aplicar_filtro(x, kernel_bordes), partes))

    img_filtrada_suavizado = np.vstack(partes_filtradas_suavizado)
    img_filtrada_bordes = np.vstack(partes_filtradas_bordes)

    cv2.imwrite("imagen_suavizada_tareas.jpg", img_filtrada_suavizado)
    cv2.imwrite("imagen_con_bordes_tareas.jpg", img_filtrada_bordes)

if __name__ == "__main__":
    main()
