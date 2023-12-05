import pygame
from pygame.sprite import _Group

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/player')
        self.rect = self.image.get_rect(center = (200,200))