from pynput import mouse, keyboard
import time
import pickle
import os

acciones = []
listener_mouse = None  # Hacer listener una variable global
listener_teclado = None

def on_press(key):
    global listener_mouse
    if key == keyboard.Key.esc: # keyboard.KeyCode.from_char('x') #para utilizar una tecla
        # Detener la grabación al presionar la tecla Esc
        listener_mouse.stop()
    

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.right:
        tiempo_actual = time.time()
        acciones.append((x, y, tiempo_actual))
        print(f"Guardando acción: ({x}, {y})")

def grabar_acciones():
    global listener_mouse, listener_teclado
    listener_mouse = mouse.Listener(on_click=on_click)
    listener_teclado = keyboard.Listener(on_press=on_press)

    with listener_mouse as l, listener_teclado as kl:
        textA = """
        ----------------------- INSTRUCCIONES -----------------------
        Click (derecho) para guardar una acción
        Mantenga presionada la tecla Esc para detener la grabación de acciones

        Las acciones se ejecutan automáticamente según la opción 
        ingresada
        -------------------------------------------------------------
        """
        print(textA)

        try:
            l.join()
        except KeyboardInterrupt:
            pass

# Resto del código permanece igual

def guardar_acciones(acciones, nombre_archivo='acciones.pkl'):

    # # Obtener el directorio base
    # directorio_base = os.path.dirname(nombre_archivo)

    # # Crear el directorio si no existe
    # os.makedirs(directorio_base, exist_ok=True)

    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(acciones, archivo)
    print(f"Acciones guardadas exitosamente en {nombre_archivo}")
    print("")
    print("")

def cargar_acciones(nombre_archivo='acciones.pkl'):
    
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
    time.sleep(3)

    # Mueve el mouse a la posición grabada y realiza clic derecho
    with mouse.Controller() as controller:
        controller.position = (x, y)
        controller.click(mouse.Button.right)

    # Imprime la acción al momento de reproducirla
    print("Reproduciendo acción:   x  | y")
    print(f"Reproduciendo acción: ({x}, {y})")

    # Iterar sobre la lista usando un índice
    for i in range(1, len(acciones)):
        x1, y1, tiempo_grabacion1 = acciones[i]
        x2, y2, tiempo_grabacion2 = acciones[i - 1]
        tiempo_transcurrido = tiempo_grabacion1 - tiempo_grabacion2

        time.sleep(tiempo_transcurrido)

        with mouse.Controller() as controller:
            controller.position = (x1, y1)
            controller.click(mouse.Button.right)

        # Imprime la acción al momento de reproducirla
        print(f"Reproduciendo acción: ({x1}, {y1})")

if __name__ == "__main__":

    textAB = """
1. Guardar y reproducir acciones
2. Grabar acciones
3. Reproducir acciones guardadas
4. No hacer nada y Salir
"""
    print(textAB)
    opcion = input("Ingrese su opcion: ")
    print(" ")

    if str(opcion) == "1":
        grabar_acciones()

        # Espera hasta que se presione la tecla 'Esc' para detener la grabación
        print("\n--Grabación detenida--\nEspere 3 segundos\n")
        time.sleep(3)

        # Guarda las acciones en un archivo
        guardar_acciones(acciones)

        # Carga las acciones desde el archivo
        acciones_cargadas = cargar_acciones()

        time.sleep(3)

        if not acciones_cargadas:
            print("Error: Lista vacía. Verifique el archivo acciones.pkl")
        else:
            # Reproduce las acciones cargadas
            reproducir_acciones(acciones_cargadas)

    elif str(opcion) == "2":
        grabar_acciones()

        # Espera hasta que se presione la tecla 'Esc' para detener la grabación
        print("Grabación detenida.\n")
        time.sleep(3)

        # Guarda las acciones en un archivo
        guardar_acciones(acciones)
    elif str(opcion) == "3":
        # Carga las acciones desde el archivo
        acciones_cargadas = cargar_acciones()

        time.sleep(3)

        if not acciones_cargadas:
            print("Error: Lista vacía. Verifique el archivo acciones.pkl")
        else:
            # Reproduce las acciones cargadas
            reproducir_acciones(acciones_cargadas)
    else:
        pass
