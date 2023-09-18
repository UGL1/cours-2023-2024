from random import randint, choice
from queue import Queue


def display(*args, **kwargs):
    pass


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


def affiche_conclusion():
    temps_attente_moyen = Caisse.temps_attente_total / Caisse.nb_clients_servis
    print(
        f"En {nb_tours} tours, {Caisse.nb_clients_servis} ont été servis. Leur temps d'attente moyen est de {temps_attente_moyen}.")
    clients_restants = 0
    while not file_attente.is_empty():
        file_attente.dequeue()
        clients_restants += 1
    print(f"Il reste encore {clients_restants} à servir.")


def moins_de_monde_ou_libre(caisse: Caisse):
    if caisse.temps_attente == 0:
        return -1
    return len(caisse.file.content)  # on est "obligés" de tricher


nb_caisses = 20
nb_nouveaux_clients_par_tour = 1
nb_tours = 100_000
tour = 0

for _ in range(nb_caisses):
    file_attente = Queue()
    Caisse(file_attente)
    file_attente.enqueue(tour)

for i in range(nb_tours):
    display(f"tour {str(tour).zfill(2)} :")
    display("----------")
    for _ in range(nb_nouveaux_clients_par_tour):
        file_attente = min(Caisse.caisses, key=moins_de_monde_ou_libre).file
        file_attente.enqueue(tour)
    for caisse in Caisse.caisses:
        caisse.actualise()
    tour += 1
affiche_conclusion()
