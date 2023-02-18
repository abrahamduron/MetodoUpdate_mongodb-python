from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    estudiante = Estudiante("Jertrudis", "Lorenzana", "87582535")
    estudiante.save(db)

    estudiante.apellido = "Duron Rios"

    estudiante.update(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()




