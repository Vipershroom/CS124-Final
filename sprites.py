import pygame
# from pygame.sprite import _Group

class Player(pygame.sprite.Sprite):
    def __init__(self, screen=None):
        super().__init__()
        self.image = pygame.draw.circle(screen,"Red", (200,200), 10.)
        self.rect = self.image.get_rect(center = (200,200))
    
    def move(self):
        pass



class Button(pygame.sprite.Sprite):

    def __init__(self, text, pos) -> None:
        super().__init__()
        self.color = "#454647"
        self.text = text
        self.font = pygame.font.SysFont('MS Mincho', 50) 
        self.image = self.font.render(text, False, self.color)
        self.rect = self.image.get_rect(midbottom = pos)
        self.active = False

    def redraw(self):
        if self.active:
            self.color = "#f5f7fa"
        else:
            self.color = "#454647"
        self.image = self.font.render(self.text, False, self.color)
    def Broadcast(self):
        return self.text