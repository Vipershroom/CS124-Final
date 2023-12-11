import pygame
from mainmenu import MainMenu
from level1 import level1
from scores import Score

def scene_manager(scene: pygame.Surface, new_scene: str, score=0):
    """
    Function responsible for switching between scenes
    """
    # Clear the scene
    scene.fill(pygame.Color("Black"))

    match new_scene:
        case "Menu":
            return MainMenu(scene)
        case "Start":
            return level1(scene)
        case "Scores":
            return Score(scene)
        case "Quit":
            exit()