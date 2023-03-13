from Sensor import Sensor

class Menu:

    def __init__(self):
        self.sns = Sensor()


    def menu(self):
        us = Sensor("US","Ultrasonico","US1", [29,31], "Puerta")
        temp = Sensor("DHT11","Temperatura","DHT1", [4], "Cocina")
        led = Sensor("LED","LED","LED1", [12], "Foco")
        while True:
            print("Menu de opciones")
            print("1.-Leer ultrasonico")
            print("2.-Leer temperatura")
            print("3.-Led")
            print("4.-Salir")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                self.sns.read(us)
            elif opcion == "2":
                self.sns.read(temp)
            elif opcion == "3":
                print("Led")
                self.sns.read(led)
            elif opcion == "4":
                print("Adios")
                break
            else:
                print("Opcion no valida")
    
if __name__ == "__main__":
    menu = Menu()
    menu.menu()
            