"""
==================== Modificaciones Futuras ====================
- Agregar opcion de elegir si click derecho o izquierdo
- Agregar opcion de generar ventanas nuevas y ocultar la original
- 
================================================================
"""

import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x350")
app.title("Grabador de Click Izquierdos")
app.resizable(width=0,height=0)

def button_function():
    # print("button pressed")
    print("combobox dropdown clicked:", radio_var.get())

label = ctk.CTkLabel(master=app, text="Seleccione una opcion")
label.pack(padx=10, pady=10)  # Alinea a la izquierda con un pequeño espacio

radio_var = tk.IntVar(value=0)
radiobutton_1 = ctk.CTkRadioButton(app, text="Grabar y Reproducir Acciones",
                                            #  command=radiobutton_event, 
                                             variable= radio_var, value=1,
                                             border_width_unchecked = 2,width=200)
radiobutton_2 = ctk.CTkRadioButton(app, text="Grabar Unicamente Acciones",
                                            #  command=radiobutton_event, 
                                             variable= radio_var, value=2,
                                             border_width_unchecked = 2,width=200)
radiobutton_3 = ctk.CTkRadioButton(app, text="Reproducir Unicamente Acciones",
                                            #  command=radiobutton_event, 
                                             variable= radio_var, value=3,
                                             border_width_unchecked = 2,width=200)
radiobutton_1.pack(padx=20, pady=5)
radiobutton_2.pack(padx=20, pady=5)
radiobutton_3.pack(padx=20, pady=5)


# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, text="Ejecutar", command=button_function)
button.pack(padx=10, pady=10)  # Alinea a la izquierda con un pequeño espacio


app.mainloop()
