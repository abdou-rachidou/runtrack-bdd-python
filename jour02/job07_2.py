import mysql.connector
import json

class EmployeManager:
    def __init__(self, config):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)

    def Create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.connection.commit()

    def Read_employe(self):
        query = """
            SELECT employe.id, employe.nom AS nom_employe, employe.prenom, employe.salaire, service.nom AS nom_service
            FROM employe
            LEFT JOIN service ON employe.id_service = service.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def Update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def Delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.connection.commit()


# Chargement du fichier JSON avec les informations de connexion
with open('config.json', 'r') as file:
    configurations = json.load(file)

# Utilisation de la deuxième configuration (Company)
configuration_company = configurations[1]

# Création d'une instance de EmployeManager
employe_manager = EmployeManager(configuration_company)

# Exemples d'utilisation
employe_manager.Create_employe('Céline', 'Emptose', 6100.00, 7)

# Affichage des employés
employes = employe_manager.Read_employe()
for employe in employes:
    print(f"{employe['id']}  {employe['nom_employe']}  {employe['prenom']}  {employe['salaire']}$  {employe['nom_service']}")

# Mise à jour du salaire
employe_manager.Update_employe(3, 1500.00)

# Affichage des employés après mise à jour
employes = employe_manager.Read_employe()
for employe in employes:
    print(f"{employe['id']}  {employe['nom_employe']}  {employe['prenom']}  {employe['salaire']}$  {employe['nom_service']}")

# Suppression d'un employé
employe_manager.Delete_employe(16)

# Affichage des employés après suppression
employes = employe_manager.Read_employe()
for employe in employes:
    print(f"{employe['id']}  {employe['nom_employe']}  {employe['prenom']}  {employe['salaire']}$  {employe['nom_service']}")

# Fermeture de la connexion
del employe_manager