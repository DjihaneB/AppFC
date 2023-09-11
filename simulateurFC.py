# # Exercice : Simulateur de fréquence cardiaque
# # Objectif : Créer un programme en langage Python qui simule la fréquence cardiaque d'un patient.
# # //////////////////////

# # Demander l'âge du patient à l'utilisateur
# age = int(input("Entrez l'âge du patient : "))

# # Calculer la fréquence cardiaque maximale en utilisant la formule
# freq_cardiaque_maximale = 220 - age

# # Demander le niveau d'intensité de l'exercice à l'utilisateur
# intensite_exercice = input("Entrez le niveau d'intensité de l'exercice (faible, moyen ou élevé) : ")

# # Calculer la fréquence cardiaque cible en fonction de l'intensité choisie
# if intensite_exercice.lower() == "faible":
#     freq_cardiaque_cible = 0.5 * freq_cardiaque_maximale
# elif intensite_exercice.lower() == "moyen":
#     freq_cardiaque_cible = 0.7 * freq_cardiaque_maximale
# elif intensite_exercice.lower() == "élevé":
#     freq_cardiaque_cible = 0.85 * freq_cardiaque_maximale
# else:
#     print("Niveau d'intensité invalide. Veuillez choisir parmi faible, moyen ou élevé.")
#     exit()

# # Afficher les résultats à l'utilisateur
# print(f"La fréquence cardiaque maximale du patient est : {freq_cardiaque_maximale} bpm")
# print(f"La fréquence cardiaque cible du patient pendant l'exercice est : {freq_cardiaque_cible} bpm")


# ----------------------


# Simulateur de fréquence cardiaque avancé

def calculer_zone_cible(freq_maximale, intensite):
    if intensite.lower() == "faible":
        return (0.5 * freq_maximale, 0.6 * freq_maximale)
    elif intensite.lower() == "moyen":
        return (0.7 * freq_maximale, 0.8 * freq_maximale)
    elif intensite.lower() == "élevé":
        return (0.85 * freq_maximale, 0.95 * freq_maximale)
    else:
        print("Niveau d'intensité invalide. Veuillez choisir parmi faible, moyen ou élevé.")
        exit()

# Demander l'âge du patient à l'utilisateur
while True:
    try:
        age = int(input("Entrez l'âge du patient : "))
        if age < 0:
            print("L'âge ne peut pas être négatif. Veuillez entrer un âge valide.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre valide pour l'âge.")

# Demander le poids du patient en kilogrammes
while True:
    try:
        poids = float(input("Entrez le poids du patient en kilogrammes : "))
        if poids <= 0:
            print("Le poids doit être supérieur à zéro. Veuillez entrer un poids valide.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre valide pour le poids.")

# Demander le sexe du patient
sexe = input("Entrez le sexe du patient (homme/femme) : ").lower()

# Calculer la fréquence cardiaque maximale en utilisant la formule en tenant compte du sexe
if sexe == "homme":
    freq_cardiaque_maximale = 220 - age
elif sexe == "femme":
    freq_cardiaque_maximale = 226 - age
else:
    print("Sexe non reconnu. Veuillez choisir entre homme et femme.")
    exit()

# Demander le niveau d'intensité de l'exercice à l'utilisateur
intensite_exercice = input("Entrez le niveau d'intensité de l'exercice (faible, moyen ou élevé) : ")

# Calculer la fréquence cardiaque cible et la zone cible en fonction de l'intensité choisie
freq_cardiaque_cible, zone_cible_max = calculer_zone_cible(freq_cardiaque_maximale, intensite_exercice)

# Demander la durée de l'exercice en minutes
while True:
    try:
        duree_exercice = int(input("Entrez la durée prévue de l'exercice en minutes : "))
        if duree_exercice < 0:
            print("La durée ne peut pas être négative. Veuillez entrer une durée valide.")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre valide pour la durée.")

# Calculer le nombre de battements cardiaques totaux prévus pour l'exercice
battements_totaux = duree_exercice * freq_cardiaque_cible

# Afficher les résultats à l'utilisateur
print(f"La fréquence cardiaque maximale du patient est : {freq_cardiaque_maximale} bpm")
print(f"La fréquence cardiaque cible du patient pendant l'exercice est : {freq_cardiaque_cible} bpm")
print(f"La zone cible de fréquence cardiaque pendant l'exercice est : {zone_cible_max} bpm")
print(f"Le nombre total de battements cardiaques prévus pendant l'exercice est : {battements_totaux} bpm")
