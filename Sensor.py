import RPi.GPIO as GPIO
import time 
#import adafruit_dht
class Sensor:
    
    def __init__(self, tipo="S/T", id="S/ID",fecha= time.strftime("%d/%m/%y"),hora= time.strftime("%H:%M:%S"),pines=[]):
        self.tipo = tipo
        self.id = id
        self.pines = pines
        self.fecha = fecha
        self.hora = hora
        GPIO.setmode(GPIO.BOARD)

    def __str__(self):
        return {'tipo': self.tipo, 'id': self.id, 'pines': self.pines}
    
    def seleccionarTipo(self,tipo):
        if tipo == "Ultrasonico":
            pass
        elif tipo == "Temperatura":
            pass
        elif tipo == "LED":
            pass

    #METODOS PARA LEER EL SENSOR Y MANDAR INFORMACION
    def usarUltrasonico(self,pines):
        GPIO.setup(pines[0],GPIO.OUT)
        GPIO.setup(pines[1],GPIO.IN)
        pass

    #METODOS PARA LEER EL SENSOR Y MANDAR INFORMACION
    def usarTemperatura(self,pin):
        GPIO.setup(pin,GPIO.OUT)
        pass

    def usarLed(self,pin):
        GPIO.setup(pin,GPIO.OUT)    
        x = 1
        while x == 1:
            print('¿Que desea hacer con el led?')
            print('1. Encender')
            print('2. Apagar')
            print('3. Salir')
            opt = int(input('Opcion: '))
            if opt == '1':
                GPIO.output(pin,True)
            elif opt == '2':
                GPIO.output(pin,False)
            elif opt == '3':
                x = 0
            else:
                print('Opcion invalida')

