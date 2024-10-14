import uasyncio as asyncio
from machine import Pin
import time

# Assuming these are custom modules, we'll keep them as is
# and assume they've been adapted for MicroPython
import micro_monitoring
from serialRead import USBSerialReader
import buzzer
import motor
import led
from botones import botonCorona, botonTeclado1, botonTeclado2, botonTeclado3
from sensor import sensorObstaculo

import uselect
import sys

spoll = uselect.poll()
spoll.register(sys.stdin, uselect.POLLIN)

# Constants
CLAVE = "123"
TIMEOUT = 15

# Global variables
estado = "B"
coronaBloqueada = True

def bloquearSistema():
    global estado
    print("Sistema bloqueado.")
    print("CONTROL: Sistema bloqueado.")
    global coronaBloqueada
    coronaBloqueada = True
    led.apagar()
    estado = "B"

def desbloquearSistema():
    global estado
    print("Sistema desbloqueado.")
    print("CONTROL: Sistema desbloqueado.")
    buzzer.apagar()
    led.encender()
    motor.abrirPuerta()
    estado = "D"

def tratarInput(inputList):
    input = "".join(str(element) for element in inputList)
    print(input)
    comando = input.strip()
    if comando == 'U':
        if estado == "D":
            return print("CONTROL: El sistema ya está desbloqueado.")
        return desbloquearSistema()
    if comando == 'L':
        if estado == "B":
            return print("CONTROL: El sistema ya está bloqueado.")
        return bloquearSistema()
    if comando == "":
        return
    return print("CONTROL: Comando no válido.")

async def operations():
    global estado, coronaBloqueada
    usbReader = USBSerialReader()

    print("CONTROL: Bienvenido al sistema de control de seguridad. Ingrese un comando:")

    while True:
        inputSerial = (sys.stdin.read(1) if spoll.poll(0) else "")
        # Read commands from control
        if inputSerial:
            tratarInput(inputSerial)
        
        btnCorona = not botonCorona.value()
        objetoDetectado = not sensorObstaculo.value()

        if estado == "B":
            if btnCorona or objetoDetectado:
                print(f"Presencia detectada. Tiene {TIMEOUT} segundos para ingresar la contraseña.")
                print("CONTROL: Presencia detectada.")
                timeout = time.time() + TIMEOUT
                claveIngresada = ""
                tiempoUltimaTecla = time.time()

                while True:
                    if not botonTeclado1.value() == 0:
                        claveIngresada += "1"
                        tiempoUltimaTecla = time.time()
                        print(claveIngresada)
                        await asyncio.sleep(0.3)

                    if not botonTeclado2.value() == 0:
                        claveIngresada += "2"
                        tiempoUltimaTecla = time.time()
                        print(claveIngresada)
                        await asyncio.sleep(0.3)

                    if not botonTeclado3.value() == 0:
                        claveIngresada += "3"
                        tiempoUltimaTecla = time.time()
                        print(claveIngresada)
                        await asyncio.sleep(0.3)

                    if time.time() - tiempoUltimaTecla > 2:
                        claveIngresada = ""
                        tiempoUltimaTecla = time.time()
                        print("Tiempo máximo entre teclas superado. Intento reseteado.")

                    if claveIngresada == CLAVE:
                        print("Contraseña correcta.")
                        desbloquearSistema()
                        break

                    if time.time() > timeout:
                        print("Tiempo agotado. Enviando alerta 🚨🚨🚨")
                        print("CONTROL: ALERTA DE INTRUSO. ALARMA ACTIVADA 🚨🚨🚨")
                        estado = "A"
                        buzzer.encender()
                        motor.cerrarPuerta()
                        break

        if estado == "D":
            if btnCorona:
                if coronaBloqueada:
                    print("Recinto de la corona desbloqueado.")
                    coronaBloqueada = False
                    await asyncio.sleep(0.3)
                else:
                    print("El recinto de la corona ya está desbloqueado")
                    await asyncio.sleep(0.3)

        await asyncio.sleep(0.1)  # Small delay to prevent blocking

def get_app_data():
    global estado
    return {
        "estado": estado,
        "alarmaActivada": estado == "A",
        "objetoDetectado": not sensorObstaculo.value(),
        "botonCorona": not botonCorona.value()
    }

async def main():
    await asyncio.gather(
        operations(),
        micro_monitoring.monitoring(get_app_data),
    )

asyncio.run(main())