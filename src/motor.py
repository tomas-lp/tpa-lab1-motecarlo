from machine import Pin
import time

# Pines del motor
PIN_MOTOR1 = 12
PIN_MOTOR3 = 13
PIN_MOTOR4 = 14
PIN_MOTOR2 = 15

STEPS = 100     # Cantidad de pasos en que el motor se moverá.
DELAY = 0.01    # Tiempo entre pasos.

# Definicion de cada bobina del motor
coil1 = Pin(PIN_MOTOR1, Pin.OUT)
coil2 = Pin(PIN_MOTOR2, Pin.OUT)
coil3 = Pin(PIN_MOTOR3, Pin.OUT)
coil4 = Pin(PIN_MOTOR4, Pin.OUT)

# Secuencia de pasos para el motor
sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

puertaAbierta = True

def set_step(w1, w2, w3, w4):
    coil1.value(w1)
    coil2.value(w2)
    coil3.value(w3)
    coil4.value(w4)

def step_motor(direction):
    for step in sequence[::direction]:
        set_step(*step)
        time.sleep(DELAY)

def abrirPuerta():
    global puertaAbierta
    if not puertaAbierta:
        for _ in range(STEPS):
            step_motor(1)  # 1 for forward
        puertaAbierta = True
    set_step(0, 0, 0, 0)  # Release the motor

def cerrarPuerta():
    global puertaAbierta
    if puertaAbierta:
        for _ in range(STEPS):
            step_motor(-1)  # -1 for backward
        puertaAbierta = False
    set_step(0, 0, 0, 0)  # Release the motor