import sqlite3
from settings_functions import get_database

path = get_database()

spotting_db = ("""Id_spott, Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Image""")


def ajout_spott(imm, mod, msn, comp, mil, ser, liv, dat, aer, cat, comm, ach, img):
    # Champs
    champs = spotting_db[len("Id_spott, "):]
    # Initialisation de la db
    con = sqlite3.connect(path)
    cursor = con.cursor()
    print(f"""INSERT INTO Spotting({champs}) VALUES(?, ?)""")

