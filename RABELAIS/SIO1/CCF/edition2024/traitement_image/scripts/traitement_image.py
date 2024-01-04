def affiche(lst):
    if lst:
        for ligne in lst:
            for x in ligne:
                print(str(x).zfill(3), end=" ")
            print()
    print()


def binarise(lst):
    ...



def cree_image_vide(n, p):
    ...

def miroir_vertical(lst):
    ...

def miroir_horizontal(lst):
    ...


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

