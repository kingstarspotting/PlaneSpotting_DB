from configparser import ConfigParser

def get_settings(file, group, var):
    config = ConfigParser()
    config.read(file)
    return config[group][var]

def get_database():
    """
    Permet d'obtenir le chemin du fichier de la DB
    """
    config = ConfigParser()
    config.read("Settings\\config.ini")
    return config["path"]["main_db"]

def get_language():
    """
    Permet d'obtenir la langue définie dans les paramètres

    OUT:
        - La langue à utiliser
    """
    config = ConfigParser()
    config.read("Settings\\config.ini")
    return config["settings"]["language"]

def get_text_lang(section: str, var: str) -> str:
    """
    Fonction qui permet d'obtenir un texte en fonction de la langue sélectionnée par l'utilisateur
    \n
    IN:\n
        - section (str): nom de la section où se trouve le texte (exemple: menu)
        - var (str): variable du texte à afficher\n
    OUT:\n
        - Le texte à afficher
    """
    lang = get_language().lower() # Récupération de la langue
    config = ConfigParser()
    config.read(f"Languages\\{lang}.ini") # Ouverture du fichier de la langue
    return config[section][var] # Renvoie le texte à afficher