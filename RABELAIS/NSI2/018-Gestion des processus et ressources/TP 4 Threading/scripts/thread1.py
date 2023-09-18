import threading
from time import perf_counter


# On crée une fonction simple

def f(n: int) -> None:
    decalage = 5 * (n - 1) * '\t'  # pour tabuler suivant n
    print(decalage + "--------------------\n")
    print(decalage + f"thread {n} commence.\n")
    print(decalage + "--------------------\n")

    for i in range(10_000):
        print(decalage + f'thread {n} vaut {i}.\n')
    print(decalage + "--------------------\n")
    print(decalage + f"thread {n} s'arrête.\n")
    print(decalage + "--------------------\n")


thread1 = threading.Thread(target=f, args=[1])
# thread1 est un processus léger qui exécutera f(1) en tâche de fond

thread2 = threading.Thread(target=f, args=[2])
# idem

thread3 = threading.Thread(target=f, args=[3])
# idem


thread1.start()
thread2.start()
thread3.start()
# on a lancé les 3 threads qui tournent en tâche de fond, pendant ce temps
# on peut faire autre chose

now = perf_counter()  # comme mesurer l'heure

thread1.join()  # attendre que thread1 se termine
thread2.join()  # idem
thread3.join()  # idem

print(f"Entre le début et la fin d'exécution des threads, {perf_counter() - now} secondes se sont écoulées")
print("Pendant ce temps, le programme principal avait la main.")
# afficher le temps écoulé
