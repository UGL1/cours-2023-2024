from Ball import *
from random import randint, choice
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

# on définit des couleurs pygame
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# on met en correspondances les couleurs de Ball avec les couleurs pygame
COLOR_LIST = {Ball.RED: RED, Ball.BLUE: BLUE, Ball.GREEN: GREEN}


def draw_ball(b: Ball):
    """Fonction toute simple qui dessine une balle"""
    pygame.draw.circle(screen, COLOR_LIST[b.col], (b.x, b.y), b.r)


# -----
# MAIN
# -----

# On crée quelques balles, pas besoin de les stocker dans une variables, elles sont stockées dans la classe.

ball_number = 50
for _ in range(ball_number):
    r = randint(5, 100)
    x = randint(r, Ball.WIDTH - r)
    y = randint(r, Ball.HEIGHT - r)
    dx = randint(-3, 3)
    dy = randint(-3, 3)
    col = choice(Ball.COLOR_LIST)
    Ball(x, y, dx, dy, r, col)
go_on = True
while go_on:
    # traditionnelle boucle qui gère les évènements pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False

    # maj du dessin proprement dit
    screen.fill(BLACK)
    Ball.update_all()
    for b in Ball.ball_list:
        draw_ball(b)
    pygame.display.flip()

    # framerate
    clock.tick(FRAMERATE)

# On fait le ménage et on s'en va
pygame.quit()
