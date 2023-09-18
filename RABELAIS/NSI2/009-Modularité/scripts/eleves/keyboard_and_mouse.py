from time import sleep, perf_counter
import win32api
from vk_codes import *

"""
This module allows to check if keys or mouse buttons are pressed in various ways.
It also allows to generate mouse and keyboard events
    - simulate a key presss and a key release as well as mouse buttons clicks
    - move mouse from a point to another, continuously, during a given amount of time
"""

is_on = [False] * 256


#################################
#                               #
# Partie 1 : Commandes clavier  #
#                               #
#################################

def is_pressed(key: int) -> bool:  # fonction déjà implémentée
    """
    checks if a key is being pressed
    key must be a VK_CODE
    """
    return bool(win32api.GetAsyncKeyState(key) & 2 ** 15)


def wait_until_released(key: int) -> None:
    """
    wait until a certain key is released (ie : not pressed)
    to lower CPU usage, it is best to sleep 10 ms beetween each time key is checked
    """
    # AIDE :
    #       dans le module time, la fonction sleep(n) arrête le programme pendant n seconde. n peut être un float, donc
    #       plus petit que 1 !

    pass


def get_key() -> int:
    """
    returns the key_code if a key's being pressed, -1 if none is.
    """
    # Aide :
    #       ne tester que les touches ayant un VK_CODE compris entre 8 et 253 (certaines touches avec un VK_CODE qui
    #       n'est pas dans cette plage de valeurs sont parfois activées sans qu'on appuie dessus.
    pass


def is_pressed_once(key: int) -> bool:
    """
    checks if a key is being pressed but only once :
    if the key was being pressed during the last call and is still being pressed,
    this function returns False... until key is released and pressed again
    """
    # Aide :
    #       Créer une structure de données globale qui retient quelles touche était déjà pressées la dernière fois
    #       qu'on a appelé is_pressed...
    if is_on[key]:
        if not is_pressed(key):
            is_on[key] = False
            return False
        else:
            return False
    else:
        if is_pressed(key):
            is_on[key] = True
            return True
        else:
            return False


################################
#                              #
# Partie 2 : Commandes souris  #
#                              #
################################

def move_mouse_relative(x: float, y: float) -> None:
    """
    moves mouse relatively
    x and y can be float but will be converted to nearest integers
    """
    win32api.mouse_event(1, int(round(x)), int(round(y)), 0, 0)


def continuous_relative_move_xy(x: int, y: int, time_interval: int) -> None:
    """
    moves mouse relatively and continuously during time_interval
    """
    pass
