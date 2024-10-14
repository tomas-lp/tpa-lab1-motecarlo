from machine import Pin

# Pines de los botones
PIN_BOTONCORONA = 5
PIN_TECLA1 = 20
PIN_TECLA2 = 21
PIN_TECLA3 = 22

# Boton de la corona
botonCorona = Pin(PIN_BOTONCORONA, Pin.IN, Pin.PULL_DOWN)

# Teclado para ingresar contraseña
botonTeclado1 = Pin(PIN_TECLA1, Pin.IN, Pin.PULL_DOWN)
botonTeclado2 = Pin(PIN_TECLA2, Pin.IN, Pin.PULL_DOWN)
botonTeclado3 = Pin(PIN_TECLA3, Pin.IN, Pin.PULL_DOWN)