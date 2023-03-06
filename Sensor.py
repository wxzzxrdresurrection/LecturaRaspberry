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
        if len(self.lista) > 1 :
            return f"La lista contiene {len(self.lista)} sensores"
        else:
            return f'tipo: {self.tipo}, id: {self.id}, descripcion : {self.descripcion}, pines: {self.pines}'
    
    def getDict(self):
        if len(self.lista) > 1 :
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
        

if __name__ == "__main__":
    listasensores = Sensor()
    sensor1 = Sensor("Temperatura", "T1",[4])
    print(sensor1)
    listasensores.agregar(sensor1)
    sensor2 = Sensor("Ultrasonico", "US1",[7,8])
    listasensores.agregar(sensor2)
    print(listasensores)
    listasensores.guardarjson("sensores",listasensores.getDict())


