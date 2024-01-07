---
title: Exercice 5 - Trouver des fichiers
...

Vous avez l'habitude, maintenant : ``bash 05_start``.

Il arrive souvent qu'on ait besoin de retrouver un fichier sur son
disque. Deux commandes sont bien pratiques en pareille situation.

La commande ``locate`` **qui n'est pas installée sur CoCalc** utilise une base de données des fichiers sur
disque et permet de retrouver très rapidement un fichier par son nom.
Le défaut est qu'il faut que le fichier soit là depuis assez longtemps
pour qu'il ait été indexé dans la base. Mais si vous cherchez un
fichier dont vous connaissez une partie du nom sans savoir du tout où
il se trouve, cette commande est faite pour vous. 

La commande ``find`` qui elle, en revanche, est installée sur CoCalc, permet de fouiller le disque de façon bien plus
approfondie. Par exemple, la commande ```find ddd -name "pas-la"```
cherche dans le répertoire ``ddd`` un fichier dont le nom est "pas-la"
(il y en a un, juste pour l'exemple).

## But de l'exercice

La commande ``find`` offre de nombreuses autres possibilités, que vous
pourrez découvrir en lisant la documentation avec ```man find```.
Cela vous permettra de répondre aux questions suivantes.

Comme précédemment, pas question de retaper la ligne de commande en
entier à chaque tentative. Soyez fainéants. Utilisez l'historique des
commandes.
Les informaticiens sont de grands fainéants prêts à tout pour faire
travailler l'ordinateur à leur place.

### Dans aaa

Un fichier nommé 'ici' se cache quelque part dans le répertoire 'aaa',
mais la commande ```tree``` n'aide pas beaucoup. Il va
falloir utiliser ``find``!


1. Que contient ce fichier 'ici'?

[reponse1]:<>(find aaa -name "ici")

### Dans bbb

Cette fois, on ne connaît même pas le nom du fichier. On sait juste
que c'est un fichier, et que le prédicat ``-type`` de ``find`` peut
nous aider.

Notez que pour chercher dans le manuel, il faut appuyer sur la touche
'/' après l'avoir ouvert avec ```man find```. Tapez ensuite
la chaîne à chercher (par exemple ``-type``) et entrée. On saute à
l'occurrence suivante avec 'n' (précédente avec 'N'), et on quitte le
manuel avec 'q'.


2. Que contient le fichier caché dans 'bbb'?

[reponse2]:<>(find bbb -type f)

### Dans ccc

Il y a maintenant une multitude de fichiers, et on cherche celui dont
la taille est supérieure à zéro. Les prédicats ``-size`` ou 
``-empty`` vont probablement nous rendre service, ainsi que les
connecteurs logiques ``-and``,``-or`` ou ``-not``, à vous de voir...


3. Que contient le fichier caché dans 'ccc'?

[reponse3]:<>(find ccc -type f -not -size 0 -exec cat {} \;) 

### Dans ddd

Cette fois, il y a une multitude de fichiers, et il faut utiliser celui
modifié plus récemment que le fichier ``timestamp`` placé à la racine de `EXO`.
Notez que c'est bien la date de dernière modification qui compte.



4. Que contient le fichier caché dans 'ddd'?

[reponse4]:<>(find ddd -type f -newer timestamp -exec cat {} \;)


[Continuer avec l'exercice 6](06.html)
