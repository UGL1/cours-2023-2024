import pygame
from random import randint, choice

WIN_WIDTH = 1000
WIN_HEIGHT = 1000
GRAY = pygame.color.Color(64, 64, 64)
WHITE = pygame.color.Color(255, 255, 255)
RED = pygame.color.Color(255, 0, 0)
BLUE = pygame.color.Color(0, 0, 255)
GREEN = pygame.color.Color(0, 255, 0)
YELLOW = pygame.color.Color(255, 255, 0)

COLORS = [GRAY, WHITE, BLUE, RED, GREEN, YELLOW]


class Ball:
    balls = []
    grav_const = 0.02

    @classmethod
    def update_all(cls):
        for i in range(len(Ball.balls)):
            balls[i].update_position()
            for j in range(len(Ball.balls)):
                if j != i:
                    balls[i].update_speed(balls[j])

    @classmethod
    def remove(cls, b):
        if b in balls:
            Ball.balls.remove(b)
            del b

    def __init__(self, r=None, pos_x=None, pos_y=None, v_x=None, v_y=None, color=None, m=1):
        if r:
            self.r = r
            self.m = m
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.v_x = v_x
            self.v_y = v_y
            if color:
                self.color = color
            else:
                self.color = choice(COLORS)
        else:
            self.r = randint(5, 100)
            self.pos_x = randint(self.r, WIN_WIDTH - self.r)
            self.pos_y = randint(self.r, WIN_HEIGHT - self.r)
            self.v_x = randint(-4, 4)
            self.v_y = randint(-4, 4)
            self.color = choice(COLORS)
        Ball.balls.append(self)

    def update_position(self):
        self.pos_x += self.v_x
        self.pos_y += self.v_y

    def draw(self):
        pygame.draw.circle(win, self.color, (int(round(self.pos_x)), int(round(self.pos_y))), self.r)

    def update_speed(self, b):
        vector = [b.pos_x - self.pos_x, b.pos_y - self.pos_y]
        norm = (vector[0] ** 2 + vector[1] ** 2) ** .5
        if norm != 0:
            self.v_x += Ball.grav_const * vector[0] * b.m / norm ** 3
            self.v_y += Ball.grav_const * vector[1] * b.m / norm ** 3


pygame.init()
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

balls = [Ball(r=30, pos_x=WIN_WIDTH // 2, pos_y=WIN_HEIGHT // 2, v_x=0, v_y=0, m=60 ** 3, color=YELLOW)]
for i in range(5):
    r = 5
    balls.append(Ball(r=r, pos_x=(i+1)*WIN_WIDTH//16, pos_y=WIN_HEIGHT//2, v_x=0, v_y=-3, m=r ** 3))

clock = pygame.time.Clock()
go_on = True
while go_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    s = pygame.Surface((WIN_WIDTH,WIN_HEIGHT))
    s.fill(0)
    s.set_alpha(10)
    win.blit(s,(0,0))
    Ball.update_all()
    for b in balls:
        b.draw()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
