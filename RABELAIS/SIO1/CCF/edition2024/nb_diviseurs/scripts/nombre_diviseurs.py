def nb_div(n: int) -> int:
	r = 0
	for i in range(1, n + 1):
		if n % i == 0:
			r = r + 1
	return r


def nb_div_tous_entiers(n: int) -> list:
	r = []
	for i in range(1, n + 1):
		r.append(nb_div(i))
	return r


def mystere(n: int) -> int:
	m = 0
	r = 0
	for i in range(1, n + 1):
		if nb_div(i) > m:
			m = nb_div(i)
			r = i
	return r


def nb_div_connus():  # Compléter cette ligne
	pass  # Enlever pass et coder


def liste_dv_connus():  # Compléter cette ligne
	pass  # Enlever pass et coder
