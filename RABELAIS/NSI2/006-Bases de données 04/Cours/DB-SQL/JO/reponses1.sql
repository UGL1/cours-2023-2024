-- Q1:
-- SELECT nom,prenom FROM Sportif;

-- Q2:
-- SELECT DISTINCT cio FROM Sportif 
-- ORDER BY cio ASC;

-- Q3:
-- SELECT nom FROM Sportif
-- WHERE cio = "FRA";
-- 
-- Q4:
-- SELECT * FROM Discipline
-- ORDER by id_sport ASC;

-- Q5:
-- SELECT nom FROM Pays
-- WHERE "France" < nom AND nom < "Russia";

-- Q6:
-- SELECT DISTINCT id_disc FROM Avoir_lieu
-- WHERE date_evenement BETWEEN "2012-07-27" AND "2012-07-31";

-- Q7:
-- SELECT nom FROM Sportif
-- WHERE cio = "FRA" OR cio="GBR";

-- Q8:
-- SELECT nom_disc FROM Discipline
-- WHERE nom_disc LIKE "%WOMEN%";

-- Q9:
-- SELECT nom FROM Pays
-- WHERE iso2 IS NULL OR iso3 IS NULL;

-- Q10:
-- SELECT nom, prenom FROM Sportif
-- WHERE sexe IS NOT NULL;

-- Q11:
-- SELECT COUNT(*)
-- FROM Sport;

-- Q12:
-- SELECT COUNT(*) 
-- FROM Discipline
-- WHERE id_sport = 1;

-- Q13:
-- SELECT COUNT(DISTINCT nom)
-- FROM Sportif;

-- Q14:
-- SELECT COUNT(*) FROM Pays
-- WHERE iso2 IS NULL;

-- Q15:
-- SELECT COUNT(*) FROM Gagner
-- WHERE medaille = "G";

-- Q16:
-- SELECT MIN(date_evenement), MAX(date_evenement)
-- FROM Avoir_lieu;

-- OU BIEN

-- SELECT DISTINCT id_disc, date_evenement
-- FROM Avoir_lieu
-- WHERE date_evenement IN(
-- 	SELECT MAX(date_evenement)
-- 	FROM Avoir_lieu)
-- 	OR date_evenement IN(
-- 	SELECT MIN(date_evenement)
-- 	FROM Avoir_lieu)
-- 	ORDER by date_evenement;

-- Q17

SELECT Sportif.nom, prenom FROM Sportif
JOIN Pays on Pays.cio = Sportif.cio
WHERE Pays.region = "Europe";

-- Q18

SELECT Discipline.nom_disc FROM Discipline
JOIN Sport on Sport.id_sport = Discipline.id_sport
WHERE Sport.nom_sport="ATHLETICS";

-- Q19

SELECT DISTINCT date_evenement
FROM Avoir_lieu
    JOIN Discipline on Discipline.id_disc = Avoir_lieu.id_disc
         JOIN Sport on Discipline.id_sport = Sport.id_sport
WHERE nom_sport ='ATHLETICS';

-- Q20

SELECT nom,prenom,medaille from Sportif
JOIN Gagner ON Sportif.id_sportif = Gagner.id_sportif
WHERE sexe IS NOT NULL ;

-- Q21:

SELECT * from Sportif
join Pays on Pays.cio=Sportif.cio
join Gagner on Gagner.id_sportif = Sportif.id_sportif
where Pays.nom="France" and Gagner.medaille = "G";

-- Q22:

-- SELECT  nom,prenom, nom_sport,nom_disc from Sportif
-- join Gagner  on Sportif.id_sportif = Gagner.id_sportif
-- join Discipline  on Discipline.id_disc = Gagner.id_disc
-- join Sport on Discipline.id_sport = Sport.id_sport
-- where medaille = "G"
