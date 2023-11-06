from random import randint




class Ball:  # une classe qui crée des balles et update leurs positions et leurs vitesses mais
    # INDEPENDANTE DE P5 : ce n'est pas Ball qui affiche les boules, ce sera une autre fonction
    # donc ZERO% P5 dans cette classe

    lst_ball = []

    def __init__(self):
        self.size = randint(10, 50)
        self.x = randint(self.size, LARGEUR_FENETRE - self.size)
        self.y = randint(self.size, HAUTEUR_FENETRE - self.size)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.dx = randint(1, 5)
        self.dy = randint(1, 5)
        Ball.lst_ball.append(self)

    @staticmethod
    def update():
        for b in Ball.lst_ball:
            b.update_ball()

    def update_ball(self):
        self.x -= self.dx
        self.y -= self.dy
        if not self.size <= self.x <= LARGEUR_FENETRE - self.size:
            self.dx *= -1
        if not self.size <= self.y <= HAUTEUR_FENETRE - self.size:
            self.dy *= -1


LARGEUR_FENETRE = 400
HAUTEUR_FENETRE = 400
