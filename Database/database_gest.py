import sqlite3
from constantes import path

def create_database():
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE "Spotting" (
	"Id_spott"	INTEGER NOT NULL UNIQUE,
	"Immatriculation"	TEXT NOT NULL,
	"Modele"	TEXT NOT NULL,
	"Msn"	INTEGER NOT NULL,
	"Compagnie"	TEXT NOT NULL,
	"Militaire"	INTEGER,
	"Service"	INTEGER,
	"Livree"	TEXT,
	"Date"	TEXT,
	"Aeroport"	TEXT NOT NULL,
	"Catalogue"	TEXT,
	"Commentaire"	TEXT,
	"Achievement"	TEXT,
	"Image"	TEXT,
	"Nbr_Immat"	INTEGER,
	"Nbr_Msn"	INTEGER,
	PRIMARY KEY("Id_spott" AUTOINCREMENT));
""")
    conn.commit()
    cursor.execute()
    conn.close()
    return 1