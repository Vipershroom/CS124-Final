import pygame
from variables import window
from sprites import Player, Bullet, Enemy
def level1(screen: pygame.Surface):
    
    clock = pygame.time.Clock()

    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    idle = True

    bullet_sprite = pygame.transform.scale(pygame.image.load('assets/misc/player_shot.png'), (25,25)).convert_alpha()
    bullets = pygame.sprite.Group()
    # move_pattern = [(i,0) for i in range(5)]
    move_pattern = (1,0)
    Enemy().move(move_pattern)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                bullets.add(Bullet(bullet_sprite,(player.sprite.rect.center[0],player.sprite.rect.center[1] - 48), len(bullets.sprites()) - 1))
                
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
        # bullets.draw(screen)
        for bullet in bullets.sprites():
            if bullet.type != len(bullets.sprites()) - 1:
                print(bullet.type)
                bullet.draw(screen)
        player.sprite.move()
        player.sprite.idle_animation()
        for i in bullets.sprites():
            i.move()
        pygame.display.update()
        clock.tick(60)