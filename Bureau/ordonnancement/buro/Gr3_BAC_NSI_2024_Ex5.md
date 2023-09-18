# EXERCICE 5 (6 points)


Cet exercice porte sur la programmation Python, la programmation orientée objet, les structures de données (file), l'ordronnancement et l'interblocage.* 

On s’intéresse aux processus et à leur ordonnancement au sein d’un système d’exploitation. On considère ici qu’on utilise un monoprocesseur.

1. Citer les 3 états dans lesquels un processus peut se trouver.

On veut simuler cet ordonnancement avec des objets.
Pour ce faire, on dispose déjà de la classe `Processus` dont voici la documentation :

**Classe Processus**:
```
p = Processus(nom: str, duree: int)
    Crée un processus de nom <nom> et de durée <duree> (exprimée en cycles d'ordonnancement)

p.execute_un_cycle()
    Exécute le processus donné pendant un cycle.

p.est_fini()
    Renvoie True si le processus est terminé, False sinon.
```

Pour simplifier, on ne s'intéresse pas aux ressources qu'un processus pourrait acquérir ou libérer.

2. Citer les seuls 2 états possibles pour un processus dans ce contexte.

Pour mettre en place l'ordonnancement, on décide d'utiliser une file, instance de la classe `File` ci-dessous.

**Classe File**
```
1  class File:
2      def __init__(self):
3          """ Renvoie une file vide """
4          self.contenu = []
5  
6      def enfile(self, element):
7          """ Enfile element dans la file """
8          self.contenu.append(element)
9
10     def defile(self):
11         """ Renvoie le premier élément de la file """
12         return self.contenu.pop(0)
13
14     def est_vide(self):
15         """ Renvoie True si la file est vide, False sinon """
16         return self.contenu == []
```

Lors de la phase de tests, on se rend compte que le code suivant produit une erreur :

```
1 f = File()
2 print(f.defile())
```

3. Rectifier sur votre copie le code de la méthode `defile` pour que le test précédent ne produise plus d'erreur.

On se propose d'ordonnancer les processus avec une méthode du type *tourniquet* dont le principe est le suivant :
à chaque cycle 
- si un nouveau processus est créé, il est mis dans la file d'attente ;
- ensuite, on défile un processus de la file d'attente et on l'exécute pendant un cycle ;
- si le processus exécuté n'est pas terminé, on le replace dans la file.

Par exemple, avec les processus suivants

+:------------------------------------------------:+
| Liste des processus                              |
+:=========:+:=================:+:================:+
| processus | cycle de création | durée en cycles  |
+-----------+-------------------+------------------+
|    A      |         2         |        3         |
+-----------+-------------------+------------------+
|    B      |         1         |        4         |
+-----------+-------------------+------------------+
|    C      |         4         |        3         |
+-----------+-------------------+------------------+
|    D      |         0         |        5         |
+-----------+-------------------+------------------+

On obtient le chronogramme ci-dessous :

![Figure 1. Chronogramme pour les processus A, B, C et D](./images/Gr3_BAC_NSI_2024_Ex5_Fig1.png){width=600px}

Pour décrire les processus et le moment de leur création, on utilise le code suivant, dans lequel `depart_proc` associe à un cycle donné le processus qui sera créé à ce moment :

```
1 p1 = Processus("p1", 4)
2 p2 = Processus("p2", 3)
3 p3 = Processus("p3", 5)
4 p4 = Processus("p4", 3)
5 depart_proc = {0: p1, 2: p2, 1: p3, 3: p4}
```

4. Recopier et compléter sur votre copie le chronogramme ce-dessous pour les processus `p1`, `p2`, `p3` et `p4`.

![Figure 2. Chronogramme pour les processus p1, p2, p3 et p4](./images/Gr3_BAC_NSI_2024_Ex5_Fig2.png){width=600px}

Pour mettre en place l’ordonnancement suivant cette méthode, on écrit la classe Ordonnanceur dont voici un code incomplet :

```
1  class Ordonnanceur:
2  
3      def __init__(self):
4          self.temps = 0
5          self.file = File()
6  
7      def ajoute_nouveau_processus(self, proc):
8          ...
9  
10     def tourniquet(self):
11         self.temps = ...
12         if not self.file.est_vide():
13             proc = ...
14             ...
15             if not proc.est_fini():
16                 ...
17             return proc.nom
18         else:
19             return None
```

5. Compléter le code ci-dessus.

À chaque appel de la méthode `tourniquet` celle-ci renvoie ou bien le nom du processus qui a été élu, ou bien `None` si elle n'a pas trouvé de processus en cours.

6. Écrire un programme qui
- utilise les variables `p1`, `p2`, `p3`, `p4` et `depart_proc` définies précédemment ;
- crée un ordonnanceur ;
- ajoute un nouveau processus à l'ordonnanceur lorsque c'est le moment ;
- affiche le processus choisi par l'ordonnanceur ;
- s'arrête lorsqu'il n'y a plus de processus à exécuter.

Dans la situation donnée en exemple, il s'avère qu'en fait, les processus utilisent des ressources :
- un fichier commun aux processus ;
- le clavier de l'ordinateur ;
- le processeur graphique (GPU) ;
- le port 25000 de la connexion Internet.

Voici le détail de ce que fait chaque processus :

+:-----------------------------------------------------------------------------------:+
| Liste des processus                                                                 |
+:==================:+:====================:+:=================:+:===================:+
|         A          |          B           |        C          |         D           |
+--------------------+----------------------+-------------------+---------------------+
|  acquérir le GPU   | acquérir le  clavier | acquerir le port  | acquérir le fichier |
+--------------------+----------------------+-------------------+---------------------+
| faire des calculs  |  aquérir le fichier  | faire des calculs |  faire des calculs  |
+--------------------+----------------------+-------------------+---------------------+
|   libérer le GPU   | libérer le clavier   | libérer le port   | acquérir le clavier |
+--------------------+----------------------+-------------------+---------------------+
|                    |  libérer le fichier  |                   | libérer le clavier  |
+--------------------+----------------------+-------------------+---------------------+
|                    |                      |                   | libérer le fichier  |
+--------------------+----------------------+-------------------+---------------------+

7. Montrer que l'ordre d'exécution donné en exemple aboutit à une situation d'interblocage.

