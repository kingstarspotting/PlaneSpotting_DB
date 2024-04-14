import sqlite3
from settings_functions import get_database

path = get_database()

spotting_db = ("""Id_spott, Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Image""")


def ajout_spott(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
    # Champs
    champs = spotting_db[len("Id_spott, "):]
    # Initialisation de la db
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    # Ajout à la table
    cursor.execute(f"""INSERT INTO Spotting({champs}) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (imm, mod, msn, comp, mil, ser, liv, dat, aer, cat, comm, ach, img))
    # Validation et exécution
    conn.commit()

def delete_spott(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
    # Initialisation de la db
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(f"""DELETE FROM Spotting WHERE Immatriculation = '{imm}' AND Modele = '{mod}' AND Msn = {msn} AND Compagnie = '{comp}' AND Militaire = {mil} AND Service = {msn} AND Livree = '{liv}' AND Date = '{dat}' AND Aeroport = '{aer}'
                AND Catalogue = '{cat}' AND Commentaire = '{comm}' AND Achievement = '{ach}' AND Image = '{img}'""")
    conn.commit()

delete_spott("F-ABCD", "A320-200", 217, "Air France", 0, 1, "", "2023/04/11", "LFBO", "Spotting à LFBO", "Test", "A remplir auto", "C:Images")