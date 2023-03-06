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
        return {'tipo': self.tipo, 'id': self.id, 'fecha' : self.fecha, 'hora':self.hora, 'pines': self.pines}
    
    def seleccionarTipo(self,tipo):
        if tipo == "Ultrasonico":
            self.usarUltrasonico(self.pines)
        elif tipo == "Temperatura":
            self.usarTemperatura(self.pines)
        elif tipo == "LED":
            self.usarLed(self.pines)

    #METODOS PARA LEER EL SENSOR Y MANDAR INFORMACION
    def usarUltrasonico(self,pines):
        GPIO.setup(pines[0],GPIO.OUT)
        GPIO.setup(pines[1],GPIO.IN)

        GPIO.output(pines[0], GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(pines[0], GPIO.LOW)
        while GPIO.input(pines[1]) == GPIO.LOW:
            pulse_start = time.time()
        while GPIO.input(pines[1]) == GPIO.HIGH:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

    #METODOS PARA LEER EL SENSOR Y MANDAR INFORMACION
    def usarTemperatura(self,pin):
        sensortemp = adafruit_dht.DHT11(pin)
        temperature_c = sensortemp.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = sensortemp.humidity
        return temperature_c,temperature_f,humidity
    

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

if __name__ == "__main__":
    sensor = Sensor("Temperatura","1",[4])
    sensor.usarLed(34)
    
