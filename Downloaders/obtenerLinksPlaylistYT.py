from pytube import Playlist
import ssl; ssl._create_default_https_context = ssl._create_unverified_context #Certificado no apto para produccion profesional
import re
import pickle
from pytube import YouTube
import time

def obtener_enlaces_de_los_videos_en_playlist(url):
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    enlaces = []
    for video_url in playlist.video_urls:
        enlaces.append(video_url)

    return enlaces

def guardar_lista_de_urls(enlaces, nombre_archivo='Downloaders/Musica_Chusito/enlaces.pkl'):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(enlaces, archivo)
    print(f"Enlaces guardadas exitosamente en {nombre_archivo}")
    print("")
    print("")

def descargar_audio(enlace):
    try:
        # Crear un objeto YouTube con la URL proporcionada
        yt = YouTube(url=enlace)
        
        # Obtener la corriente de audio solamente
        video = yt.streams.get_audio_only()

        # Descargar el video
        video.download(output_path=r"Downloaders/Musica_Chusito")
        
        print(f"Video Descargado: {yt.title}")
        
    except Exception as e:
        # Capturar y mostrar cualquier error que ocurra durante la descarga
        print(f"Some Error!: {e}")
    print("")

# url_playlist = r"https://www.youtube.com/playlist?list=PL6Go6XFhidEAac3TgkP8EfLF1bA1odl4e"
url_playlist = input("Ingrese la url de la playlist:  ")
enlaces = obtener_enlaces_de_los_videos_en_playlist(url_playlist)

cont = 1
for enlace in enlaces:
    print(f"{cont} - {enlace}")
    # descargar_audio(enlace)
    time.sleep(2)
    cont += 1
    # if cont == 4:
    #     break


# guardar_lista_de_urls(enlaces)





