import pygame
from variables import window
from sprites import Player
def level1(screen: pygame.Surface):
    
    clock = pygame.time.Clock()

    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    sprite_sheet = player.sprite.get_full_spritesheet(0,0,32,48, 8, 3)
    print(sprite_sheet)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.sprite.left_pressed = True
                if event.key == pygame.K_RIGHT:
                    player.sprite.right_pressed = True
                if event.key == pygame.K_UP:
                    player.sprite.up_pressed = True
                if event.key == pygame.K_DOWN:
                    player.sprite.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.sprite.left_pressed = False
                if event.key == pygame.K_RIGHT:
                    player.sprite.right_pressed = False
                if event.key == pygame.K_UP:
                    player.sprite.up_pressed = False
                if event.key == pygame.K_DOWN:
                    player.sprite.down_pressed = False
        
        screen.blit(bg, (0,0))
        rend_val = 1
        for i in range(len(sprite_sheet)):
            for k in range(len(sprite_sheet[i])):
                screen.blit(pygame.transform.scale(sprite_sheet[i][k], (50,90)), (100 + k * 50, 100 * rend_val))
            rend_val += 1
        player.draw(screen)
        player.sprite.move()
        pygame.display.update()
        clock.tick(60)