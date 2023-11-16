import os
import shutil

def organizar_archivos(carpeta):
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1]
            carpeta_destino = os.path.join(carpeta, extension[1:].lower())
            
            # Crear la carpeta de destino si no existe
            if not os.path.exists(carpeta_destino):
                os.makedirs(carpeta_destino)
            
            # Mover el archivo a la carpeta de destino
            shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
            
            # Imprimimos el nombre del archivo y hacia que carpeta fue movido
            # print(f"Archivo {archivo} movido a {carpeta_destino}") 
    
    print("Organización de archivos completada.")

# Ejemplo de uso
carpeta_entrada = input("Ingresa la Ruta de la carpeta a ordenar: ") # Variable para obtener la ruta de la carpeta a ordenar
organizar_archivos(carpeta_entrada)
