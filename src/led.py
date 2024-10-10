import digitalio
import board

#Ubicacion del led de la placa.
BOARD_LED = board.LED

#Configuracion del led.
led = digitalio.DigitalInOut(BOARD_LED)
led.direction = digitalio.Direction.OUTPUT

def encender():
    led.value = True

def apagar():
    led.value = False