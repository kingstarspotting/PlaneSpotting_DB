import sqlite3
from settings_functions import get_database


path = get_database()

flight_db = ("""Id_vol, Indicatif, Depart, Arrivee, Immatriculation, Msn, Modele, Compagnie, Date""")

class flight_control:
    def __init__(self):
        pass
    
    def check_data(self, ind: str, dep: str, arr: str, imm: str, msn: int, mod: str, comp: str, date: str):
        """
        Vérifie les données entrées lors de l'ajout d'un vol, retourne False si les conditions ne sont pas respectées ou True si tout est bon
        """
        # Vérification du msn
        if (not type(msn) == int):
            return False
        # A compléter
        