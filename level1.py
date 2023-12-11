import pygame
from variables import window
from sprites import Player, Bullet, Enemy, Label
import random
def level1(screen: pygame.Surface):

    """
    Loads the scene for level 1, with both game loop and resources.
    """
    
    clock = pygame.time.Clock()

    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    idle = True

    bullet_sprite = pygame.transform.scale(pygame.image.load('assets/misc/player_shot.png'), (25,25)).convert_alpha()
    bullets = pygame.sprite.Group()

    bullet_enemy_sprite = pygame.transform.scale(pygame.image.load('assets/misc/enemy_shot.png'), (25,25)).convert_alpha()
    bullet_enemy = pygame.sprite.Group()
    Bullet(bullet_sprite,(player.sprite.rect.center[0],player.sprite.rect.center[1] - 48), len(bullets.sprites()) - 1)
    

    wave2_time = False
    wave3_time = False

    enemy = wave1()
    
    score = pygame.sprite.GroupSingle(Label("Score",0,780))
    lives = pygame.sprite.GroupSingle(Label("Lives",player.sprite.lives,740))

    time1 = 0

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z] and not player.sprite.dead:
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

            
        
        screen.blit(bg, (0,0))
        score.draw(screen)
        lives.draw(screen)
        if not player.sprite.dead:
            player.draw(screen)
            player.sprite.invinc = False
        bullet_enemy.draw(screen)
        player.sprite.move(bullet_enemy, lives.sprite)
        player.sprite.idle_animation()
        for bullet in bullets.sprites():
            if bullet.type != len(bullets.sprites()) - 1:
                bullet.draw(screen)
        enemy.draw(screen)


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
        
        
        
        
        
        for i in enemy.sprites():
            i.move(bullets, score.sprite)
            i.shoot(bullet_enemy_sprite,bullet_enemy)
        for i in bullets.sprites():
            i.move()
        
        for i in bullet_enemy.sprites():
            i.move()
        
        
        
        
        print(time1)
        if time1 >= 500 and not wave2_time:
            l = wave2()
            for i in l:
                enemy.add(i)
            wave2_time = True

        if time1 >= 1500 and not wave3_time:
            l = wave3()
            for i in l:
                enemy.add(i)
            wave3_time = True

        if time1 >= 3500:
            # game over
            pass
        print(player.sprite.lives)
        if player.sprite.lives <= 0:
            clock = pygame.time.Clock()
            return "Menu"
            
        
        pygame.display.update()
        time1 += 1
        clock.tick(60)

def wave1():
    grp = pygame.sprite.Group()
    for i in range(6):
        grp.add(Enemy([(random.choice([10, 0, 25, 50, 25, 100, 150, 400, 500]),random.choice([0,0, 10, 25, 50, 100]))] + [(random.randrange(100,600), random.randrange(0,400)) for _ in range(4)] + [(-50,-50)], i * 20 ))
    return grp

def wave2():
    grp = []
    for i in range(16):
        grp.append(Enemy([(random.choice([10, 0, 25, 50, 25, 100, 150, 400, 500]),random.choice([0,0, 10, 25, 50, 100]))] + [(random.randrange(100,600), random.randrange(0,400)) for _ in range(4)] + [(-50,-50)], i * 20 ))
    return grp

def wave3():
    grp = []
    for i in range(12):
        grp.append(Enemy([(random.choice([10, 0, 25, 50, 25, 100, 150, 400, 500]),random.choice([0,0, 10, 25, 50, 100]))] + [(random.randrange(100,600), random.randrange(0,400)) for _ in range(20)] + [(-50,-50)], i * 20, 720 ))
    return grp