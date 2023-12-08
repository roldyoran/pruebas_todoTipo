import keyboard

# Tecla que queremos verificar
tecla_objetivo = 'a'

# Comprobar si la tecla está siendo presionada
if keyboard.is_pressed(tecla_objetivo):
    print(f"La tecla {tecla_objetivo} está siendo presionada.")
else:
    print(f"La tecla {tecla_objetivo} no está siendo presionada.")
