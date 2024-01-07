---
title: Exercice 1 - Créer des fichiers et des répertoires
...

# Petit tutoriel

Comme les autres systèmes d'exploitation, Linux range les fichiers dans une
arborescence de répertoires. Voici quelques commandes utiles. Tapez-les une à une pour constater le résultat.

- `pwd` savoir où on est sur le disque (Print Working Directory)
- ```mkdir machin``` créer un nouveau répertoire nommé machin
- ```ls``` lister les fichiers et répertoires du répertoire courant
- ```cd machin``` entrer dans le répertoire machin (Change Directory)
- ```cd ..``` aller dans le répertoire "..", c'est-à-dire un étage plus haut
- ```touch bidule``` créer un fichier vide nommé bidule (ou change sa date d'accès si le fichier existe)
- ```rm bidule``` effacer le fichier bidule. Attention, c'est une opération irréversible.
- ```rmdir machin``` effacer le répertoire machin (il faut qu'il soit
  vide). On peut aussi utiliser ```rm -r machin``` pour effacer
  récursivement ```machin``` et tout son contenu.
- ```clear``` permet d'effacer l'écran pour nettoyer.

Au besoin, lisez la documentation de ces commandes avec par exemple
```man ls``` ('q' pour quiter cette aide).

Sachez aussi que :

- les touches ↑ et ↓ du clavier permettent de naviguer dans l'historique des commandes déjà tapées
- la touche ↹ (tabulation) permet de compléter un nom de fichier

# Au travail

Il s'agit maintenant de créer l'aborescence suivante.

```
📁 EXO
├── 📁 dir1
│    └── 📁 dir2
│         └── 🖹 doc1
└── 📁 dir3
    └── 🖹 doc2
```

Les logos sont juste là pour l'explication, les noms de fichiers et
répertoires ne doivent contenir que des lettres et des chiffres dans
cet exercice. 

Le répertoire au sommet est l'endroit où commence
l'exercice, noté `EXO`.

Pour commencer l'exercice, dans le terminal, entrez ``bash 01_start``


Coincé? Utilisez la commande ```ls -R``` pour afficher
*récursivement* le contenu de tous les répertoires.

Si c'est plus grave, tapez ``cd`` pour revenir au répertoire de départ et ``bash 01_start`` pour tout recommencer.

Lorsque vous avez terminé, tapez ``bash 01_verif`` pour vérifier et passer à l'exercice suivant.

[Continuer avec l'exercice 2](02.html)
