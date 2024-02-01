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

# Exécuter la requête pour calculer la capacité totale des salles
query = "SELECT SUM(capacite) FROM salle"
cursor.execute(query)

# Récupérer le résultat
result = cursor.fetchone()[0]

# Afficher le résultat
print(f"La capacité totale des salles est de {result}")

# Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()