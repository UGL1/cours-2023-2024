class Horloge:
    def __init__(self):
        self.t = 0

    def cycle_suivant(self):
        self.t += 1

    def temps(self):
        return self.t


horloge = Horloge()


class Ressource:
    def __init__(self, nom: str):
        self.nom = nom
        self.libre = True
        self.possesseur = None

    def est_libre(self) -> bool:
        return self.libre

    def detenu_par(self):
        return self.possesseur

    def acquerir(self, poss):
        self.possesseur = poss
        self.libre = False

    def liberer(self):
        self.possesseur = None
        self.libre = True

    def __str__(self):
        result = f"Ressource :{self.nom}"
        if self.libre:
            result += " - libre"
        else:
            result += f" - détenue par {self.possesseur.nom}"
        return result



