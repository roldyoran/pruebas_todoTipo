"""
==================== Modificaciones Futuras ====================
- Agregar opcion de seleccionar carpeta de descarga
- Agregar opcion de descarga de audio y de video por separado
- Agregar opcion de descarga masiva por ingreso de varias urls
- Unir con el YT_Playlist downloader
================================================================
"""

import tkinter
import customtkinter
import certifi
import urllib3
from pytube import YouTube
import os
import ssl; ssl._create_default_https_context = ssl._create_unverified_context

# Configuración del certificado de confianza
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)

# Configuración de la apariencia del tema y colores predeterminados
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Función para iniciar la descarga cuando se hace clic en el botón
def startdownload():
    try:
        # Crear un objeto YouTube con la URL proporcionada
        yt = YouTube(url=link.get())
        
        # Obtener la corriente de audio solamente
        video = yt.streams.get_audio_only()

        titleLabel.configure(text=yt.title, text_color="white")
        
        # Descargar el video
        video.download()
        
        # Actualizar la etiqueta de finalización
        finishLabel.configure(text="Task Completed!", text_color="green", )
        
    except Exception as e:
        # Capturar y mostrar cualquier error que ocurra durante la descarga
        # print(f"Some Error!: {e}")
        finishLabel.configure(text=f"Error: [{e}]")

# Crear la aplicación Tkinter
app = customtkinter.CTk()
app.title("Youtube Downloader")
app.geometry("620x280")

# Crear una etiqueta para el título
title = customtkinter.CTkLabel(app, text="Insert Youtube link")
title.pack(padx=10, pady=10)

# Crear una variable de cadena para almacenar la URL
url_var = tkinter.StringVar()

# Crear un cuadro de entrada para la URL
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack(padx=10, pady=10)

# Crear un botón para iniciar la descarga
download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10, pady=20)

titleLabel = customtkinter.CTkLabel(app, text="")
titleLabel.pack(padx=10, pady=5)

# Crear una etiqueta para mostrar el estado de finalización
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(padx=10, pady=5)

# Iniciar el bucle principal de la aplicación
app.mainloop()
