class File:
    def __init__(self):
        self.content = []

    def enfile(self, element):
        self.content.append(element)

    def defile(self):
        return self.content.pop(0)


collier = File()

for i in range(7):
    collier.enfile(i)

resultat = []
for i in range(6):
    resultat.append(collier.defile())
    collier.enfile(collier.defile())
    collier.enfile(collier.defile())
resultat.append(collier.defile())

print(resultat)

