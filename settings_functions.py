from configparser import ConfigParser

def get_settings(file, group, var):
    """
    Permet d'obtenir des paramètres divers
    """
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

def get_color_theme():
    """
    Permet d'obtenir le thème de couleur sélectionnée par l'utilisateur et la couleur secondaire
    """
    config = ConfigParser()
    config.read("Settings\\config.ini")
    return (config["settings"]["display_mode"], config["settings"]["secondary_color"])

def get_color():
    """
    Permet d'obtenir les couleurs en fonctions du thème choisi par l'utilisateur\n
    Out:\n
        - color[0] = Bg_color
        - color[1] = relief_color
        - color[2] = secondary_color
        - color[3] = text_color
    """
    color_theme = get_color_theme()
    config = ConfigParser()
    config.read("Settings\\colors.ini")
    bg_color = config[color_theme[0]]["bg_color"]
    relief_color = config[color_theme[0]]["relief_color"]
    secondary_color = config["secondary_color"][color_theme[1]]
    text_color = config[color_theme[0]]["text_color"]
    return (bg_color, relief_color, secondary_color, text_color)

