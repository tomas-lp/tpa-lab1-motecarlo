import digitalio
import board

#Pin del sensor.
PIN_RECEPTOR = board.GP3

#Configuración del sensor.
sensorObstaculo = digitalio.DigitalInOut(PIN_RECEPTOR)
sensorObstaculo.direction = digitalio.Direction.INPUT
sensorObstaculo.pull = digitalio.Pull.DOWN