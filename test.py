def test():
    date = input("Date: ")
    # Format de la date AAAA/MM/JJ
    annee = date[:4] # Année dans la date
    mois = date[5:7] # Mois dans la date
    jour = date[8:10] # Jour dans la date
    
    # Vérification du format de la date
    try:
        annee = int(annee)
        mois = int(mois)
        jour = int(jour)
        print(annee, mois, jour)
    except:
        return False
    
    # Vérification de la validité de la date
    mois_entier = [2,4,6,9,11]



test()
# Trouver une fonction de correction de la date