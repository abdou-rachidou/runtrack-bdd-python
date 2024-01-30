import mysql.connector
import json

# Chargement du fichier JSON avec les informations de connexion
with open('config.json', 'r') as file:
    configuration = json.load(file)

# Utilisation de la première configuration (laplateforme)
    configuration_laplateforme = configuration[0]

# Création de la connexion
mybasedata = mysql.connector.connect(**configuration_laplateforme)

# Création du curseur à partir de la connexion
cursor = mybasedata.cursor()

# Exécution de la requête pour récupérer les noms et capacités de la table "salle"
cursor.execute("SELECT nom, capacite FROM salle")

# Récupération de tous les résultats
resultats = cursor.fetchall()


# Exécution de la requête pour calculer la superficie totale des étages
cursor.execute("SELECT SUM(superficie) FROM etage")

# Récupération du résultat
superficie = cursor.fetchone()[0]

# Affichage du résultat
print(f"La superficie de La Plateforme est de {superficie} m2")

# Fermeture du curseur
cursor.close()

# Fermeture de la connexion
mybasedata.close()