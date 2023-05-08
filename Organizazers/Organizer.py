# Se importa las librearias a utilizar para el manejo de carpetas y archivos
import os
import shutil


path = input("Enter Path: ") # Variable para obtener la ruta de la carpeta a ordenar
files = os.listdir(path)     # Se ingresa a la carpeta

# Para cada archivo dentro de la carpeta se obtiene su extension y se crea
# o ingresa el archivo a su respectiva carpeta
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
