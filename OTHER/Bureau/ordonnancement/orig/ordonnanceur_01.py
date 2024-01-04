class Processus:
    def __init__(self, nom: str, duree: int, priorite: int = 0):
        self.nom = nom
        self.duree = duree
        self.priorite = priorite
        self.reste = duree

    def execute_un_cycle(self):
        self.reste -= 1

    def est_fini(self) -> bool:
        return self.reste == 0


class File:
    def __init__(self):
        self.contenu = []

    def enfile(self, element):
        self.contenu.append(element)

    def defile(self):
        return self.contenu.pop(0)

    def est_vide(self) -> bool:
        return self.contenu == []


class Ordonnanceur:

    def __init__(self):
        self.liste_proc = []
        self.temps = 0
        self.file = File()

    def ajoute_nouveau_processus(self, proc: Processus):
        self.file.enfile(proc)

    def tourniquet(self) -> str | None:
        self.temps += 1
        if not self.file.est_vide():
            proc: Processus = self.file.defile()
            proc.execute_un_cycle()
            if not proc.est_fini():
                self.file.enfile(proc)
            return proc.nom
    #
    # def sjf(self) -> str:
    #     if not self.file.est_vide():
    #         proc: Processus = min(self.file.contenu, key=lambda p: p.duree)
    #         proc.execute_un_cycle()
    #         if proc.est_fini():
    #             self.file.contenu.remove(proc)
    #         return proc.nom
    #
    # def srjf(self) -> str:
    #     if not self.file.est_vide():
    #         proc: Processus = min(self.file.contenu, key=lambda p: p.reste)
    #         proc.execute_un_cycle()
    #         if proc.est_fini():
    #             self.file.contenu.remove(proc)
    #         return proc.nom


p1 = Processus("P1", 3)
p2 = Processus("P2", 4)
p3 = Processus("P3", 2)
p4 = Processus("P4", 5)

depart_proc = {2: p1, 1: p2, 4: p3, 0: p4}

ordonnanceur = Ordonnanceur()

fini = False
while not fini:
    if ordonnanceur.temps in depart_proc:
        ordonnanceur.ajoute_nouveau_processus(depart_proc[ordonnanceur.temps])
    elu = ordonnanceur.tourniquet()
    if elu:
        print(elu, end=" ")
    else:
        fini = True
