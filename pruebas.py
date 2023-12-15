import tkinter as tk
from tkinter import filedialog

def abrir_seleccionador_archivos():
    # Abre el cuadro de diálogo de selección de archivos
    archivo_seleccionado = filedialog.askopenfilename(title="Seleccionar archivo")

    # Imprime la ruta del archivo seleccionado (puedes hacer lo que quieras con la ruta)
    print("Archivo seleccionado:", archivo_seleccionado)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Seleccionador de Archivos")

# Crear un botón para abrir el cuadro de diálogo de selección de archivos
boton_seleccionar_archivo = tk.Button(ventana, text="Seleccionar Archivo", command=abrir_seleccionador_archivos)
boton_seleccionar_archivo.pack(pady=20)

# Iniciar el bucle de eventos
ventana.mainloop()
