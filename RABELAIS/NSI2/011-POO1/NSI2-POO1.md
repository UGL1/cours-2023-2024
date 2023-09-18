    \chapter{\large programmation[-1em]\fontsize{35pt}{42pt}\selectfont\titlefont POO - partie 1}
    \introduction{La POO c'est la classe !}
    

            -      Pour représenter des  entités qui ont des caractéristiques et des fonctionnalités communes, on fabrique  une *classe* qui décrit le modèle général que suit une entité;
            -      chaque entité qu'on crée suivant la classe s'appelle *une instance* de cette classe, c'est un *objet* qui a ses propres *membres* :
                -      ses variables, appelées *attributs*;
                -      ses propres fonctions, appelées *méthodes*.    
            -      la classe elle même peut avoir ses propres attributs et méthodes;
            -      les objets peuvent interagir entre eux, avec la classe et « avec l'extérieur».
        
    
        La *programmation orientée objet* (ou programmation objet, ou POO) est un *paradigme de programmation* qui pousse un peu plus loin la notion de modularité et d'encapsulation que nous avons déjà vue. 
        
    ## Un exemple simple et complet
    
    ### Pourquoi concevoir un objet ?
    On imagine qu'on veut représenter une liste de rectangles, chacun ayant ses propres dimensions. On peut les représenter par une liste de listes :
```python
rectangles=[
            [3, 4], 
            [5, 6], 
            [7, 8]
           ]
```
    Ce n'est pas très parlant. 
    Supposons maintenant qu'on veuille calculer la surface d'un rectangle. Avec des listes on écrira
```python
def area(rect : list)-> float :
    return rect[0]*rect[1]
```
    Ça marche, mais comme écrit précédemment, ce n'est pas très élégant et si on utilise cette méthode pour des structures plus complexes qu'un simple rectangle dans des programmes longs, on risque fort de finir par se tromper.
    
    On peut alors se dire qu'on va utiliser une liste de dictionnaires :
```python
rectangles=[
            {'width' : 3, 'height' : 4}, 
            {'width' : 5, 'height' : 6}, 
            {'width' : 7, 'height' : 8}
           ]
```

    C'est encore assez encombrant même si c'est mieux. Autant passer le cap et définir un objet.
    ### Créons la classe
    
    ```python
class Rectangle:

def __init__(self, w: float, h: float):
    self.width = w
    self.height = h
```
    
    On a donc défini une *classe* `#!python Rectangle` (les noms de classe commencent par des majuscules) à l'intérieur de laquelle on a défini la *méthode* `#!python __init__`.
    
        Une *classe* est un ensemble de membres.
        Un *membre* peut être une méthode ou un attribut.
        Une *méthode* est une fonction.
        Un *attribut* est une variable ou une constante.
    
    Cette méthode `#!python __init__` est spéciale, comme sa forme le laisse penser. En Python les méthodes spéciales sont entourées de 2 "_" de part et d'autre. Ces « doubles tirets bas » se disent *double underscore* en Anglais et on abrège souvent en *dunder*. `#!python __init__` peut donc se lire/dire *dunder init*.
    Cette méthode s'appelle le constructeur.
        Un constructeur est une méthode qui crée et renvoie un *objet*. On dit que cet objet est *une instance de la classe*.
    
    Dans le code de `#!python __init__`, on remarque que le premier paramètre s'appelle `#!python self` : il fait référence à l'objet que la méthode crée.
    À partir de 2 `#!python float`, ce constructeur instancie un objet de la classe `#!python Rectangle`. Cet objet possède 2 attributs : `#!python width` et `#!python height`. Voici comment on s'en sert :
    
>>> r1 = Rectangle(3,4)
>>> r1.width
3
>>> r1.height
4
>>>  r2 = Rectangle(5,6)
>>> r2.width
5
>>> r2.height
6
    On a crée 2 objets différents, chacun d'eux possède *les mêmes attributs* mais avec *des valeurs différentes*.
    
    ### Créons des méthodes
    
    On veut pouvoir calculer le périmètre et l'aire d'un rectangle, donc, toujours à l'intérieur de la classe, on définit les méthodes suivantes :
    
    ```python
def perimeter(self):
    return (self.width + self.height) * 2
        
def area(self):
    return self.width * self.height
```
    
    
    On peut maintenant les utiliser 
    
>>> r1.perimeter()
14
>>> r1.area()
>>> 12
        Il faut bien noter qu'on écrit `#!python r.perimeter()` *avec des parenthèses*, pour évaluer le résultat de cette méthode . Sans parenthèses, on fait référence à la méthode elle-même.
    D'ailleurs certaines méthodes requièrent un ou plusieurs paramètres, comme par exemple celle-ci :
    
    ```python
def rescale_by_factor(self, f: float):
    self.width *= f
    self.height *= f
        ```
    Cette méthode sert à redimensionner le rectangle. Il faut remarquer que quand une méthode s'applique à une instance de la classe, alors son premier paramètre *doit impérativement* être `#!python self`.
    
>>> r1.rescale_by_factor(10)
>>> r1.width
30
>>> r1.height
40
    
    ### Différence entre classe et instance
    
            -      Un *attribut d'instance* est une variable attachée à chaque instance de la classe. Deux instances différentes peuvent donc très bien présenter des valeurs différentes pour cet attribut.
            Un *attribut de classe* est une variable qui n'est pas directement liée aux instances de la classe mais à la classe elle-même.
            -      De la même manière on distingue les *méthodes d'instances* des * méthodes de classe* : on peut dire qu'une méthode d'instance prend cette instance en paramètre (c'est ce fameux `#!python self`) alors qu'une méthode de classe non.
    
    Redéfinissons la classe `#!python Rectangle` (on garde les mêmes méthodes d'instance `#!python area` et `#!python perimeter`) pour qu'elle garde une trace des objets créés.
    
    ```python
class Rectangle:
    rectangle_list = []
    
    @classmethod
    def rectangles_count(cls) -> int:
        return len(cls.rectangle_list)
    
    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h
        Rectangle.rectangle_list.append(self)
        ```
    
        -      On a ajouté un attribut de classe `#!python rectangle_list`. Ce nom d'attribut est valable à l'intérieur de définition la classe, mais partout ailleurs, y compris dans les méthodes d'instances, on devra l'appeler `#!python Rectangle.rectangle_list`.
        -      On a ajouté une méthode de classe, comme on peut le voir à l'aide du *décorateur* `#!python @classmethod` (un décorateur c'est une notion assez compliquée que l'on verra peut-être plus tard).
        Comme c'est une méthode de classe, elle doit impérativement prendre en premier paramètre la classe elle-même, ce qui est symbolisé par le paramètre `#!python cls`. Elle renvoie la longueur de la liste `#!python Rectangle.rectangle_list`.
        -     Enfin à l'intérieur du constructeur `#!python __init__` on rajoute l'objet créé `#!python self` à la liste `#!python Rectangle.rectangle_list`. Pour ce dernier point on peut se demander comment on peut ajouter un objet en train d'être créé, et qui va sans doute être modifié plus tard, à la liste. La réponse est que `#!python self` est une référence, pas une valeur, tout comme pour les listes.
    \exostart
    
        Créer une classe `#!python Angle`:
            -      une instance de cette classe contient un unique attribut appelé `#!python mesure`, qui est un `#!python float` compris entre 0 inclus et 360 exclu;
            -      le constructeur `#!python __init__` prend en paramètre un `#!python float` mais doit s'arranger pour que `#!python mesure` reste bien entre 0 et 360;
            -      implémenter une méthode `#!python affiche` : par exemple `#!python a.affiche()` doit afficher `#!python angle de 60 degrés`;
            -     implémenter une méthode `#!python ajoute` qui prend en paramètre une autre instance de la classe `#!python Angle` et renvoie un angle dont la mesure est la somme des deux angles. Par exemple si `#!python a` et `#!python b` sont deux angles de mesures 200 et 300, alors `#!python a.ajoute(b)` doit renvoyer un angle de mesure 140.
            -      implémenter les méthodes `#!python cos` et `#!python sin` à l'aide des fonctions du module `#!python math`. Attention, ceux-ci fonctionnent en radian donc pour convertir les degrés en radians il faut multiplier par $\frac{\pi}{180}$.
    
            \includegraphics[width=4cm]{img/domeeno}
        Bravo à toi, tu viens d'obtenir un stage chez Domeeno's Pizza ! 
        
            -      Tu dois écrire une classe `#!python Pizza` :
                -      le constructeur permet de créer une pizza « vide»;
                -      les attributs d'une instance sont :
                    -      la taille : M, L ou XL;
                    -      la pâte : classique, fine, pan ou mozza crust pour une M, pan ou fine pour L, fine pour XL;
                    -      la sauce de base : BBQ, tomate ou crème;
                    -      un maximum de 6 ingrédients parmi la liste ci-dessous    
                Tous ces attributs seront initialisés à `#!python None` par le constructeur;
                -  pour composer la pizza on pourra créer les méthodes suivantes :
                    -      `#!python select_size` pour la taille;
                    -      `#!python select_dough` pour la pâte;
                    -      `#!python add_ingredient` pour ajouter un ingrédient;
                    -      `#!python remove_ingredient` pour en enlever un;
                -  quand la pizza est prête   on appelera `#!python get_price` pour obtenir son prix;
            Pour les ingrédients et leur prix, le plus sage est de créer un dictionnaire dans la classe `#!python Pizza` (un peu comme la variable `#!python rectangle_list` du cours.)
                    \hline\rowcolor{UGLiOrange}
                    \color{white}**Article **&\color{white}**Prix** 
                    \hline
                    taille M  &  7,99 
                    \hline
                    taille L  &  7,99 \hline
                    taille XL  &  16,50 \hline
                    mozza crust & 2,90\hline
                    pan & 1,50\hline
                    base crème & gratuit\hline
                    base BBQ & gratuit\hline
                    base tomate & gratuit\hline
                    ananas & 1,30\hline
                    bacon & 2,00\hline
                    boulettes b\oe uf & 1,80\hline
                    champignons & 1,30\hline
                    mozzarella & 2,00\hline
                    oignons & 1,00 \hline
                    poivrons & 1,50 \hline
                    piments & 1,00 \hline
                    
                    
                    
                    \hline
            -      Implémenter une méthode de classe `#!python order` qui prend en paramètre une pizza et
                -      stocke cette instance dans une variable de classe de type liste;
                -      ajoute son prix à une variable de classe `#!python total_income`.
