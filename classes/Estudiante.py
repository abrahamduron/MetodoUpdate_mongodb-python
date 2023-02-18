from classes.DbMongo import DbMongo
from bson.objectid import ObjectId  #Para que me reconozco el ObjetID
class Estudiante:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.__collection = "estudiante"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id = result.inserted_id

    def update (self, db):
        collection = db[self.__collection]
        filterToUse = {'_id' : self.__id}
        objStore = {'$set' : self.__dict__}
        collection.update_one(filterToUse, objStore)


    """def update(self, id_Estudiante):
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
        return resp.modified_count"""