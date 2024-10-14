from machine import Pin

# Pin del buzzer
PIN_BUZZER = 2

# Configuración del buzzer
buzzer = Pin(PIN_BUZZER, Pin.OUT)

def encender():
    buzzer.value(1)

def apagar():
    buzzer.value(0)