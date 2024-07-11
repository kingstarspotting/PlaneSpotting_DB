import sqlite3
from settings_functions import get_database

#path = get_database()

path = "database\\main_database2.db"



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
	"Fav"	INTEGER,
	PRIMARY KEY("Id_spott" AUTOINCREMENT)
);
""")
    conn.commit()
    cursor.execute("""
CREATE TABLE "Vols" (
	"Id_vol"	INTEGER NOT NULL UNIQUE,
	"Indicatif"	TEXT NOT NULL,
	"Depart"	TEXT NOT NULL,
	"Arrivee"	TEXT NOT NULL,
	"Duree"	REAL,
	"Immatriculation"	TEXT NOT NULL,
	"Msn"	INTEGER,
	"Modele"	TEXT NOT NULL,
	"Compagnie"	TEXT NOT NULL,
	"Date"	TEXT NOT NULL,
	PRIMARY KEY("Id_vol" AUTOINCREMENT)
);
""")
    conn.commit()
    cursor.execute("""
CREATE TABLE "Objectif_spotting" (
	"Id_Objs"	INTEGER NOT NULL UNIQUE,
	"Type"	TEXT NOT NULL,
	"Immatriculation"	TEXT,
	"Modele"	TEXT,
	"Msn"	INTEGER,
	"Compagnie"	TEXT,
	"Livree"	TEXT,
	PRIMARY KEY("Id_Objs" AUTOINCREMENT)
);
""")
    conn.commit()
    conn.close()
    return 1

create_database()