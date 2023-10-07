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

    with ThreadPoolExecutor(max_workers=4) as executor:
        img_filtrada_suavizado = executor.submit(aplicar_filtro, img, kernel_suavizado).result()
        img_filtrada_bordes = executor.submit(aplicar_filtro, img, kernel_bordes).result()

    cv2.imwrite("imagen_suavizada_tareas.jpg", img_filtrada_suavizado)
    cv2.imwrite("imagen_con_bordes_tareas.jpg", img_filtrada_bordes)

if __name__ == "__main__":
    main()
