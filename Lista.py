from JsonClass import Conversion

class Lista(Conversion):
    #INICIALIZAR LOS VALORES DE LA CLASE
    def __init__(self):
        self.lista = [] 
        super().__init__()
#INSERTAR LOS ELEMENTOS EN LA LISTA
    def agregar(self, elemento):
        self.lista.append(elemento)
        
    def eliminar(self, elemento):
        self.lista.remove(self.buscar(elemento))
        
    def mostrar(self):
        for item in self.lista:
            print(item)
    
