import sqlite3
from settings_functions import get_database

path = get_database()

spotting_db = ("""Id_spott, Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Image""")


def ajout_spott(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
    # Champs
    champs = spotting_db[len("Id_spott, "):]
    # Initialisation de la db
    con = sqlite3.connect(path)
    cursor = con.cursor()
    print(f"""INSERT INTO Spotting({champs}) VALUES(?, ?)""")

print(path)
ajout_spott("F-ABCD", "A320-200", 217, "Air France", 0, 1, "", "2023/04/11", "LFBO", "Spotting à LFBO", "Test", "A remplir auto", "C:Images")