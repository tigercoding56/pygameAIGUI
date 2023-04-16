import pygame
from pygame.locals import *
from listboxex import Button
from listboxex import ListBox

pygame.init()

FPS = 30
WINDOW_SIZE = (640, 480)
WINDOW_TITLE = 'Button and List Box Example'

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)
clock = pygame.time.Clock()

button = Button(50, 50, 100, 50, 'Click Me')
list_box = ListBox(50, 150, 200, 200, ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6'])

selected_item = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

        button.handle_event(event)
        list_box.handle_event(event)

    screen.fill((255, 255, 255))

    button.draw(screen)
    list_box.draw(screen)

    if list_box.selected_item is not None:
        selected_item = list_box.items[list_box.selected_item]
    else:
        selected_item = None

    pygame.display.update()
    clock.tick(FPS)
    if selected_item:
        print("Selected item:",selected_item)