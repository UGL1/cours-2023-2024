# Classe indépendante de pygame

class Ball:
    WIDTH = 800  # indépendant de pygame
    HEIGHT = 600  # idem
    RED = "red"  # idem
    BLUE = "blue"  # idem
    GREEN = "green"  # idem
    COLOR_LIST = (RED, BLUE, GREEN)  # idem

    ball_list = []  # pour stocker les balles

    @classmethod
    def update_all(cls):
        for ball in cls.ball_list:
            ball.update()

    def __init__(self, x, y, dx, dy, r, col):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.col = col
        Ball.ball_list.append(self)  # on ajoute à l'attribut de classe

    def update(self):
        self.x += self.dx
        if not self.r <= self.x <= Ball.WIDTH - self.r:
            self.dx *= -1
        self.y += self.dy
        if not self.r <= self.y <= Ball.HEIGHT - self.r:
            self.dy *= -1
