import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode(window)
score = 0
clock = pygame.time.Clock()

# Main menu
bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()
font = pygame.font.SysFont('MS Mincho', 50)
text = font.render('Game Title', False, 'Black')


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    # Main menu
    screen.blit(bg, (0,0))
    screen.blit(text, (200,200))
    pygame.display.update()
    clock.tick(60)