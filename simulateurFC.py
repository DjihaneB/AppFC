# Exercice : Simulateur de fréquence cardiaque
# Objectif : Créer un programme en langage Python qui simule la fréquence cardiaque d'un patient.
# //////////////////////

# Demander l'âge du patient à l'utilisateur
age = int(input("Entrez l'âge du patient : "))

# Calculer la fréquence cardiaque maximale en utilisant la formule
freq_cardiaque_maximale = 220 - age

# Demander le niveau d'intensité de l'exercice à l'utilisateur
intensite_exercice = input("Entrez le niveau d'intensité de l'exercice (faible, moyen ou élevé) : ")

# Calculer la fréquence cardiaque cible en fonction de l'intensité choisie
if intensite_exercice.lower() == "faible":
    freq_cardiaque_cible = 0.5 * freq_cardiaque_maximale
elif intensite_exercice.lower() == "moyen":
    freq_cardiaque_cible = 0.7 * freq_cardiaque_maximale
elif intensite_exercice.lower() == "élevé":
    freq_cardiaque_cible = 0.85 * freq_cardiaque_maximale
else:
    print("Niveau d'intensité invalide. Veuillez choisir parmi faible, moyen ou élevé.")
    exit()

# Afficher les résultats à l'utilisateur
print(f"La fréquence cardiaque maximale du patient est : {freq_cardiaque_maximale} bpm")
print(f"La fréquence cardiaque cible du patient pendant l'exercice est : {freq_cardiaque_cible} bpm")
