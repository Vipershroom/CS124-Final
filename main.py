import pygame
from scenemanager import scene_manager
from variables import window
pygame.init()
screen = pygame.display.set_mode(window)
5
# Default Scene 
scene_tag = "Start"

# Transition scene5
while True:
    current_scene = scene_manager(screen, scene_tag)
    scene_tag = current_scene