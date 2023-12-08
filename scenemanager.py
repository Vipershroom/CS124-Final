import pygame
from mainmenu import MainMenu
from level1 import level1

def scene_manager(scene: pygame.Surface, new_scene: str):
    
    # Clear the scene
    scene.fill(pygame.Color("Black"))

    match new_scene:
        case "Menu":
            return MainMenu(scene)
        case "Start":
            return level1(scene)
        case "Scores":
            exit()
        case "Quit":
            exit()