from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    Estudiante.delete_all(db)  #Borra todos los documentos creados.

    #Creamos instancias de la clase Estudiante
    #estudiante = Estudiante("Abraham", "Duron", "96904707")
    estudiante = Estudiante("Sheryl", "Montoya", "95126202")
    estudiante.save(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()
