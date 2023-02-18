from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("Sheryl", "Montoya", "96904707")
    estudiante.save()
    estudiante.nombre = "Esmeralda"
    estudiante.apellido = "Castro"
    estudiante.telefono = "85105235"
    estudiante.update('63e7d6c38fe491575b2f3f7f')
    
if __name__ == "__main__":
    load_dotenv()
    main()




