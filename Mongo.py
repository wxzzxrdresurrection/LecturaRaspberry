from pymongo import MongoClient
from tqdm import tqdm
import time
import os
from SensorValor import SensorValor
from JsonClass import Conversion

class Mongo(Conversion):

    def __init__(self,nombrecoleccion,bd):
        self.cadena = 'mongodb+srv://wizzard:Luis200315@cluster0.gbgv62y.mongodb.net/?retryWrites=true&w=majority'
        self.nombrecoleccion = nombrecoleccion
        self.bd = bd
        self.listaoffline= SensorValor()
        self.listatemporal = SensorValor()
        super().__init__()

    def testConnection(self):
        try:
            myclient = MongoClient(self.cadena)
            print("Conexion exitosa")
            return myclient
        except:
            print("Error de conexion")
            return False
        
    
#METODO PARA INSERTAR UN DOCUMENTO EN MONGODB
    def insertarDocumento(self,coleccion,documento):
        coleccion.insert_one(documento.getDict())
        
#METODO PARA ELIMINAR EL DOCUMENTO DE UNA COLECICON(NO USAR)
    def eliminarDocumento(self,key,value):
        documento = self.coleccion.find_one({key : value})
        self.coleccion.delete_one(documento)
        print("Documento Eliminado")

#METODO PARA ACTUALIZAR UN DOCUMENTO DE UNA COLECCION
    def actualizarDocumento(self,key,value,documento):
        self.coleccion.update_one({key : value},{"$set":documento})
        print("Documento Actualizado")

#METODO PARA VALIDAR SI EL DOCUMENTO YA EXISTE
    def validarInsertar(self,documento):
        if self.coleccion.find_one({"identificador": documento["identificador"]}) == None:
            self.insertarDocumento(documento)
        else:
            print("El codigo ya existe")

#METODO PARA INTENTAR GUARDAR EL SENSOR EN MONGODB
    def insertarAMongo(self,doc):
        con = self.testConnection()
        if con != False:
            #ENTRAR A COLECCION
            basasedatos = con[self.bd] 
            coleccion = basasedatos[self.nombrecoleccion]
            #VERIFICAR SI EL ARCHIVO SIN CONEXION TIENE CONTENIDO
            if os.path.exists('sensoresOffline.json'):
                #docDesconectado = self.leerjson('sensoresOffline')
                #SI TIENE CONTENIDO, INTENTAR GUARDARLO EN MONGOD
                #self.coleccion.insert_many(docDesconectado)
                #LIMPIAR EL ARCHIVO SIN CONEXION
                os.remove('sensoresOffline.json')
            try:
                self.insertarDocumento(coleccion,doc)         
            except:
                self.guardarJSONTemporal(doc)
        else:
            print("No se logro conectar con MongoDB, guardando localmente")
            self.guardarEnLocal(doc)


#METODO PARA GUARDAR SIN CONEXION
    def guardarEnLocal(self,data):
        self.listaoffline.agregar(data)
        self.guardarjson('sensoresOffline',self.listaoffline.getDict())
        
    
    def guardarJSONTemporal(self,objeto):
        self.listatemporal.agregar(objeto)
        self.guardarjson('sensoresTemporales',self.listatemporal.getDict())
