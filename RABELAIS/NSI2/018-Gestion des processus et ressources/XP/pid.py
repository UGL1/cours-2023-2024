from os import getpid
import ctypes
from time import sleep

def space_pressed() -> bool:
    return bool(ctypes.windll.user32.GetAsyncKeyState(32) & 2 ** 15)


pid = getpid()
while not space_pressed():
    sleep(0.01)

for i in range(1000):
    print(f'Je suis le processus n° {pid}')

