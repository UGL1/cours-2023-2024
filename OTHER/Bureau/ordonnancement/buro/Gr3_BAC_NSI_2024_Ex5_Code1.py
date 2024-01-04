class File:
    def __init__(self):
        """ Renvoie une file vide """
        self.contenu = []

    def enfile(self, element):
        """ Enfile element dans la file """
        self.contenu.append(element)

    def defile(self):
        """ Renvoie le premier élément de la file """
        return self.contenu.pop(0)

    def est_vide(self):
        """ Renvoie True si la file est vide, False sinon """
        return self.contenu == []
