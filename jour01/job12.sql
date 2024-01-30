# La rzquête pour inserer un nouveau étudiant 
INSERT INTO etudiant (nom, prenom, email, age)
VALUES ('Dupuis', 'Martin', 'martin.dupuis@laplateforme.io', 18);

# La requête pour recuperer les etrudiant de la meme famille
SELECT * FROM etudiant WHERE nom = 'Dupuis';