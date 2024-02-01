import mysql.connector

# Se connecter à la base de données MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="motdepasse",
    database="LaPlateforme"
)

# Créer un curseur pour exécuter les requêtes SQL
cursor = conn.cursor()

# Exécuter la requête SELECT pour récupérer les noms et les capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

# Récupérer les résultats et les afficher
results = cursor.fetchall()
for row in results:
    nom, capacite = row
    print(f"Nom: {nom}\tCapacité: {capacite}")

# Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()