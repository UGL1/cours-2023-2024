import threading

moteur = threading.Lock()
camera = threading.Lock()
wifi = threading.Lock()

def p1():
    print('P1 attend le moteur')
    moteur.acquire()
    print('P1 a acquis le moteur')

    print('P1 attend le wifi')
    wifi.acquire()
    print('P1 a acquis le wifi.')

    print('P1 libère le moteur')
    moteur.release()

    print('P1 libère le wifi')
    wifi.release()


def p2():
    print('P2 attend le wifi')
    wifi.acquire()
    print('P2 a acquis le wifi')

    print('P2 attend la caméra')
    camera.acquire()
    print('P2 a acquis la caméra.')

    print('P2 libère le wifi')
    wifi.release()

    print('P2 libère la caméra')
    camera.release()

def p3():
    print('P3 attend la caméra')
    camera.acquire()
    print('P3 a acquis la caméra')

    print('P3 attend le moteur')
    moteur.acquire()
    print('P3 a aquis le moteur')

    print('P3 libère la caméra')
    camera.release()

    print('P3 libère le moteur')
    moteur.release()


P1 = threading.Thread(target=p1)
P2 = threading.Thread(target=p2)
P3 = threading.Thread(target=p3)

P1.start()
P2.start()
P3.start()

P1.join()
P2.join()
P3.join()
