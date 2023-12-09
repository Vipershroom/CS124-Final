import pygame
from variables import window
from sprites import Player, Bullet
def level1(screen: pygame.Surface):
    
    clock = pygame.time.Clock()

    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    idle = True

    bullets = pygame.sprite.Group()
    bullets

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                if len(bullets.sprites()) <= 50:
                    bullets.add(Bullet((player.sprite.rect.center[0],player.sprite.rect.center[1] - 48)))
                
            if keys[pygame.K_LEFT]:
                player.sprite.left_pressed = True
            else:
                player.sprite.left_pressed = False

            if keys[pygame.K_RIGHT]:
                player.sprite.right_pressed = True
            else:
                player.sprite.right_pressed = False
            if keys[pygame.K_UP]:
                player.sprite.up_pressed = True
            else:
                player.sprite.up_pressed = False
            if keys[pygame.K_DOWN]:
                player.sprite.down_pressed = True
            else:
                player.sprite.down_pressed = False

            
            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT:
            #         player.sprite.left_pressed = False
            #     if event.key == pygame.K_RIGHT:
            #         player.sprite.right_pressed = False
            #     if event.key == pygame.K_UP:
            #         player.sprite.up_pressed = False
            #     if event.key == pygame.K_DOWN:
            #         player.sprite.down_pressed = False

            
        
        screen.blit(bg, (0,0))
        if player.sprite.right_pressed:
            idle = False
            player.sprite.direction_change('right')
        elif player.sprite.left_pressed:
            idle = False
            player.sprite.direction_change('left')

        if not player.sprite.right_pressed and player.sprite.left_pressed and idle:
            idle = True
            player.sprite.current_sprite = 0

        if idle:
            player.sprite.idle_animation()
        

        player.draw(screen)
        bullets.draw(screen)
        player.sprite.move()
        player.sprite.idle_animation()
        for i in bullets.sprites():
            i.move()
        pygame.display.update()
        clock.tick(60)