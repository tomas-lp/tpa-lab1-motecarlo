import digitalio
import board
import time
from adafruit_motor import stepper

#Pines del motor.
PIN_MOTOR1 = board.GP12
PIN_MOTOR2 = board.GP13
PIN_MOTOR3 = board.GP14
PIN_MOTOR4 = board.GP15

STEPS = 500     #Cantidad de pasos en que el motor se moverá.
DELAY = 0.01    #Tiempo entre pasos.

#Definicion de cada bobina del motor.
coil1 = digitalio.DigitalInOut(PIN_MOTOR1)
coil2 = digitalio.DigitalInOut(PIN_MOTOR2)
coil3 = digitalio.DigitalInOut(PIN_MOTOR3)
coil4 = digitalio.DigitalInOut(PIN_MOTOR4)

coil1.direction = digitalio.Direction.OUTPUT
coil2.direction = digitalio.Direction.OUTPUT
coil3.direction = digitalio.Direction.OUTPUT
coil4.direction = digitalio.Direction.OUTPUT

#Definicion del motor.
motor = stepper.StepperMotor(coil1, coil2, coil3, coil4, microsteps=None)
puertaAbierta = True

def abrirPuerta():
    global puertaAbierta
    if not puertaAbierta:
        for step in range(STEPS):
            motor.onestep(direction=stepper.FORWARD)
            time.sleep(DELAY)
        motor.release()
        puertaAbierta = True

def cerrarPuerta():
    global puertaAbierta
    if puertaAbierta:
        for step in range(STEPS):
            motor.onestep(direction=stepper.BACKWARD)
            time.sleep(DELAY)
        motor.release()
        puertaAbierta = False
