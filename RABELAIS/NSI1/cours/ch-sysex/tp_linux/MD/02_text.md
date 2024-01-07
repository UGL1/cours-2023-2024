---
title: Exercice 2 - Renommer et déplacer
...

Nous avons vu quelques commandes pour se déplacer sur le disque et
pour créer des fichiers et répertoires. Pour ne pas les oublier,
imprimez le [pense-bête du shell](https://framagit.org/mquinson/C-2nd-language/raw/master/refcard/refcard-shell.pdf?inline=false).

Dans cet exercice, nous allons apprendre à déplacer des fichiers.

## Petit tutoriel

Pour commencer, dans le terminal, entrez ``bash 02_start``

Utilisez la commande ```tree``` pour voir la situation
initiale.

La commande `mv` permet de déplacer (MoVe) des fichiers et
répertoires. Sa syntaxe est très facile : De base, 
```mv toto bidule``` permet de renommer le fichier `toto` en `bidule`.
Cela marche aussi si `toto` est un répertoire. Vérifiez le résultat
avec la commande ```tree```.

Si le second paramètre de la commande `mv` existe, ça doit être un
répertoire dans lequel le premier paramètre est déplacé. Par exemple
```mv bidule dir1``` déplace le fichier `bidule` dans le
répertoire `dir1`. Vérifiez l'état courant avec 
```tree``` ou ```ls -R``` (listing récursif).

Enfin, si vous passez plus de deux paramètres à la commande `mv`, tous
ceux du début de la ligne sont déplacés dans le répertoire indiqué en
dernier paramètre. Par exemple ```mv machin dir1/bidule truc``` déplace les fichiers `machin` et `dir1/bidule`
(c'est-à-dire le fichier `bidule` placé dans `dir1`) dans le
répertoire `truc`. Vérifiez l'état actuel avec ```tree```.

La commande `mv`, comme beaucoup d'autres, accepte beaucoup de
paramètres intéressants. Par exemple `mv -i [paramètres habituels]`
passe en mode interactif : vous devez confirmer chaque opération qui écrase
un fichier existant.
Consultez le manuel de cette commande en tapant
```man mv```.

# Au travail

Si vous avez bien suivi le tutoriel, votre arborescence devrait être la suivante:
```
📁 EXO
├── 📁 dir1
│    └── 📁 dir2
│         └── 🖹 doc1
└── 📁 dir3
    └── 🖹 doc2
```

L'objectif est de renommer tous les éléments pour les mettre en
majuscule, comme suit. Il n'est pas possible de juste recréer
l'arborescence, car le contenu des fichiers doc1 et doc2 doit être
préservé.

```
📁 EXO
├── 📁 DIR1
│    └── 📁 DIR2
│         └── 🖹 DOC1
└── 📁 DIR3
    └── 🖹 DOC2
```

Coincé? Utilisez la commande ```tree``` pour afficher récursivement
le contenu de tous les répertoires. 

Si c'est plus grave, tapez ``cd`` pour revenir au répertoire de départ et ``bash 02_start`` pour tout recommencer.

Lorsque vous avez terminé, tapez ``bash 02_verif`` pour vérifier et passer à l'exercice suivant.

[Continuer avec l'exercice 3](03.html)