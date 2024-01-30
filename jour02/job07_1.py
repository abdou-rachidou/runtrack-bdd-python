import mysql.connector
import json

# Chargement du fichier JSON avec les informations de connexion
with open('config.json', 'r') as file:
    configurations = json.load(file)

# Utilisation de la deuxième configuration (Company)
configuration_company = configurations[1]

# Création de la connexion
mybasedata_company = mysql.connector.connect(**configuration_company)

# Création du curseur à partir de la connexion
cursor_company = mybasedata_company.cursor(dictionary=True)

# Utilisation de la méthode execute du curseur avec une jointure
query = """
    SELECT employe.id, employe.nom AS nom_employe, employe.prenom, employe.salaire, service.nom AS nom_service
    FROM employe
    LEFT JOIN service ON employe.id_service = service.id
"""

cursor_company.execute(query)

# Récupération de toutes les lignes de la méthode execute
results_company = cursor_company.fetchall()

# Imprimer chaque ligne directement
for employe in results_company:
    print(f"{employe['id']}  {employe['nom_employe']}  {employe['prenom']}  {employe['salaire']}$  {employe['nom_service']}")

# Fermeture du curseur
cursor_company.close()

# Fermeture de la connexion
mybasedata_company.close()