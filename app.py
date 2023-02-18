from classes import Estudiante, DbMongo
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("Jertrudis", "Lorenzana", "87582535")
    estudiante.save()
    estudiante.nombre = "Wendy"
    estudiante.apellido = "Navas"
    estudiante.telefono = "95287525"
    estudiante.update('63f06143205a5b1d524e6c26')
    
if __name__ == "__main__":
    load_dotenv()
    main()




