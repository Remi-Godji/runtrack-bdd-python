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

# Exécuter la requête pour calculer la superficie totale des étages
query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)

# Récupérer le résultat
result = cursor.fetchone()[0]

# Afficher le résultat
print(f"La superficie de La Plateforme est de {result} m2")

# Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()