import re

def recherche(chaine, mot):
    return mot in chaine

def contient_chiffres(chaine):
    return any(char.isdigit() for char in chaine)

def remplacer_espaces_par_tirets(chaine):
    return chaine.replace(" ", "-")

def format_telephone(val):
    pattern = re.compile(r'\d{2}-\d{3}-\d{4}')
    return bool(pattern.match(val))


def format_email(val):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(val))



