
/*
SELECT Sportif.nom,Sportif.prenom FROM Sportif
JOIN Gagner G on Sportif.id_sportif = G.id_sportif
JOIN Pays  on Sportif.cio = Pays.cio
WHERE medaille = 'G' AND Pays.nom ='France'
/*
/*
personnes qui ont gagné une médaille et dont on connait le sexe

SELECT nom,prenom,medaille from Sportif
JOIN Gagner ON Sportif.id_sportif = Gagner.id_sportif
WHERE sexe IS NOT NULL ;
*/


/*
Jours pendant lesquels un évènement lié à l'athlétisme eu lieu

SELECT DISTINCT date_evenement
FROM Discipline
    JOIN Avoir_lieu Al on Discipline.id_disc = Al.id_disc
         JOIN Sport on Discipline.id_sport = Sport.id_sport
WHERE nom_sport ='ATHLETICS'
ORDER BY nom_disc
 */

/*
Disciplines de l'athlétisme

SELECT nom_disc
FROM Discipline
         JOIN Sport on Discipline.id_sport = Sport.id_sport
WHERE nom_sport ='ATHLETICS'
ORDER BY nom_disc
 */
/*
Sportifs ayant obtenu une médaille d'or

SELECT  nom,prenom, nom_sport,nom_disc from Sportif
join Gagner G on Sportif.id_sportif = G.id_sportif
join Discipline D on D.id_disc = G.id_disc
join Sport S on D.id_sport = S.id_sport
where medaille ='G'
order by nom_sport;
 */