import pygame
from queue2 import Queue2
from random import randint

now = 0
nb_checkouts = 3
nb_new_per_turn = 2
GRID_WIDTH = nb_checkouts * 2 + 4
GRID_HEIGHT = nb_checkouts * 3
SIZE = 20
SCREEN_WIDTH = SIZE * GRID_WIDTH
SCREEN_HEIGHT = SIZE * GRID_HEIGHT
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
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


def display_info():
    total = len(queue)

    for i in range(min(total, 100)):
        pygame.draw.rect(screen, GREEN, ((i % GRID_WIDTH) * SIZE, (3 + i // GRID_WIDTH) * SIZE, SIZE, SIZE))
        pygame.draw.rect(screen, WHITE, ((i % GRID_WIDTH) * SIZE, (3 + i // GRID_WIDTH) * SIZE, SIZE, SIZE), 2)
    draw = font.render("Time : " + str(now).zfill(2), True, 0)
    screen.blit(draw, (SCREEN_WIDTH - draw.get_width(), SCREEN_HEIGHT - draw.get_height()))
    draw = font.render("Total waiting Time : " + str(CheckOut.total_waiting_time).zfill(2), True, 0)
    screen.blit(draw, (SCREEN_WIDTH - draw.get_width(), SCREEN_HEIGHT - 3 * draw.get_height()))


class CheckOut:
    nb_checkouts = 0
    total_waiting_time = 0
    checkouts = []

    def __init__(self, queue: Queue2):
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


queue = Queue2()
for i in range(nb_checkouts):
    CheckOut(queue)
    queue.enqueue(now)

n = 5
go_on = True
while go_on and now < n:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    screen.fill(WHITE)
    clock.tick(10)
    for i in range(CheckOut.nb_checkouts):
        display_checkout(CheckOut.checkouts[i], i)
    display_info()
    pygame.display.flip()
    pygame.image.save(screen, "../../img/single_queue" + str(now).zfill(2) + ".png")
    now += 1
    for _ in range(nb_new_per_turn):
        queue.enqueue(now)
    for c in CheckOut.checkouts:
        c.update()
        if c.is_free() and not c.queue.is_empty():
            c.serve()
print(CheckOut.total_waiting_time / (n - len(queue)))

pygame.quit()
