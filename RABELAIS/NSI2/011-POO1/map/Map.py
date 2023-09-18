from RectMap import *
import pygame


class Map:
    def __init__(self, filename: str, width, height):
        pygame.init()
        self.MAP = pygame.image.load(filename)
        self.MAP_WIDTH, self.MAP_HEIGHT = self.MAP.get_width(), self.MAP.get_height()
        RectMap.set_whole_world(self.MAP_WIDTH, self.MAP_HEIGHT, 20)
        self.rect = RectMap(0, 0, width, height)
        self.WINDOW_WIDTH = width
        self.WINDOW_HEIGHT = height
        self.clock = pygame.time.Clock()
        self.window = None
        self.running = False
        self.speed = 50

    def draw(self):
        self.window.fill(0)
        temp_map = pygame.Surface((int(round(self.rect.width)), int(round(self.rect.height))))
        temp_map.blit(self.MAP, (0, 0), area=(int(round(self.rect.left)),
                                              int(round(self.rect.top)),
                                              int(round(self.rect.width)),
                                              int(round(self.rect.height))))
        temp_map = pygame.transform.smoothscale(temp_map, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.window.blit(temp_map, (0, 0))
        pygame.display.flip()

    def start(self):
        self.window = pygame.display.set_mode((self.rect.width, self.rect.height), pygame.NOFRAME)
        self.running = True

    def check(self):
        pygame.event.pump()
        kb_state = pygame.key.get_pressed()
        if kb_state[pygame.K_RIGHT]:
            self.rect.translate_constrained(self.rect.zoom_factor()* self.speed, 0)
            self.draw()
        if kb_state[pygame.K_LEFT]:
            self.rect.translate_constrained(-self.rect.zoom_factor() * self.speed, 0)
            self.draw()
        if kb_state[pygame.K_UP]:
            self.rect.translate_constrained(0, -self.rect.zoom_factor() * self.speed)
            self.draw()
        if kb_state[pygame.K_DOWN]:
            self.rect.translate_constrained(0, self.rect.zoom_factor() * self.speed)
            self.draw()

        if kb_state[pygame.K_KP_PLUS]:
            self.rect.zoom_in(self.rect.center_x, self.rect.center_y, 1 / 1.01)
            self.draw()

        if kb_state[pygame.K_KP_MINUS]:
            self.rect.zoom_out(1.05)
            self.draw()

        if kb_state[pygame.K_ESCAPE]:
            self.running = False
        self.clock.tick(144)

    def stop(self):
        pygame.quit()
