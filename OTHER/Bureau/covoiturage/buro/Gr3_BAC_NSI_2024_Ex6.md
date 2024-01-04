# Exercice 6 (8 points)

*Cet exercice porte sur les schémas relationnels, les bases de données, le langage SQL, la programmation orientée objet
et le langage Python.*

L’énoncé de cet exercice utilise tout ou partie des mots suivants du langage SQL :
`SELECT, FROM, WHERE, JOIN ON, INSERT INTO, VALUES, COUNT, ORDER BY, DELETE, UPDATE, SET, AVG, LIKE`.

Les types de données sont les suivants :

`TEXT` pour les chaînes de caractères ;
`INTEGER` pour les nombres entiers ;
`REAL` pour les nombres non entiers ;
`DATETIME` pour les dates, au format `AAAA-MM-JJ HH:MM:SS`.

Sarah, étudiante en informatique à l'université, décide de mettre au point sa propre application de covoiturage qui
permettrait aux étudiants d'organiser leurs trajets pour venir assister aux cours, puis rentrer chez eux.
Elle interroge donc ChatGPT et entre : *Donne-moi un modèle de base de données pour le covoiturage*.

Voici le modèle « brut » que ChatGPT propose :

```
Table "Utilisateurs" :
    - ID (identifiant unique)
    - Nom
    - Prénom
    - Adresse e-mail
    - Mot de passe
    - Numéro de téléphone
    - Autres informations utilisateur (âge, photo de profil, etc.)

Table "Trajets" :
    - ID (identifiant unique)
    - ID de l'utilisateur conducteur (clé étrangère faisant référence à la table "Utilisateurs")
    - Lieu de départ
    - Lieu d'arrivée
    - Date et heure de départ
    - Nombre de places disponibles
    - Prix par passager
    - Informations supplémentaires sur le trajet (étapes intermédiaires, flexibilité des horaires, etc.)

Table "Réservations" :
    - ID (identifiant unique)
    - ID de l'utilisateur passager (clé étrangère faisant référence à la table "Utilisateurs")
    - ID du trajet réservé (clé étrangère faisant référence à la table "Trajets")
    - Statut de réservation (confirmée, en attente, annulée, etc.)

Table "Avis" :
    - ID (identifiant unique)
    - ID de l'utilisateur émetteur de l'avis (clé étrangère faisant référence à la table "Utilisateurs")
    - ID de l'utilisateur recevant l'avis (clé étrangère faisant référence à la table "Utilisateurs")
    - ID du trajet associé à l'avis (clé étrangère faisant référence à la table "Trajets")
    - Note attribuée (sur une échelle de 1 à 5)
    - Commentaire
```

Sarah reprend ces informations et rédige le début du modèle relationnel en respectant les consignes suivantes :

- un symbole `*` indique une clé primaire ;
- un symbole `#` indique une clé étrangère, faisant référence à une clé primaire du même nom dans une autre table.

```
Utilisateur(    
    *id_util        NUM,
    nom             TEXT,
    prenom          TEXT,
    mail            TEXT, 
    mdp             TEXT,
    tel             TEXT,
    infos           TEXT)

Trajet( 
    *id_traj        NUM, 
    #id_util        NUM, -- référence à Utilisateur.id_util
    ville_dep       TEXT, 
    ville_arr       TEXT, 
    date_dep        DATETIME, 
    nb_places       NUM, 
    prix_place      NUM, 
    infos           TEXT)   

Reservation(
    *id_res         NUM,
    #id_util        NUM, -- référence à Utilisateur.id_util
    #id_traj        NUM, -- référence à Trajet.id_traj
    statut          TEXT)
```

Elle s'aperçoit que dans ce modèle, l'attribut `statut` de `Reservation` peut *a priori* prendre toutes les valeurs.

1. Donner le type de la contrainte à ajouter à l'attribut `statut` pour restreindre ses valeurs possibles aux seules
   valeurs `en attente`, `confirmée` ou `annulée`.

2. Compléter le modèle relationnel donnant le schéma de la relation `Avis` en respectant les conventions d'écritures
   ci-dessus.

3. Donner la requête SQL permettant d'obtenir toutes les notes obtenues par l'utilisateur.trice dont l'identifiant est
   45.

Sarah aimerait utiliser un service de messagerie instantanée pour envoyer par SMS des rappels aux utilisateurs
lorsqu'ils ont un trajet prévu.
Or, elle s'aperçoit que certains utilisateurs ont un numéro de téléphone fixe : il commence par 02, contrairement aux
utilisateurs de portables qui ont un numéro commençant par 06 ou 07.

4. Ecrire une requête permettant à Sarah de récupérer les emails de tous les utilisateurs qui ont indiqué un numéro de
   téléphone fixe.


L'utilisateur 34 a oublié son mot de passe, Sarah décide de le réinitialiser à `12345678`.

5. Écrire la requête qu'il a écrite pour faire cela.

6. Donner la requête SQL permettant d'obtenir les destinations de tous les trajets effectués par Jean Dupont (on suppose
   qu'il n'y a qu'un seul Jean Dupont dans la base de données).


Un ami de Sarah qui suit des cours de cybersécurité se penche sur son projet. Il lui annonce qu'il y a une faille de
sécurité très grossière au niveau de la relation `Utilisateur`.

7. Expliquer d'où vient la faille et comment il faudrait la corriger (pour la suite de l'exercice, on ne fera pas cette
   correction pourtant impérative).

Sarah a réécrit son application avec un *Framework* Python dédié aux applications web. Celui-ci permet d'interagir
avec la base de données sans utiliser SQL : les tables sont accessibles *via* des objets dont les attributs sont les
colonnes de chaque table. On peut également modifier les objets du moment qu'on respecte les contraintes d'intégrité de
la base.
Ce procédé s'appelle l'ORM (*Object-Relational Mapping* en anglais).

Par exemple, la table `Utilisateur` est accessible *via* l'objet `utilisateur`, et pour afficher les utilisateurs dont
le nom de famille est `Dupont`

```
for u in utilisateur:
    if u.nom == "Dupond":
        print(u)
```

Pour connaître le nombre d'utilisateurs, il suffit d'évaluer `len(utilisateur)`.

Pour afficher les identifiants de trajets de toutes les personnes prénommées `Jean`, on écrit :

```
for u in utilisateur:
    for t in trajet:
        if t.id_util == u.id_util:  # revient à faire la jointure
            if u.prenom == `Jean`:
                print(u.id_util)
```

Certains utilisateurs ont la fâcheuse tendance d'annuler très souvent leur trajet. Par souci de performance, Sarah
aimerait
récupérer la liste des identifiants des utilisateurs qui ont annulé au moins 75% de leurs trajets pour leur envoyer un
mail
d'avertissement. Il commence par comptabiliser les trajets et les trajets annulés de chaque utilisateur à l'aide du code
suivant

```
# Crée deux dictionnaires dont les clés sont les id des utilisateurs et les valeurs zéro
nb_trajets = {u.id_util: 0 for u in utilisateurs}
nb_annulations = {u.id_util: 0 for u in utilisateurs}

for t in trajet :
    nb_trajets[... ] += 1
    if t.statut == "annulé":
        ...
```

8. Compléter le code ci-dessus.

Sarah peut maintenant récupérer sa liste.

9. Écrire un script qui permet d'avoir les identifiants des qui ont annulé au moins 75% de leurs trajets dans une liste
   appelée `liste_probleme`





