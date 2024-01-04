def temps_de_vol(n: int) -> int:
	compteur = 0
	while n != 1:
		compteur += 1
		if n % 2 == 1:
			n = 3 * n + 1
		else:
			n = n // 2
	return compteur


def hauteur_de_vol():  # Compléter cette ligne
	pass  # Enlever pass et coder


def vole_bien():  # Compléter cette ligne
	pass  # Enlever pass et coder
