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

