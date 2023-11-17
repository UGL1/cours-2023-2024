from Cercle import *

c1 = Cercle(0, 0, 1)  # crée un cercle c1 de centre (0,0) et de rayon 1
c2 = Cercle(3, 1, 5)  # idem
c3 = Cercle(-1, 4, 1)  # idem
c2.decale(-1, 2)  # décale le centre ce c2 de (-1,2)
c3.dilate(2)  # multiplie le rayon de c3 par 2
print(c1)  # affiche correctement c1
print(c2)  # idem
print(c3)  # idem

print(c2.contient(c1))  # va afficher True car c1 est « à l'intérieur de c2 »
print(c2.contient(c3))  # False
print(c1.chevauche(c3))  # False car c1 et c2 n'ont aucun point commun
print(c2.chevauche(c3))  # True
