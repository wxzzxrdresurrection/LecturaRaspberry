import time
from Lista import Lista
from Mongo import Mongo


class SensorValor(Lista):

    def __init__(self, sensor="S/SENSOR", valor="S/VALOR",fecha="S/FECHA",hora="S/HORA"):
        self.sensor = sensor
        self.valor = valor
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f'Sensor: {self.sensor}, Valor: {self.valor}, Fecha: {self.fecha}, Hora: {self.hora}'
    
    def getDict(self):
        if len(self.lista) > 0 :
            arreglo = []
            for item in self.lista:
                arreglo.append(item.getDict())
            return arreglo
        else:
            return {
                'sensor': self.sensor.getDict(),
                'valor': self.valor,
                'fecha': self.fecha,
                'hora': self.hora
            }
        
    def addValor(self,valor):
        SensorValor = SensorValor()

