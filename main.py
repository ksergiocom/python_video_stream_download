from datetime import datetime

import requests
from tqdm import tqdm

def descargar_video(url, nombre_archivo, cookies):
    # Configurar los encabezados para incluir las cookies
    headers = {
        'Cookie': cookies
    }

    # Realizar la solicitud HTTP para descargar el video, incluyendo las cookies
    with requests.get(url, headers=headers, stream=True) as respuesta:
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # Obtener la longitud total del archivo
            total_length = int(respuesta.headers.get('content-length'))

            # Abrir un archivo para guardar el contenido del video
            with open(nombre_archivo, 'wb') as archivo, tqdm(
                    desc=nombre_archivo,
                    total=total_length,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as barra:
                for chunk in respuesta.iter_content(chunk_size=1024):
                    tamaño = archivo.write(chunk)
                    barra.update(tamaño)
            print(f"Video descargado: {nombre_archivo}")
        else:
            print(f"Error al descargar el video: {respuesta.status_code}")

# URL del stream de video
url_stream = "URL_ARCHIVO"


# Nombre del archivo donde se guardará el video
nombre_archivo = f"video_descargado_{datetime.now()}.mp4"

# Cookie(s) requerida(s) para la solicitud
cookies = "nombre_cookie=valor_cookie; otra_cookie=otro_valor"

descargar_video(url_stream, nombre_archivo, cookies)
