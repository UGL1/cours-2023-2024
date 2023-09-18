from Ballplus import *
from random import randint, uniform
import pygame

# on initialise pygame
pygame.init()

# on récupère ces valeurs dans la classe mais on pourrait les redimensionner...
SCREEN_WIDTH, SCREEN_HEIGHT = Ball.WIDTH, Ball.HEIGHT
# on définit la surface d'affichage
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# on définit une horloge et un framerate
FRAMERATE = 60
clock = pygame.time.Clock()


def color(b: Ball):
    return pygame.Color(int(b.col[0] * 255), int(b.col[1] * 255), int(b.col[2] * 255))


def draw_ball(b: Ball):
    """Fonction toute simple qui dessine une balle"""
    pygame.draw.circle(screen, color(b), (b.x, b.y), b.r)

    # -----
    # MAIN
    # -----

    # On crée quelques balles, pas besoin de les stocker dans une variables, elles sont stockées dans la classe.

    ball_number = 50
    ball_list = []
    for _ in range(ball_number):
        r = randint(5, 100)
        x = randint(r, Ball.WIDTH - r)
        y = randint(r, Ball.HEIGHT - r)
        dx = randint(-3, 3)
        dy = randint(-3, 3)
        col = (uniform(0,1),uniform(0,1),uniform(0,1))
        ball_list.append(Ball(x, y, dx, dy, r, col))
    go_on = True
    while go_on:
        # traditionnelle boucle qui gère les évènements pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go_on = False

        # maj du dessin proprement dit
        screen.fill(0)
        for b in ball_list:
            b.update()
        pygame.display.flip()

        # framerate
        clock.tick(FRAMERATE)

    # On fait le ménage et on s'en va
    pygame.quit()
