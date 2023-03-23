import RPi.GPIO as GPIO
import time 
from Lista import Lista
import adafruit_dht
from gpiozero import LED
from Mongo import Mongo
from SensorValor import SensorValor
import board

class Sensor(Lista):
    
    def __init__(self,clave ="S/C" ,tipo="S/T", id="S/ID",pines=[],descripcion="S/Desc"):
        self.clave = clave
        self.tipo = tipo
        self.id = id
        self.pines = pines
        self.descripcion = descripcion
        self.listasensorvalor = SensorValor()
        self.mongo = Mongo("ValoresRaspberry","Raspberry")
        super().__init__()
        GPIO.setmode(GPIO.BOARD)

    def __str__(self):
        if len(self.lista) > 0:
            longitud =len(self.lista)
        else:
            pass
    
    def crearSensor(self):
        listasensores = Sensor()
        try: 
            listasensores = self.getObjfromList("listasensores")
        except:
            print("Archivo no existente")
        clave = input("Ingrese la clave del sensor: ")
        tipo = input("Ingrese el tipo de sensor: ")
        id = input("Ingrese el id del sensor: ")
        npines = input("Cuantos pines tiene el sensor: ")
        pines = []
        for i in range(int(npines)):
            pin = int(input("Ingrese el pin: "))
            pines.append(pin)
        descripcion = input("Ingrese la descripcion del sensor: ")
        sns = Sensor(clave,tipo,id,pines,descripcion)
        listasensores.agregar(sns)
        print(listasensores)
        self.guardarjson('listasensores',listasensores.getDict())
        print(sns)

    def getObjfromList(self,archivo):
        data = self.leerjson(archivo)
        for p in data:
            listasensores = Sensor()
            listasensores.agregar(Sensor(p['clave'],p['tipo'],p['id'],p['pines'],p['descripcion']))
        return listasensores

    def getDict(self):
        if len(self.lista) > 0 :
            arreglo = []
            for item in self.lista:
                arreglo.append(item.getDict())
            return arreglo
        else:
            return  {
                        'clave': self.clave,
                        'tipo': self.tipo,
                        'id': self.id, 
                        'descripcion' : self.descripcion,
                        'pines' : self.pines,
                    }

    def getKey(self,sensor):
        return sensor.clave
    
    def read(self,sensor):
        key = self.getKey(sensor)
        print(key)
        if key == "DHT11":
            return self.readTemp(sensor)
        elif key == "US":
            return self.readUltra(sensor)
        elif key == "LED":
            return self.estadoLed(sensor)
        else:
            return "Error"
        
    def readTemp(self,sensor):
        dhtDevice = adafruit_dht.DHT11(board.D17)
        pin = sensor.pines[0]
        while True:
            print("Iniciando sensor")            
            humedad = dhtDevice.humidity
            temperatura = dhtDevice.temperature
            if humedad is not None and temperatura is not None:    
                nuevosensor = SensorValor(sensor,temperatura,time.strftime("%d%m%Y"),time.strftime("%H%M%S"))
                nuevosensor2 = SensorValor(sensor,humedad,time.strftime("%d%m%Y"),time.strftime("%H%M%S"))
                #self.mongo.insertarAMongo(nuevosensor.getDict())
                #self.mongo.insertarAMongo(nuevosensor2.getDict())
                print(temperatura)
                print(humedad)
                return
            else:
                print("Fallo la lectura. Intente de nuevo!")
            
    
                
            
     
    def readUltra(self,sensor):
        trigger = sensor.pines[1]
        echo = sensor.pines[0]
        GPIO.setup(trigger, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        pulse_start = 0
        pulse_end = 0
        pulse_duration = 0
        print("Iniciando sensor")
        while True:
            GPIO.output(trigger, False)
            time.sleep(0.5)
            GPIO.output(trigger, True)
            time.sleep(0.00001)
            GPIO.output(trigger, False)
            print("Esperando respuesta")
            while GPIO.input(echo) == GPIO.LOW:
                pulse_start = time.time()
            while GPIO.input(echo) == GPIO.HIGH:
                pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            nuevosensor = SensorValor(sensor,distance,time.strftime("%d%m%Y"),time.strftime("%H%M%S"))
            #self.mongo.insertarAMongo(nuevosensor)
            print("Distance:",distance,"cm")
            return
    
    def estadoLed(self,sensor):
        pin = sensor.pines[0]
        GPIO.setup(pin,GPIO.OUT)
        print(pin)
        GPIO.output(pin,GPIO.HIGH)
        print("ENCENDER")
        time.sleep(2)
        GPIO.output(pin,GPIO.LOW)
        print("APAGAR")
        
    def readTodos(self):
        listasensores = self.getObjfromList("listasensores")
        for sensor in listasensores:
            self.read(sensor)


if __name__ == "__main__":
    while True:
        sns = Sensor()
        sns.crearSensor()
    
    


