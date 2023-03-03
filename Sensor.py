import RPi.GPIO as GPIO
class Sensor:
    
    def __init__(self, tipo="S/T", id="S/ID",pines=[5,6]):
        self.tipo = tipo
        self.id = id
        self.pines = pines

    def __str__(self):
        return {'tipo': self.tipo, 'id': self.id, 'pines': self.pines}
    
    def seleccionarTipo(self,tipo):
        if tipo == "Ultrasonico":
            pass
        elif tipo == "Temperatura":
            pass
        elif tipo == "LED":
            pass

    def usarUltrasonico(self):
        #METODOS PARA LEER EL SENSOR Y MANDAR INFORMACION
        pass

    def usarTemperatura(self):
        #METODOS PARA LEER EL SENSOR Y MANDAR INFORMACION
        pass

    def usarLed(self):
        GPIO.setup(self.pines,GPIO.OUT)