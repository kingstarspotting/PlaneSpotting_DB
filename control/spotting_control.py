def ajout_spotting_ctrl(imm: str, mod: str, msn: int, comp: str, mil: int, ser: int, liv: str, dat: str, aer: str, cat: str, comm: str, ach: str, img: str):
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

