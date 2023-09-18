import pygame
from RectMap import *

pygame.init()
window = pygame.display.set_mode((800, 600))
WHITE = pygame.Color(255, 255, 255)


def draw(r: RectMap):
    pygame.draw.rect(window, WHITE, (int(round(r.left)), int(round(r.top)), int(round(r.width)), int(round(r.height))), 1)


RectMap.set_whole_world(800,600, 10)
a = RectMap(100,200,80,60)
draw(a)
pygame.display.flip()
go_on = True
while go_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            window.fill(0)
            draw(a.zoom_in(x,y,1/1.3))
        elif pygame.mouse.get_pressed()[2]:
            window.fill(0)
            draw(a.zoom_out(1.3))
            print(a)
    pygame.display.flip()
pygame.quit()
