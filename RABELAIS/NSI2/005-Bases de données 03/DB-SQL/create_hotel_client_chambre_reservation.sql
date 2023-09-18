DROP TABLE IF EXISTS Hotel;
CREATE TABLE Hotel
(
    nom_hotel TEXT NOT NULL PRIMARY KEY,
    adresse   TEXT NOT NULL
);

INSERT INTO Hotel
VALUES ('hotel1', 'adresse1'),
       ('hotel2', 'adresse2');


DROP TABLE IF EXISTS Chambre;
CREATE TABLE Chambre
(
    num_ch    INTEGER PRIMARY KEY,
    prix      INTEGER NOT NULL,
    nom_hotel TEXT REFERENCES Hotel (nom_hotel) ON UPDATE CASCADE ON DELETE CASCADE
);
INSERT INTO Chambre
VALUES (1, 50, 'hotel1'),
       (2, 100, 'hotel1'),
       (3, 50, 'hotel2'),
       (4, 100, 'hotel2');

DROP TABLE IF EXISTS Client;
CREATE TABLE Client
(
    num_client INTEGER PRIMARY KEY,
    nom_client TEXT NOT NULL
);
INSERT INTO Client
VALUES (1, 'Dupont'),
       (2, 'Durand');

DROP TABLE IF EXISTS Reservation;
CREATE TABLE Reservation
(
    num_resa    INTEGER PRIMARY KEY,
    date_resa   TEXT NOT NULL,
    num_client  TEXT REFERENCES Client (num_client) ON DELETE CASCADE ON UPDATE CASCADE,
    num_chambre INTEGER REFERENCES Chambre (num_ch) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO Reservation VALUES (209,'2020-01-01',1,3)
