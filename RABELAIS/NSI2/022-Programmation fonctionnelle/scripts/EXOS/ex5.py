from time import sleep


def evaluate_with_delay(f, n: int, d: float):
    for x in range(n):
        print(f(x), end=" ")
        sleep(d/1000)


evaluate_with_delay(lambda x: x * 2, 10, 1000) # affiche 0 2 4 6 8 10 12 14 16 18  seconde par seconde
