# Crée deux dictionnaires dont les clés sont les id des utilisateurs et les valeurs zéro
nb_trajets = {u.id_util: 0 for u in utilisateurs}

nb_annulations = {u.id_util: 0 for u in utilisateurs}
for t in trajet:
    nb_trajets[t.id_util] += 1
    if t.statut == "annulé":
        ...