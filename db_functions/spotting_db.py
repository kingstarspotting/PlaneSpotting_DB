import sqlite3
from Functions.settings_functions import get_database


path = get_database()

spotting_db = ("""Id_spott, Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Image, Nbr_Immat, Nbr_Msnk, Fav""")


class Spotting_db:
    def __init__(self):
        pass

    def database_display(self):
        """
        Fonction récupérant les données de la base de donnée afin de les afficher par la suite
        """
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Nbr_Immat, Nbr_Msn, Fav FROM Spotting""")
        rows = cursor.fetchall() # Sélection du nombre
        conn.close()
        return rows



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
    
    def add_spott(self, imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str, nbr_imm: int, nbr_msn: int):
        # Champs
        champs = spotting_db[len("Id_spott, "):]
        # Initialisation de la db
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        # Ajout à la table
        cursor.execute(f"""INSERT INTO Spotting({champs}) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (imm, mod, msn, comp, mil, ser, liv, dat, aer, cat, comm, ach, img, nbr_imm, nbr_msn))
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

    def get_nombre_msn(self, modele, msn):
        """
        Compte le nombre de fois ou ce modèle (msn) a été spotté (en comptant le spott enregistré)

        """
        if msn:
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute(f"""SELECT COUNT(DISTINCT Date) FROM Spotting WHERE Modele = '{modele}' AND Msn = {msn}""")
            nombre = cursor.fetchone()[0] # Sélection du nombre
            conn.close()
            return nombre+1
        else:
            return False

    # A continuer
    def get_achievement(self, nbr_imm, nbr_msn):
        achievement = ""
        if nbr_imm == 1:
            print(achievement) 

    def get_all_immatriculations(self, modele, msn):
        """
        Fonction renvoyant toutes les immatriculations enregistrées qu'a eu un avion. 
        """
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT DISTINCT Immatriculation FROM Spotting WHERE Modele = '{modele}' AND Msn = {msn}""")
        immatriculations = cursor.fetchall() # Sélection du nombre
        conn.close()
        # Conversion en chaine et 
        for i in range(len(immatriculations)):
            immatriculations[i] = str(immatriculations[i]).replace("('", "")
            immatriculations[i] = str(immatriculations[i]).replace("',)", "")
        return immatriculations



