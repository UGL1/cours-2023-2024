import threading

# on définit les 3 ressources
moteur = threading.Lock()
camera = threading.Lock()
wifi = threading.Lock()


def p1() -> None:
    """
    p1 effectue les actions du processus P1, en utilisant les ressources
    moteur, camera et wifi, et en affichant avec des print ce qu'il fait en détail
    """
    print('P1 attend le moteur')
    moteur.acquire()
    print('P1 a acquis le moteur')

    # à continuer

def p2(): # à coder
    pass

def p3(): # à coder
    pass


# création des 3 threads
P1 = threading.Thread(target=p1)
P2 = threading.Thread(target=p2)
P3 = threading.Thread(target=p3)

# lancer les 3 threads


# attendre que les 3 threads soient terminés

