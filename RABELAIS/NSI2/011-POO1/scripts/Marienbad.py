class Marienbad:
    def __init__(self, joueur1: str, joueur2: str):
        self.tas = (1, 2, 3, 4, 5, 6)
        self.allumettes = [1, 2, 3, 4, 5, 6]
        self.joueurs = (joueur1, joueur2)
        self.tour = 0

    def __str__(self):
        result = "tas : \t\t\t" + str(self.tas) + "\nallumettes : \t" + str(self.allumettes) + "\n"
        result += "-------- Prochain joueur : " + self.joueurs[self.tour] + "--------"
        return result

    def verifie(self, n: int, t: int) -> bool:
        return self.allumettes[t] >= n

    def enlever(self, n: int, t: int) -> None:
        self.allumettes[t] -= n

    def termine(self) -> bool:
        for i in range(6):
            if self.allumettes[i] != 0:
                return False
        return True



