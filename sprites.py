import pygame
# from pygame.sprite import _Group

class Player(pygame.sprite.Sprite):
    
    def parse_spritesheet_row(self, x,y, width, height, row):

        sprite = pygame.Surface((width,height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprites_image, (0,0), (x,y,width,height))

        if row < 0:
            return [sprite]
        
        if row - 4 <= 0:
            return [sprite] + self.parse_spritesheet_row(x + width, y, width, height, row -1)

        return [sprite] + self.parse_spritesheet_row(x + width, y, width, height, row -1)
    
    def get_full_spritesheet(self, x,y, width, height, row, col):
        sprite_list = []
        for _ in range(col):
            sprite_list += [self.parse_spritesheet_row(x,y,width,height, row)]
        self.sprite_sheet = sprite_list

    def __init__(self):
        super().__init__()
        self.sprites_image = pygame.transform.scale(pygame.image.load('assets/player/reimu.png'), (255,145)).convert_alpha()
        self.sprite_sheet = []
        self.get_full_spritesheet(0,0,32,48, 8, 3)
        # self.sprite_sheet = []
        self.image = self.sprite_sheet[0][0]
        self.rect = self.image.get_rect(center = (200,600))
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        self.x = 100
        self.y = 100
        self.current_sprite = 0
    
    def move(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.rect.x += self.velX
        self.rect.y += self.velY


    
    def idle_animation(self):
        print(len(self.sprite_sheet[0]))
        if self.current_sprite >= 8:
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprite_sheet[0][self.current_sprite], (50,70)).convert_alpha()
        self.current_sprite += 1
        self.rect = self.image.get_rect(center=self.rect.center)

    def direction_change():
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