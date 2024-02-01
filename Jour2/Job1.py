import mysql.connector

# Paramètres de connexion à la base de données
host = "localhost"
user = "root"
password = "motdepasse"
database = "LaPlateforme"

# Créer une connexion à la base de données
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter une requête pour récupérer tous les étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Récupérer les résultats de la requête
etudiants = cursor.fetchall()

# Afficher les résultats
for etudiant in etudiants:
    print(etudiant)

# Fermer le curseur et la connexion à la base de données
cursor.close()
conn.close()
