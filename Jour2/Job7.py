import mysql.connector

class Employe:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="motdepasse",
            database="entreprise"
        )
        self.cursor = self.conn.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Employé ajouté avec succès.")

    def read_employes(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        employes = self.cursor.fetchall()
        for employe in employes:
            print(employe)

    def update_employe(self, employe_id, salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Salaire de l'employé mis à jour avec succès.")

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Employé supprimé avec succès.")

    def close(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe Employe
employe_manager = Employe()
employe_manager.create_employe("Brown", "Robert", 3200.00, 1)
employe_manager.read_employes()
employe_manager.update_employe(5, 3500.00)
employe_manager.delete_employe(3)

# Fermer correctement les ressources
employe_manager.close()