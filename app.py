from classes import Estudiante, DbMongo, Tipoestudiante
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    Estudiante.delete_all(db)  #Borra todos los documentos creados.
    Tipoestudiante.delete_all(db)
##################################################################################
    Tipoestudiante("Primaria").save(db)
    Tipoestudiante("Secundaria").save(db)
    Tipoestudiante("Superior").save(db)
#################################################################################

    dictTipos = Tipoestudiante.get_dict(db)
    print(dictTipos)

    Estudiante("Abraham"
               ,"Duron"
               ,"96904707"
               ,dictTipos["Primaria"]).save(db)

    Estudiante("Sheryl"
               ,"Montoya"
               ,"95126202"
               ,dictTipos["Superior"]).save(db)

    Estudiante.print_full_report_long_path(db)
    Estudiante.print_full_report_short_path(db)

    client.close()
    
if __name__ == "__main__":
    load_dotenv()
    main()
