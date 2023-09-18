import pygame
from random import randint, choice

WIN_WIDTH = 800
WIN_HEIGHT = 600
GRAY = pygame.color.Color(64, 64, 64)
WHITE = pygame.color.Color(255, 255, 255)
RED = pygame.color.Color(255, 0, 0)
BLUE = pygame.color.Color(0, 0, 255)
GREEN = pygame.color.Color(0, 255, 0)
COLORS = [GRAY, WHITE, BLUE, RED, GREEN]


class Ball:
    def __init__(self):
        self.r = randint(5, 100)
        self.pos_x = randint(self.r, WIN_WIDTH - self.r)
        self.pos_y = randint(self.r, WIN_HEIGHT - self.r)
        self.v_x = randint(-4, 4)
        self.v_y = randint(-4, 4)
        self.color = choice(COLORS)

    def update(self):
        self.pos_x += self.v_x
        if not self.r <= self.pos_x <= WIN_WIDTH - self.r:
            self.v_x *= -1
        self.pos_y += self.v_y
        if not self.r <= self.pos_y <= WIN_HEIGHT - self.r:
            self.v_y *= -1

    def draw(self):
        pygame.draw.circle(win, self.color, (self.pos_x, self.pos_y), self.r)


pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

balls = [Ball() for i in range(100)]

clock = pygame.time.Clock()
go_on = True
while go_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    win.fill(0)
    for b in balls:
        b.update()
        b.draw()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
