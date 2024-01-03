import requests

def descargar_video(url, nombre_archivo):
    # Realizar la solicitud HTTP para descargar el video
    respuesta = requests.get(url, stream=True)

    # Verificar si la solicitud fue exitosa
    if respuesta.status_code == 200:
        # Abrir un archivo para guardar el contenido del video
        with open(nombre_archivo, 'wb') as archivo:
            for chunk in respuesta.iter_content(chunk_size=1024 * 1024):
                if chunk:  # filtrar los keep-alive chunks
                    archivo.write(chunk)
        print(f"Video descargado: {nombre_archivo}")
    else:
        print("Error al descargar el video")

# URL del stream de video
url_stream = "URL_DEL_ARCHIVO"

# Nombre del archivo donde se guardará el video
nombre_archivo = "video_descargado.mp4"

descargar_video(url_stream, nombre_archivo)
