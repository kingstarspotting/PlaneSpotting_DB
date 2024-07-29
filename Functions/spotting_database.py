import sqlite3
from Functions.settings_functions import get_database

path = get_database()
spotting_db = ("""Id_spott, Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Image, Nbr_Immat, Nbr_Msn, Fav""")

class Spotting:
    def __init__(self):
        pass

    def check_data(self, imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
        """
        Retourne False si les conditions d'ajout ne sont pas respectées, True si tout est bon.
        """
        # Vérification du msn, du code ICAO, et du format de la date
        if (not type(msn) == int) or (not len(aer) == 4) or (dat[4] != "/" or dat[7] != "/"):
            return False
        # Si tout va bien
        else:
            return True
    
    def add_spott(self, imm, mod, msn, comp, mil, ser, liv, dat, aer, cat, comm, ach, img, nbr_imm, nbr_msn, fav):
        # Champs
        champs = spotting_db[len("Id_spott, "):]
        # Initialisation de la db
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        # Ajout à la table
        cursor.execute(f"""INSERT INTO Spotting({champs}) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (imm, mod, msn, comp, mil, ser, liv, dat, aer, cat, comm, ach, img, nbr_imm, nbr_msn, fav))
        # Validation et exécution
        conn.commit()
        conn.close()

    def delete_spott(self, imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
        # Initialisation de la db
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""DELETE FROM Spotting WHERE Immatriculation = '{imm}' AND Modele = '{mod}' AND Msn = {msn} AND Compagnie = '{comp}' AND Militaire = {mil} AND Service = {msn} AND Livree = '{liv}' AND Date = '{dat}' AND Aeroport = '{aer}'
                    AND Catalogue = '{cat}' AND Commentaire = '{comm}' AND Achievement = '{ach}' AND Image = '{img}'""")
        conn.commit()
        conn.close()
    
    def get_nombre_immatriculation(self, immatriculation, modele, msn):
        """
        Compte le nombre de fois ou l'immatriculation sur cet avion a été spotté (en comptant le spott enregistré)
        """
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT COUNT(DISTINCT Date) FROM Spotting WHERE Immatriculation = '{immatriculation}' AND Modele = '{modele}' AND Msn = {msn}""")
        nombre = cursor.fetchone()[0] # Sélection du nombre
        conn.close()
        return nombre+1

test = Spotting
test.add_spott("F-ABCD" ,"A380", 3, "Air Test", 1, 1, "Livrée Test", "2020/12/26", "LFBO", "Spotting à Toulouse Blagnac", "Magnifique Spott", "Première capture", "AAA", 1, 1, 1, 1)