import pygame
from scenemanager import scene_manager
from variables import window
pygame.init()
screen = pygame.display.set_mode(window)
score = 0

# Default Scene 
scene_tag = "Menu"

"""
Global game loop
"""
while True:
    current_scene = scene_manager(screen, scene_tag, score)
    scene_tag = current_scene