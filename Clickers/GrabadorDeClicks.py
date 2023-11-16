import keyboard
from pynput import mouse
import time
import pickle  # Agregamos la importación del módulo pickle

acciones = []

listener = None  # Hacer listener una variable global

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        tiempo_actual = time.time()
        acciones.append((x, y, tiempo_actual))
        print(f"Guardando acción: ({x}, {y})")
    elif pressed and button == mouse.Button.right:
        print("")
        print("Click Izquierdo reconocido correctamente")
        print("Presione la tecla X para detener la grabacion de movimientos\n")
        # Detener la grabación al hacer clic derecho
        listener.stop()

def grabar_acciones():
    global listener  # Hacer listener global
    listener = mouse.Listener(on_click=on_click)
    with listener as l:
        print("Haz clic derecho para guardar una acción.")
        l.join()

def guardar_acciones(acciones, nombre_archivo='Clickers/acciones.pkl'):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(acciones, archivo)
    print(f"Acciones guardadas exitosamente en {nombre_archivo}")
    print("")
    print("")

def cargar_acciones(nombre_archivo='Clickers/acciones.pkl'):
    try:
        with open(nombre_archivo, 'rb') as archivo:
            acciones_cargadas = pickle.load(archivo)
            return acciones_cargadas
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return []
    

def reproducir_acciones(acciones):
    print("Reproduciendo acciones...")


    # para el primer click
    x, y, tiempo_grabacion = acciones[0]
    tiempo_transcurrido = time.time() - tiempo_grabacion

    # Espera el tiempo transcurrido desde la grabación
    time.sleep(4)

    # Mueve el mouse a la posición grabada y realiza clic izquierdo
    with mouse.Controller() as controller:
        controller.position = (x, y)
        controller.click(mouse.Button.left)

    # Imprime la acción al momento de reproducirla
    print(f"Reproduciendo acción: ({x}, {y})")

    # Iterar sobre la lista usando un índice
    for i in range(1, len(acciones)):
        x1, y1, tiempo_grabacion1 = acciones[i]
        x2, y2, tiempo_grabacion2 = acciones[i - 1]
        tiempo_transcurrido = tiempo_grabacion1 - tiempo_grabacion2

        time.sleep(tiempo_transcurrido)

        with mouse.Controller() as controller:
            controller.position = (x1, y1)
            controller.click(mouse.Button.left)

        # Imprime la acción al momento de reproducirla
        print(f"Reproduciendo acción: ({x1}, {y1})")

if __name__ == "__main__":
    grabar_acciones()

    # Espera hasta que se presione la tecla 'X' para detener la grabación
    keyboard.wait("X")
    print("Grabación detenida.\n")

    time.sleep(3)

    # Guarda las acciones en un archivo
    guardar_acciones(acciones)

    # Carga las acciones desde el archivo
    acciones_cargadas = cargar_acciones()

    time.sleep(3) 

    if not acciones_cargadas:
        print("El error de lista vacia, ver su archivo acciones.pkl")
    else:
        # Reproduce las acciones cargadas
        reproducir_acciones(acciones_cargadas)
    