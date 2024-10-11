from serialRead import USBSerialReader
from sensor import sensorObstaculo
import buzzer
import motor
import led
from botones import botonCorona, botonTeclado1, botonTeclado2, botonTeclado3
import time

#Constantes
CLAVE = "123"                   #Contraseña para desbloquear el sistema.
TIMEOUT = 10                    #Tiempo de espera para ingresar la contraseña, en segundos.

#Variables del sistema.
estado = "B"                    #Estado del sistema. Puede ser "B"(bloqueado), "D"(desbloqueado) o "A"(alerta).
coronaBloqueada = True          #Estado del recinto que protege la corona.
usbReader = USBSerialReader()   #Permite leer inputs desde control.

def bloquearSistema():
    global estado
    print("Sistema bloqueado.")
    print("CONTROL: Sistema bloqueado.")
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

def tratarInput(input):
    comando = input.strip()
    if "UNLOCK" in comando:
        if estado == "D":
            return print("CONTROL: El sistema ya está desbloqueado.")

        if comando == ("UNLOCK " + CLAVE):
            return desbloquearSistema()

        return print("CONTROL: Contraseña incorrecta.")

    if "LOCK" in comando:
        if estado == "B":
            return print("CONTROL: El sistema ya está bloqueado.")

        return bloquearSistema()

    return print("CONTROL: Comando no válido.")

print("CONTROL: Bienvenido al sistema de control de seguridad. Ingrese un comando:")


while True:
    #Lee comandos desde control.
    inputSerial = usbReader.read()
    if inputSerial:
        tratarInput(inputSerial)

    #El boton de la corona y el sensor funcionan de forma inversa.
    btnCorona = not botonCorona.value
    objetoDetectado = not sensorObstaculo.value

    if estado == "B":
        if btnCorona or objetoDetectado:
            print(f"Presencia detectada. Tiene {TIMEOUT} segundos para ingresar la contraseña.")
            print("CONTROL: Presencia detectada.")
            timeout = time.time() + TIMEOUT
            claveIngresada = ""
            tiempoUltimaTecla = time.time()

            while True:
                if botonTeclado1.value:
                    claveIngresada = claveIngresada + "1"
                    tiempoUltimaTecla = time.time()
                    print (claveIngresada)
                    time.sleep(0.3)

                if botonTeclado2.value:
                    claveIngresada = claveIngresada + "2"
                    tiempoUltimaTecla = time.time()
                    print (claveIngresada)
                    time.sleep(0.3)

                if botonTeclado3.value:
                    claveIngresada = claveIngresada + "3"
                    tiempoUltimaTecla = time.time()
                    print (claveIngresada)
                    time.sleep(0.3)

                if time.time() - tiempoUltimaTecla > 2:
                    claveIngresada = ""
                    tiempoUltimaTecla = time.time()
                    print ("Tiempo máximo entre teclas superado. Intento reseteado.")

                if claveIngresada == CLAVE:
                    print("Contraseña correcta.")
                    desbloquearSistema()
                    break

                if time.time() > timeout: #Si el tiempo para ingresar la contraseña se agotó.
                    print(estado)
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
                time.sleep(0.3)
            else:
                print("El recinto de la corona ya está desbloqueado")
                time.sleep(0.3)
