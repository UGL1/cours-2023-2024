def compresse(ligne: list) -> list:
	resultat = []
	valeur = 0
	compteur = 0
	i = 0
	while i < len(ligne):
		if ligne[i] == valeur:
			compteur += 1
		else:
			valeur = 1 - valeur
			resultat.append(compteur)
			compteur = 1
		i += 1
	resultat.append(compteur)
	return resultat


def taux_compression():  # Compléter cette ligne
	pass  # enlever pass et coder


def decompresse():  # Compléter cette ligne
	pass  # enlever pass et coder


lst1 = [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
lst2 = compresse(lst1)
print(taux_compression(lst1))
print(decompresse(lst2))
