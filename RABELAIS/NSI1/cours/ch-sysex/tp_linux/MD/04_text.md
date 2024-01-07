---
title: Exercice 4 - Lire le contenu des fichiers
...


Commencez donc par un petit ``bash 04_start``.


Il existe de nombreuses commandes pour afficher le contenu des
fichiers à l'écran. La plus simple est ```cat fichier```,
qui affiche le contenu du fichier sur la console. 

Si on affiche un fichier contenant non pas du texte mais du binaire,
on peut avoir des résultats surprenants: 
```cat fichier-binaire``` affiche un fichier peu
intelligible en l'état. Si votre terminal est ... dérangé après un tel
affichage, il suffit de taper ```reset``` pour tout
réinitialiser. 

Si le fichier est plus long, cette méthode permet assez facilement de
voir la fin du contenu. C'est déjà ça. Par exemple, 
```cat fichier_long``` risque de vous remplir l'écran. Et
si on demande à afficher un programme binaire, c'est long ET illisible
à priori: ```cat /bin/cat``` affiche le programme cat
lui-même. 

Si on veut voir le début d'un fichier, on peut utiliser la commande 
```head fichier_long``` qui n'affiche que les premières
lignes du fichier passé. On peut aussi préciser que l'on veut les 50
premières lignes avec l'option ``-n``: ```head -n 50 fichier_long```

De même, la commande ```tail -n 10 fichier_long``` permet
d'afficher les 10 dernières lignes d'un fichier long.
Enfin, la commande ```less fichier_long``` permet
de se promener dans l'affichage d'un fichier : la navigation se fait avec
les mêmes raccourcis que le manuel (le manuel appelle ``less`` en interne).
Pour rappel : les flèches et page vers le haut/bas permettent de se déplacer
dans le fichier, `q` quitte le programme et on voit l'aide avec `h`.

## But de l'exercice

Pour passer à la suite, il suffit de trouver différents mots de passe,
répartis dans différents fichiers du répertoire. 

Normalement ``Ctrl-C`` ne fonctionne pas dans le terminal et il faut
sélectionner à la souris puis faire ``Ctrl-Inser`` pour copier, et
``Shift-Inser`` pour coller. 

**Ceci dit, dans CoCalc, les développeurs ont eu la bonne idée d'autoriser également les bons vieux ``CTRL+C`` pour copier et 
``CTRL+V`` pour coller, donc il ne faut pas vous en priver.**

Bien entendu, il est presque impossible de taper la bonne commande,
juste du premier coup. On pourrait la copier/coller depuis juste au
dessus avec ``Ctrl+Inser`` et ``Shift+Inser``, mais ce serait affreusement
lent et frustrant. Il y a bien mieux : on peut retrouver les commandes
qu'on vient d'écrire simplement avec les flèches haut/bas et les
modifier. 

En fait, le terminal est un truc de fainéants où tout est fait pour
vous simplifier la vie, vous allez voir. Vous avez la flemme de
chercher manuellement dans l'historique la ligne où vous utilisez
``head``? Tapez simplement ``Ctrl-R`` pour passer en mode recherche, et
écrivez ``head``. Le shell va fouiller l'historique pour vous. Appuyez
sur ``Entrée`` quand vous l'avez trouvé. Essayez aussi d'utiliser les
flèches pendant/après la recherche ou de refaire ``Ctrl-R`` en cours de
recherche: c'est assez bien fait. 


1. Quel est le contenu du fichier `mot-de-passe` ?


2. Quelle information se cache à la fin du fichier `cache-cache-passe` ?


3. Quelle information se cache au début du fichier `cache-cache-passe` ?


4. Quelle information se cache un peu après le début du fichier `cache-cache-passe` ?


5. Quelle information se cache vers le milieu du fichier `cache-cache-passe` ?



Vous ne trouvez pas les informations ? Essayez avec les commandes
``cat``, ``head`` et ``less``.


[Continuer avec l'exercice 5](05.html)