for u in utilisateur:
    for t in trajet:
        if t.id_util == u.id_util:  # revient à faire la jointure
            if u.prenom == `Jean`:
                print(u.id_util)