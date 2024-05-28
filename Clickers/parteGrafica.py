"""
==================== Modificaciones Futuras ====================
- Agregar opcion de elegir si click derecho o izquierdo
- Agregar opcion de generar ventanas nuevas y ocultar la original
- 
================================================================
"""

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from tkinter import filedialog


ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Window screen
app = ctk.CTk(fg_color="#161616")  # create CTk window like you do with the Tk window
app.title("Grabador de Clicks")
app_width = 700
app_height = 400
display_width = app.winfo_screenwidth()
display_height = app.winfo_screenheight()

left_display = int(display_width / 2 - app_width / 2)
top_display = int(display_height / 2 - app_height / 2)

app.geometry(f"{app_width}x{app_height}+{left_display}+{top_display}")

app.minsize(600, 350)
app.maxsize(800, 500)
# app.resizable(False, False)
app.attributes("-topmost", True)

# Colos
PRIMARY = "#e84393"
SECONDARY = "#fd79a8"


# Functions
# def obtenerContenidoTextBox():
#     print(textbox.get("1.0", "end-1c"))

def play():
    pass

def selectFile():
    # Abre el cuadro de diálogo de selección de archivos
    # archivo_seleccionado = filedialog.askopenfilename(title="Seleccionar archivo")
    
    # Imprime la ruta del archivo seleccionado (puedes hacer lo que quieras con la ruta)
    # print("Archivo seleccionado:", archivo_seleccionado)
    textbox34.configure(state="normal")
    textbox34.insert(tk.END, str("archivo_seleccionado") + '\n')
    textbox34.configure(state="disabled")

# IMAGES
# my_image = ctk.CTkImage(light_image=Image.open("Clickers/MANDALAS-4-Puntas.ppm"),
#                                   dark_image=Image.open("Clickers/MANDALAS-4-Puntas.ppm"),
#                                   size=(40, 40))


# Frames
frame1 = ctk.CTkFrame(app, fg_color="#282828") # transparent
frame2 = ctk.CTkFrame(app, fg_color="#282828")
frame3 = ctk.CTkFrame(app, fg_color="#282828")

frame32 = ctk.CTkFrame(frame3, fg_color="#161616")



radio_var = tk.IntVar(value=0)
radiobutton_1 = ctk.CTkRadioButton(frame32, 
                                   text="Click Derecho ", 
                                   variable=radio_var, 
                                   value=1, 
                                   radiobutton_height=20, 
                                   radiobutton_width=20,
                                   fg_color=PRIMARY,
                                   border_width_unchecked=10,
                                   border_width_checked=10)
radiobutton_2 = ctk.CTkRadioButton(frame32, 
                                   text="Click Izquierdo", 
                                   variable=radio_var, 
                                   value=2, 
                                   radiobutton_height=20, 
                                   radiobutton_width=20,
                                   fg_color=PRIMARY,
                                   border_width_unchecked=10,
                                   border_width_checked=10)

# Labels
image_label = ctk.CTkLabel(frame1, image=None, text="")  # display image with a CTkLabel
label11 = ctk.CTkLabel(frame1, text="11", fg_color="purple")
label12 = ctk.CTkLabel(frame1, text="12", fg_color="green")

label21 = ctk.CTkLabel(frame2, text="21", fg_color="blue")
label22 = ctk.CTkLabel(frame2, text="22", fg_color="orange")
label23 = ctk.CTkLabel(frame2, text="23", fg_color="blue")

label31 = ctk.CTkLabel(frame3, text="31", fg_color="#161616")
# label32 = ctk.CTkLabel(frame3, text="32", fg_color="yellow")
# label33 = ctk.CTkLabel(frame3, text="33", fg_color="red")
# label34 = ctk.CTkLabel(frame3, text="34", fg_color="white")

button33 = ctk.CTkButton(frame3, 
                         text="PLAY", 
                         fg_color=PRIMARY, 
                         width=160, 
                         hover_color=SECONDARY, 
                         command=selectFile, 
                         corner_radius=32)
textbox34 = ctk.CTkTextbox(frame3, state="disabled")

# App grid
app.columnconfigure(0, weight=2)  # uniform = 'a'
app.columnconfigure((1,2,3), weight=3)
app.rowconfigure(0, weight=1)
app.rowconfigure((1,2,3), weight=2)

# FRAMES GRID
# frame1
frame1.columnconfigure(0,  weight=1)
frame1.columnconfigure((1,2), weight=3)
frame1.rowconfigure(0, weight=1)

# frame3
frame3.columnconfigure((0,1), weight=1, uniform='a')
frame3.rowconfigure((0), weight=1)
frame3.rowconfigure((1), weight=2)
frame3.rowconfigure((3), weight=4)

# LAYOUT
# Frames
frame1.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
frame2.grid(row=1, column=0, rowspan=3, sticky="nsew", padx=10, pady=10)
frame3.grid(row=1, column=1, columnspan=3, rowspan=3, sticky="nsew", padx=10, pady=10)

# content frame1
image_label.grid(row=0, column=0)
label12.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)

# content frame2
label21.pack(expand=True,  fill="both", padx=5, pady=5)
label22.pack(expand=True,  fill="both", padx=5, pady=5)
label23.pack(expand=True,  fill="both", padx=5, pady=5)

# content frame3
label31.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
frame32.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
button33.grid(row=1, column=1)
textbox34.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

radiobutton_1.pack(expand=True, pady=2)
radiobutton_2.pack(expand=True, pady=2)

# layout
# label1.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
# label2.grid(row=1, column=0, rowspan=3, sticky="nsew", padx=5, pady=5)
# label3.grid(row=1, column=1, columnspan=3, rowspan=3, sticky="nsew", padx=5, pady=5)

# label1.pack(expand = True, fill="both", side="top")
# label2.pack(expand = True, fill="both", side="left")
# label3.pack(expand = True, fill="both", side="left")

app.mainloop()
