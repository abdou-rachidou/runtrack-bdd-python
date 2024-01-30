import mysql.connector
import json

# Chargement du fichier JSON avec les informations de connexion
with open('config.json', 'r') as file:
    configurations = json.load(file)

# Utilisation de la première configuration (laplateforme)
config_laplateforme = configurations[0]

# Création de la connexion
mybasedata = mysql.connector.connect(**config_laplateforme)

# Création du curseur à partir de la connexion
cursor = mybasedata.cursor()

# Utilisation de la méthode execute du curseur
cursor.execute("SELECT * FROM etudiant")

# Récupération de toutes les lignes de la méthode execute
results = cursor.fetchall()
print(results)

# Fermeture du curseur
cursor.close()

# Fermeture de la connexion
mybasedata.close()