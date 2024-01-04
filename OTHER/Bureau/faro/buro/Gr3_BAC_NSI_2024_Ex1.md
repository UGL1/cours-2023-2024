# EXERCICE 1 (6 points)

*Cet exercice porte sur la programmation Python, la programmation orientée objets, les tests et la structure de données
pile.*

Le *mélange faro* consiste à partager un jeu de cartes en deux moitiés et intercaler les cartes des deux moitiés.
On suppose que le nombre de cartes est pair.

Pour modéliser le jeu de cartes, on décide d'utiliser une pile qui sera une instance de la classe `Pile` dont voici un
exemple d'utilisation :

```
1 jeu = Pile() # crée une pile vide et la place dans jeu
2 jeu.empile(1) # empile la valeur 1
3 print(jeu.depile()) # dépile 1 et affiche cette valeur
4 print(jeu.est_vide()) # affiche True puisque la pile est vide
```

On appelle $n$ le nombre de cartes dans le jeu, on rappelle que $n$ est *pair*.
Le jeu de cartes est alors modélisé par une pile appelée `jeu` de sommet 1, puis 2 en dessous, *et cætera* jusqu'au bas
de la pile qui contient $n-1$, comme illustré sur la figure ci-dessous.

![Figure 1. Pile représentant un jeu de cartes](./images/Gr3_BAC_NSI_2024_Ex1_Fig1.png){width=200px}

Le mélange faro est réalisé ainsi :

**Étape 1** : on dépile la moitié de `jeu` dans une deuxième pile appelée `moitie1`.

**Étape 2** : on dépile le reste de `jeu` dans une troisième pile appelée `moitie2`.

**Étape 3** : on empile alternativement et dans cet ordre un élément de `moitie1` puis un élément de `moitie2` jusqu'à
vider les 2 piles.

Dans l'exemple suivant les contenus initiaux de `jeu`, `moitie1` et `moitie2` sont représentés ci-dessous :

![Figure 2. Contenus initiaux des 3 piles](./images/Gr3_BAC_NSI_2024_Ex1_Fig2.png){width=600px}

1. Représenter sur votre copie les contenus de ces trois piles à la fin de chaque étape du mélange faro.

Voici le code de la fonction `produire_jeu` qui

- en entrée prend un entier `n` supposé pair ;
- renvoie une instance de la classe `Pile` qui représente le jeu de cartes.

```
1 def produire_jeu(n: int) -> Pile:
2     resultat = Pile()
3     for i in range(n, ...):
4         resultat.empile(...)
5     return resultat
```

2. Recopier et compléter sur votre copie le code de la fonction `produire_jeu`.

Ci-dessous figure le code de la fonction `scinder_jeu` qui

- en entrée prend
    - une instance de la classe `Pile` qui est le jeu que l'on veut partager en 2 moitiés ;
    - un entier `n` qui est la taille de la pile.
- renvoie 2 piles qui sont les deux moitiés du jeu.
```
1 def scinder_jeu(p, n):
2   m1 = Pile()
3   m2 = Pile()
4   for i in range(n):
5       m1.empile(p.depile())
6   for i in range(n):
7       m2.empile(p.depile())
8   return m1, m2
```
3. Ce code comporte des erreurs. Indiquer les numéros de lignes à rectifier ainsi que les rectifications à apporter.

La fonction `recombiner`

- prend en entrée deux instances `m1` et `m2`de la classe `Pile` qui sont respectivement la première et la deuxième
  moitié d'un jeu de cartes ;
- renvoie une instance de la classe `Pile` qui est le jeu obtenu en y empilant alternativement et dans cet ordre les
  éléments de `m1` et de  `m2`.

4. Écrire le code de la fonction `recombiner`.

On veut maintenant écrire le code de la fonction `faro` qui

- en entrée prend
    - une instance de la classe `Pile` qui est le jeu que l'on veut mélanger ;
    - un entier `n` qui est la taille de la pile.
- ne renvoie rien mais mélange le jeu en appliquant le mélange faro.

5. Écrire le code de la fonction `faro`.

Un résultat de mathématiques assure qu'étant donné un jeu de n cartes (n pair), en répétant suffisamment de fois le
mélange faro, on finira par remettre le jeu dans l'ordre initial.
On aimerait trouver, pour un entier n donné, ce nombre minimal de répétitions nécessaires. Pour cela, on utilisera une
fonction `identiques` qui

- en entrée prend 2 instances de la classe `Pile` ;
- renvoie `True` si ces deux piles ont les mêmes éléments, en même nombre et dans le même ordre, et False sinon.

La fonction `identiques` ne modifie pas les piles données en entrée.

Pour s'assurer que la fonction `identiques` fonctionne correctement, on a commencé à produire un jeu de tests :

```
1 p1 = Pile()
2 p1.empile(1)
3 p2 = Pile()
4 assert identiques(p1, p2) == False
```

6. Compléter ce jeu de tests.

On veut finalement écrire la fonction `ordre_faro` qui

- en entrée prend un entier n ;
- renvoie le plus petit nombre de répétitions du mélange faro pour qu'un jeu de n cartes soit remis dans son ordre
  initial.

7. Écrire le code de la fonction `faro`.

