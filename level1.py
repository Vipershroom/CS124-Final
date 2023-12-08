import pygame
from variables import window
from sprites import Player
def level1(screen: pygame.Surface):
    
    clock = pygame.time.Clock()

    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()

    player = pygame.sprite.GroupSingle()
    player.add(Player())
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()

        screen.blit(bg, (0,0))
        pygame.display.update()
        clock.tick(60)