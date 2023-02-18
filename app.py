from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    Estudiante.delete_all(db)
    #############################
    estudiante = Estudiante("Jertrudis", "Vichenzo", "87582535")
    estudiante.save(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()




