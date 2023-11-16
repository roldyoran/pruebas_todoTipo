import keyboard
from pynput import mouse
import time
import random

acciones = []
listener = None  # Hacer listener una variable global

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        tiempo_actual = time.time()
        acciones.append((x, y, tiempo_actual))
        print(f"Guardando acción: ({x}, {y})")
    elif pressed and button == mouse.Button.right:
        print("Click Izquierdo reconocido correctamente")
        print("Presione la tecla X para detener la grabacion de movimientos")
        # Detener la grabación al hacer clic derecho
        listener.stop()

def grabar_acciones():
    global listener  # Hacer listener global
    listener = mouse.Listener(on_click=on_click)
    with listener as l:
        print("Haz clic izquierdo en cualquier lugar para detener la grabación.")
        l.join()

def reproducir_acciones(acciones):
    print("Reproduciendo acciones...")

    # para el primer click 
    x, y, tiempo_grabacion = acciones[0]
    tiempo_transcurrido = time.time() - tiempo_grabacion

    
    random_time = random.uniform(2, 6)
    # Espera el tiempo transcurrido desde la grabación
    time.sleep(random_time)

    # Mueve el mouse a la posición grabada y realiza clic izquierdo
    with mouse.Controller() as controller:
        controller.position = (x, y)
        controller.click(mouse.Button.left)

    # Imprime la acción al momento de reproducirla
    print(f"Reproduciendo acción: ({x}, {y})")
    
    contador = 0

    # Iterar sobre la lista usando un índice
    for i in range(1, len(acciones)):
        x1, y1, tiempo_grabacion1 = acciones[i]
        x2, y2, tiempo_grabacion2 = acciones[i - 1]
        tiempo_transcurrido = tiempo_grabacion1 - tiempo_grabacion2

        # valor_actual = acciones[i]
        # valor_anterior = acciones[i - 1]

        time.sleep(tiempo_transcurrido)

        with mouse.Controller() as controller:
            controller.position = (x1, y1)
            controller.click(mouse.Button.left)

        # Imprime la acción al momento de reproducirla
        print(f"Reproduciendo acción: ({x1}, {y1})")
    
        # # Hacer algo con los valores actuales y anteriores
        # print(f"Valor actual: {valor_actual}, Valor anterior: {valor_anterior}")
        # FIN

    # ORIGINALES NO BORRAR

    # for accion in acciones:
    #     x, y, tiempo_grabacion = accion
    #     tiempo_transcurrido = time.time() - tiempo_grabacion

        
    #     random_time = random.uniform(2, 6)
    #     # Espera el tiempo transcurrido desde la grabación
    #     time.sleep(random_time)

    #     # Mueve el mouse a la posición grabada y realiza clic izquierdo
    #     with mouse.Controller() as controller:
    #         controller.position = (x, y)
    #         controller.click(mouse.Button.left)

    #     # Imprime la acción al momento de reproducirla
    #     print(f"Reproduciendo acción: ({x}, {y})")

if __name__ == "__main__":
    grabar_acciones()

    # Espera hasta que se presione la tecla 'X' para detener la grabación
    keyboard.wait("X")

    print("Grabación detenida.")
    reproducir_acciones(acciones)
