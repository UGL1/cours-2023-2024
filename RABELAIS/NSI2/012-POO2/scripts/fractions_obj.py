class Fraction:

    def pgcd(self) -> int:
        a = self.d
        b = self.n
        a, b = max(a, b), min(a, b)
        while b != 0:
            a, b = b, a % b
        return a

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def simplify(self):
        p = self.pgcd()
        self.n //= p
        self.d //= p

    def __add__(self, other):
        result = Fraction(self.n * other.d + self.d * other.n, self.d * other.d)
        result.simplify()
        return result

    def __sub__(self, other):
        result = Fraction(self.n * other.d - self.d * other.n, other.d * self.d)
        result.simplify()
        return result

    def __mul__(self, other):
        result = Fraction(self.n * other.n, self.d * other.d)
        result.simplify()
        return result

    def __truediv__(self, other):
        result = Fraction(self.n * other.d, self.d * other.n)
        result.simplify()
        return result

    def __eq__(self, other):
        return self.n * other.d == self.d * other.n

    def __ne__(self, other):
        return self.n * other.d != self.d * other.n

    def __lt__(self, other):
        return self.n / self.d < other.n / other.d

    def __le__(self, other):
        return self.n / self.d <= other.n / other.d

    def __gt__(self, other):
        return self.n / self.d > other.n / other.d

    def __ge__(self, other):
        return self.n / self.d >= other.n / other.d

    def __str__(self):
        return str(self.n) + ' / ' + str(self.d)
