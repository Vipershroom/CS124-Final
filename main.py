import pygame
from variables import *
from sprites import *
from scenemanager import scene_manager
pygame.init()

screen = pygame.display.set_mode(window)
scene_tag = "Menu"

# Transition scene
while True:
    current_scene = scene_manager(screen, scene_tag)
    scene_tag = current_scene