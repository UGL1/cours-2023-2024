DROP TABLE IF EXISTS Pays; -- recréer la table de zéro
CREATE TABLE Pays
(
    nom_pays   TEXT PRIMARY KEY,
    population INTEGER CHECK (population > 0), -- contraintes utilisateur,
    superficie INTEGER CHECK (superficie > 0)
);

DROP TABLE IF EXISTS Livre;
CREATE TABLE Livre
(
    num_isbn INTEGER PRIMARY KEY,
    titre    TEXT,
    annee    TEXT CHECK (date(annee) BETWEEN '1900' AND '2100')
);

DROP TABLE IF EXISTS Auteur;
CREATE TABLE Auteur
(
    id_auteur      INTEGER PRIMARY KEY,
    nom_pays       TEXT REFERENCES Pays (nom_pays)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    nom            TEXT,
    prenom         TEXT,
    date_naissance TEXT,
    UNIQUE (nom, prenom)

);

DROP TABLE IF EXISTS Ecrire;
CREATE TABLE Ecrire
(
    id_auteur    INTEGER REFERENCES Auteur (id_auteur)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    num_isbn     INTEGER REFERENCES Livre (num_isbn)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    nb_chapitres INTEGER,
    PRIMARY KEY (id_auteur, num_isbn)
);

INSERT INTO Pays
VALUES ('France', 672051, 67064000),
       ('Italie', 301336, 66436000),
       ('Royaume-Uni', 242900, 60317000);

INSERT INTO Livre
VALUES (9782070349579, 'la peste', '2008-01-31'),
       (9782072730672, 'les misérables', '2017-06-29'),
       (9782072864537, 'notre-dame de paris', '2019-04-234'),
       (9782867465987, "d'acier", '2021-05-07'),
       (9782221133651, "et je t'emmène", '2015-05-15'),
       (9788806221898, 'accabadora', '2014-05-20'),
       (9791093835334, 'salvation', '2018-11-14'),
       (9782266121026, 'le silmarillion', '2003-11-20'),
       (9781093798357, 'la chambre 13', '2013-01-13');

INSERT INTO Auteur
VALUES (1, 'France', 'Hugo', 'Victor', '1802-02-26'),
       (2, 'France', 'Camus', 'Albert', '1913-11-07'),
       (4, 'Italie', 'Avallone', 'Silvia', '1948-04-13'),
       (5, 'Italie', 'Ammaniti', 'Niccolo', '1966-09-25'),
       (6, 'Italie', 'Murgia', 'Michela', '1972-06-03'),
       (7, 'Royaume-Uni', 'Hamilton', 'Peter', '1960-03-02'),
       (8, 'Royaume-Uni', 'Tolkien', 'John', '1892-01-03'),
       (9, 'Royaume-Uni', 'Rhode James', 'Montague', '1862-08-01');

INSERT INTO Ecrire
VALUES (1, 9782072730672, 0),
       (1, 9782072864537, 0), -- 1 apparaît 2 fois.
       (2, 9782070349579, 0),
       (4, 9782867465987, 0),
       (5, 9782221133651, 0),
       (6, 9788806221898, 0),
       (7, 9791093835334, 0),
       (8, 9782266121026, 0),
       (9, 9781093798357, 0),
       (8, 9781093798357, 0);
