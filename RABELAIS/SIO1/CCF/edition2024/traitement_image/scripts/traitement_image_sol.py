def affiche(lst):
    for ligne in lst:
        for x in ligne:
            print(str(x).zfill(3), end=" ")
        print()
    print()


def binarise(lst):
    n = len(lst)
    p = len(lst[0])
    for i in range(n):
        for j in range(p):
            if lst[i][j] < 128:
                lst[i][j] = 0
            else:
                lst[i][j] = 255



def cree_image_vide(n, p):
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(p):
            ligne.append(0)
        resultat.append(ligne)
    return resultat

def miroir_vertical(lst):
    n = len(lst)
    p = len(lst[0])
    resultat = cree_image_vide(n,p)
    for i in range(n):
        for j in range(p):
            resultat[i][j] = lst[i][p-1-j]
    return resultat

def miroir_horizontal(lst):
    n = len(lst)
    p = len(lst[0])
    resultat = cree_image_vide(n, p)
    for i in range(n):
        for j in range(p):
            resultat[i][j] = lst[n-1-i][j]
    return resultat


image = [[255, 255, 0, 128],
         [255, 255, 0, 0],
         [204, 165, 128, 64]]

affiche(image)
binarise(image)
affiche(image)

image = [[255, 255, 0, 128],
         [255, 255, 0, 0],
         [204, 165, 128, 64]]
affiche(miroir_vertical(image))
affiche(miroir_horizontal(image))

