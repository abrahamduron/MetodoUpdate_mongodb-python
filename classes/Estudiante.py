from classes.DbMongo import DbMongo
from bson.objectid import ObjectId
class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "estudiante"

    def save(self):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        collection.insert_one(self.__dict__)
        client.close()
        
    def update(self, id_Estudiante):
        client, db = DbMongo.getDB()
        collection = db[self.__collection]
        resp = collection.update_one(  
        {
        '_id': ObjectId(id_Estudiante)
        }, 
        {
            '$set': {
                "nombre": self.nombre,
                "apellido": self.apellido,
                "telefono": self.telefono,
            }
        })
        return resp.modified_count 