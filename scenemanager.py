import pygame
import mainmenu
from variables import *

def scene_manager(scene: pygame.Surface, new_scene: str):
    
    # Clear the scene
    scene.fill(pygame.Color("Black"))

    match new_scene:
        case "Menu":
            return mainmenu.MainMenu(scene)
        case "Start":
            exit()