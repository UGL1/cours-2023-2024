from queue2 import Queue2
from random import randint, choice
import pygame

now = 0
nb_checkouts = 20
nb_init = 3
nb_new_per_turn = 2
GRID_WIDTH = nb_checkouts * 2 + 1
GRID_HEIGHT = nb_checkouts * 2
SIZE = 20
SCREEN_WIDTH = SIZE * GRID_WIDTH
SCREEN_HEIGHT = SIZE * GRID_HEIGHT
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
print(pygame.init())
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), SIZE - 2)


def get_color(c):
    t = c.waiting_time / CheckOut.nb_checkouts
    return (int(255 * t), 0, int(255 * (1 - t)))


def display_checkout(c, i):
    color = get_color(c)
    pygame.draw.rect(screen, color, ((2 * i + 1) * SIZE, 1 * SIZE, SIZE, SIZE))
    draw = font.render(str(c.waiting_time), True, WHITE)
    screen.blit(draw, (int((2 * i + 1.5) * SIZE - draw.get_width() // 2), int(1.5 * SIZE - draw.get_height() // 2)))
    n = min(len(c.queue), nb_checkouts)
    for j in range(n):
        pygame.draw.rect(screen, GREEN, ((2 * i + 1) * SIZE, (2 + j) * SIZE, SIZE, SIZE))
        pygame.draw.rect(screen, 0, ((2 * i + 1) * SIZE, (2 + j) * SIZE, SIZE, SIZE), 2)


def display_info():
    total = sum(len(c.queue) for c in CheckOut.checkouts)
    draw = font.render("People waiting : " + str(total), True, WHITE)
    screen.blit(draw, (SCREEN_WIDTH - draw.get_width(), SCREEN_HEIGHT - draw.get_height()))


class CheckOut:
    nb_checkouts = 0
    total_waiting_time = 0
    checkouts = []

    @staticmethod
    def least_queued_checkout():
        min_checkout = CheckOut.checkouts[0]
        for c in CheckOut.checkouts:
            if c.waiting_time == 0:
                return c
            if len(c.queue) < len(min_checkout.queue):
                min_checkout = c
        return min_checkout

    @staticmethod
    def display():
        print("-" * 60)
        for i in range(len(CheckOut.checkouts)):
            print(
                f"Checkout n° {i} :  Waiting time={CheckOut.checkouts[i].waiting_time}, people waiting={len(CheckOut.checkouts[i].queue)}")
        input()

    def __init__(self, queue: Queue2):
        self.ready_in = 0
        self.queue = queue
        self.waiting_time = 0
        CheckOut.nb_checkouts += 1
        CheckOut.checkouts.append(self)

    def serve(self):
        assert self.waiting_time == 0
        CheckOut.total_waiting_time += now - self.queue.dequeue()
        self.waiting_time = randint(1, CheckOut.nb_checkouts)

    def update(self):
        self.waiting_time = max(0, self.waiting_time - 1)

    def is_free(self):
        return self.waiting_time == 0


for _ in range(20):
    c = CheckOut(Queue2())
    for i in range(nb_init):
        c.queue.enqueue(now - nb_init)

n = 100000
go_on = True
while go_on and now < n:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    screen.fill(0)
    clock.tick(10)
    for i in range(CheckOut.nb_checkouts):
        display_checkout(CheckOut.checkouts[i], i)
    display_info()
    pygame.display.flip()
    now += 1
    for _ in range(nb_new_per_turn):
        c = CheckOut.least_queued_checkout()
        c.queue.enqueue(now)
    for c in CheckOut.checkouts:
        c.update()
        if c.is_free() and not c.queue.is_empty():
            c.serve()

r = sum(len(c.queue) for c in CheckOut.checkouts)
print(CheckOut.total_waiting_time / (n - r))
