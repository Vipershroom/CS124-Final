import pygame
from variables import *
from sprites import *

def MainMenu(screen):
    # Main menu

    clock = pygame.time.Clock()

    # Initialize background
    bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()
    font = pygame.font.SysFont('MS Mincho', 50)
    text = font.render('Game Title', False, 'White')
    menu_buttons = pygame.sprite.Group()

    # Add buttons to Sprite Group
    menu_buttons.add(Button("Start", (300,300)))
    menu_buttons.add(Button("Scores", (300,400)))
    menu_buttons.add(Button("Quit", (300,500)))


    # Start as default active
    menu_buttons.sprites()[0].active = True
    menu_buttons.sprites()[0].redraw()
    current_active = 0

    while True:
        # Input Handler
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
            if events.type == pygame.KEYDOWN:
                # Switches Menu Buttons
                if events.key == pygame.K_DOWN:
                    menu_buttons.sprites()[current_active].active = False
                    menu_buttons.sprites()[current_active].redraw()
                    current_active += 1
                    if current_active == len(menu_buttons.sprites()):
                        current_active = 0
                    menu_buttons.sprites()[current_active].active = True
                    menu_buttons.sprites()[current_active].redraw()
                if events.key == pygame.K_UP:
                    menu_buttons.sprites()[current_active].active = False
                    menu_buttons.sprites()[current_active].redraw()
                    current_active -= 1
                    if current_active < 0:
                        current_active = len(menu_buttons.sprites())-1
                    menu_buttons.sprites()[current_active].active = True
                    menu_buttons.sprites()[current_active].redraw()

                # Broadcasts which button was pressed
                if events.key == pygame.K_RETURN:
                    return menu_buttons.sprites()[current_active].Broadcast()
        # Main menu
        screen.blit(bg, (0,0))
        screen.blit(text, (200,100))
        menu_buttons.draw(screen)
        pygame.display.update()
        clock.tick(60)