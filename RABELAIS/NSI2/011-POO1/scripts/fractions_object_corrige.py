class Fraction:

    def __init__(self, n: int, d: int):
        self.num = n
        self.den = d

    def add(self, other):
        return Fraction(self.den * other.num + self.num * other.den, self.den * other.den)

    def __str__(self):
        return str(self.num) + " / " + str(self.den)


f1 = Fraction(2,5)
print("Je crée une première fraction :",f1)
f2 = Fraction(3,7)
print("Je crée une autre fraction :",f2)
print("Leur somme vaut :",f1.add(f2))
