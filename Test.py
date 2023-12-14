from fonction import*
# Exemple 1
chaine_test = "Bonjour, comment ça va ?"
mot_test = "comment"
if recherche(chaine_test, mot_test):
    print(f"Le mot '{mot_test}' existe dans la chaîne.")
else:
    print(f"Le mot '{mot_test}' n'existe pas dans la chaîne.")

# Exemple 2
chaine_test = "Hello123"
if contient_chiffres(chaine_test):
    print("La chaîne contient des chiffres.")
else:
    print("La chaîne ne contient pas de chiffres.")


# Exemple 3
chaine_test = "Ceci est un exemple de chaîne"
chaine_modifiee = remplacer_espaces_par_tirets(chaine_test)
print(f"Chaine modifiée : {chaine_modifiee}")

# Exemple 4
numero_test = "12-345-6789"
if format_telephone(numero_test):
    print(f"Le numéro de téléphone {numero_test} est au format attendu.")
else:
    print(f"Le numéro de téléphone {numero_test} n'est pas au format attendu.")

# Exemple 5
email_test = "exemple@domaine.com"
if format_email(email_test):
    print(f"L'adresse e-mail {email_test} est au format attendu.")
else:
    print(f"L'adresse e-mail {email_test} n'est pas au format attendu.")