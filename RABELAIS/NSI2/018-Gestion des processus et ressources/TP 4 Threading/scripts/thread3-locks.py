import threading

lock = threading.Lock()
g = 0


def f(n):
    global g
    print(f'Début thread {n}')
    for i in range(1_000_000):
        lock.acquire()
        g += 1
        lock.release()
    print(f'End thread {n}')


threads = []
for _ in range(4):
    threads.append(threading.Thread(target=f, args=[_]))

for t in threads:
    t.start()

for t in threads:
    t.join()
print(g)
