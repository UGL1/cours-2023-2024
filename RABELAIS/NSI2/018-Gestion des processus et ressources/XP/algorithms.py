from typing import *
from stack import Stack
from process import Process
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()


def draw_process(lst: List[Process]) -> None:
    count = []
    for j in range(len(lst)):
        i = 0
        while i < len(count):
            if lst[j] == count[i]:
                y = i
                break
            else:
                i += 1
        if i == len(count):
            y = i
            count.append(lst[j])
        ax.add_patch(Rectangle((j, y), 1, 1, facecolor=lst[j].color))
    for i in range(len(count)):
        plt.arrow(0, y=i, dx=len(lst), dy=0, width=0.05, color='black')


def fifo(lst: List[Process]) -> List[Process]:
    result = []
    for process in lst:
        for _ in range(process.duration):
            result.append(process)
    return result


L = [Process('1', 0, 4), Process('2', 3, 5, 0, 'red'), Process('3', 5, 4, 0, 'green')]

draw_process(fifo(L))
plt.show()
