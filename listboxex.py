import pygame
from pygame import *

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.normal_color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.selected_color = (100, 100, 100)
        self.font = pygame.font.SysFont('Arial', 20)
        self.surface = self.font.render(self.text, True, (0, 0, 0))

    def draw(self, surface):
        color = self.normal_color

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                color = self.selected_color
            else:
                color = self.hover_color

        pygame.draw.rect(surface, color, self.rect)
        text_rect = self.surface.get_rect(center=self.rect.center)
        surface.blit(self.surface, text_rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.selected = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if self.rect.collidepoint(event.pos) and self.selected:
                    self.selected = False
                    self.clicked = True
                else:
                    self.selected = False

    def is_clicked(self):
        if self.clicked:
            self.clicked = False
            return True
        return False
# class ListBox:
#     def __init__(self, x, y, width, height, font, item_height, items):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.font = font
#         self.item_height = item_height
#         self.items = items
#         self.selected_item = 0
#         self.offset = 0
# 
#     def draw(self, surface):
#         pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 2)
#         for i, item in enumerate(self.items):
#             if i == self.selected_item:
#                 color = (175, 175, 175)
#             else:
#                 color = (221, 221, 221)
#             item_surface = self.font.render(item, True, (0, 0, 0))
#             item_rect = item_surface.get_rect(topleft=(self.x + 2, self.y + i*self.item_height + 2))
#             pygame.draw.rect(surface, color, (self.x + 2, self.y + i*self.item_height + 2, self.width - 4, self.item_height - 2))
#             surface.blit(item_surface, item_rect)
# 
#     def handle_event(self, event):
#         if event.type == MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             if self.x <= mouse_pos[0] <= self.x + self.width:
#                 if self.y <= mouse_pos[1] <= self.y + self.height:
#                     idx = (mouse_pos[1] - self.y) // self.item_height + self.offset
#                     if idx < len(self.items):
#                         self.selected_item = idx
# 
#         if event.type == MOUSEWHEEL:
#             if event.y > 0:
#                 self.offset = max(0, self.offset-1)
#             elif event.y < 0:
#                 self.offset = min(len(self.items)-1, self.offset+1)
# 
#         if event.type == KEYDOWN:
#             if event.key == K_UP:
#                 self.selected_item = max(0, self.selected_item-1)
#             elif event.key == K_DOWN:
#                 self.selected_item = min(len(self.items)-1, self.selected_item+1)
#             else:
#                 self.set_selected_item(event.key - ord('1'))
#     def set_selected_item(self, idx):
#         if idx >= 0 and idx < len(self.items):
#             self.selected_item = idx
class ListBox:
    def __init__(self, x, y, width, height, items):
        self.rect = pygame.Rect(x, y, width, height)
        self.items = items
        self.font = pygame.font.SysFont('Arial', 20)
        self.item_height = self.font.get_linesize() + 10
        self.visible_items = height // self.item_height
        self.selected_item = None
        self.offset = 0

    def draw(self, surface):
        items_to_render = self.items[self.offset:self.offset+self.visible_items]

        for i, item in enumerate(items_to_render):
            item_rect = pygame.Rect(self.rect.left, self.rect.top+(i*self.item_height), self.rect.width, self.item_height)

            if i + self.offset == self.selected_item:
                color = (100, 100, 100)
            else:
                color = (200, 200, 200)

            pygame.draw.rect(surface, color, item_rect)

            item_surface = self.font.render(item, True, (0, 0, 0))
            text_rect = item_surface.get_rect(center=item_rect.center)
            surface.blit(item_surface, text_rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                item = (mouse_pos[1] - self.rect.top) // self.item_height
                if item < len(self.items) and item + self.offset != self.selected_item:
                    self.selected_item = item + self.offset
        elif event.type == MOUSEWHEEL:
            if event.y > 0:
                self.offset = max(0, self.offset-1)
            elif event.y < 0:
                self.offset = min(len(self.items)-self.visible_items, self.offset+1)
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                self.selected_item = max(0, self.selected_item-1)
                if self.selected_item < self.offset:
                    self.offset = self.selected_item
            elif event.key == K_DOWN:
                self.selected_item = min(len(self.items)-1, self.selected_item+1)
                if self.selected_item >= self.offset+self.visible_items:
                    self.offset = self.selected_item - self.visible_items + 1
