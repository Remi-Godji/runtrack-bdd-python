mysql> USE LaPlateforme;
Database changed
mysql> CREATE TABLE etage (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255) NOT NULL,
    -> numero INT NOT NULL,
    -> superficie INT NOT NULL
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE salle (
    -> id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR(255) NOT NULL,
    -> id_etage INT NOT NULL,
    -> capacite INT NOT NULL,
    -> FOREIGN KEY (id_etage) REFERENCES etage(id)
    -> );
Query OK, 0 rows affected (0.09 sec)
