import digitalio
import board

#Pines de los botones
PIN_BOTONCORONA = board.GP5
PIN_TECLA1 = board.GP20
PIN_TECLA2 = board.GP21
PIN_TECLA3 = board.GP22

#Boton de la corona.
botonCorona = digitalio.DigitalInOut(PIN_BOTONCORONA)
botonCorona.direction = digitalio.Direction.INPUT
botonCorona.pull = digitalio.Pull.DOWN

#Teclado para ingresar contraseña.
botonTeclado1 = digitalio.DigitalInOut(PIN_TECLA1)
botonTeclado1.direction = digitalio.Direction.INPUT
botonTeclado1.pull = digitalio.Pull.DOWN

botonTeclado2 = digitalio.DigitalInOut(PIN_TECLA2)
botonTeclado2.direction = digitalio.Direction.INPUT
botonTeclado2.pull = digitalio.Pull.DOWN

botonTeclado3 = digitalio.DigitalInOut(PIN_TECLA3)
botonTeclado3.direction = digitalio.Direction.INPUT
botonTeclado3.pull = digitalio.Pull.DOWN