class Ordonnanceur:

    def __init__(self):
        self.temps = 0
        self.file = File()

    def ajoute_nouveau_processus(self, proc):
        ...

    def tourniquet(self):
        self.temps = ...
        if not self.file.est_vide():
            proc = ...
            ...
            if not proc.est_fini():
                ...
            return proc.nom
        else:
            return None