from Ball import *
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


# on met en correspondances les couleurs de Ball avec les couleurs pygame
def color(b: Ball):
    return pygame.Color(int(b.col[0] * 255), int(b.col[1] * 255), int(b.col[2] * 255))


def draw_ball(b: Ball):
    """Fonction toute simple qui dessine une balle"""
    pygame.draw.circle(screen, color(b), (int(b.x), int(b.y)), int(b.r))


# -----
# MAIN
# -----

# On crée quelques balles, pas besoin de les stocker dans une variables, elles sont stockées dans la classe.

ball_number = 1000
ball_list = []
for _ in range(ball_number):
    r = randint(2, 5)
    x = randint(r, Ball.WIDTH - r)
    y = randint(r, Ball.HEIGHT - r)
    dx = randint(-3, 3)
    dy = randint(-3, 3)
    col = (uniform(0, 1), uniform(0, 1), uniform(0, 1))
    ball_list.append(Ball(x, y, dx, dy, r, col))
go_on = True
while go_on:
    # traditionnelle boucle qui gère les évènements pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False

    # maj du dessin proprement dit
    screen.fill(0)
    to_be_removed = []
    new_balls = []
    for i in range(len(ball_list) - 1):
        for j in range(i + 1, len(ball_list)):
            if i not in to_be_removed and j not in to_be_removed and ball_list[i].meets(ball_list[j]):
                to_be_removed.extend([i, j])
                new_balls.append(ball_list[i] + ball_list[j])
    ball_list = [ball_list[i] for i in range(len(ball_list)) if i not in to_be_removed]
    ball_list.extend(new_balls)
    for b in ball_list:
        draw_ball(b)
        b.update_pos()
    pygame.display.flip()

    # framerate
    clock.tick(FRAMERATE)

# On fait le ménage et on s'en va
pygame.quit()
