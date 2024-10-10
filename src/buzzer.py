import digitalio
import board

#Pin del buzzer
PIN_BUZZER = board.GP2

#Configuración del buzzer
buzzer = digitalio.DigitalInOut(PIN_BUZZER)
buzzer.direction = digitalio.Direction.OUTPUT

def encender():
    buzzer.value = True

def apagar():
    buzzer.value = False