BEGIN TRANSACTION;

DROP TABLE IF EXISTS Departement;
CREATE TABLE IF NOT EXISTS Departement
(
    idDepartement INT PRIMARY KEY,
    numero        TEXT NOT NULL,
    nom           TEXT NOT NULL
);

DROP TABLE IF EXISTS "Ville";
CREATE TABLE IF NOT EXISTS "Ville"
(
    idVille       INT PRIMARY KEY,
    nom           TEXT NOT NULL,
    codePostal    INT  NOT NULL,
    nbHabitants   INT,
    idDepartement INT  NOT NULL REFERENCES Departement (idDepartement)

);

COMMIT;
