import RPi.GPIO as GPIO
import time 
from Lista import Lista
import Adafruit_DHT
from gpiozero import LED
class Sensor(Lista):
    
    def __init__(self,clave ="S/C" ,tipo="S/T", id="S/ID",pines=[],descripcion="S/Desc"):
        self.clave = clave
        self.tipo = tipo
        self.id = id
        self.pines = pines
        self.descripcion = descripcion
        super().__init__()
        GPIO.setmode(GPIO.BCM)

    def __str__(self):
        if len(self.lista) > 0:
            return f"La lista contiene {len(self.lista)} sensores"
        else:
            return f'tipo: {self.tipo}, id: {self.id}, descripcion : {self.descripcion}, pines: {self.pines}'
    
    def crearSensor(self):
        listasensores = Sensor()
        tipo = input("Ingrese el tipo de sensor: ")
        id = input("Ingrese el id del sensor: ")
        npines = input("¿Cuantos pines tiene el sensor?")
        pines = []
        for i in range(int(npines)):
            pin = int(input("Ingrese el pin: "))
            pines.append(pin)
        descripcion = input("Ingrese la descripcion del sensor: ")
        sns = Sensor(tipo,id,pines,descripcion)
        listasensores.agregar(sns)
        print(listasensores)
        self.guardarjson('listasensores',listasensores.getDict())
        print(sns)

    def getDict(self):
        if len(self.lista) > 0 :
            arreglo = []
            for item in self.lista:
                arreglo.append(item.getDict())
            return arreglo
        else:
            return  {
                        'tipo': self.tipo,
                        'id': self.id, 
                        'descripcion' : self.descripcion,
                        'pines' : self.pines,
                        'hora':time.strftime("%H:%M:%S", time.localtime()),
                        'fecha':time.strftime("%d/%m/%y", time.localtime())
                    }

    def getType(self,sensor):
        return sensor.tipo
    
    def read(self,sensor):
        tipo = self.getType(sensor)
        if tipo == "DHT11":
            return self.readTemp()
        elif tipo == "LUZ":
            return self.readLuz()
        elif tipo == "US":
            return self.readUltra()
        elif tipo == "LED":
            return self.estadoLed()
        else:
            return "Error"
        
    def readTemp(self,pin):
        dhtDevice = Adafruit_DHT.DHT11
        try:
            humedad, temperatura = dhtDevice.read(pin[0])
            return temperatura, humedad
        except:
            return "Error"
     
    def readUltra(self,pines):
        trigger = pines[0]
        echo = pines[1]
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)

        GPIO.output(trigger, False)
        time.sleep(0.5)
        GPIO.output(trigger, True)
        time.sleep(0.00001)
        GPIO.output(trigger, False)
        while GPIO.input(echo) == GPIO.LOW:
            pulse_start = time.time()
        while GPIO.input(echo) == GPIO.HIGH:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

    def estadoLed(self):
        led = LED(17)
        if led.is_lit:
            led.on()
            return "Encendido"
        else:
            led.off()
            return "Apagado"

        

if __name__ == "__main__":
    sns = Sensor()
    
    


