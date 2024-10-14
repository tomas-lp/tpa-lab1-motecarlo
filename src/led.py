from machine import Pin

# Ubicacion del led de la placa
# En la Raspberry Pi Pico W, el LED onboard está conectado al pin 'LED' (usualmente GPIO 25)
BOARD_LED = 'LED'

# Configuracion del led
led = Pin(BOARD_LED, Pin.OUT)

def encender():
    led.on()

def apagar():
    led.off()