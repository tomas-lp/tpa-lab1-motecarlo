from machine import Pin

# Pin del sensor
PIN_RECEPTOR = 3

# Configuración del sensor
sensorObstaculo = Pin(PIN_RECEPTOR, Pin.IN, Pin.PULL_DOWN)