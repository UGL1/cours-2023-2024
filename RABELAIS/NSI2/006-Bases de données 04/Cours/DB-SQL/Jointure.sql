DROP TABLE IF EXISTS T1;
CREATE TABLE T1 (
	couleur	TEXT PRIMARY KEY,
    temps_sechage INTEGER
);

DROP TABLE IF EXISTS T2;
CREATE TABLE T2 (
    objet   TEXT PRIMARY KEY,
	color	TEXT REFERENCES T1(couleur) ON UPDATE CASCADE ON DELETE CASCADE
	
);


INSERT INTO T1 VALUES 
 ('bleu',3),
 ('rouge',2),
 ('vert',2),
 ('noir',1);


INSERT INTO T2 VALUES 
 ("chapeau", 'bleu'),
 ("pantalon", 'bleu'),
 ("tee-shirt",'rouge'),
 ("sweater", "noir");

COMMIT;
