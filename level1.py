import pygame
from variables import window

def level1(screen: pygame.Surface):
    
    clock = pygame.time.Clock()

    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()

        screen.blit(bg, (0,0))
        pygame.display.update()
        clock.tick(60)