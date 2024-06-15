import sqlite3
from settings_functions import get_database


path = get_database()

spotting_db = ("""Id_spott, Immatriculation, Modele, Msn, Compagnie, Militaire, Service, Livree, Date, Aeroport, Catalogue, Commentaire, Achievement, Image, Nbr_Immat, Nbr_Msn""")


class Spotting_control:
    def __init__(self):
        pass

    def check_data(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
        """
        Fonction de contrôle qui vérifie que l'ajout d'un spott est valable
        Retourne un code d'erreur:
            0 Si tout va bien
            1 immatriculation
            2 modèle
            3 msn
            4 compagnie
            5 militaire
            6 service
            7 livrée
            8 date
            9 aéroport
            10 catalogue
            11 commentaire
            12 achievement
            13 image
        """
        # Si le msn n'est pas un entier
        if not type(msn) == int:
            return 3
        # Si l'aéroport n'est pas un code ICAO
        if not len(aer) == 4:
            return 9
        # Vérification du format de la date (aaaa/mm/jj)
        if dat[4] != "/" or dat[7] != "/":
            return 8
        # Si tout va bien
        return 0
    
    def ajout_spott(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str, nbr_imm: int, nbr_msn: int):
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
    
    def delete_spott(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
        # Initialisation de la db
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""DELETE FROM Spotting WHERE Immatriculation = '{imm}' AND Modele = '{mod}' AND Msn = {msn} AND Compagnie = '{comp}' AND Militaire = {mil} AND Service = {msn} AND Livree = '{liv}' AND Date = '{dat}' AND Aeroport = '{aer}'
                    AND Catalogue = '{cat}' AND Commentaire = '{comm}' AND Achievement = '{ach}' AND Image = '{img}'""")
        conn.commit()
        conn.close()
    
    def get_nombre_immatriculation(immatriculation, modele, msn):
        """
        Compte le nombre de fois ou l'immatriculation sur cet avion a été spotté (en comptant le spott enregistré)
        """
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT COUNT(DISTINCT Date) FROM Spotting WHERE Immatriculation = '{immatriculation}' AND Modele = '{modele}' AND Msn = {msn}""")
        nombre = cursor.fetchone()[0] # Sélection du nombre
        conn.close()
        return nombre+1

    def get_nombre_msn(modele, msn):
        """
        Compte le nombre de fois ou ce modèle (msn) a été spotté (en comptant le spott enregistré)

        """
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute(f"""SELECT COUNT(DISTINCT Date) FROM Spotting WHERE Modele = '{modele}' AND Msn = {msn}""")
        nombre = cursor.fetchone()[0] # Sélection du nombre
        conn.close()
        return nombre+1

    # A continuer
    def get_achievement(nbr_imm, nbr_msn):
        achievement = ""
        if nbr_imm == 1:
            print(achievement) 

    def get_all_immatriculations(modele, msn):
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



