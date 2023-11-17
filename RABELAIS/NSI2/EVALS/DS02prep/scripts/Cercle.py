from math import sqrt


def distance(xa, ya, xb, yb):  # La distance usuelle (on ne demande pas de la coder)
    return sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


class Cercle:

    def __init__(self, x: float, y: float, rayon: float):
        self.x = x
        self.y = y
        self.rayon = rayon

    def dilate(self, facteur):  # on multiplie le rayon par un facteur >0
        self.rayon *= facteur

    def decale(self, dx: float, dy: float):  # on translate
        self.x += dx
        self.y += dy

    def contient(self, other):
        return distance(self.x, self.y, other.x, other.y) <= self.rayon - other.rayon

    def chevauche(self, other):
        return not self.contient(other) and distance(self.x, self.y, other.x, other.y) <= self.rayon + other.rayon

    def __str__(self):
        return f"Cercle : centre({self.x}, {self.y}) rayon {self.rayon}."
