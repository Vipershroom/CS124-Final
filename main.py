import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode(window)

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    pygame.display.update()