# Classe indépendante de pygame
from math import sqrt


class Ball:
    WIDTH = 800  # indépendant de pygame
    HEIGHT = 600  # idem

    def __init__(self, x, y, dx, dy, r, col):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.col = col

    def update(self):
        self.x += self.dx
        if not self.r <= self.x <= Ball.WIDTH - self.r:
            self.dx *= -1
        self.y += self.dy
        if not self.r <= self.y <= Ball.HEIGHT - self.r:
            self.dy *= -1

    def meets(self, other):
        return (self.r + other.r) ** 2 > (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def __add__(self, other):
        new_r = sqrt(self.r ** 2 + other.r ** 2)
        vector_x, vector_y = other.x - self.x, other.y - self.y
        factor = other.r ** 2 / (self.r ** 2 + other.r ** 2)
        new_x, new_y = self.x + vector_x * factor, self.y + vector_y * factor
        new_dx = (self.dx * self.r ** 2 + other.dx * other.r ** 2) / (self.r ** 2 + other.r ** 2)
        new_dy = (self.dy * self.r ** 2 + other.dy * other.r ** 2) / (self.r ** 2 + other.r ** 2)
        new_col = tuple(
            (self.col[i] * self.r ** 2 + other.col[i] * other.r ** 2) / (self.r ** 2 + other.r ** 2) for i in range(3))
        return Ball(new_x, new_y, new_dx, new_dy, new_r, new_col)
