from configparser import ConfigParser

def get_settings(file, group, var):
    config = ConfigParser()
    config.read(file)
    return config[group][var]

def get_database():
    config = ConfigParser()
    config.read("Settings\\path.ini")
    return config["path"]["main_db"]