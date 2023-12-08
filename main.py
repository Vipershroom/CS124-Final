import pygame
from variables import *
from sprites import *
from scenemanager import scene_manager
pygame.init()

screen = pygame.display.set_mode(window)
scene_tag = "Menu"
while True:
    current_scene = scene_manager(screen, scene_tag)
    scene_tag = current_scene

# Main menu

# Initialize background
# bg = pygame.transform.scale(pygame.image.load('assets/background/sky.png'), window).convert()
# font = pygame.font.SysFont('MS Mincho', 50)
# text = font.render('Game Title', False, 'White')
# menu_buttons = pygame.sprite.Group()

# # Add buttons to Sprite Group
# menu_buttons.add(Button("Start", (300,300)))
# menu_buttons.add(Button("Scores", (300,400)))
# menu_buttons.add(Button("Quit", (300,500)))


# # Start as default active
# menu_buttons.sprites()[0].active = True
# menu_buttons.sprites()[0].redraw()
# current_active = 0

