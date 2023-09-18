-- 4. Combien d’enregistrements possède la table Nobel ?

SELECT COUNT(*)
FROM Nobel;

-- 5. Dans quelle discipline Paul Krugman est-il devenu Prix Nobel ?

SELECT sujet
FROM Nobel
WHERE laureat = "Paul Krugman";



-- 6. En quelle année Albert Fert a-t-il eu le prix Nobel ?

SELECT annee
FROM Nobel
WHERE laureat = "Albert Fert";

-- 7. Comment afficher le nom de tous les lauréats en évitant les doublons ? (809 enregistrements)

SELECT DISTINCT laureat 
FROM Nobel;


-- 8. Comment afficher le nom de toutes les 
-- disciplines en évitant les doublons ? 

SELECT DISTINCT sujet
FROM Nobel;

-- 9. Quelle est la discipline de Wilhelm 
-- Conrad Röntgen ? (1 enregistrement)

SELECT sujet
FROM Nobel
WHERE laureat = "Wilhelm Conrad Röntgen";

-- 10. Dans quelle discipline Paul Krugman 
-- est-il devenu Prix Nobel ? (1 enregistrement)

SELECT sujet
FROM Nobel
WHERE laureat="Paul Krugman";

-- 11. En quelle année Albert Fert a-t-il eu le prix Nobel ? (1 enregistrement)

SELECT annee
FROM Nobel
WHERE laureat = "Albert Fert";

-- 12. Quelle est l’année de distinction de Pierre Curie ? (1 enregistrement)

SELECT annee
FROM Nobel
WHERE laureat="Pierre Curie";

-- 13. Quelle est l’année de distinction et la matière de Bertha von Suttner ? (1 enregistrement)

SELECT annee, sujet
FROM Nobel
WHERE laureat="Bertha von Suttner";

-- 14. Quels sont les lauréats distingués au XXI e siècle ? (97 enregistrements)

SELECT DISTINCT laureat
FROM Nobel
WHERE annee >= 2000;

-- 15. Quels sont les lauréats du prix Nobel de la Paix durant la deuxième guerre mondiale ?

SELECT laureat
FROM Nobel
WHERE annee BETWEEN 1939 AND 1945;
	AND sujet= "Paix";

-- 16. Quels sont les lauréats distingués en Médecine en 1901 et en 2001 ? (4 enregistrements)

SELECT laureat
FROM Nobel
WHERE annee = 1901 OR annee = 2001
	AND sujet ="Médecine";

-- 17. Quels sont les lauréats des prix nobel de Physique et de Médecine en 2008 ? (3

SELECT	laureat
FROM 	Nobel
WHERE 	(		
			sujet = "Physique"
		OR 	sujet = "Médecine"
		)
		AND	annee = 2008;

-- 1. Combien d’enregistrements au total comporte la table ? (816 enregistrements)

SELECT COUNT(*)
FROM Nobel;

-- 2. Combien de personnes ont reçu le prix Nobel de la paix ? (119 enregistrements)

SELECT COUNT(laureat) -- COUNT(*)
FROM Nobel
WHERE sujet="Paix";

-- 3. Combien de personnes ont reçu le prix Nobel de littérature ? (105 enregistrements)

SELECT	COUNT(*)
FROM	Nobel
WHERE	sujet="Littérature";
-- 4. Combien de personnes ont reçu le prix Nobel de mathématiques ? (0 enregistrements)

SELECT	COUNT(*)
FROM	Nobel
WHERE	sujet="Mathématiques";

-- 5. Combien de personnes ont reçu un prix Nobel en 1901 ? (6 enregistrements)

SELECT DISTINCT COUNT(laureat)
FROM Nobel
WHERE annee=1901;

-- 6. Combien de personnes ont reçu un prix Nobel de chimie en 1939 ? (2 enregistrements)

SELECT COUNT(laureat)
FROM Nobel
WHERE sujet="Chimie"
AND annee=1939;

-- 7. En quelle année a été décerné le premier prix Nobel d’économie ? (Réponse : 1969)

SELECT MIN(annee)
FROM Nobel
WHERE sujet="Economie";

-- 8. Combien de prix Nobel a reçu Marie Curie ? (Réponse : 2)
SELECT COUNT(*)
FROM Nobel
WHERE laureat="Marie Curie"

-- 9. Quels sont les prix lauréats, leur discipline et l’année de distinction de tous les prix
-- Nobel contenant cohen dans leur nom (on ne fera pas de distinction de casse) ? (2
-- enregistrements)
SELECT * 
FROM Nobel
WHERE laureat LIKE "%cohen%";

-- 10. Combien y a-t-il eu de lauréats en Physique et en Chimie ? (335 enregistrements)

SELECT DISTINCT COUNT(laureat)
FROM Nobel
WHERE sujet="Physique" OR sujet="Chimie";

-- 11. Combien y a-t-il eu de lauréats de Médecine et de littérature en 2000 ? (4 enregistrements)

-- 12. Nombre de lauréats différents parmi les prix Nobel de la paix ? (116 enregistrements)
-- Requêtes de mise à jour

-- 1. En 2019, Esther Duflo a reçu le prix Nobel d’économie. Écrivez la requête permettant
-- d’insérer cet enregistrement.

-- 2. Quelle requête permet de modifier l’enregistrement précédent pour accoler le nom
-- d’époux (Banerjee) après celui de Duflo ?

-- 3. De nombreuses pétitions circulent pour retirer le prix Nobel à Aung San Suu Kyi. Quelle
-- requête permettrait cela ?