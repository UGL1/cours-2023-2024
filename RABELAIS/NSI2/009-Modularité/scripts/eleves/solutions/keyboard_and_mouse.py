from time import sleep, perf_counter_ns
import win32api
from vk_codes import *

"""
This module allows to check if keys or mouse buttons are pressed in various ways.
It also allows to generate mouse and keyboard events
    - simulate a key presss and a key release as well as mouse buttons clicks
    - move mouse from a point to another, continuously, during a given amount of time
"""


isOn = [False] * 256


def is_pressed(key: int) -> bool:
    """
    checks if a key is being pressed
    """
    return bool(win32api.GetAsyncKeyState(key) & 2 ** 15)


def press_key(key: int) -> None:
    """
    simulates a key press or a mouse click
    """
    if not isOn[key]:
        isOn[key] = True
    if key == VK_LBUTTON:
        win32api.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    elif key == VK_RBUTTON:
        win32api.mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    elif key == VK_MBUTTON:
        win32api.mouse_event(MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
    else:
        win32api.keybd_event(key, 0, 0, 0)


def press_and_release_key(key: int) -> None:
    """
    simulates a key press or a mouse click with release
    
    """
    press_key(key)
    sleep(0.001)
    release_key(key)
    isOn[key] = False


def release_key(key: int) -> None:
    """
    simulates a key or a mouse button released
    """
    if isOn[key]:
        isOn[key] = False
    if key == VK_LBUTTON:
        win32api.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    elif key == VK_RBUTTON:
        win32api.mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
    elif key == VK_MBUTTON:
        win32api.mouse_event(MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
    win32api.keybd_event(key, 0, 2, 0)


def is_pressed_once(key: int) -> bool:
    """
    checks if a key is being pressed but only once :
    if the key was being pressed during the last call and is still being pressed,
    this function returns False... until key is released and pressed again
    """
    if is_pressed(key):
        if isOn[key]:
            return False
        else:
            isOn[key] = True
            return True
    elif isOn[key]:
        isOn[key] = False
    return False


def wait_until_released(key: int) -> None:
    """
    pauses until key's released
    """
    while bool(win32api.GetAsyncKeyState(key) & 2 ** 15):
        pass
    isOn[key] = False


def get_key() -> int:
    """
    returns the key_code if a key's being pressed
    """
    while True:
        for i in range(8, 254):
            if bool(win32api.GetAsyncKeyState(i) & 2 ** 15):
                return i


def move_mouse_relative(x, y) -> None:
    """
    moves mouse relatively
    """
    win32api.mouse_event(1, int(round(x)), int(round(y)), 0, 0)


def continuous_relative_move_xy(x: int, y: int, time_interval: int) -> None:
    """
    moves mouse relatively and continuously during time_interval
    """
    actual_sum_x = 0
    actual_sum_y = 0
    duration = 0
    start = perf_counter_ns()
    while duration < time_interval:
        theoric_sum_x = x * duration / time_interval
        theoric_sum_y = y * duration / time_interval

        delta_x = int(round(theoric_sum_x - actual_sum_x))
        delta_y = int(round(theoric_sum_y - actual_sum_y))

        move_mouse_relative(delta_x, delta_y)
        actual_sum_x += delta_x
        actual_sum_y += delta_y
        sleep(0.001)
        now = perf_counter_ns()
        duration = (now - start) / (10 ** 6)
    if actual_sum_x < x:
        move_mouse_relative(x - actual_sum_x, 0)
    if actual_sum_y < y:
        move_mouse_relative(0, y - actual_sum_y)


def mouse_mouse_from_to(x1, y1, x2, y2, duration) -> None:
    """
    moves mouse continuously during time_interval from (x1,y1) to (x2,y2)
    """
    win32api.SetCursorPos((x1, y1))
    continuous_relative_move_xy(x2 - x1, y2 - y1, duration)


def move_mouse_to(x, y, duration=0) -> None:
    """
moves mouse continuously during time_interval from current position to (x,y)
"""

    if not duration:
        win32api.SetCursorPos((x, y))
    else:
        x1, y1 = win32api.GetCursorPos()
        continuous_relative_move_xy(x - x1, y - y1, duration)
