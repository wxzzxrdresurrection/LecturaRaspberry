#import RPi.GPIO as GPIO
import time 
from Lista import Lista
#import adafruit_dht
class Sensor(Lista):
    
    def __init__(self, tipo="S/T", id="S/ID",pines=[],descripcion="S/Desc"):
        self.tipo = tipo
        self.id = id
        self.pines = pines
        self.descripcion = descripcion
        
        super().__init__()
        #GPIO.setmode(GPIO.BOARD)

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
    
    def read(self,tipo):
        if tipo == "Temperatura":
            return self.readTemp()
        elif tipo == "Humedad":
            return self.readHum()
        elif tipo == "Luz":
            return self.readLuz()
        elif tipo == "Ultrasonico":
            return self.readUltra()
        else:
            return "Error"
        
    def readTemp(self):
        #dhtDevice = adafruit_dht.DHT11(4)
        #try:
        #    temperature = dhtDevice.temperature
        #    return temperature
        #except RuntimeError as error:
        #    print(error.args[0])
        #    return "Error"
        #finally:
        #    dhtDevice.exit()
        return 20
    
    def readHum(self):
        #dhtDevice = adafruit_dht.DHT11(4)
        #try:
        #    humidity = dhtDevice.humidity
        #    return humidity
        #except RuntimeError as error:
        #    print(error.args[0])
        #    return "Error"
        #finally:
        #    dhtDevice.exit()
        return 50
    
    def readLuz(self):
        #GPIO.setup(4, GPIO.IN)
        #return GPIO.input(4)
        return 1
    
    def readUltra(self):
        #GPIO.setup(7, GPIO.OUT)
        #GPIO.setup(8, GPIO.IN)
        #GPIO.output(7, False)
        #time.sleep(0.5)
        #GPIO.output(7, True)
        #time.sleep(0.00001)
        #GPIO.output(7, False)
        #while GPIO.input(8) == 0:
        #    pulse_start = time.time()
        #while GPIO.input(8) == 1:
        #    pulse_end = time.time()
        #pulse_duration = pulse_end - pulse_start
        #distance = pulse_duration * 17150
        #distance = round(distance, 2)
        #return distance
        return 10
    

        

if __name__ == "__main__":
    sns = Sensor()
    sns.crearSensor()
    


