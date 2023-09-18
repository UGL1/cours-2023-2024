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


-- Question 5

INSERT INTO Departement VALUES
    (01,"76","Seine-Maritime");

-- Question 6

INSERT INTO Ville VALUES
    (01,"Rouen",76000,01,110169);

-- Question 7

INSERT INTO Ville VALUES
    (02,"Dieppe",76100,01,29965),
    (03,"Envermeu",76630,01,2098);

-- Question 8

INSERT INTO Departement VALUES
    (02,"27","Eure");

INSERT INTO Ville VALUES
    (04,"Igoville",76100,02,27460);

-- Question 9
INSERT INTO Ville VALUES
    (04,"Le Neubourg",76100,02,27110);

COMMIT;

-- Question 10

INSERT INTO Ville VALUES
(6,'Trouville', 14360, 3, 4628),
(7,'Mézidon-Canon', 14270,  3,4838),
(8,'Crèvecoeur-en-Auge', 14340, 3,480);

-- Question 11

UPDATE Ville
SET nom = 'Trouville-Sur-Mer'
WHERE nom = 'Trouville';

-- Question 12

DELETE FROM Ville
WHERE nom = 'Médizon-Canon' OR nom = 'Crèvecoeur-en-Auge';
INSERT INTO Ville VALUES
(9,'Mézidon-Vallée-d’Auge', 14431, 3,9 712);

-- 13

SELECT COUNT(*) from Departement

-- 14

SELECT COUNT(*) from Ville

-- 15

SELECT COUNT(*) from Ville
JOIN Departement ON Ville.idDepartement = Departement.idDepartement
    WHERE Departement.nom = 'Eure';

-- Etc


