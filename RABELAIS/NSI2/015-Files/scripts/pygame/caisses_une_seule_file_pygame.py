from random import randint
from queue2 import Queue2 as Queue
import pygame


class Caisse:
    nb_caisse = 0  # nombre de caisses qui va augmenter de 1 à chaque fois qu'on en crée une
    temps_attente_total = 0
    caisses = []
    nb_clients_servis = 0

    def __init__(self, file: Queue):
        self.temps_attente = 0  # une caisse créée est libre tout de suite
        self.file = file  # elle reçoit ses clients d'une file donnée
        Caisse.nb_caisse += 1  # on actualise le nombre de caisse
        self.numero = Caisse.nb_caisse  # on attribue un numéro à la caisse.
        Caisse.caisses.append(self)
        display(f"Caisse créée. Nombre de caisses : {Caisse.nb_caisse}")

    def sert_client(self):
        client = self.file.dequeue()
        Caisse.nb_clients_servis += 1
        display(f"Caisse n°{str(self.numero).zfill(2)} sert un client arrivé dans la file à l'heure {client}.", end=" ")
        temps_attente_client = tour - client
        display(f"Temps d'attente du client : {temps_attente_client} tour.", end=" ")
        Caisse.temps_attente_total += temps_attente_client
        self.temps_attente = randint(1, Caisse.nb_caisse)
        display(f"Le temps de service du client sera de {self.temps_attente} tour.")

    def actualise(self):
        self.temps_attente = self.temps_attente - 1 if self.temps_attente > 0 else 0  # Merci à Damien pour la syntaxe
        if self.temps_attente == 0 and not self.file.is_empty():
            self.sert_client()

def display(*arg,**kwargs):
    pass

def affiche_conclusion():
    temps_attente_moyen = Caisse.temps_attente_total / Caisse.nb_clients_servis
    display(
        f"En {NB_TOURS} tours, {Caisse.nb_clients_servis} ont été servis. Leur temps d'attente moyen est de {temps_attente_moyen}.")
    clients_restants = 0
    while not file_attente.is_empty():
        file_attente.dequeue()
        clients_restants += 1
    display(f"Il reste encore {clients_restants} à servir.")


NB_CAISSES = 20
NB_NOUVEAUX_CLIENTS_PAR_TOUR = 2
NB_TOURS = 1000

GRID_WIDTH = NB_CAISSES * 2 + 8
GRID_HEIGHT = NB_CAISSES+8

SIZE = 20
SCREEN_WIDTH = SIZE * GRID_WIDTH
SCREEN_HEIGHT = SIZE * GRID_HEIGHT
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), SIZE - 4)


def get_color(c: Caisse):
    t = c.temps_attente / Caisse.nb_caisse
    return (int(255 * t), 0, int(255 * (1 - t)))


def display_checkout(c: Caisse, i):
    color = get_color(c)
    pygame.draw.rect(screen, color, ((2 * i + 1) * SIZE, 1 * SIZE, SIZE, SIZE))
    draw = font.render(str(c.temps_attente).zfill(2), True, WHITE)
    screen.blit(draw, (int((2 * i + 1.5) * SIZE - draw.get_width() // 2), int(1.5 * SIZE - draw.get_height() // 2)))


def display_info():
    total = len(file_attente)
    for i in range(min(total, 100)):
        pygame.draw.rect(screen, GREEN, ((i % GRID_WIDTH) * SIZE, (3 + i // GRID_WIDTH) * SIZE, SIZE, SIZE))
        pygame.draw.rect(screen, WHITE, ((i % GRID_WIDTH) * SIZE, (3 + i // GRID_WIDTH) * SIZE, SIZE, SIZE), 2)
    draw = font.render("Tour : " + str(tour).zfill(2), True, 0)
    screen.blit(draw, (SCREEN_WIDTH - draw.get_width(), SCREEN_HEIGHT - draw.get_height()))
    draw = font.render("Temps d'attente total : " + str(Caisse.temps_attente_total).zfill(2), True, 0)
    screen.blit(draw, (SCREEN_WIDTH - draw.get_width(), SCREEN_HEIGHT - 3 * draw.get_height()))
    if Caisse.nb_clients_servis > 0:
        draw = font.render("Temps d'attente moyen : " + str(round(Caisse.temps_attente_total / Caisse.nb_clients_servis,4)),
                           True, 0)
        screen.blit(draw, (SCREEN_WIDTH - draw.get_width(), SCREEN_HEIGHT - 5 * draw.get_height()))


tour = 0  # heure de départ

file_attente = Queue()  # file d'attente vide


for _ in range(NB_CAISSES):
    Caisse(file_attente)
    file_attente.enqueue(tour)  # on met autant de personnes que de caisses dans la file
go_on = True
while go_on and tour < NB_TOURS:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    screen.fill(WHITE)
    clock.tick(10)
    for i in range(Caisse.nb_caisse):
        display_checkout(Caisse.caisses[i], i)
    display_info()
    pygame.display.flip()
    #pygame.image.save(screen, "../../img/single_queue" + str(tour).zfill(2) + ".png")
    for _ in range(NB_NOUVEAUX_CLIENTS_PAR_TOUR):
        file_attente.enqueue(tour)
    for caisse in Caisse.caisses:
        caisse.actualise()
    tour += 1
    clock.tick(10)
affiche_conclusion()
pygame.quit()
