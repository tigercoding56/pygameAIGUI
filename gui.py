import pygame, sys
from pygame.locals import *


class GUI:

    def __init__(self, window_size, window_title):
        self.window_size = window_size
        self.window_title = window_title
        self.screen = None
        self.font = None
        self.font_size = None

    def init_gui(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_title)
        self.font_size = 24
        self.font = pygame.font.SysFont(None, self.font_size)

    def draw_button(self, surface, x, y, width, height, text):
        pygame.draw.rect(surface, (0, 0, 255), (x, y, width, height))
        font_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = font_surface.get_rect(center=(x + width / 2,
                                                  y + height / 2))
        surface.blit(font_surface, text_rect)

    def draw_listbox(self, surface, x, y, width, height, items):
        pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height))
        item_height = 30
        for idx, item in enumerate(items):
            item_surface = self.font.render(item, True, (0, 0, 0))
            item_rect = item_surface.get_rect(topleft=(x + 10, y + 10 +
                                                       idx * item_height))
            surface.blit(item_surface, item_rect)

    def get_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    return mouse_pos