import threading

compteur = 0


def f():
    global compteur
    for i in range(1_000_00):
        compteur += 1


threads = []
for _ in range(1000):
    threads.append(threading.Thread(target=f))

for t in threads:
    t.start()

for t in threads:
    t.join()
print(compteur)
