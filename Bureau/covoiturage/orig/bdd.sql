CREATE TABLE Utilisateur
(
    id_util INTEGER PRIMARY KEY,
    nom     TEXT,
    mail    TEXT,
    prenom  TEXT,
    mdp     TEXT,
    tel     TEXT,
    infos   TEXT
);

CREATE TABLE Trajet
(
    id_traj    INTEGER PRIMARY KEY,
    id_util    INTEGER REFERENCES Utilisateur (id_util),
    ville_dep  TEXT,
    ville_arr  TEXT,
    date_dep   TEXT,
    nb_places  INTEGER,
    prix_place NUMERIC,
    infos      TEXT
);

CREATE TABLE Reservation
(
    id_res  INTEGER PRIMARY KEY,
    id_util INTEGER REFERENCES Utilisateur (id_util),
    id_traj INTEGER REFERENCES Trajet (id_traj),
    statut  TEXT CHECK (statut in ('en attente', 'en cours', 'terminé', 'annulé'))
);

CREATE TABLE Avis
(
    id_avis     INTEGER PRIMARY KEY,
    id_emetteur INTEGER REFERENCES Utilisateur (id_util),
    id_receveur INTEGER REFERENCES Utilisateur (id_util),
    note        INTEGER,
    infos       TEXT
);



