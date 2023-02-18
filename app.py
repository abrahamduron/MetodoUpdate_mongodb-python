from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
   # estudiante = Estudiante("Jertrudis", "Lorenzana", "87582535")
   # estudiante.save(db)
    #estudiante.apellido = "Duron Rios"
   # estudiante.update(db)
   # estudiante.delete(db)

    lista_estudiantes = Estudiante.get_list(db)
    #print(lista_estudiantes[0].name)
    lista_estudiantes[0].delete(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()




