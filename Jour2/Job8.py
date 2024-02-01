import mysql.connector

class ZooManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="motdepasse",
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Animal ajouté avec succès.")

    def supprimer_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Animal supprimé avec succès.")

    def modifier_animal(self, animal_id, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, animal_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Animal modifié avec succès.")

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animaux = self.cursor.fetchall()
        for animal in animaux:
            print(animal)

    def afficher_animaux_cages(self):
        query = "SELECT a.nom, c.id FROM animal AS a LEFT JOIN cage AS c ON a.id_cage = c.id"
        self.cursor.execute(query)
        animaux_cages = self.cursor.fetchall()
        for animal_cage in animaux_cages:
            print(f"Animal: {animal_cage[0]}, Cage: {animal_cage[1]}")

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        superficie_totale = self.cursor.fetchone()[0]
        print(f"Superficie totale de toutes les cages: {superficie_totale} m²")

    def close(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe ZooManager
zoo_manager = ZooManager()
zoo_manager.ajouter_animal("Lion", "Félin", 1, "2015-06-12", "Afrique")
zoo_manager.ajouter_animal("Girafe", "Mammifère", 2, "2010-03-25", "Afrique")
zoo_manager.afficher_animaux()
zoo_manager.afficher_animaux_cages()
zoo_manager.calculer_superficie_totale()
zoo_manager.supprimer_animal(1)
zoo_manager.modifier_animal(2, "Girafe", "Mammifère", 3, "2010-03-25", "Afrique")
zoo_manager.close()